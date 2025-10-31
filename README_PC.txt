═══════════════════════════════════════════════════════════════════════════
🕷️  BOTS NOCTURNO - GUÍA DE INSTALACIÓN Y USO EN PC 🕷️
═══════════════════════════════════════════════════════════════════════════

Esta guía te ayudará a ejecutar tus bots de Highrise directamente desde tu PC.

═══════════════════════════════════════════════════════════════════════════
📋 REQUISITOS PREVIOS
═══════════════════════════════════════════════════════════════════════════

1. Python 3.10 o superior instalado en tu PC
   - Descarga desde: https://www.python.org/downloads/
   - Durante la instalación, marca la opción "Add Python to PATH"

2. Conexión a Internet estable

═══════════════════════════════════════════════════════════════════════════
🔧 INSTALACIÓN PASO A PASO
═══════════════════════════════════════════════════════════════════════════

PASO 1: Descargar los archivos del proyecto
─────────────────────────────────────────────────────────────────────────
Descarga TODOS estos archivos a una carpeta en tu PC:

   Archivos principales:
   ✓ main.py                  (Bot principal)
   ✓ cantinero_bot.py         (Bot cantinero)
   ✓ run.py                   (Lanzador de bots)
   ✓ requirements.txt         (Dependencias)
   ✓ config.json              (Configuración bot principal)
   ✓ cantinero_config.json    (Configuración bot cantinero)
   
   Carpeta de datos:
   ✓ data/                    (Carpeta completa con todos sus archivos)

PASO 2: Abrir terminal/consola en la carpeta del proyecto
─────────────────────────────────────────────────────────────────────────
   
   Windows:
   • Abre la carpeta donde descargaste los archivos
   • Mantén presionada la tecla Shift y haz clic derecho en un espacio vacío
   • Selecciona "Abrir ventana de PowerShell aquí" o "Abrir ventana de comandos aquí"
   
   Mac/Linux:
   • Abre Terminal
   • Navega a la carpeta: cd /ruta/a/la/carpeta

PASO 3: Instalar dependencias
─────────────────────────────────────────────────────────────────────────

Ejecuta este comando en la terminal:

   pip install -r requirements.txt

Espera a que termine la instalación. Verás mensajes indicando que se están
descargando e instalando los paquetes necesarios.

═══════════════════════════════════════════════════════════════════════════
🚀 EJECUTAR LOS BOTS
═══════════════════════════════════════════════════════════════════════════

Una vez instaladas las dependencias, ejecuta:

   python run.py

El lanzador mostrará:
• Los bots que se van a ejecutar
• La sala a la que se conectarán
• Te pedirá confirmar presionando ENTER

Luego verás los logs de ambos bots ejecutándose simultáneamente.

Para DETENER los bots:
• Presiona Ctrl+C en la terminal

═══════════════════════════════════════════════════════════════════════════
⚙️ CONFIGURACIÓN
═══════════════════════════════════════════════════════════════════════════

Los archivos de configuración ya están listos con tus credenciales:

📄 config.json (Bot Principal)
─────────────────────────────────────────────────────────────────────────
{
  "api_token": "b0c7b29926c42a39987057723b8def359ce211d320ecd7f946401fdf9b14d56ah",
  "room_id": "686c527e9668a3cb40e1f58d",
  "owner_id": "662aae9b602b4a897557ec18",
  "admin_ids": ["669da7b73867bac51391c757"],
  ...
}

📄 cantinero_config.json (Bot Cantinero)
─────────────────────────────────────────────────────────────────────────
{
  "api_token": "e85f532a8d3060b6e6bc2ebafdf9a657d052c51897524926f4e6b226edd7d68d",
  "room_id": "686c527e9668a3cb40e1f58d",
  ...
}

⚠️ IMPORTANTE: ¡MANTÉN ESTOS ARCHIVOS SEGUROS!
• No compartas tus API tokens con nadie
• No subas estos archivos a GitHub o servicios públicos
• Haz backup de estos archivos en un lugar seguro

═══════════════════════════════════════════════════════════════════════════
✨ NUEVAS FUNCIONALIDADES IMPLEMENTADAS
═══════════════════════════════════════════════════════════════════════════

