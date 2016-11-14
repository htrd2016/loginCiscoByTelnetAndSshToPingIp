#username password cisco_ip ip_to_ping zabbix_server_ip
nohup python ./pingByTelnetSwitch.py test test 192.168.103.252 192.168.103.51 192.168.103.112 > pingByTelnetSwitch.log &
nohup python ./pingBySSHRouter.py test test 192.192.96.254 192.168.103.51 192.168.103.112 > pingBySSHRouter.log &
