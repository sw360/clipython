# -------------------------------------------------------------------------------
# (c) 2023 Siemens AG
# All Rights Reserved.
# Author: thomas.graf@siemens.com
#
# Licensed under the MIT license.
# SPDX-License-Identifier: MIT
# -------------------------------------------------------------------------------

import xml.etree.ElementTree as ET

from .cli_file_item_base import CliFileItemBase


class CliIrrelevantFiles(CliFileItemBase):
    """Encapsulates the irrelevant files."""

    CONTENT_TAG = "Content"

    def __init__(self) -> None:
        CliFileItemBase.__init__(self)
        self.files: list[str] = []
        self.hashes: list[str] = []

    def _read_from_element(self, element: ET.Element) -> None:
        """Read irrelevant files from XML element."""
        self._read_files_from_element(element)

    def _append_to_xml(self, parent: ET.Element) -> None:
        """Write irrelevant files to XML element."""
        cr = ET.SubElement(parent, "IrrelevantFiles")

        CliFileItemBase._append_to_xml(self, cr)
