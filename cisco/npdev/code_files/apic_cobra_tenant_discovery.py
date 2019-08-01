from __future__ import print_function
# Copyright 2016 Cisco Systems, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

#!/usr/bin/env python


# Import access classes
from cobra.mit.access import MoDirectory
from cobra.mit.session import LoginSession
from cobra.mit.request import ConfigRequest
from cobra.mit.request import ClassQuery

# Import model classes
from cobra.model.fvns import VlanInstP, EncapBlk
from cobra.model.infra import RsVlanNs
from cobra.model.fv import Tenant, Ctx, BD, RsCtx, Ap, AEPg, RsBd, RsDomAtt
from cobra.model.vmm import DomP, UsrAccP, CtrlrP, RsAcc

# Turn off warnings
import requests
requests.packages.urllib3.disable_warnings()

# Policy information
TENANT_INFO = [{'name': 'Cobra_Tenant_1',
                'ctx': 'pvn1',
                'bd': 'bd1',
                'ap': [{'name': 'OnlineStore1',
                        'epgs': [{'name': 'app1'},
                                 {'name': 'web1'},
                                 {'name': 'db1'},
                                ]
                       },
                      ]
                },
                {'name': 'Cobra_Tenant_2',
                'ctx': 'pvn2',
                'bd': 'bd2',
                'ap': [{'name': 'OnlineStore2',
                        'epgs': [{'name': 'app2'},
                                 {'name': 'web2'},
                                 {'name': 'db2'},
                                ]
                       },
                      ]
                },
                {'name': 'Cobra_Tenant_3',
                'ctx': 'pvn3',
                'bd': 'bd3',
                'ap': [{'name': 'OnlineStore3',
                        'epgs': [{'name': 'app3'},
                                 {'name': 'web3'},
                                 {'name': 'db3'},
                                ]
                       },
                      ]
                }
              ]

# CONNECT TO APIC
print('Initializing connection to APIC.\n**')
moDir = MoDirectory(LoginSession('https://apic', 'admin', 'cisco123'))
moDir.login()

# Get the top level Policy Universe Directory
uniMo = moDir.lookupByDn('uni')

print("Starting Tenant Creation.\n**")
for tenant in TENANT_INFO:
    print("Creating tenant %s.." % (tenant['name']))
    fvTenantMo = Tenant(uniMo, tenant['name'])
    
    # Create Private Network
    Ctx(fvTenantMo, tenant['ctx'])
    
    # Create Bridge Domain
    fvBDMo = BD(fvTenantMo, name=tenant['bd'])
    
    # Create association to private network
    RsCtx(fvBDMo, tnFvCtxName=tenant['ctx'])
    
    # Create Application Profile
    for app in tenant['ap']:
        print('Creating Application Profile: %s' % app['name'])
        fvApMo = Ap(fvTenantMo, app['name'])
        
        # Create EPGs 
        for epg in app['epgs']:
            
            print("Creating EPG: %s..." % (epg['name'])) 
            fvAEPgMo = AEPg(fvApMo, epg['name'])
            
            # Associate EPG to Bridge Domain 
            RsBd(fvAEPgMo, tnFvBDName=tenant['bd'])

    # Commit each tenant separately
    tenantCfg = ConfigRequest()
    tenantCfg.addMo(fvTenantMo)
    moDir.commit(tenantCfg)
print('All tenants created.\n**')

print("Get the tenants by class.\n**")
tnQuery = ClassQuery('fvTenant')
tnMos = moDir.query(tnQuery)
for tnMo in tnMos:  
    print(tnMo.dn)

print("Get the tenants by DN and delete them.\n**")
for tenant in TENANT_INFO:
    tnMo = moDir.lookupByDn('uni/tn-{0}'.format(tenant['name']))        
    print(tnMo.name)
    print("Deleting tenant %s.." % (tenant['name']))
    tnMo.delete()
    tenantCfg = ConfigRequest()
    tenantCfg.addMo(tnMo)
    moDir.commit(tenantCfg)
    
    

