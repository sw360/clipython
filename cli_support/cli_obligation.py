# -------------------------------------------------------------------------------
# (c) 2019-2023 Siemens AG
# All Rights Reserved.
# Author: thomas.graf@siemens.com
#
# Licensed under the MIT license.
# SPDX-License-Identifier: MIT
# -------------------------------------------------------------------------------

import xml.etree.ElementTree as ET

from .xml_base import XmlBase


class CliObligation(XmlBase):
    """Encapsulates an obligation"""

    TOPIC_TAG = "Topic"
    TEXT_TAG = "Text"
    LICENSES_TAG = "Licenses"
    LICENSE_TAG = "License"

    def __init__(self) -> None:
        self.text: str = ""
        self.topic: str = ""
        self.licenses: list[str] = []

    def _read_from_element(self, element: ET.Element) -> None:
        """Read license from XML element."""
        for elem in element:
            if elem.tag == self.TOPIC_TAG:
                if elem.text:
                    self.topic = elem.text
                if self.topic:
                    self.topic = self.topic.strip()
                continue

            if elem.tag == self.TEXT_TAG:
                if elem.text:
                    self.text = elem.text
                if self.text:
                    self.text = self.text.strip()
                continue

            if elem.tag == self.LICENSES_TAG:
                for elem2 in elem:
                    if elem2.tag == self.LICENSE_TAG and elem2.text:
                        self.licenses.append(elem2.text.strip())
                continue

    def _append_to_xml(self, parent: ET.Element) -> None:
        """Write license to XML element."""
        obl = ET.SubElement(parent, "Obligation")
        node = ET.SubElement(obl, "Topic")
        cdata = self.CDATA(self.topic)
        node.append(cdata)

        node = ET.SubElement(obl, "Text")
        cdata = self.CDATA(self.text)
        node.append(cdata)

        licenses = ET.SubElement(obl, "Licenses")
        for license in self.licenses:
            lic = ET.SubElement(licenses, "License")
            cdata = self.CDATA(license)
            lic.append(cdata)
