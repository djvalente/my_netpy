import time
import paramiko

conn_params = paramiko.SSHClient()

conn_params.set_missing_host_key_policy(paramiko.AutoAddPolicy())
conn_params.connect(
    hostname="10.128.23.1",
    port=22,
    username="djvalente1",
    password="Val150732",
    look_for_keys=False,
    allow_agent=False,
)

# Get an interactive shell
conn = conn_params.invoke_shell()

conn.send("terminal length 0 \n")
conn.send("show running-config \n")
time.sleep(2.0)

with open("sw_bit_run.txt","w") as handle:
    handle.write(conn.recv(65535).decode("utf-8"))

conn.close()
