# Tmate TelegramBOT - Terminal remota

**Tmate_TelegramBOT** es un script que automatiza la ejecucución de una terminal remota con ayuda de tmate y permite ver el estado de la sesion en un chat de telegram con ayuda de un bot. Esto con el objetivo de tener una terminal desde un telefono movil sin la necesidad de usar una computadora

---

## Cración del bot
Para crear el bot debes hacerlo con ayuda **de @BotFather**(https://t.me/BotFather) desde telegram. Una vez creado el bot debes asignarle los siguiente comandos:
```
start - Muestra un mensaje de bienvenida
crear_sesion - Crea una sesión de tmate y envía los enlaces
matar_sesion - Termina la sesión activa de tmate
estado_sesion - Verifica si hay una sesión activa
obtener_enlace_ssh - Muestra el enlace SSH de la sesión activa
obtener_enlace_web - Muestra el enlace Web (solo lectura) de la sesión
ver_mensajes - (Próximamente) Ver mensajes del sistema o logs
```
luego obten la API del bot y guardala para mas tarde

## Instalación

#### Clonar el directorio
```bash
git clone https://github.com/klinavi/tmate_telegramBOT.git
cd tmate_telegramBOT
```

#### Instalar requirements.txt

Para instalar **requirements.txt** debes ejecutar el siguiente comando:

```bash
pip install -r requirements.txt
```

#### Colocar la API del bot en el .env

Aqui debes colocar la API del bot que te da **@BotFather** en un .env, para esto ejecuta el siguiente comando y modifica el .env poniendo tu API donde se indica:
```bash
# Duplica el archivo .env.example y luego modifica el .env
cp .env.example .env
```

#### Ejecutar el bot
```
./launch.sh
```
