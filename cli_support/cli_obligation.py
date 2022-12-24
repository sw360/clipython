# -------------------------------------------------------------------------------
# (c) 2019-2022 Siemens AG
# All Rights Reserved.
# Author: thomas.graf@siemens.com
#
# Licensed under the MIT license.
# SPDX-License-Identifier: MIT
# -------------------------------------------------------------------------------

import xml.etree.ElementTree as ET


class CliObligation:
    """Encapsulates an obligation"""

    TOPIC_TAG = "Topic"
    TEXT_TAG = "Text"
    LICENSES_TAG = "Licenses"
    LICENSE_TAG = "License"

    def __init__(self):
        self.text = ""
        self.topic = ""
        self.licenses = []

    def read_from_element(self, element: ET.Element):
        for elem in element:
            if elem.tag == self.TOPIC_TAG:
                self.topic = elem.text
                if self.topic:
                    self.topic = self.topic.strip()
                continue

            if elem.tag == self.TEXT_TAG:
                self.text = elem.text
                if self.text:
                    self.text = self.text.strip()
                continue

            if elem.tag == self.LICENSES_TAG:
                for elem2 in elem:
                    if elem2.tag == self.LICENSE_TAG:
                        self.licenses.append(elem2.text.strip())
                continue
