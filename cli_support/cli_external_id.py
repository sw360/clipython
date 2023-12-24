# -------------------------------------------------------------------------------
# (c) 2023 Siemens AG
# All Rights Reserved.
# Author: thomas.graf@siemens.com
#
# Licensed under the MIT license.
# SPDX-License-Identifier: MIT
# -------------------------------------------------------------------------------

import xml.etree.ElementTree as ET

from .xml_base import XmlBase


class CliExternalId(XmlBase):
    """Encapsulates an external id"""

    KEY_TAG = "Key"
    VALUE_TAG = "Value"

    def __init__(self) -> None:
        self.key: str = ""
        self.value: str = ""

    def _read_from_element(self, element: ET.Element) -> None:
        """Read external id from XML element."""
        for elem in element:
            if elem.tag == self.KEY_TAG:
                if elem.text:
                    self.key = elem.text
                if self.key:
                    self.key = self.key.strip()
                continue

            if elem.tag == self.VALUE_TAG:
                if elem.text:
                    self.value = elem.text
                if self.value:
                    self.value = self.value.strip()
                continue

    def _append_to_xml(self, parent: ET.Element) -> None:
        """Write external id to XML element."""
        obl = ET.SubElement(parent, "ExternalId")
        node = ET.SubElement(obl, "Key")
        cdata = self.CDATA(self.key)
        node.append(cdata)

        node = ET.SubElement(obl, "Value")
        cdata = self.CDATA(self.value)
        node.append(cdata)
