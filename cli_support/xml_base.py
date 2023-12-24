# -------------------------------------------------------------------------------
# (c) 2023 Siemens AG
# All Rights Reserved.
# Author: thomas.graf@siemens.com
#
# Licensed under the MIT license.
# SPDX-License-Identifier: MIT
# -------------------------------------------------------------------------------

import xml.etree.ElementTree as ET


class XmlBase:
    """Common base class to XML serialization."""
    CDATA_ID = "![CDATA["

    def CDATA(self, text: str = "") -> ET.Element:
        """Helper method to allow serialization of CDATA."""
        element = ET.Element(self.CDATA_ID)
        element.text = text
        return element

    def bool2str(self, value: bool) -> str:
        """Convert bool to string for XML export."""
        if value:
            return "true"

        return "false"

    def get_value(self, elem: ET.Element) -> str:
        if elem.text is not None:
            return elem.text.strip()

        return ""
