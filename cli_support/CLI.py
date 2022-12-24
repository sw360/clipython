# -------------------------------------------------------------------------------
# (c) 2019-2022 Siemens AG
# All Rights Reserved.
# Author: thomas.graf@siemens.com
#
# Licensed under the MIT license.
# SPDX-License-Identifier: MIT
# -------------------------------------------------------------------------------

import xml.etree.ElementTree as ET

from .cli_copyright import CliCopyright
from .cli_export_restriction import CliExportRestriction
from .cli_license import CliLicense
from .cli_obligation import CliObligation


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

    def read_from_file(self, filename: str):
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
                    if "," in taglist:
                        self.tags = taglist.split(",")
                    else:
                        self.tags = taglist.split(" ")
                continue
