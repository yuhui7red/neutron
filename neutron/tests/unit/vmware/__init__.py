# vim: tabstop=4 shiftwidth=4 softtabstop=4

# Copyright 2013 OpenStack Foundation.
# All Rights Reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

import os

import neutron.plugins.nicira.api_client.client_eventlet as client
from neutron.plugins.nicira import extensions
import neutron.plugins.nicira.NvpApiClient as nsxapi
from neutron.plugins.nicira import nvplib
from neutron.plugins.nicira.vshield.common import VcnsApiClient as vcnsapi
from neutron.plugins.nicira.vshield import vcns
import neutron.plugins.nicira.vshield.vcns_driver as vcnsdriver
import neutron.plugins.vmware.plugin as neutron_plugin

plugin = neutron_plugin.NsxPlugin
service_plugin = neutron_plugin.NsxServicePlugin
api_helper = nsxapi.NVPApiHelper
api_client = client.NvpApiClientEventlet
vcns_class = vcns.Vcns
vcns_driver = vcnsdriver.VcnsDriver
vcns_api_helper = vcnsapi.VcnsApiHelper

STUBS_PATH = os.path.join(os.path.dirname(__file__), 'etc')
NSXEXT_PATH = os.path.dirname(extensions.__file__)
NSXAPI_NAME = '%s.%s' % (api_helper.__module__, api_helper.__name__)
NSXLIB_NAME = nvplib.__name__
PLUGIN_NAME = '%s.%s' % (plugin.__module__, plugin.__name__)
SERVICE_PLUGIN_NAME = '%s.%s' % (service_plugin.__module__,
                                 service_plugin.__name__)
CLIENT_NAME = '%s.%s' % (api_client.__module__, api_client.__name__)
VCNS_NAME = '%s.%s' % (vcns_class.__module__, vcns_class.__name__)
VCNS_DRIVER_NAME = '%s.%s' % (vcns_driver.__module__, vcns_driver.__name__)
VCNSAPI_NAME = '%s.%s' % (vcns_api_helper.__module__, vcns_api_helper.__name__)


def get_fake_conf(filename):
    return os.path.join(STUBS_PATH, filename)


def nsx_method(method_name, module_name='nvplib'):
    return '%s.%s.%s' % ('neutron.plugins.nicira', module_name, method_name)
