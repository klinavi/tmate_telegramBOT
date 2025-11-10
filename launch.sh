#!/usr/bin/env bash

# Cerrar cualquier sesión previa de tmate
tmate -S /tmp/tmate.sock kill-session 2>/dev/null || true

clear
cat << 'EOF'
 _____    _                                ____  _          _ _      
|_   _|__| | ___  __ _ _ __ __ _ _ __ ___ / ___|| |__   ___| | |_/\__
  | |/ _ \ |/ _ \/ _` | '__/ _` | '_ ` _ \\___ \| '_ \ / _ \ | \    /
  | |  __/ |  __/ (_| | | | (_| | | | | | |___) | | | |  __/ | /_  _\
  |_|\___|_|\___|\__, |_|  \__,_|_| |_| |_|____/|_| |_|\___|_|_| \/  
                 |___/                                               
EOF
echo "--------------------------------------------------------------------------------"

DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
echo "[+] Ejecutando main.py..."
python3 "$DIR/main.py"

