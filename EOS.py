import getpass
import sys
import telnetlib

HOST = '172.16.126.141'
user = raw_input('Enter your hostname: ')
password = getpass.getpass()

tn = telnetlib.Telnet(HOST, timeout = 10)

tn.read_until('Username: ')
tn.write(user + '\n')

if password:
	tn.read_until('Password:')
	tn.write(password + '\n')
tn.write('en\n')
tn.write('conf t\n')
tn.write('int lo 0\n')
tn.write('ip addr 1.1.1.1 255.255.255.255\n')
tn.write('end\n')
tn.write('exit\n')

print tn.read_all()
