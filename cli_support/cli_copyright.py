# -------------------------------------------------------------------------------
# (c) 2019-2023 Siemens AG
# All Rights Reserved.
# Author: thomas.graf@siemens.com
#
# Licensed under the MIT license.
# SPDX-License-Identifier: MIT
# -------------------------------------------------------------------------------

import xml.etree.ElementTree as ET
from typing import List

from .cli_file_item_base import CliFileItemBase


class CliCopyright(CliFileItemBase):
    """Encapsulates a copyright statement."""

    CONTENT_TAG = "Content"

    def __init__(self) -> None:
        CliFileItemBase.__init__(self)
        self.text: str = ""
        self.files: List[str] = []
        self.hashes: List[str] = []

    def _read_from_element(self, element: ET.Element) -> None:
        """Read copyright from XML element."""
        self._read_files_from_element(element)
        for elem in element:
            if elem.tag == self.CONTENT_TAG and elem.text:
                if elem.text is not None:
                    self.text = elem.text.strip()
                continue

    def _append_to_xml(self, parent: ET.Element) -> None:
        """Write copyright to XML element."""
        cr = ET.SubElement(parent, "Copyright")
        node = ET.SubElement(cr, "Content")
        cdata = self.CDATA(self.text)
        node.append(cdata)

        CliFileItemBase._append_to_xml(self, cr)
