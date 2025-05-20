import subprocess
import time
import os

# Conda environment name
env = "encryptedai"

# Absolute path to this directory
base_path = r"C:\Users\kmadu\Downloads\Projects\EncryptedAI\federated"

# Scripts to launch
client_scripts = [
    "client_a.py",
    "client_b.py",
    "client_c.py",
    "client_d.py",
    "client_e.py"
]

# Launch server
print("[INFO] Starting server...")
subprocess.Popen(
    ["cmd.exe", "/k", f'conda activate {env} && python server.py'],
    cwd=base_path,  # ✅ sets working directory directly
    creationflags=subprocess.CREATE_NEW_CONSOLE

)

# Wait a few seconds before starting clients
time.sleep(10)

# Launch each client in a new terminal
for script in client_scripts:
    print(f"[INFO] Launching {script}...")
    subprocess.Popen(
        ["cmd.exe", "/k", f'conda activate {env} && python {script}'],
        cwd=base_path,
        creationflags=subprocess.CREATE_NEW_CONSOLE
    )
    time.sleep(1)


# #new code 
# import subprocess
# import time
# import os

# # Conda environment name
# env = "encryptedai"

# # Absolute path to this directory
# base_path = r"C:\Users\kmadu\Downloads\Projects\EncryptedAI\federated"

# # Scripts to launch
# client_scripts = [
#     "client_a.py",
#     "client_b.py",
#     "client_c.py",
#     "client_d.py",
#     "client_e.py"
# ]

# # Launch server in a new terminal window
# print("[INFO] Starting server...")
# subprocess.Popen(
#     ["cmd.exe", "/k", f'conda activate {env} && cd /d "{base_path}" && python server.py'],
#     creationflags=subprocess.CREATE_NEW_CONSOLE  # ✅ keeps it alive in a new window
# )

# # Wait to let server boot up
# time.sleep(10)

# # Launch clients in separate terminal windows
# for script in client_scripts:
#     print(f"[INFO] Launching {script}...")
#     subprocess.Popen(
#         ["cmd.exe", "/k", f'conda activate {env} && cd /d "{base_path}" && python {script}'],
#         creationflags=subprocess.CREATE_NEW_CONSOLE  # ✅ separate window per client
#     )
#     time.sleep(3)  # Optional: Stagger to avoid race conditions
