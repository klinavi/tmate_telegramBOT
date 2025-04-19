# Tmate TelegramBOT - Terminal remota

**Tmate_TelegramBOT** es un script que automatiza la ejecución de una terminal remota con ayuda de **tmate**, y permite ver el estado de la sesión en un chat de Telegram mediante un bot. Su objetivo es ofrecer acceso a una terminal desde un teléfono móvil, sin necesidad de usar una computadora.
---

## Cración del bot
Para crear el bot, debes hacerlo con ayuda de [@BotFather](https://t.me/BotFather) desde Telegram. Una vez creado el bot, asígnale los siguientes comandos:

```
start - Muestra un mensaje de bienvenida
crear_sesion - Crea una sesión de tmate y envía los enlaces
matar_sesion - Termina la sesión activa de tmate
estado_sesion - Verifica si hay una sesión activa
obtener_enlace_ssh - Muestra el enlace SSH de la sesión activa
obtener_enlace_web - Muestra el enlace Web (solo lectura) de la sesión
ver_mensajes - (Próximamente) Ver mensajes del sistema o logs
```
Luego, obtén el token del bot (API key) y guárdalo para más adelante.

## Instalación

#### Instalación de tmate
Para instlar tmate puede usar los siguientes comandos:
```bash
#Distros basada en debian
sudo apt update
sudo apt install tmate -y
#Distros basadas en Arch
sudo pacman -Syu tmate

```

#### Clonar el repositorio
```bash
git clone https://github.com/klinavi/tmate_telegramBOT.git
cd tmate_telegramBOT
```

#### Instalar requirements.txt

Instala los paquetes necesarios desde requirements.txt con:

```bash
pip install -r requirements.txt
```

#### Configurar la API del BOT

Aqui debes colocar la API del bot que te da **@BotFather** en un .env, para esto ejecuta el siguiente comando:
```bash
# Duplica el archivo .env.example y luego modifica el .env
cp .env.example .env
```
Abre el archivo .env y reemplaza `TOKEN=` con tu API key proporcionada por @BotFather.

#### Ejecutar el bot
Inicia el bot con:
```
./launch.sh
```

