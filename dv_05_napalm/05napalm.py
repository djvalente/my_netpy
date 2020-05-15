
from napalm import get_network_driver
from jinja2 import Environment, FileSystemLoader
from yaml import safe_load

with open("/home/djvalente/Devnet/NetPy/dv_05_napalm/SW_list.yml","r") as handle:
    sw_root = safe_load(handle)

driver = get_network_driver("ios")  # devices suportados pelo Netmiko (Escolhoemo 'ios')

for switch in sw_root["sw_list"]:
    conn = driver (
        hostname=switch["ip"], username="djvalente1", password="Val150732"
    )
    conn.open()

    facts = conn.get_facts()
    #print (facts)
    print (f"{switch['name']} model type: {facts['model']}")

    """
    # comparação das diferenças e commit das alterções se necessario
    # usavamos o mesmo metodo usado no netmiko (jinja2) para construir a nova config

    conn.load_merge_candidate(config=new_vlan_config)
    diff = conn.compare_config()
    if diff:
        print(diff)
        print("Committing configuration changes")
        conn.commit_config()
    else:
        print("no diff; config up to date")
    """
    conn.close()