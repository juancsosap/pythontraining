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

from ydk.services import CRUDService
from ydk.providers import NetconfServiceProvider
from ydk.models.openconfig import openconfig_bgp as oc_bgp
from ydk.errors import YPYModelError

#The provider is the underlying implementation that connects to the device
xr_provider = NetconfServiceProvider(address='xrv', port=830, username='cisco', password='cisco', protocol='ssh')

#CRUDSerice provides the CRUD functions
crud_service = CRUDService()

#Configuration entity for BGP
bgp_config = oc_bgp.Bgp()

#Read and print the initial value
initial_bgp = crud_service.read(xr_provider, bgp_config)
print("The initial BGP ASN value is - " + str(initial_bgp.global_.config.as_))

#Set a new value
if initial_bgp.global_.config.as_:
    bgp_config.global_.config.as_ = initial_bgp.global_.config.as_-1
    #Delete the configuration entity so that we can create a new one
    crud_service.delete(xr_provider, bgp_config)
else:
    bgp_config.global_.config.as_ = 65000 
#Create the configuration
crud_service.create(xr_provider, bgp_config)

#Read and print the new value
new_bgp = crud_service.read(xr_provider, bgp_config)
print("The new BGP ASN value is - " + str(new_bgp.global_.config.as_))

if initial_bgp.global_.config.as_:
    #Reset to initial value
    crud_service.delete(xr_provider, bgp_config)
    crud_service.create(xr_provider, initial_bgp)
    #Read and print the value now that we have reset it
    initial_bgp = crud_service.read(xr_provider, bgp_config)
    print("The BGP ASN value is now - " + str(initial_bgp.global_.config.as_))

#Try and set to invalid value
bgp_config.global_.config.as_ = -1
try:
    crud_service.create(xr_provider, bgp_config)
except YPYModelError as e:
    print("Setting the ASN to -1 didn't work, as expected - " + str(e))
   
xr_provider.close()
