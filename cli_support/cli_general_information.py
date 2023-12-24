# -------------------------------------------------------------------------------
# (c) 2023 Siemens AG
# All Rights Reserved.
# Author: thomas.graf@siemens.com
#
# Licensed under the MIT license.
# SPDX-License-Identifier: MIT
# -------------------------------------------------------------------------------

import xml.etree.ElementTree as ET

from .xml_base import XmlBase


class CliGeneralInformation(XmlBase):
    """Encapsulates the general information"""
    REPORTID_TAG = "ReportId"
    REVIEWED_BY_TAG = "ReviewedBy"
    COMPONENT_NAME_TAG = "ComponentName"
    COMMUNITY_TAG = "Community"
    COMPONENT_VERSION_TAG = "ComponentVersion"
    COMPONENT_HASH_TAG = "ComponentHash"
    COMPONENT_RELEAESE_DATE_TAG = "ComponentReleaseDate"
    LINK_COMPONENT_MGNT_TAG = "LinkComponentManagement"
    LINK_SCAN_TOOL_TAG = "LinkScanTool"
    COMPONENT_ID_ELEMENT_TAG = "ComponentId"
    COMPONENT_TYPE_TAG = "Type"
    COMPONENT_ID_TAG = "Id"

    def __init__(self) -> None:
        self.report_id: str = ""
        self.reviewed_by: str = ""
        self.component_name: str = ""
        self.community: str = ""
        self.component_version: str = ""
        self.component_hash: str = ""
        self.component_release_date: str = ""
        self.link_component_management: str = ""
        self.link_scan_tool: str = ""
        self.component_id: str = ""
        self.component_id_type: str = ""

    def _read_from_element(self, element: ET.Element) -> None:
        """Read general information from XML element."""
        for elem in element:
            if elem.tag == self.REPORTID_TAG:
                self.report_id = self.get_value(elem)
                continue

            if elem.tag == self.REVIEWED_BY_TAG:
                self.reviewed_by = self.get_value(elem)
                continue

            if elem.tag == self.COMPONENT_NAME_TAG:
                self.component_name = self.get_value(elem)
                continue

            if elem.tag == self.COMMUNITY_TAG:
                self.community = self.get_value(elem)
                continue

            if elem.tag == self.COMPONENT_VERSION_TAG:
                self.component_version = self.get_value(elem)
                continue

            if elem.tag == self.COMPONENT_HASH_TAG:
                self.component_hash = self.get_value(elem)
                continue

            if elem.tag == self.COMPONENT_RELEAESE_DATE_TAG:
                self.component_release_date = self.get_value(elem)
                continue

            if elem.tag == self.LINK_COMPONENT_MGNT_TAG:
                self.link_component_management = self.get_value(elem)
                continue

            if elem.tag == self.LINK_SCAN_TOOL_TAG:
                self.link_scan_tool = self.get_value(elem)
                continue

            if elem.tag == self.COMPONENT_ID_ELEMENT_TAG:
                for el in elem:
                    if el.tag == self.COMPONENT_TYPE_TAG:
                        self.component_id_type = self.get_value(el)
                        continue

                    if el.tag == self.COMPONENT_ID_TAG:
                        self.component_id = self.get_value(el)
                        continue
                continue

    def _append_to_xml(self, parent: ET.Element) -> None:
        """Write general information to XML element."""
        gi = ET.SubElement(parent, "GeneralInformation")
        node = ET.SubElement(gi, "ReportId")
        node.text = self.report_id

        node = ET.SubElement(gi, "ReviewedBy")
        node.text = self.reviewed_by

        node = ET.SubElement(gi, "ComponentName")
        node.text = self.component_name

        node = ET.SubElement(gi, "Community")
        node.text = self.community

        node = ET.SubElement(gi, "ComponentVersion")
        node.text = self.component_version

        node = ET.SubElement(gi, "ComponentHash")
        node.text = self.component_hash

        node = ET.SubElement(gi, "ComponentReleaseDate")
        node.text = self.component_release_date

        hash_data = ET.SubElement(gi, "LinkComponentManagement")
        cdata = self.CDATA(self.link_component_management)
        hash_data.append(cdata)

        hash_data = ET.SubElement(gi, "LinkScanTool")
        cdata = self.CDATA(self.link_scan_tool)
        hash_data.append(cdata)

        ci = ET.SubElement(gi, "ComponentId")

        node = ET.SubElement(ci, "Type")
        node.text = self.component_id_type

        node = ET.SubElement(ci, "Id")
        node.text = self.component_id
