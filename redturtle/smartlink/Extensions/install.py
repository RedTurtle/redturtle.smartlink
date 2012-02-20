# -*- coding: utf-8 -*-

from redturtle.smartlink import logger
from zope import interface
from Products.CMFPlone.utils import getFSVersionTuple

from redturtle.smartlink.interfaces import ISmartLinked
from redturtle.smartlink import smartlinkMessageFactory as _

def install(portal, reinstall=False):
    setup_tool = portal.portal_setup
    setup_tool.setBaselineContext('profile-redturtle.smartlink:default')
    setup_tool.runAllImportStepsFromProfile('profile-redturtle.smartlink:default')
    if not reinstall:
        portal.plone_utils.addPortalMessage(_('install_info',
                                              default=u'Starting from now, all Links created in this site will be Smart Link.\n'
                                                      u'If you have already created Link types in this site, you can migrate '
                                                      u'them to Smart Link using the "Smart Link: migrate ATLink to Smart Link" '
                                                      u'import step.'),
                                            type='info')


def uninstall(portal, reinstall=False):
    setup_tool = portal.portal_setup
    setup_tool.setBaselineContext('profile-redturtle.smartlink:uninstall')
    setup_tool.runAllImportStepsFromProfile('profile-redturtle.smartlink:uninstall')
    if getFSVersionTuple()[0]>=4:
        unregisterIcon(portal)
    if not reinstall:
        removeSmartLinkMarks(portal)
        portal.plone_utils.addPortalMessage(_('uninstall_warning',
                                              default=u'Keep in mind that contents created with Smart Link are still using Smart Link code '
                                                      u'and they will be broken if you remove the product from your Plone installation.\n'
                                                      u'You can convert them back to basic ATLink using the "Smart Link: migrate from Smart Link to ATLink" '
                                                      u'import step.'),
                                            type='warning')


def removeSmartLinkMarks(portal):
    """Remove all Smart Link marker interfaces all around the site"""
    catalog = portal.portal_catalog
    smartlinkeds = catalog(object_provides=ISmartLinked.__identifier__)

    logger.info("Uninstall Smart Link: removing flag to internally linked contents...")
    for linked in smartlinkeds:
        content = linked.getObject()
        # Bee lazy, so use the already developed procedure for the delete-events
        unLink(portal, content)
        interface.noLongerProvides(content, ISmartLinked)
        content.reindexObject(['object_provides'])
        logger.info("   unmarked %s" % '/'.join(content.getPhysicalPath()))
    logger.info("...done. Thanks you for using me!")

    # TODO: the perfect world is the one where SmartLink(s) are converted back to ATLink(s)


def unLink(portal, object):
    """Remove the reference from the smart link and the object itself, changing the internal link to
    a normal external link.
    """
    reference_catalog = portal.reference_catalog
    backRefs = reference_catalog.getBackReferences(object, relationship='internal_page')
    for r in backRefs:
        r.setInternalLink(None)
        r.setExternalLink(object.absolute_url())
        r.reindexObject(['getRemoteUrl'])


def unregisterIcon(portal):
    """Remove icon expression from Link type"""
    portal_types = portal.portal_types
    link = portal_types.getTypeInfo("Link")
    #link.icon_expr = ''
    link.content_icon = ''
    link.manage_changeProperties(content_icon='', icon_expr='')
    logger.info("Removing icon type info")


