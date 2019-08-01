# ACI Cobra Packets
from cobra.mit.access import MoDirectory
from cobra.mit.session import LoginSession
from cobra.mit.request import ConfigRequest
from cobra.internal.codec.xmlcodec import toXMLStr

# ACI Models
from cobra.model.fv import Tenant
from cobra.model.fv import Ap
from cobra.model.vz import Filter

def get_tenantByName(moDir, name):

	# Lookup Object
	mo = moDir.lookupByDn('uni/tn-{0}'.format(name))
	return mo

def get_tenants(moDir):

	# Lookup Object
	moList = moDir.lookupByClass('fvTenant')
	return moList

def get_tenantByName(moDir, name):

	# Lookup Object
	mo = moDir.lookupByDn('uni/tn-{0}'.format(name))
	return mo

def config_obj(moDir, mo):

	# Create Config Request
	CfgRqst = ConfigRequest()
	CfgRqst.addMo(mo)

	# Commit Config Request
	moDir.commit(CfgRqst)

def config_tenant(moDir, name):

	# Build Configuration Object
	uniMo = moDir.lookupByDn('uni')
	new_mo = Tenant(uniMo, name=name)

	config_obj(moDir, new_mo)

def config_app(moDir, tenant, name, descr):

	# Build Configuration Object
	ap_mo = Ap(tenant, name, descr)

	config_obj(moDir, ap_mo)

def apic_login(url, username, password):

	# Create Session
	session = LoginSession(url, username, password)
	moDir = MoDirectory(session)

	#Login
	moDir.login()

	return moDir


if __name__ == "__main__":

	username = 'admin'
	password = 'Cisco123'
	protocol = 'https'
	host = 'apic'

	apic = '{0}://{1}'.format(protocol, host)

	moDir = apic_login(apic, username, password)
	
	config_tenant(moDir, 'Finance')

	tenants = get_tenants(moDir)
	for tenant in tenants:
		print tenant.name

	tenant = get_tenantByName(moDir, 'Finance')
	print 'Dn:',str(tenant.dn)

	config_app(moDir,'Finance-3Tier-App','new ANP for Finance')

