# -------------------------------------------------------------------------------
# (c) 2019 Siemens AG
# All Rights Reserved.
# Author: thomas.graf@siemens.com
#
# Licensed as Siemens Inner Source, see top-level License.md file for details.
# -------------------------------------------------------------------------------

import xml.etree.ElementTree as ET


class CliFileItemBase:
    """Common base class to handle files and file hashes"""

    FILES_TAG = "Files"
    FILEHASH_TAG = "FileHash"

    def __init__(self):
        self.files = []
        self.hashes = []

    def read_files_from_element(self, element):
        for elem in element:
            if elem.tag == self.FILES_TAG:
                if elem.text is not None:
                    filelist = elem.text.strip()
                    self.files = filelist.split()
                continue

            if elem.tag == self.FILEHASH_TAG:
                if elem.text is not None:
                    hashlist = elem.text.strip()
                    self.hashes = hashlist.split()
                continue


class CliCopyright(CliFileItemBase):
    """Encapsulates a copyright statement"""

    CONTENT_TAG = "Content"

    def __init__(self):
        CliFileItemBase.__init__(self)
        self.text = ""
        self.files = []
        self.hashes = []

    def read_from_element(self, element):
        self.read_files_from_element(element)
        for elem in element:
            if elem.tag == self.CONTENT_TAG:
                if elem.text is not None:
                    self.text = elem.text.strip()
                continue


class CliLicense(CliFileItemBase):
    """Encapsulates a license"""

    CONTENT_TAG = "Content"
    ACKNOWLEDGEMENTS_TAG = "Acknowledgements"
    TAGS_TAG = "Tags"

    def __init__(self):
        CliFileItemBase.__init__(self)
        self.license_text = ""
        self.type = ""
        self.name = ""
        self.spdx_identifier = ""
        self.acknowledgements = []
        self.tags = []
        self.files = []
        self.hashes = []

    def read_from_element(self, element):
        self.type = element.attrib["type"]
        self.name = element.attrib["name"]

        if "spdxidentifier" in element.attrib:
            self.spdx_identifier = element.attrib["spdxidentifier"]

        self.read_files_from_element(element)

        for elem in element:
            if elem.tag == self.CONTENT_TAG:
                if elem.text is not None:
                    self.license_text = elem.text.strip()
                continue

            if elem.tag == self.ACKNOWLEDGEMENTS_TAG:
                if elem.text is not None:
                    self.acknowledgements.append(elem.text.strip())
                continue

            if elem.tag == self.TAGS_TAG:
                if elem.text is not None:
                    taglist = elem.text.strip()
                    self.tags = taglist.split(" ")
                continue


class CliExportRestriction(CliFileItemBase):
    """Encapsulates an export restriction"""

    CONTENT_TAG = "Content"
    CONTENT_TAG = "Content"

    def __init__(self):
        CliFileItemBase.__init__(self)
        self.export_restriction_text = ""
        self.export_restriction_comment = ""

    def read_from_element(self, element):
        self.read_files_from_element(element)
        for elem in element:
            if elem.tag == self.CONTENT_TAG:
                self.export_restriction_text = elem.text.strip()
                continue


class CliObligation:
    """Encapsulates an obligation"""

    TOPIC_TAG = "Topic"
    TEXT_TAG = "Text"
    LICENSES_TAG = "Licenses"
    LICENSE_TAG = "License"

    def __init__(self):
        self.text = ""
        self.topic = ""
        self.licenses = []

    def read_from_element(self, element):
        for elem in element:
            if elem.tag == self.TOPIC_TAG:
                self.topic = elem.text.strip()
                continue

            if elem.tag == self.TEXT_TAG:
                self.text = elem.text.strip()
                continue

            if elem.tag == self.LICENSES_TAG:
                for elem2 in elem:
                    if elem2.tag == self.LICENSE_TAG:
                        self.licenses.append(elem2.text.strip())
                continue


