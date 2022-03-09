# -------------------------------------------------------------------------------
# (c) 2019-2022 Siemens AG
# All Rights Reserved.
# Author: thomas.graf@siemens.com
#
# Licensed under the MIT license.
# SPDX-License-Identifier: MIT
# -------------------------------------------------------------------------------

import xml.etree.ElementTree as ET

from .cli_file_item_base import CliFileItemBase


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

    def read_from_element(self, element: ET.Element):
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
                    if "," in taglist:
                        self.tags = taglist.split(",")
                    else:
                        self.tags = taglist.split(" ")
                continue
