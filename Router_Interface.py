import getpass
import telnetlib

HOST = "10.10.10.100"
user = input("Enter your telnet account: ")
password = getpass.getpass()

tn = telnetlib.Telnet(HOST)

tn.read_until(b"Username: ")
tn.write(user.encode('ascii') + b"\n")
if password:
    tn.read_until(b"Password: ")
    tn.write(password.encode('ascii') + b"\n")

tn.write(b"ena\n")
tn.write(b"samar123\n")
tn.write(b"sh ip int bri\n")
tn.write(b"conf t\n")
tn.write(b"int lo0\n")
tn.write(b"ip add 100.100.100.100 255.255.255.255\n")
tn.write(b"end\n")
tn.write(b"exit\n")

print(tn.read_all().decode('ascii'))
