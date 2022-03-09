# -------------------------------------------------------------------------------
# (c) 2019-2022 Siemens AG
# All Rights Reserved.
# Author: thomas.graf@siemens.com
#
# Licensed under the MIT license.
# SPDX-License-Identifier: MIT
# -------------------------------------------------------------------------------

import xml.etree.ElementTree as ET


class CliFileItemBase:
    """Common base class to handle files and file hashes"""

    FILES_TAG = "Files"
    FILEHASH_TAG = "FileHash"

    def __init__(self):
        self.files = []
        self.hashes = []

    def read_files_from_element(self, element: ET.Element):
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
