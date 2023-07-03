from netmiko import ConnectHandler

device = {
    'device_type': 'cisco_ios',
    'ip': '192.168.100.65',
    'username': 'cisco',
    'password': 'cisco123!',
}

connection = ConnectHandler(**device)

interface_ip_output = connection.send_command('show ip interface brief')
print('Información de las IP y estado de las interfaces:')
print(interface_ip_output)


connection.disconnect()