✅ Envío de 100 corazones completo
─────────────────────────────────────────────────────────────────────────
Problema anterior: Al enviar 100 corazones, solo se enviaban 30
Solución: Ahora el bot envía los 100 corazones completos cuando un admin 
          o propietario usa el comando !heart @usuario 100

✅ Comandos con respuestas contextuales
─────────────────────────────────────────────────────────────────────────
Los comandos de interacción ahora responden según el contexto:
• Si usas !heartall, !punch @user, !heart @user en whisper → respuesta en whisper
• Si usas los mismos comandos en chat público → respuesta en público
• Comandos afectados: !heart, !heartall, !thumbs, !clap, !wave, !punch,
  !slap, !flirt, !scare, !electro, !hug, !ninja, !laugh, !boom

✅ Flash Mode mejorado
─────────────────────────────────────────────────────────────────────────
Problema anterior: Flash mode se activaba en todos los pisos
Solución: Ahora el flash mode se activa cuando:
          • El usuario sube O baja desde/hacia altura >= 10 bloques
          • La altura de origen o destino debe ser >= 10.0 bloques
          • No funciona en los pisos normales del bar (solo alturas altas)

═══════════════════════════════════════════════════════════════════════════
🔍 SOLUCIÓN DE PROBLEMAS
═══════════════════════════════════════════════════════════════════════════

Problema: "python no se reconoce como comando"
Solución: Reinstala Python y marca "Add Python to PATH" durante instalación

Problema: "No module named 'highrise'"
Solución: Ejecuta nuevamente: pip install -r requirements.txt

Problema: "Error al conectar a la sala"
Solución: Verifica que los API tokens en config.json sean correctos

Problema: Los bots se desconectan
Solución: • Verifica tu conexión a Internet
          • Asegúrate de que los tokens sean válidos
          • El lanzador reiniciará automáticamente los bots si se caen

═══════════════════════════════════════════════════════════════════════════
📂 ESTRUCTURA DE ARCHIVOS
═══════════════════════════════════════════════════════════════════════════

tu-carpeta-bots/
│
├── main.py                    # Bot principal con todos los comandos
├── cantinero_bot.py          # Bot cantinero (floss y mensajes)
├── run.py                    # Lanzador de ambos bots
├── requirements.txt          # Lista de dependencias
├── config.json               # Configuración bot principal
├── cantinero_config.json     # Configuración bot cantinero
├── README_PC.txt            # Esta guía
│
├── data/                     # Carpeta de datos persistentes
│   ├── vip.txt              # Lista de usuarios VIP
│   ├── hearts.txt           # Corazones de usuarios
│   ├── activity.txt         # Actividad de usuarios
│   ├── user_info.json       # Información de usuarios
│   ├── bot_inventory.json   # Inventario del bot
│   └── teleport_points.txt  # Puntos de teletransporte
│
├── bot_log.txt              # Logs del bot (se crea automáticamente)
└── bot_responses.txt        # Respuestas del bot (se crea automáticamente)

═══════════════════════════════════════════════════════════════════════════
💡 CONSEJOS ÚTILES
═══════════════════════════════════════════════════════════════════════════

1. Mantén la ventana de terminal abierta mientras los bots estén corriendo

2. Los bots se reiniciarán automáticamente si hay un error temporal

3. Puedes ver los logs en tiempo real en la terminal

4. Para ejecutar solo un bot, edita run.py y comenta la línea del bot 
   que no quieras ejecutar

5. Haz backup regular de la carpeta data/ para no perder información de VIPs

═══════════════════════════════════════════════════════════════════════════
📞 SOPORTE
═══════════════════════════════════════════════════════════════════════════

Si tienes problemas:
1. Revisa esta guía completa
2. Verifica que Python esté instalado correctamente
3. Asegúrate de que todos los archivos estén en la misma carpeta
4. Verifica que los API tokens sean correctos

═══════════════════════════════════════════════════════════════════════════

🕷️ ¡Disfruta de tus bots NOCTURNO! 🕷️

═══════════════════════════════════════════════════════════════════════════
