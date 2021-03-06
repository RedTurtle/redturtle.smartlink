Changelog
=========

1.3.3 (unreleased)
------------------

- Nothing changed yet.


1.3.2 (2017-04-24)
------------------

- Removed wrong import in `keepLink` event.
  [cekk]


1.3.1 (2017-03-28)
------------------

- Fixed issue with new proxy feature.
  Local activation flag was unproperly ignored
  [keul]
- Fixed an error at creation object
  [ekulos]
- Fix `keepLink` event. now we handle correctly DX and AT contents
  [cekk]

1.3.0 (2016-12-23)
------------------

- End of the official support to Plone 3: it *may* still work but has not been tested.
  [keul]
- New feature: a way to use title and description of the referenced internal content
  (Poor Man `bda.contentproxy`__).
  This close `#6`__.
  [keul]

__ https://pypi.python.org/pypi/bda.contentproxy
__ https://github.com/RedTurtle/redturtle.smartlink/issues/6

1.2.2 (2016-06-15)
------------------

- Fix `keepLink` event for Dexterity items (with referenceablebehavior enabled)
  referenced by a smartlink. Now we can delete the DX content without errors.
  [cekk]


1.2.1 (2013-02-15)
------------------

- Removed longly deprecated actionicons.xml [keul]
- Modern inclusion of referencebrowserwidget [keul]
- Restored tests on Plone 3.3 that were broken in version 1.2 [keul]
- Removed old ununsed import step (close `#1`__) [keul]
- Fixed product to be Plone 4.3 compatible [keul]
- Old (4.2 and below) link_icon.gif now included with the product [keul]

__ https://github.com/RedTurtle/redturtle.smartlink/issues/1

1.2.0 (2012-10-25)
------------------

- Added support for plone.app.imaging [cekk]

1.1.3 (2012-09-13)
------------------

* Smart Link uninstall was changing the Generic Setup baseline context.
  When we found it, we restore the "``profile-Products.CMFPlone:plone``"
  (part of issue `#1`__)
  [keul]
* when uninstalling, restore old ATLink automatically
  [keul]
* fixed many bad formatted portal messages visualization
  [keul]
* uninstall now remove the persisten utility (fix the other
  part of issue `#1`__)
  [keul]

__ https://github.com/RedTurtle/redturtle.smartlink/issues/1
__ https://github.com/RedTurtle/redturtle.smartlink/issues/1

1.1.2 (2012-05-23)
------------------

* fixed a bug on Plone 3 if plone.app.blob is not present [keul]

1.1.1 (2012-05-18)
------------------

* fixed tests for Plone 4.2 compatibility [keul]
* migrating "fake external links" now support the migration of URLs that
  explicitly use "*resolveuid*" (sometimes Plone users are really evil)
  [keul]

1.1.0 (2012-02-20)
------------------

* added a link to the view that migrate to blob from the control panel [keul]
* added a new ``Smart Link: access configuration`` permission for site configuration
  that "Site Administrator" role can handle [keul]
* added an utility to convert "fake external" link to internal [keul]
* aligned all ``Link.xml`` files to be Plone 4 compliant [keul]
* In Plone 4 the related items were duplicated (if used).
  Now Plone 3.3 requires `collective.relateditems`__ [keul]
* Moved URL transformation features to an ``ILinkNormalizerUtility`` [keul]
* fixed all tests to be compatible again with Plone 3.3.6 [keul]
* fixed bug when providing a non ASCII URL (close `#8`__) [keul]
* provide a count of updated links when using the administration
  utility (close `#6`__) [keul]
* provided an import step to migrate ATLink to Smart Link (close `#7`__) [keul]
* provided an import step to go back to ATLink from Smart Link [keul]

__ http://plone.org/products/collective.relateditems
__ http://plone.org/products/smart-link/issues/8
__ http://plone.org/products/smart-link/issues/6
__ http://plone.org/products/smart-link/issues/7

1.0.0 (2011-11-03)
------------------

* Plone 4.1 compatibility
* size of a smart link is the size of its image [keul]
* finally removed the fss.zcml. It's time to BLOB man! [keul]
* added the BLOB extension for image field [mircoangelini]
* added BLOB migration view: ``blob-smartlink-migration`` [mircoangelini]
* fixed icon handling, going back to the Plone 3 icons, disabling
  Sunburst CSS-sprite with a new ``smart_link.css`` resource [keul]
* when linking an internal content, do not display a simple URL
  but a link using item's title [keul]

1.0.0rc2 (2010-11-06)
---------------------

