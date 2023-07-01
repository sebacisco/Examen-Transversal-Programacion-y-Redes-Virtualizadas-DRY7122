from ncclient import manager

router_ip = "192.168.100.65"
username = "cisco"
password = "cisco123!"

new_hostname = "GonzalezLicanqueoHenriquez"

config_template = '''
<config>
    <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
        <hostname>{new_hostname}</hostname>
    </native>
</config>
'''

with manager.connect(
    host=router_ip,
    port=830,
    username=username,
    password=password,
) as m:
    config = config_template.format(new_hostname=new_hostname)
    response = m.edit_config(target="running", config=config)
    print("Cambio de nombre del router exitoso")
