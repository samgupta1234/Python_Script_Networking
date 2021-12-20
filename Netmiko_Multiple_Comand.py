from netmiko import ConnectHandler

iosv_l2_s4 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.122.75',
    'username': 'samar',
    'password': 'samar123',
}

iosv_l2_s5 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.122.76',
    'username': 'samar',
    'password': 'samar123',
}

iosv_l2_s6 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.122.77',
    'username': 'samar',
    'password': 'samar123',
}

with open('iosv_l2_cisco_design') as f:
    lines = f.read().splitlines()
print (lines)

all_devices = [iosv_l2_s4, iosv_l2_s5, iosv_l2_s6]

for devices in all_devices:
    net_connect = ConnectHandler(**devices)
    output = net_connect.send_config_set(lines)
    print (output)
