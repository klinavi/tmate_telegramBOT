#!/usr/bin/env bash

# Ir al directorio del script (repositorio)
DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$DIR"

echo "[+] Actualizando repositorio desde GitHub..."
git pull origin master

echo "[✓] Repositorio actualizado correctamente."

