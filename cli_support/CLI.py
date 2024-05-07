# -------------------------------------------------------------------------------
# (c) 2019-2024 Siemens AG
# All Rights Reserved.
# Author: thomas.graf@siemens.com
#
# Licensed under the MIT license.
# SPDX-License-Identifier: MIT
# -------------------------------------------------------------------------------

import sys
import xml.etree.ElementTree as ET
from typing import Any, List, Optional

from .cli_assessment_summary import CliAssessmentSummary
from .cli_copyright import CliCopyright
from .cli_export_restriction import CliExportRestriction
from .cli_external_id import CliExternalId
from .cli_general_information import CliGeneralInformation
from .cli_irrelevant_files import CliIrrelevantFiles
from .cli_license import CliLicense
from .cli_obligation import CliObligation
from .xml_base import XmlBase

# have our own serialization to handle CDATA
ET._original_serialize_xml = ET._serialize_xml  # type: ignore


def _serialize_xml(write, elem, qnames, namespaces, short_empty_elements, **kwargs) -> Any:  # type: ignore
    if elem.tag == XmlBase.CDATA_ID:
        write("<%s%s]]>" % (elem.tag, elem.text))
        return
    return ET._original_serialize_xml(write, elem, qnames, namespaces, short_empty_elements, **kwargs)  # type: ignore


ET._serialize_xml = ET._serialize["xml"] = _serialize_xml  # type: ignore


class CliFile(XmlBase):
    """Encapsulates a CLI file, i.e. all licenses and copyrights
    found in a component"""

    LICENSE_TAG = "License"
    COPYRIGHT_TAG = "Copyright"
    EXPORTRESTRICTIONS_TAG = "ExportRestrictions"
    OBLIGATION_TAG = "Obligation"
    TAGS_TAG = "Tags"
    GENERAL_INFORMATION_TAG = "GeneralInformation"
    ASSESSMENT_SUMMARY_TAG = "AssessmentSummary"
    EXTERNAL_IDS_TAG = "ExternalIds"
    IRRELEVANT_FILES_TAG = "IrrelevantFiles"
    COMMENT_TAG = "Comment"

    def __init__(self) -> None:
        self.filename: str = ""
        self.component: str = ""
        self.creator: str = ""
        self.date: str = ""
        self.baseDoc: str = ""
        self.toolUsed: str = ""
        self.componentId: str = ""
        self.includesAcknowledgements: bool = False
        self.componentSha1: str = ""
        self.version: str = ""

        self.general_information = CliGeneralInformation()
        self.assessment_summary = CliAssessmentSummary()

        self.licenses: List[CliLicense] = []
        self.copyrights: List[CliCopyright] = []
        self.obligations: List[CliObligation] = []
        self.tags: List[str] = []
        self.export_restrictions: List[CliExportRestriction] = []
        self.external_ids: List[CliExternalId] = []
        self.irrelevant_files = CliIrrelevantFiles()
        self.comment: str = ""

    def read_from_file(self, filename: str) -> None:
        tree = ET.parse(filename)
        root = tree.getroot()

        self.filename = filename
        self.component = root.attrib["component"]
        self.creator = root.attrib["creator"]
        self.date = root.attrib["date"]
        self.baseDoc = root.attrib["baseDoc"]

        if "toolUsed" in root.attrib:
            self.toolUsed = root.attrib["toolUsed"]

        if "componentID" in root.attrib:
            self.componentId = root.attrib["componentID"]

        if "includesAcknowledgements" in root.attrib:
            if root.attrib["includesAcknowledgements"].lower() == "true":
                self.includesAcknowledgements = True

        if "componentSHA1" in root.attrib:
            self.componentSha1 = root.attrib["componentSHA1"]

        if "Version" in root.attrib:
            self.version = root.attrib["Version"]

        for elem in root:
            if elem.tag == self.LICENSE_TAG:
                lic = CliLicense()
                lic._read_from_element(elem)
                self.licenses.append(lic)
                continue

            if elem.tag == self.COPYRIGHT_TAG:
                copyr = CliCopyright()
                copyr._read_from_element(elem)
                self.copyrights.append(copyr)
                continue

            if elem.tag == self.EXPORTRESTRICTIONS_TAG:
                restriction = CliExportRestriction()
                restriction._read_from_element(elem)
                self.export_restrictions.append(restriction)
                continue

            if elem.tag == self.OBLIGATION_TAG:
                obligation = CliObligation()
                obligation._read_from_element(elem)
                self.obligations.append(obligation)
                continue

            if elem.tag == self.GENERAL_INFORMATION_TAG:
                self.general_information._read_from_element(elem)
                continue

            if elem.tag == self.ASSESSMENT_SUMMARY_TAG:
                self.assessment_summary._read_from_element(elem)
                continue

            if elem.tag == self.EXTERNAL_IDS_TAG:
                for el in elem:
                    ext_id = CliExternalId()
                    ext_id._read_from_element(el)
                    self.external_ids.append(ext_id)
                continue

            if elem.tag == self.IRRELEVANT_FILES_TAG:
                self.irrelevant_files._read_from_element(elem)
                continue

            if elem.tag == self.COMMENT_TAG:
                self.comment = self.get_value(elem)
                continue

            if elem.tag == self.TAGS_TAG:
                if elem.text is not None:
                    taglist = elem.text.strip()
                    if taglist:
                        if "," in taglist:
                            self.tags = taglist.split(",")
                        else:
                            self.tags = taglist.split(" ")
                continue

    def write_to_file(self, filename: str) -> None:
        """Write CLI data to a file with the given name."""
        root = ET.Element(
            "ComponentLicenseInformation",
            component=self.component,
            creator=self.creator,
            date=self.date,
            baseDoc=self.baseDoc,
            toolUsed=self.toolUsed,
            componentID=self.componentId,
            includesAcknowledgements=self.bool2str(self.includesAcknowledgements),
            componentSHA1=self.componentSha1,
            Version="1.6")

        self.general_information._append_to_xml(root)
        self.assessment_summary._append_to_xml(root)

        for license in self.licenses:
            license._append_to_xml(root)

        for copyright in self.copyrights:
            copyright._append_to_xml(root)

        for obligation in self.obligations:
            obligation._append_to_xml(root)

        for expr in self.export_restrictions:
            expr._append_to_xml(root)

        self.irrelevant_files._append_to_xml(root)

        extids = ET.SubElement(root, "ExternalIds")
        for extid in self.external_ids:
            extid._append_to_xml(extids)

        tags = ET.SubElement(root, "Tags")
        tags.text = ",".join(str(x) for x in self.tags)

        comment = ET.SubElement(root, "Comment")
        if self.comment:
            cdata = self.CDATA(self.comment)
            comment.append(cdata)

        tree = ET.ElementTree(root)
        if not sys.version_info < (3, 9):
            ET.indent(tree)
        else:
            self._pretty_print(root)
        tree.write(filename, encoding="UTF-8")

    def _pretty_print(self, current: ET.Element, parent: Optional[ET.Element] = None,
                      index: int = -1, depth: int = 0) -> None:
        """Helper function that mimics indent() of Python 3.9."""
        for i, node in enumerate(current):
            self._pretty_print(node, current, i, depth + 1)
        if parent is not None:
            if index == 0:
                parent.text = '\n' + ('\t' * depth)
            else:
                parent[index - 1].tail = '\n' + ('\t' * depth)
            if index == len(parent) - 1:
                current.tail = '\n' + ('\t' * (depth - 1))