class CliFile:
    """Encapsulates a CLI file, i.e. all licenses and copyrights
    found in a component"""

    LICENSE_TAG = "License"
    COPYRIGHT_TAG = "Copyright"
    EXPORTRESTRICTIONS_TAG = "ExportRestrictions"
    OBLIGATION_TAG = "Obligation"
    TAGS_TAG = "Tags"

    def __init__(self):
        self.filename = ""
        self.component = ""
        self.creator = ""
        self.date = ""
        self.baseDoc = ""
        self.toolUsed = ""
        self.componentId = ""
        self.includesAcknowledgements = False
        self.componentSha1 = ""
        self.version = ""

        self.licenses = []
        self.copyrights = []
        self.obligations = []
        self.tags = []
        self.irrelevant_files = []
        self.export_restrictions = []

    def read_from_file(self, filename):
        tree = ET.parse(filename)
        root = tree.getroot()

        self.filename = filename
        self.component = root.attrib["component"]
        self.creator = root.attrib["creator"]
        self.date = root.attrib["date"]
        self.baseDoc = root.attrib["baseDoc"]

        if "toolUsed" in root.attrib:
            self.toolUsed = root.attrib["toolUsed"]

        if "componentID" in root.attrib:
            self.componentId = root.attrib["componentID"]

        if "includesAcknowledgements" in root.attrib:
            self.includesAcknowledgements = root.attrib["includesAcknowledgements"]

        if "componentSHA1" in root.attrib:
            self.componentSha1 = root.attrib["componentSHA1"]

        if "Version" in root.attrib:
            self.version = root.attrib["Version"]

        for elem in root:
            if elem.tag == self.LICENSE_TAG:
                lic = CliLicense()
                lic.read_from_element(elem)
                self.licenses.append(lic)
                continue

            if elem.tag == self.COPYRIGHT_TAG:
                copyr = CliCopyright()
                copyr.read_from_element(elem)
                self.copyrights.append(copyr)
                continue

            if elem.tag == self.EXPORTRESTRICTIONS_TAG:
                restriction = CliExportRestriction()
                restriction.read_from_element(elem)
                self.export_restrictions.append(restriction)
                continue

            if elem.tag == self.OBLIGATION_TAG:
                obligation = CliObligation()
                obligation.read_from_element(elem)
                self.obligations.append(obligation)
                continue

            if elem.tag == self.TAGS_TAG:
                if elem.text is not None:
                    taglist = elem.text.strip()
                    self.tags = taglist.split(" ")
                continue


class LicenseTools:
    """Tools for license and CLI file processing."""

    NOT_README_TAG = "NOT_README_OSS"
    NON_FUNCTIONAL_TAG = "NON_FUNCTIONAL"
    NON_USED_DUAL_LICENSE_TAG = "NOT_USED_DUAL_LICENSE"
    MANUAL_CHECK_NEEDED_TAG = "MANUAL_CHECK_NEEDED"

    def __init__(self):
        pass

    @staticmethod
    def get_global_license(clifile):
        """Determines the global license."""
        for lic in clifile.licenses:
            if lic.type.upper() == "GLOBAL":
                return license

        return None

    @staticmethod
    def get_non_global_licenses(clifile):
        """Gets the non global licenses."""
        result = []
        for lic in clifile.licenses:
            if lic.type.upper() != "GLOBAL":
                result.append(license)

        return result

    @staticmethod
    def has_license(clifile, spdx_identifier):
        """Determines whether the specified component has the
        specified license."""
        for lic in clifile.licenses:
            if lic.spdx_identifier.upper() == spdx_identifier.upper():
                return True

        return False

    @staticmethod
    def is_source_code_shipping_license(lic):
        """Determines whether this is a license where the source code needs to
       be ready to be shipped to customers."""
        licenseUpper = lic.upper()
        if "GPL" in licenseUpper:
            return True
        if "CDDL" in licenseUpper:
            return True
        if "EPL" in licenseUpper:
            return True
        if "ECOS" in licenseUpper:
            return True
        if "EUPL" in licenseUpper:
            return True
        if "MPL" in licenseUpper:
            return True
        if "MS-RL" in licenseUpper:
            return True

        return False

    @staticmethod
    def is_multi_license(lic):
        """Determines whether the licenses is a dual/multi license."""
        licenseUpper = lic.upper()
        if "DUAL" in licenseUpper:
            return True
        if "TRIPLE" in licenseUpper:
            return True
        if "QUADRUPLE" in licenseUpper:
            return True
        if "MULTI" in licenseUpper:
            return True

        return False

    @staticmethod
    def is_do_not_use_license(lic):
        """Determines whether this license is a 'do not use' license."""
        typeUpper = lic.type.upper()
        if typeUpper == "OTHER_RED":
            return True
        if typeUpper == "OTHERRED":
            return True
        if typeUpper == "RED":
            return True

        return False

    @staticmethod
    def has_multi_license(clifile):
        """Determines whether this component has at least one multi license."""
        for lic in clifile.licenses:
            if LicenseTools.is_multi_license(lic):
                return True

        return False

    @staticmethod
    def has_do_not_use_files(clifile):
        """Determines whether this component has at least one
        'do not use' license/file."""
        for lic in clifile.licenses:
            if LicenseTools.is_do_not_use_license(lic):
                return True

        return False

    @staticmethod
    def has_source_code_shipping_license(clifile):
        """Determines whether this component has at least one license
        where the source code needs to get shipped."""
        for lic in clifile.licenses:
            if LicenseTools.is_source_code_shipping_license(lic):
                return True

        return False

    @staticmethod
    def license_has_not_readme_tag(lic):
        """Determines whether the specified item has a
        'not for Readme_OSS' tag."""
        for tag in lic.tags:
            if tag.upper() == LicenseTools.NOT_README_TAG:
                return True

        return False

    @staticmethod
    def component_has_not_readme_tag(clifile):
        """Determines whether the specified item has a
        'not for Readme_OSS' tag."""
        for tag in clifile.tags:
            if tag.upper() == LicenseTools.NOT_README_TAG:
                return True

        return False
