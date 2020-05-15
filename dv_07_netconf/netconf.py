"""
Script usa NETCONF para retirar configs de uma lista de Switch num formato XML
"""

from ncclient import manager
from lxml.etree import tostring
from yaml import safe_load

with open("/home/djvalente/Devnet/NetPy/dv_07_netconf/SW_list.yml", "r") as handle:
    SW_ROOT = safe_load(handle)

for switch in SW_ROOT["sw_list"]:
    connect_params = {
        "host": switch["ip"],
        "username": "djvalente1",
        "password": "Val150732",
        "hostkey_verify": False,
        "allow_agent": False,
        "look_for_keys": False,
    }
    with manager.connect(**connect_params) as conn:
        print(f"{switch['ip']}: Connection open")

        get_resp = conn.get_config(source="running")
        if get_resp.ok:
            xml_config = tostring(get_resp.data_ele, pretty_print=True)
            print(xml_config.decode().strip())
        else:
            print(f"{switch['ip']}: Errors: {','.join(get_resp.errors)}")
