#!/usr/bin/env python3
import os
import logging
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
import command_manager  # Importa las funciones desde command_manager.py

# Cargar variables de entorno desde un archivo .env
load_dotenv()
TOKEN = os.getenv("TOKEN")

if not TOKEN:
    raise ValueError("❌ No se encontró el TOKEN en las variables de entorno. Define TOKEN en tu .env.")

# Configurar logging: mostramos INFO para ver comandos, pero ocultamos datos sensibles
logging.basicConfig(
    format="%(asctime)s - %(levelname)s - %(message)s",
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# Silenciar logs de librerías externas que no necesitamos
logging.getLogger("httpx").setLevel(logging.WARNING)
logging.getLogger("telegram.vendor.ptbutils.request").setLevel(logging.WARNING)

# Comandos disponibles
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    logger.info(f"/start ejecutado por {update.effective_user.id}")
    await update.message.reply_text("¡Hola! Soy tu bot de tmate. ¿Cómo puedo ayudarte hoy?")

async def crear_sesion(update: Update, context: ContextTypes.DEFAULT_TYPE):
    logger.info(f"/crear_sesion ejecutado por {update.effective_user.id}")
    command_manager.crear_sesion()
    ssh, ssh_ro = command_manager.obtener_enlaces()
    msg = f"✅ Sesión creada.\n🔗 SSH: `{ssh}`\n🔗 Web (solo lectura): `{ssh_ro}`"
    await update.message.reply_text(msg, parse_mode='Markdown')

async def matar_sesion(update: Update, context: ContextTypes.DEFAULT_TYPE):
    logger.info(f"/matar_sesion ejecutado por {update.effective_user.id}")
    command_manager.cerrar_sesion()
    await update.message.reply_text("❌ Sesión terminada.")

async def estado_sesion(update: Update, context: ContextTypes.DEFAULT_TYPE):
    logger.info(f"/estado_sesion ejecutado por {update.effective_user.id}")
    estado = command_manager.sesion_activa()
    msg = "🟢 Sesión activa." if estado else "🔴 No hay sesión activa."
    await update.message.reply_text(msg)

async def obtener_enlace_ssh(update: Update, context: ContextTypes.DEFAULT_TYPE):
    logger.info(f"/obtener_enlace_ssh ejecutado por {update.effective_user.id}")
    if command_manager.sesion_activa():
        ssh, _ = command_manager.obtener_enlaces()
        await update.message.reply_text(f"🔗 Enlace SSH:\n`{ssh}`", parse_mode='Markdown')
    else:
        await update.message.reply_text("⚠️ No hay una sesión activa.")

async def obtener_enlace_web(update: Update, context: ContextTypes.DEFAULT_TYPE):
    logger.info(f"/obtener_enlace_web ejecutado por {update.effective_user.id}")
    if command_manager.sesion_activa():
        _, ssh_ro = command_manager.obtener_enlaces()
        await update.message.reply_text(f"🔗 Enlace Web (solo lectura):\n`{ssh_ro}`", parse_mode='Markdown')
    else:
        await update.message.reply_text("⚠️ No hay una sesión activa.")

async def ver_mensajes(update: Update, context: ContextTypes.DEFAULT_TYPE):
    logger.info(f"/ver_mensajes ejecutado por {update.effective_user.id}")
    await update.message.reply_text("📩 Próximamente podrás ver logs o mensajes del sistema.")

# Ejecutar el bot
def main():
    app = Application.builder().token(str(TOKEN).strip()).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("crear_sesion", crear_sesion))
    app.add_handler(CommandHandler("matar_sesion", matar_sesion))
    app.add_handler(CommandHandler("estado_sesion", estado_sesion))
    app.add_handler(CommandHandler("obtener_enlace_ssh", obtener_enlace_ssh))
    app.add_handler(CommandHandler("obtener_enlace_web", obtener_enlace_web))
    app.add_handler(CommandHandler("ver_mensajes", ver_mensajes))

    logger.info("[✓]Bot iniciado correctamente (token oculto). Esperando comandos...")
    app.run_polling()

if __name__ == "__main__":
    main()
    try:
        del TOKEN
    except NameError:
        pass

