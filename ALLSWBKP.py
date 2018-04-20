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

        tn.write('term len 0\n')
        tn.write('sh run\n')
        tn.write('exit\n')

    elif i is '172.16.126.140':
        user = raw_input('Enter your JUNIPER hostname: ')
        password = getpass.getpass()

        tn = telnetlib.Telnet(HOST[1], timeout = 5)

        tn.read_until('login:')
        tn.write(user + '\n')

        if password:
            tn.read_until('Password:')
            tn.write(password + '\n')
        tn.write('show configuration | display set\n')
        tn.write('exit\n')


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
        tn.write('term len 0\n')
        tn.write('sh runn\n')
        tn.write('exit\n')

    readall = tn.read_all()
    File = open('File' +str(i), 'w')
    File.write(readall)
    File.write('\n')
    File.close()
    print('copy of '+i+' completed')


