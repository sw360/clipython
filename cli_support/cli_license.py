# -------------------------------------------------------------------------------
# (c) 2019-2024 Siemens AG
# All Rights Reserved.
# Author: thomas.graf@siemens.com
#
# Licensed under the MIT license.
# SPDX-License-Identifier: MIT
# -------------------------------------------------------------------------------

import xml.etree.ElementTree as ET
from typing import List

from .cli_file_item_base import CliFileItemBase


class CliLicense(CliFileItemBase):
    """Encapsulates a license."""

    CONTENT_TAG = "Content"
    ACKNOWLEDGEMENTS_TAG = "Acknowledgements"
    TAGS_TAG = "Tags"

    def __init__(self) -> None:
        CliFileItemBase.__init__(self)
        self.license_text: str = ""
        self.type: str = ""
        self.name: str = ""
        self.spdx_identifier: str = ""
        self.acknowledgements: List[str] = []
        self.tags: List[str] = []
        self.files: List[str] = []
        self.hashes: List[str] = []

    def _read_from_element(self, element: ET.Element) -> None:
        """Read license from XML element."""
        self.type = element.attrib["type"]
        self.name = element.attrib["name"]

        if "spdxidentifier" in element.attrib:
            self.spdx_identifier = element.attrib["spdxidentifier"]

        self._read_files_from_element(element)

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
                    elif " " in taglist:
                        self.tags = taglist.split(" ")
                    else:
                        self.tags.append(taglist)
                continue

    def _append_to_xml(self, parent: ET.Element) -> None:
        """Write license to XML element."""
        lic = ET.SubElement(
            parent,
            "License",
            type=self.type,
            name=self.name,
            spdxidentifier=self.spdx_identifier)
        node = ET.SubElement(lic, "Content")
        cdata = self.CDATA(self.license_text)
        node.append(cdata)

        CliFileItemBase._append_to_xml(self, lic)

        if len(self.acknowledgements) > 0:
            ack = ET.SubElement(lic, "Acknowledgements")
            cdata = self.CDATA("\n".join(str(x) for x in self.acknowledgements))
            ack.append(cdata)

        tags = ET.SubElement(lic, "Tags")
        tags.text = ",".join(str(x) for x in self.tags)
