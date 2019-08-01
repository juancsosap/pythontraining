from lxml import etree
from ncclient import manager

host = 'csr1kv'
port = 830
user = 'cisco'
pwd = 'cisco'

if __name__ == "__main__":

	with manager.connect(host=host, port=port, username=user, password=pwd, hostkey_verify=False, device_params={'name': 'csr'}, allow_agent=False, look_for_keys=False) as device:

		get_filter = """
			<native xmkns="http://www.cisco.com/ns/yang/ned/ios">
			 <interface>
			  <GigabitEthernet>
			   <name>1</name>
			  </GigabitEthernet>
			 </interface>
			</native> 
		"""

		nc_get_reply = device.get(('subtree', get_filter))
		print etree.tostring(nc_get_reply.data_ele, pretty_print=True)

		nc_filter = """
			<config>
			 <native xmkns="http://www.cisco.com/ns/yang/ned/ios">
			  <interface>
			   <Loopback>
			    <name>101</name>
			    <ip>
			     <address>
			      <primary>
			       <address>10.101.1.1</address>
			       <mask>255.255.255.0</mask>
			      </primary>
			      <secondaries>
			       <secondary>
			        <address>20.101.1.1</address>
			        <mask>255.255.255.0</mask>
			       </secondary>
			      </secondaries>
			     </address>
			    </ip>
			   </Loopback>
			  </interface>
			 </native>
			</config>
		""" 

		nc_reply = device.edit_config(target='running', config=nc_filter)
		print nc_reply
		print type(nc_reply)