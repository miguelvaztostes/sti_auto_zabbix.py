import os
import pandas as pd
from pyzabbix import ZabbixAPI

zabbix_url = 'http://enderecozabbix/zabbix'
zabbix_user = 'user'
zabbix_password = 'senha'

zabbix = ZabbixAPI(zabbix_url)
zabbix.login(zabbix_user, zabbix_password)


file_path = os.path.join(os.getcwd(), 'DHCP APS FMRP Vlan 130', 'cameras_fmrp.xlsx')

template_name = 'Hikvision camera by HTTP'


df_hosts = pd.read_excel(file_path, usecols=[6, 9], names=['Nome', 'IP'], skiprows=[0])


for index, row in df_hosts.iterrows():

    hostname = row['Nome']
    ip_address = row['IP']

    
    host = zabbix.host.create(
        host=hostname,
        interfaces=[{
            'type': 2, 
            'main': 1,
            'useip': 1,
            'ip': ip_address,
            'dns': '',
            'port': '161',
            'bulk': 1,
            'interfaceid': 0
        }],
        groups=[{
            'groupid': '1'  
        }],
        templates=[{
            'templateid': zabbix.template.get(filter={'host': template_name})[0]['templateid']
        }]
    )

  
    print(f'Host "{hostname}" adicionado com sucesso! ID: {host["hostids"]}')
