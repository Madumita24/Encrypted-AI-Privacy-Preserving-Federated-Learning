import subprocess
import time
import os

env = "encryptedai"
base_path = r"C:\Users\kmadu\Downloads\Projects\Encrypted AI – Privacy-Preserving Federated Learning\federated"


scripts = [
    "client_a.py", "client_b.py", "client_c.py", "client_d.py", "client_e.py"
]

# Start server
subprocess.Popen(["cmd.exe", "/k", f'conda activate {env} && cd /d "{base_path}" && python server.py'])
time.sleep(3)

# Start each client
for script in scripts:
    subprocess.Popen(["cmd.exe", "/k", f'conda activate {env} && cd /d "{base_path}" && python {script}'])
