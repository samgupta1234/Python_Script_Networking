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

    
    
============================
iosv_l2_cisco_design: Below are the commands we can test or can run any command which are supported into the running devices.
snmp-server community sam RO
snmp-server community sam RW

ntp server 87.81.181.2 
ntp update-calendar

clock timezone PST -8
clock summer-time PDT recurring
service timestamps debug datetime msec localtime 
service timestamps log datetime msec localtime

vlan 100
 name Data
vlan 101
 name Voice
vlan 102
 name Test 

interface vlan 1
 description In-band Management

ip default-gateway 192.168.122.1
