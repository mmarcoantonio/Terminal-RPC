import psutil
from pypresence import Presence
import time

# here goes your client id / app id
id = '1245378474454024334'

def terminal_status():
    # search for the process name in the OS
    for proc in psutil.process_iter(['name']):

        try:
            if 'gnome-terminal-' in proc.info['name']:
                status_check = {"terminal_name": "GNOME Terminal", "status": True}
                return status_check
            elif 'kitty' in proc.info['name']:
                status_check = {"terminal_name": "Kitty", "status": True}
                return True
            elif 'Konsole' in proc.info['name']:
                status_check = {"terminal_name": "Konsole","status": True}
                return status_check
            elif 'iTerm2' in proc.info['name']:
                status_check = {"terminal_name": "iTerm2","status": True}
                return status_check
            elif 'Terminal' in proc.info['name']:
                status_check = {"terminal_name": "MacOs Terminal","status": True}
                return status_check
            
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    
    status_check = {"status": False}
    return status_check

def update_activity_discord():
    check = terminal_status()

    if check["status"]:
        rpc.update(state="Usando o " + check["terminal_name"], start=1, large_image="terminalicon")
    else:
        rpc.clear()

rpc = Presence(id)
rpc.connect()

try:
    while True:
        update_activity_discord()
        time.sleep(2)
except KeyboardInterrupt:
    rpc.clear()
    rpc.close()
