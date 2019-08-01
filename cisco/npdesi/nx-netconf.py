#!/usr/bin/env python

from ncclient import manager

host = 'nxosv'
port = 22
user = 'cisco'
pwd = 'cisco'

# GET REQUEST - Get Info

device = manager.connect(host=host, port=port, username=user, password=pwd, hostkey_verify=False, device_params={'name': 'nexus'}, allow_agent=False, look_for_keys=False)

get_filter = """
				<show>
				 <hostname>
				 </hostname>
				</show>
			 """

nc_get_reply = device.get(('subtree', get_filter))
print nc_get_reply.xml
ns_map = {'mod': 'http://www.cisco.com/nxos:1.0:vdc_mgr'}
xml_rsp = nc_get_reply.data_ele.find('.//mod:hostname', ns_map)
value = xml_rsp.text
print value

device.close_session()

# EXEC_COMMAND REQUEST

with manager.connect(host=host, port=port, username=user, password=pwd, hostkey_verify=False, device_params={'name': 'nexus'}, allow_agent=False, look_for_keys=False) as device:

	commands = ['configure terminal', 
	           'interface Ethernet2/6', 
	           'description "Configured by Python ncclient"']

	nc_config_reply = device.exec_command(commands)
