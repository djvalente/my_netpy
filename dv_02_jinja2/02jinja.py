
import time
import paramiko
from yaml import safe_load
from jinja2 import Environment, FileSystemLoader

#lista de switchs
with open("/home/djvalente/Devnet/NetPy/dv_02_jinja2/SW_list.yml","r") as handle:
        sw_root = safe_load(handle)

# passar pelos switch
for switch in sw_root["sw_list"]:
    if switch["type"]=="cisco":
        j_file="cisco_vlan.j2"
    else:
        j_file="other..."

    # buscar as VLANs a criar
    with open("/home/djvalente/Devnet/NetPy/dv_02_jinja2/SW_vlans.yml", "r") as handle:
        vlans = safe_load(handle)

    # Preparar o codigo para criar as vlans de acordo com a sintaxe Cisco do template Jinja 2
    j2_env = Environment(
        loader=FileSystemLoader("/home/djvalente/Devnet/NetPy/dv_02_jinja2"), trim_blocks=True, autoescape=True
    )
    template = j2_env.get_template(j_file)
    
    new_vlan_config = template.render(data=vlans)

    conn_params = paramiko.SSHClient()
    conn_params.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    conn_params.connect(
        hostname=switch["ip"],
        port=22,
        username="djvalente1",
        password="Val150732",
        look_for_keys=False,
        allow_agent=False,
    )

    conn = conn_params.invoke_shell()

    conn.send(new_vlan_config + " \n")
    time.sleep(2.0)

    conn.close()