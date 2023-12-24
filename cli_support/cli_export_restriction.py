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


class CliExportRestriction(CliFileItemBase):
    """Encapsulates an export restriction"""

    CONTENT_TAG = "Content"
    COMMENT_TAG = "Comment"

    def __init__(self) -> None:
        CliFileItemBase.__init__(self)
        self.export_restriction_text: str = ""
        self.export_restriction_comment: str = ""

    def _read_from_element(self, element: ET.Element) -> None:
        """Read export restriction from XML element."""
        self._read_files_from_element(element)
        for elem in element:
            if elem.tag == self.CONTENT_TAG and elem.text:
                self.export_restriction_text = elem.text.strip()
                continue

            if elem.tag == self.COMMENT_TAG and elem.text:
                self.export_restriction_comment = elem.text.strip()
                continue

    def _append_to_xml(self, parent: ET.Element) -> None:
        """Write export restriction to XML element."""
        lic = ET.SubElement(parent, "ExportRestrictions")
        node = ET.SubElement(lic, "Content")
        cdata = self.CDATA(self.export_restriction_text)
        node.append(cdata)

        CliFileItemBase._append_to_xml(self, lic)

        node = ET.SubElement(lic, "Comment")
        cdata = self.CDATA(self.export_restriction_comment)
        node.append(cdata)
