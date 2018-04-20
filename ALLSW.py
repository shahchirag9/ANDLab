import getpass
import sys
import telnetlib

HOST = ('172.16.126.139','172.16.126.140','172.16.126.141') 


for i in HOST:
    if i is '172.16.126.139':

        user = raw_input('Enter your CISCO hostname: ')
        password = getpass.getpass()

        tn = telnetlib.Telnet(HOST[0], timeout = 5)
        tn.read_until('Username:')
        tn.write(user + '\n')

        if password:
      	    tn.read_until('Password:')
	    tn.write(password + '\n')

        tn.write('conf t\n')
        tn.write('int lo0\n')
        tn.write('ip addr 1.1.1.1 255.255.255.255\n')
        tn.write('end\n')
        tn.write('exit\n')

        print tn.read_all()

    elif i is '172.16.126.140':
        user = raw_input('Enter your JUNIPER hostname: ')
        password = getpass.getpass()

        tn = telnetlib.Telnet(HOST[1], timeout = 5)

        tn.read_until('login:')
        tn.write(user + '\n')

        if password:
            tn.read_until('Password:')
            tn.write(password + '\n')
        tn.write('configure\n')
        tn.write('set interfaces lo0 unit 0 family inet address 1.1.1.1/32\n')
        tn.write('commit and-quit\n')
        tn.write('exit\n')

        print tn.read_all()

    elif i is '172.16.126.141':

        user = raw_input('Enter your ARISTA hostname: ')
        password = getpass.getpass()

        tn = telnetlib.Telnet(HOST[2], timeout = 10)

        tn.read_until('Username:')
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

