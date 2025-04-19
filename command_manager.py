#!/usr/bin/env python3

import os
import subprocess
import time

# Permitir que la ruta del socket se configure mediante variable de entorno
SOCKET_PATH = os.getenv("TMATE_SOCKET_PATH", "/tmp/tmate.sock")

def crear_sesion():
    # Crear nueva sesión de tmate sin matar otras existentes
    subprocess.run(['tmate', '-S', SOCKET_PATH, 'new-session', '-d'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    for _ in range(10):
        result = subprocess.run(['tmate', '-S', SOCKET_PATH, 'wait', 'tmate-ready'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        if result.returncode == 0:
            break
        time.sleep(1)

def obtener_enlaces():
    ssh = subprocess.check_output(['tmate', '-S', SOCKET_PATH, 'display', '-p', '#{tmate_ssh}']).decode().strip()
    ssh_ro = subprocess.check_output(['tmate', '-S', SOCKET_PATH, 'display', '-p', '#{tmate_ssh_ro}']).decode().strip()
    return ssh, ssh_ro

def cerrar_sesion():
    subprocess.run(['tmate', '-S', SOCKET_PATH, 'kill-session'])

def sesion_activa():
    result = subprocess.run(['tmate', '-S', SOCKET_PATH, 'list-sessions'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return b"windows" in result.stdout
