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

from .xml_base import XmlBase


class CliFileItemBase(XmlBase):
    """Common base class to handle files and file hashes"""

    FILES_TAG = "Files"
    FILEHASH_TAG = "FileHash"

    def __init__(self) -> None:
        self.files: List[str] = []
        self.hashes: List[str] = []

    def _read_files_from_element(self, element: ET.Element) -> None:
        """Read files and hashes from XML element."""
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

    def _append_to_xml(self, parent: ET.Element) -> None:
        """Write files and hashes to XML element."""
        file_data = ET.SubElement(parent, "Files")
        cdata = self.CDATA("\n".join(str(x) for x in self.files))
        file_data.append(cdata)

        hash_data = ET.SubElement(parent, "FileHash")
        cdata = self.CDATA("\n".join(str(x) for x in self.hashes))
        hash_data.append(cdata)