* reStructured text fixes [keul]
* uninstall was not working under Plone 4.0 (this close `#5`__) [keul]
* URL utility description updated with latests features added in 1.0 version [keul]
* fixed duplicated icon when using (or not using anymore) this product on Plone 4 (close `#4`__).
  To make those additional icon disappear from Plone UI you may need a catalog update. [keul]
* configuration icon was not displayed properly on Plone 4 [keul]
* added the "*Front-end main URL*" feature (close `#3`__) [keul]

__ http://plone.org/products/smart-link/issues/5
__ http://plone.org/products/smart-link/issues/4
__ http://plone.org/products/smart-link/issues/3

1.0.0rc1 (2010-09-12)
---------------------

* Plone 4 compatibility [keul]
* The explicit use of *iw.fss* has been removed. The *fss.zcml* is still there and you can still include
  it if you like, but you must do this manually [keul]
* *ISmartLink* also extends the *IImageContent* interface [keul]
* A better uninstall procedure, that remove Plone UI stuff and restore original linked object status [keul]
* Added the *favicon* field, that drive the icon's link [keul]
* Added the *anchor* field, for manage anchor in internal links [keul]
* Moved new and old secondary fields to the *Advanced* fieldset [keul]
* The "unlink" event when deleting a referenced object has been removed: keeping an additional index only for
  this feature was not a soo good idea. Now the internal link will display the latest memoized link [keul]
* Aligned the *smartlink_view* with the latest Plone *link_view*, so now will also display the message
  when you are not redirected to the target URL (however this will be untranslated on Plone < 3.3) [keul]
* Added tests [keul]
* Updated and fixed labels and texts all around and i18n translation too [keul]
* Splitted UI error warn when you don't provide neither internal and external link, from the fact that you
  provide both of them [keul]
* When unlinking an internal content, it's cleaned from marker interface [keul]
* Switched front-end and back-end order in the config panel [keul]
* Fixed a bug that force the front-end URLs in config panel to be unique [keul]

0.7.3 (2010-06-03)
------------------

* fix #2 - error upgrading from 0.4.* to 0.7.* (missing utility) [mauro]

0.7.2 (2010-04-06)
------------------

* The "*smartLink*" event was using *directlyProvides* instead of *alsoProvides*... this was
  corrupting some target objects (like: it was impossible to internally link a file that
  use blobs) [keul]
* Removed the Plone 3.3+ dependency because Smart Link is providing the same feature
  given by Plone 3.3 also on older Plone versions [keul]

0.7.1 (2010-03-26)
------------------

* Version 0.7 had a stupid, unused dependency [keul]

0.7.0 (2010-03-26)
------------------

* Added z3c.autoinclude support [keul]
* From this version the minimum requirement is Plone *3.3* [keul]
* Aligned with changes done to ATLink from Plone 3.3 [keul]
* Added a fake *link_redirect_view* [keul]

0.6.1 (2010-03-10)
------------------

* Fixed egg format [keul]
* README updated [keul]

0.6.0 (Unreleased)
------------------

* Changed name of tool [fdelia]
* Added icon for tool [fdelia]

0.5.1 (2010-02-02)
------------------

* Fix for the corrupted version 0.5.0 [fdelia]

0.5.0 (2010-01-25)
------------------

* Added configuration panel to transform back-end links in front-end links [fdelia]
* Added configuration panel to have internal links relative and not absolute [fdelia]

0.4.0 (2009-09-12)
------------------

* Keep relations of internal link even if the target content is renamed/moved [keul]
* Added a marker interface for internally linked contents [keul]
* When target object is deleted, the internal relation became a normal absolute URL info [keul]

0.3.1 (2009-08-30)
------------------

* Restored the original *remoteUrl* StringField , due to continuous bad integration with 3rd party
  products (like p4a and collective.flowplayer) [keul]

0.3.0 (2009-08-02)
------------------

* Fixed syntax error on relation name ("internal_page" was "interal_page") [keul]
* Disabled the backup of basic Plone ATLink [keul]
* Fixed some integration problem in content/link.py related to p4a (remoteUrl) [lucabel]
* Fixed major bug in post_validate (validation was useless) [fdelia]
* Internalization with i18ndude [fdelia]
* Created italian translation [micecchi]
* Clean uninstall (restoring the original ATLink in portal_types) [keul]

0.2.0beta (2009-04-03)
----------------------

* Added a lot of ATLink methods not migrated to the SmartLink class.
* Fixed a bug that lead all reordering actions in folders with SmartLink inside to failure (or to chaotic results).
  After migrating to this version from the 0.1.0 you can also launch the **fix_meta_data** external method
  or your folder will remains broken.

0.1.0dev (2009-03-27)
---------------------

* Initial release
