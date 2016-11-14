import telnetlib
import time
import os
import sys

user = sys.argv[1]
password = sys.argv[2]
serverip =  sys.argv[3]
iptoping = sys.argv[4]
zabbixserverip = sys.argv[5]

tn = telnetlib.Telnet(serverip)

tn.read_until("Username: ")
tn.write(user + "\n")

if password:
    print(tn.read_until("Password: "))
    tn.write(password + "\n")
#    print(password)
    #print(tn.read_all())
    tn.read_until(">")

while True:
    try:
        tn.write("ping " + iptoping + "\r\n")
        data = tn.read_until(">")
        print(data)
        indexStart = data.find("Success rate is ")
        indexEnd = data.find(" percent");
        if (indexStart>0 and indexEnd>0):
            #print(indexStart)
            #print(indexEnd)
            indexStart+=16
            per = data[indexStart:indexEnd]
            print(per.strip())
            os.system("zabbix_sender -z "+ zabbixserverip +" -s \"cisco router\" -k router.ping.mc -o "+per.strip())
        time.sleep(1)
#       print(indexStart)
    except Exception,e:  
        print Exception,":",e
        time.sleep(10)

tn.write("exit\n")

print(tn.read_all()) 
