
from netmiko import Netmiko
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

    conn = Netmiko(
        host=switch["ip"],
        username="djvalente1",
        password="Val150732",
        device_type="cisco_ios"   #aqui poderiamos usar a variavel do tipo 
    )

    result = conn.send_config_set(new_vlan_config.split("\n"))

    print(result)

    conn.disconnect()
