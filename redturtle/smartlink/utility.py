from zope.interface import implements
from zope.schema.fieldproperty import FieldProperty
from zope.component import getUtility
from redturtle.smartlink.interfaces.utility import ISmartlinkConfig
from redturtle.smartlink import smartlinkMessageFactory as _
from OFS.SimpleItem import SimpleItem

def rn_config_adapter(context):
    """Form Adapter"""
    return getUtility(ISmartlinkConfig,name="smartlink_config",context=context)

class SmartlinkConfig(SimpleItem):
    """Smartlink Utility"""
    implements(ISmartlinkConfig)
    relativelink = FieldProperty(ISmartlinkConfig['relativelink'])
    frontendlink = FieldProperty(ISmartlinkConfig['frontendlink'])
    backendlink= FieldProperty(ISmartlinkConfig['backendlink'])
    