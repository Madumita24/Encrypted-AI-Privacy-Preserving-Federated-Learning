import subprocess
import os
import time

# Set your conda environment name
env_name = "encryptedai"

# Get the absolute path to the current folder
folder_path = os.path.abspath(os.path.dirname(__file__))

# Create the base launch command prefix
activate_and_cd = f'conda activate {env_name} && cd /d "{folder_path}" && '

# List of scripts to run
scripts = ["server.py", "client_a.py", "client_b.py", "client_c.py", "client_d.py", "client_e.py"]

# Launch server first
print("[INFO] Launching Flower Server...")
subprocess.Popen(["cmd.exe", "/k", activate_and_cd + "python server.py"])

# Wait 5 seconds for the server to start
time.sleep(5)

# Launch all clients
for script in scripts[1:]:
    print(f"[INFO] Launching {script}...")
    subprocess.Popen(["cmd.exe", "/k", activate_and_cd + f"python {script}"])
