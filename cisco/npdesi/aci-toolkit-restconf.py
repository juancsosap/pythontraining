def apic_login(url, username, password):

	# Create Session
	session = Session(url, username, password)

	#Login
	session.login()

	return session

def get_tenant(session, name):

	# Get all Tenants
	tenants = Tenant.get(session)

	# Get Spacific Tenant
	tenant = Tenant.get_deep(session, [name])

	return tenant

def commit_obj(session, obj):

	# Check Objectreate Config Request
	obj.get_json()

	# Commit Config Request
	obj.push_to_apic(session)


if __name__ == "__main__":

	username = 'admin'
	password = 'Cisco123'
	protocol = 'https'
	host = 'apic'

	apic = '{0}://{1}'.format(protocol, host)

	session = apic_login(apic, username, password)

	tenant = Tenant('Finance')

	app = AppProfile('app_tk', tenant)

	context = Context('vrf_tk', tenant)

	bd = BridgeDomain('bd_tk', tenant)
	bd.add_context(context)

	epg = EPG('epg_tk', app)
	epg.add_bd(bd)

	resp = session.push_to_apic(tenant.get_url(), tenant.get_json())



	interfaces = Interface.get(session)
	interfaces = Interface.get(session=session, pod_parent='1', node='101', module='1', port='15')

	intf = interfaces[0]
	print intf.porttype # Print leaf

	print intf.port # Print 15

	print intf.name # Print eth 1/101/1/15

	print intf.mtu # Print 9000

	print intf.adminstatus # Print up

	print intf.speed # Print inherit

	print intf.descr # Print None

	print intf.is_cdp_enabled() # Print False


	while True:
		if Tenant.has_events(session):
			tenant = Tenant.get_event(session)
			if tenant.is_deleted():
				print('Tenant:', tenant.name, '(deleted)')
			else:
				print('Tenant:', tenant.name, '(created or modified)')



