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


class CliAssessmentSummary(XmlBase):
    """Encapsulates the assessment summary."""
    GENERAL_ASSESSMENT_TAG = "GeneralAssessment"
    CRITICAL_FILES_TAG = "CriticalFilesFound"
    DEPENDENCY_NOTES_TAG = "DependencyNotes"
    EXPORT_RESTRICTIONS_TAG = "ExportRestrictionsFound"
    USAGE_RESTRICTIONS_TAG = "UsageRestrictionsFound"
    ADDITIONAL_NOTES_TAG = "AdditionalNotes"

    def __init__(self) -> None:
        self.general_assessment: str = ""
        self.critical_files_found: str = "None"
        self.dependency_notes: str = "None"
        self.export_restrictions_found: str = "None"
        self.usage_restrictions_found: str = "None"
        self.additional_notes: str = ""

    def _read_from_element(self, element: ET.Element) -> None:
        """Read assessment summary from XML element."""
        for elem in element:
            if elem.tag == self.GENERAL_ASSESSMENT_TAG:
                self.general_assessment = self.get_value(elem)
                continue

            if elem.tag == self.CRITICAL_FILES_TAG:
                self.critical_files_found = self.get_value(elem)
                continue

            if elem.tag == self.DEPENDENCY_NOTES_TAG:
                self.dependency_notes = self.get_value(elem)
                continue

            if elem.tag == self.EXPORT_RESTRICTIONS_TAG:
                self.export_restrictions_found = self.get_value(elem)
                continue

            if elem.tag == self.USAGE_RESTRICTIONS_TAG:
                self.usage_restrictions_found = self.get_value(elem)
                continue

            if elem.tag == self.ADDITIONAL_NOTES_TAG:
                self.additional_notes = self.get_value(elem)
                continue

    def _append_to_xml(self, parent: ET.Element) -> None:
        """Write assessment summary to XML element."""
        gi = ET.SubElement(parent, "AssessmentSummary")
        node = ET.SubElement(gi, "GeneralAssessment")
        cdata = self.CDATA(self.general_assessment)
        node.append(cdata)

        node = ET.SubElement(gi, "CriticalFilesFound")
        node.text = self.critical_files_found

        node = ET.SubElement(gi, "DependencyNotes")
        node.text = self.dependency_notes

        node = ET.SubElement(gi, "ExportRestrictionsFound")
        node.text = self.export_restrictions_found

        node = ET.SubElement(gi, "UsageRestrictionsFound")
        node.text = self.usage_restrictions_found

        node = ET.SubElement(gi, "AdditionalNotes")
        cdata = self.CDATA(self.additional_notes)
        node.append(cdata)
