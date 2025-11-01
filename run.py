import asyncio
import json
import threading
from flask import Flask
from highrise import Highrise
from highrise import BaseBot
import os

# === CARGAR CONFIG ===
def load_config(file):
    try:
        with open(file, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception as e:
        print(f"Error cargando {file}: {e}")
        return None

# === BOT PRINCIPAL ===
class BotPrincipal(BaseBot):
    async def on_start(self):
        print("Bot Principal conectado!")

    async def on_chat(self, user, message):
        if message.lower() == "!hola":
            await self.highrise.chat("¡Hola desde el Principal!")

# === BOT CANTINERO ===
class BartenderBot(BaseBot):
    async def on_start(self):
        print("Bot Cantinero conectado!")

    async def on_chat(self, user, message):
        if message.lower() == "!trago":
            await self.highrise.chat("¡Aquí tienes tu trago!")

# === SERVIDOR WEB PARA MANTENER VIVO ===
app = Flask(__name__)

@app.route('/')
def home():
    return "Bots NOCTURNO activos 🚀"

def run_flask():
    port = int(os.environ.get("PORT", 3000))
    app.run(host="0.0.0.0", port=port)

# === MAIN ===
async def main():
    print("\n" + "="*60)
    print("NOCTURNO BOTS LAUNCHER")
    print("="*60 + "\n")

    # Cargar configs
    config_main = load_config("config.json")
    config_cantinero = load_config("cantinero_config.json")

    if not config_main or not config_main.get("api_token") or not config_main.get("room_id"):
        print("Falta config.json o datos")
        return

    if not config_cantinero or not config_cantinero.get("api_token"):
        print("Falta cantinero_config.json o token")
        return

    room_id = config_main["room_id"]

    # Bot Principal
    bot1 = BotPrincipal()
    await bot1.highrise.connect(config_main["api_token"], room_id)

    # Bot Cantinero
    bot2 = BartenderBot()
    await bot2.highrise.connect(config_cantinero["api_token"], room_id)

    print(f"\nAmbos bots conectados a la sala: {room_id}")
    print("Presiona Ctrl+C para detener\n")

    # Mantener vivo
    try:
        while True:
            await asyncio.sleep(60)
    except KeyboardInterrupt:
        print("\nDeteniendo bots...")
        await bot1.highrise.close()
        await bot2.highrise.close()

if __name__ == "__main__":
    # Ejecutar Flask en un hilo aparte
    threading.Thread(target=run_flask).start()
    # Ejecutar bot principal
    asyncio.run(main())
