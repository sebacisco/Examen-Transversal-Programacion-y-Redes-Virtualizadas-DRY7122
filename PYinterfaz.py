from ncclient import manager

router_ip = "192.168.100.65"
username = "cisco"
password = "cisco123!"

config_template = '''
<config>
  <interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
    <interface>
      <name>Loopback2</name>
      <description>Interfaz</description>
      <type xmlns:ianaift="urn:ietf:params:xml:ns:yang:iana-if-type">ianaift:softwareLoopback</type>
      <enabled>true</enabled>
      <ipv4 xmlns="urn:ietf:params:xml:ns:yang:ietf-ip">
        <address>
          <ip>2.2.2.2</ip>
          <netmask>255.255.255.255</netmask>
        </address>
      </ipv4>
    </interface>
  </interfaces>
</config>
'''
with manager.connect(
    host=router_ip,
    port=830,
    username=username,
    password=password,
) as m:
    response = m.edit_config(target="running", config=config_template)
    print("Cambio de interfaz exitoso")


