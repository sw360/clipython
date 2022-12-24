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
    CONTENT_TAG = "Content"

    def __init__(self):
        CliFileItemBase.__init__(self)
        self.export_restriction_text = ""
        self.export_restriction_comment = ""

    def read_from_element(self, element: ET.Element):
        self.read_files_from_element(element)
        for elem in element:
            if elem.tag == self.CONTENT_TAG:
                self.export_restriction_text = elem.text.strip()
                continue
