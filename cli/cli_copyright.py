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


class CliCopyright(CliFileItemBase):
    """Encapsulates a copyright statement"""

    CONTENT_TAG = "Content"

    def __init__(self):
        CliFileItemBase.__init__(self)
        self.text = ""
        self.files = []
        self.hashes = []

    def read_from_element(self, element: ET.Element):
        self.read_files_from_element(element)
        for elem in element:
            if elem.tag == self.CONTENT_TAG:
                if elem.text is not None:
                    self.text = elem.text.strip()
                continue
