
import getpass
import sys
import telnetlib

HOST = '172.16.126.140'
user = raw_input('Enter your hostname: ')
password = getpass.getpass()

tn = telnetlib.Telnet(HOST, timeout = 5)

tn.read_until('login:')
tn.write(user + '\n')

if password:
	tn.read_until('Password:')
	tn.write(password + '\n')
tn.write('configure\n')
for l in range(1,6):
    tn.write('set interfaces lo0 unit 0 family inet address ' + str(l) + '.' + str(l) + '.' + str(l) + '.' + str(l) + '/32\n')
tn.write('commit and-quit\n')
tn.write('exit\n')

print tn.read_all()
