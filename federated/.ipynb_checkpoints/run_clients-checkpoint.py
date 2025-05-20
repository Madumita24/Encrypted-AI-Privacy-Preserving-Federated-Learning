import subprocess
import os
import time

# Set your Conda environment name
env_name = "encryptedai"

# Paths
project_root = os.path.dirname(os.path.dirname(__file__))  # go up from /federated/
server_dir = os.path.join(project_root, "server")
client_dir = os.path.join(project_root, "client")

# Client script names
client_scripts = [
    "client_a.py",
    "client_b.py",
    "client_c.py",
    "client_d.py",
    "client_e.py"
]

# Start the server
print("[INFO] Launching Flower Server...")
subprocess.Popen([
    "cmd.exe", "/k",
    f"conda activate {env_name} && cd /d {server_dir} && python server.py"
])

# Give server a few seconds to start
time.sleep(20)

# Start clients
for script in client_scripts:
    print(f"[INFO] Launching {script}...")
    subprocess.Popen([
        "cmd.exe", "/k",
        f"conda activate {env_name} && cd /d {client_dir} && python {script}"
    ])
