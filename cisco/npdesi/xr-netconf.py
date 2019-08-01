from lxml import etree
from ncclient import manager

host = 'xrv'
port = 830
user = 'cisco'
pwd = 'cisco'

if __name__ == "__main__":

	with manager.connect(host=host, port=port, username=user, password=pwd, hostkey_verify=False, device_params={'name': 'iosxr'}, allow_agent=False, look_for_keys=False) as device:

		get_filter = """
			<interface-configurations xmkns="http://www.cisco.com/ns/yang/Cisco-IOS-XR-ifmgr-cfg">
			 <interface-configuration>
			  <interface-name>MgmtEth0/0/CPU0/0</interface-name>
			 </interface-configuration>
			</interface-configurations> 
		"""

		nc_get_reply = device.get(('subtree', get_filter))
		print etree.tostring(nc_get_reply.data_ele, pretty_print=True)

		nc_filter = """
			<config>
			 <interface-configurations xmkns="http://www.cisco.com/ns/yang/Cisco-IOS-XR-ifmgr-cfg">
			  <interface-configuration>
			   <active>act</active>
			   <interface-name>Loopback100</interface-name>
			   <interface-virtual/>
			  </interface-configuration>
			 </interface-configurations>
			</config>
		""" 

		nc_reply = device.edit_config(target='cadidate', config=nc_filter)
		device.commit()
		
		print nc_reply
		print type(nc_reply)