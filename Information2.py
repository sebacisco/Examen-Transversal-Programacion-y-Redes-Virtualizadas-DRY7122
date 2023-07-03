from netmiko import ConnectHandler

device = {
    'device_type': 'cisco_ios',
    'ip': '192.168.100.65',
    'username': 'cisco',
    'password': 'cisco123!',
}

connection = ConnectHandler(**device)

running_config_output = connection.send_command('show running-config')
print('Running-config:')
print(running_config_output)

connection.disconnect()
