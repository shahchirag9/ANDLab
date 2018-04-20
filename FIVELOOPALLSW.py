import getpass
import sys
import telnetlib

HOST = ('172.16.126.139','172.16.126.140','172.16.126.141') 

user = raw_input('Enter your hostname: ')
password = getpass.getpass()

for i in HOST:
    if i is '172.16.126.139':


        tn = telnetlib.Telnet(HOST[0], timeout = 5)
        tn.read_until('Username:')
        tn.write(user + '\n')

        if password:
      	    tn.read_until('Password:')
	    tn.write(password + '\n')

        tn.write('conf t\n')
        for l in range(1,6):
            tn.write('int lo ' + str(l) + '\n')
            tn.write('ip addr ' + str(l) + '.' + str(l) + '.' + str(l) + '.' + str(l) + ' 255.255.255.255\n')
        tn.write('end\n')
        tn.write('exit\n')

        print tn.read_all()

    elif i is '172.16.126.140':

        tn = telnetlib.Telnet(HOST[1], timeout = 5)

        tn.read_until('login:')
        tn.write(user + '\n')

        if password:
            tn.read_until('Password:')
            tn.write(password + '\n')
	for l in range(1,6):
            tn.write('configure\n')
            tn.write('set interfaces lo0 unit' + str(l) + 'family inet address ' + str(l) + '.' + str(l) + '.' + str(l) + '.' + str(l) + '/32\n')
        tn.write('commit and-quit\n')
        tn.write('exit\n')

        print tn.read_all()

    elif i is '172.16.126.141':


        tn = telnetlib.Telnet(HOST[2], timeout = 10)

        tn.read_until('Username:')
        tn.write(user + '\n')

        if password:
            tn.read_until('Password:')
            tn.write(password + '\n')
        tn.write('en\n')
        tn.write('conf t\n')
	for l in range(1,6):
            tn.write('int lo ' + str(l) + '\n' )
            tn.write('ip addr ' + str(l) + '.' + str(l) + '.' + str(l) + '.' + str(l) + ' 255.255.255.255\n')
        tn.write('end\n')
        tn.write('exit\n')

        print tn.read_all()

