from netmiko import ConnectHandler

device = {
    'device_type': 'cisco_ios',
    'ip': '192.168.100.65',
    'username': 'cisco',
    'password': 'cisco123!',
}

connection = ConnectHandler(**device)

show_version_output = connection.send_command('show version')
print('Show version:')
print(show_version_output)

connection.disconnect()