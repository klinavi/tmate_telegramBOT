#!/usr/bin/env bash

# Cerrar cualquier sesión previa de tmate
tmate -S /tmp/tmate.sock kill-session 2>/dev/null || true

# Mostrar título con echo (sin figlet)
clear
echo "--------------------------------------------------------------------------------"
echo " _                   _       ____   ___ _____ "
echo "| |_ _ __ ___   __ _| |_ ___| __ ) / _ \\_   _|"
echo "| __| '_ \` _ \\ / _\` | __/ _ \\  _ \\| | | || |  "
echo "| |_| | | | | | (_| | ||  __/ |_) | |_| || |  "
echo " \\__|_| |_| |_|\\__,_|\\__\\___|____/ \\___/ |_|  "
echo "--------------------------------------------------------------------------------"

# Ir al directorio del script y ejecutar main.py
DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
python3 "$DIR/main.py"

