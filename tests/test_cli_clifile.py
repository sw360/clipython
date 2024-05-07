# -------------------------------------------------------------------------------
# (c) 2022-2024 Siemens AG
# All Rights Reserved.
# Author: thomas.graf@siemens.com
#
# Licensed under the MIT license.
# SPDX-License-Identifier: MIT
# -------------------------------------------------------------------------------

import os
import unittest
from typing import List

from cli_support import (CliCopyright, CliExportRestriction, CliExternalId,
                         CliFile, CliIrrelevantFiles, CliLicense,
                         CliObligation)


class CliFileTest(unittest.TestCase):
    TESTFILE1 = "tests/fixtures/CLIXML_MIT_simple.xml"
    TESTFILE2 = "tests/fixtures/CLIXML_COMPLETE_simple.xml"
    TESTFILE3 = "tests/fixtures/CLIXML_Minimal.xml"
    TESTFILE4 = "dummy.xml"
    TESTFILE5 = "tests/fixtures/CLIXML_Full.xml"

    @staticmethod
    def delete_file(filename: str) -> None:
        """Delete the given file."""
        try:
            if os.path.exists(filename):
                os.remove(filename)
        except Exception as ex:
            print("Error removing file:", filename, repr(ex))

    def compare_file_to_text(self, filename: str, expected: List[str]) -> None:
        with open(filename) as file:
            data = file.readlines()

        self.assertEqual(len(data), len(expected))
        index = 0
        for line in data:
            t1 = line.strip()
            t2 = expected[index].strip()
            self.assertEqual(t1, t2)
            index += 1

    def test_constructor(self) -> None:
        lib = CliFile()
        self.assertEqual("", lib.filename)
        self.assertEqual("", lib.component)
        self.assertEqual("", lib.creator)
        self.assertEqual("", lib.date)
        self.assertEqual("", lib.baseDoc)
        self.assertEqual("", lib.toolUsed)
        self.assertEqual("", lib.componentId)
        self.assertEqual(False, lib.includesAcknowledgements)
        self.assertEqual("", lib.componentSha1)
        self.assertEqual("", lib.version)

        self.assertIsNotNone(lib.licenses)
        self.assertEqual(0, len(lib.licenses))
        self.assertIsNotNone(lib.copyrights)
        self.assertEqual(0, len(lib.copyrights))
        self.assertIsNotNone(lib.obligations)
        self.assertEqual(0, len(lib.obligations))
        self.assertIsNotNone(lib.tags)
        self.assertEqual(0, len(lib.tags))
        self.assertIsNotNone(lib.irrelevant_files)
        self.assertIsNotNone(lib.export_restrictions)
        self.assertEqual(0, len(lib.export_restrictions))

    def test_read_from_file_simple(self) -> None:
        lib = CliFile()
        lib.read_from_file(self.TESTFILE1)
        self.assertEqual(self.TESTFILE1, lib.filename)
        self.assertEqual("TestFile1", lib.component)
        self.assertEqual("john.doe@cli.com", lib.creator)
        self.assertEqual("2022-03-08", lib.date)
        self.assertEqual("/srv/fotransfer/repository/report", lib.baseDoc)
        self.assertEqual("SpdxToCliConverter", lib.toolUsed)
        self.assertEqual("12345", lib.componentId)
        self.assertEqual(False, lib.includesAcknowledgements)
        self.assertEqual("5243c0eac8c674732802731670657c93855f4071", lib.componentSha1)
        self.assertEqual("1.4", lib.version)

        self.assertIsNotNone(lib.licenses)
        self.assertEqual(1, len(lib.licenses))

        self.assertIsNotNone(lib.copyrights)
        self.assertEqual(1, len(lib.copyrights))

        self.assertIsNotNone(lib.obligations)
        self.assertEqual(0, len(lib.obligations))

        self.assertIsNotNone(lib.tags)
        self.assertEqual(2, len(lib.tags))

        self.assertIsNotNone(lib.irrelevant_files)

        self.assertIsNotNone(lib.export_restrictions)
        self.assertEqual(0, len(lib.export_restrictions))

    def test_read_from_file_complete(self) -> None:
        lib = CliFile()
        lib.read_from_file(self.TESTFILE2)
        self.assertEqual(self.TESTFILE2, lib.filename)
        self.assertEqual("TestFile2", lib.component)
        self.assertEqual("john.doe@cli.com", lib.creator)
        self.assertEqual("2022-03-09", lib.date)
        self.assertEqual("/srv/fotransfer/repository/report", lib.baseDoc)
        self.assertEqual("SpdxToCliConverter", lib.toolUsed)
        self.assertEqual("12345", lib.componentId)
        self.assertEqual(True, lib.includesAcknowledgements)
        self.assertEqual("5243c0eac8c674732802731670657c93855f4071", lib.componentSha1)
        self.assertEqual("1.5", lib.version)

        self.assertIsNotNone(lib.licenses)
        self.assertEqual(2, len(lib.licenses))
        self.assertEqual("MIT License", lib.licenses[0].name)
        self.assertEqual("Apache-2.0", lib.licenses[1].name)

        self.assertIsNotNone(lib.copyrights)
        self.assertEqual(1, len(lib.copyrights))

        self.assertIsNotNone(lib.obligations)
        self.assertEqual(3, len(lib.obligations))

        self.assertIsNotNone(lib.tags)
        self.assertEqual(2, len(lib.tags))

        self.assertIsNotNone(lib.irrelevant_files)

        self.assertIsNotNone(lib.export_restrictions)
        self.assertEqual(1, len(lib.export_restrictions))

    def test_read_from_file_minimal(self) -> None:
        lib = CliFile()
        lib.read_from_file(self.TESTFILE3)
        self.assertEqual(self.TESTFILE3, lib.filename)
        self.assertEqual("TestFileX", lib.component)
        self.assertEqual("john.doe@cli.com", lib.creator)
        self.assertEqual("2022-03-08", lib.date)
        self.assertEqual("/srv/fotransfer/repository/report", lib.baseDoc)
        self.assertEqual("SpdxToCliConverter", lib.toolUsed)
        self.assertEqual("12345", lib.componentId)
        self.assertEqual(False, lib.includesAcknowledgements)
        self.assertEqual("5243c0eac8c674732802731670657c93855f4071", lib.componentSha1)
        self.assertEqual("1.4", lib.version)

        self.assertIsNotNone(lib.licenses)
        self.assertEqual(0, len(lib.licenses))

        self.assertIsNotNone(lib.copyrights)
        self.assertEqual(0, len(lib.copyrights))

        self.assertIsNotNone(lib.obligations)
        self.assertEqual(0, len(lib.obligations))

        self.assertIsNotNone(lib.tags)
        self.assertEqual(0, len(lib.tags))

        self.assertIsNotNone(lib.irrelevant_files)

        self.assertIsNotNone(lib.export_restrictions)
        self.assertEqual(0, len(lib.export_restrictions))

        self.assertIsNotNone(lib.general_information)

        self.assertIsNotNone(lib.assessment_summary)

    def test_write_file_minimal(self) -> None:
        first = '<ComponentLicenseInformation component="" creator="" date="" baseDoc="" toolUsed="" '
        first = first + 'componentID="" includesAcknowledgements="false" componentSHA1="" Version="1.6">\n'
        expected = first + '''<GeneralInformation>
    <ReportId />
    <ReviewedBy />
    <ComponentName />
    <Community />
    <ComponentVersion />
    <ComponentHash />
    <ComponentReleaseDate />
    <LinkComponentManagement />
    <LinkScanTool />
    <ComponentId>
      <Type />
      <Id />
    </ComponentId>
  </GeneralInformation>
  <AssessmentSummary>
    <GeneralAssessment />
    <CriticalFilesFound>None</CriticalFilesFound>
    <DependencyNotes>None</DependencyNotes>
    <ExportRestrictionsFound>None</ExportRestrictionsFound>
    <UsageRestrictionsFound>None</UsageRestrictionsFound>
    <AdditionalNotes />
  </AssessmentSummary>
  <IrrelevantFiles />
  <ExternalIds />
  <Tags />
  <Comment />
</ComponentLicenseInformation>'''

        self.delete_file(self.TESTFILE4)
        lib = CliFile()
        lib.write_to_file(self.TESTFILE4)

        lines_expected = expected.splitlines()
        self.compare_file_to_text(self.TESTFILE4, lines_expected)

        self.delete_file(self.TESTFILE4)

    def test_write_file(self) -> None:
        self.delete_file(self.TESTFILE4)
        lib = CliFile()

        lib.filename = "CLIXML_Full.xml"
        lib.component = "MyComp, 1.2.3"
        lib.creator = "Me"
        lib.date = "2023-12-23"
        lib.baseDoc = "Some doc"
        lib.toolUsed = "clipython"
        lib.componentId = "007"
        lib.includesAcknowledgements = False
        lib.componentSha1 = "dead"
        lib.version = "1.6"

        lib.general_information.report_id = "112233"
        lib.general_information.reviewed_by = "TG"
        lib.general_information.component_name = "MyComp"
        lib.general_information.community = "Me"
        lib.general_information.component_version = "1.2.3"
        lib.general_information.component_hash = "DEADBEEF"
        lib.general_information.link_component_management = "https://anylink.com"
        lib.general_information.link_scan_tool = "https://anothertools.com"
        lib.general_information.component_id_type = "package-url"
        lib.general_information.component_id = "pkg:npm/%40angular/animation@12.3.1"
        lib.general_information.component_release_date = "2023-12-23"

        lib.assessment_summary.general_assessment = "abc"
        lib.assessment_summary.critical_files_found = "None"
        lib.assessment_summary.dependency_notes = "yes"
        lib.assessment_summary.export_restrictions_found = "yes"
        lib.assessment_summary.usage_restrictions_found = "yes"
        lib.assessment_summary.additional_notes = "xyz"

        license = CliLicense()
        license.license_text = "some text"
        license.name = "Apache Software License, Version 2.0"
        license.spdx_identifier = "Apache-2.0"
        license.type = "global"
        license.acknowledgements.append("Apache NOTICE file...")
        license.tags.append("OSS")
        license.files.append("license1.txt")
        license.hashes.append("12AB")
        lib.licenses.append(license)

        copyright = CliCopyright()
        copyright.text = "Copyright (c) by me"
        copyright.files.append("copyright1.txt")
        copyright.hashes.append("12CD")
        lib.copyrights.append(copyright)

        obligation = CliObligation()
        obligation.text = "you have to"
        obligation.topic = "obligation"
        obligation.licenses.append("AGPL-9.0")
        lib.obligations.append(obligation)

        lib.tags.append("t1")
        lib.tags.append("OSS")

        export_restriction = CliExportRestriction()
        export_restriction.export_restriction_text = "ECCN=N"
        export_restriction.export_restriction_comment = "This is no fake!"
        export_restriction.files.append("export_restriction1.txt")
        export_restriction.hashes.append("12EF")
        lib.export_restrictions.append(export_restriction)

        external_id = CliExternalId()
        external_id.key = "category"
        external_id.value = "fun"
        lib.external_ids.append(external_id)

        lib.irrelevant_files = CliIrrelevantFiles()
        lib.irrelevant_files.files.append("ir1.txt")
        lib.irrelevant_files.hashes.append("12AB")
        lib.comment = "some comment"

        lib.write_to_file(self.TESTFILE4)

        with open(self.TESTFILE5) as file:
            expected = file.readlines()
        self.compare_file_to_text(self.TESTFILE4, expected)

        self.delete_file(self.TESTFILE4)

    def test_read_from_full_file(self) -> None:
        lib = CliFile()
        lib.read_from_file(self.TESTFILE5)
        self.assertEqual(self.TESTFILE5, lib.filename)

        self.assertEqual(lib.component, "MyComp, 1.2.3")
        self.assertEqual(lib.creator, "Me")
        self.assertEqual(lib.date, "2023-12-23")
        self.assertEqual(lib.baseDoc, "Some doc")
        self.assertEqual(lib.toolUsed, "clipython")
        self.assertEqual(lib.componentId, "007")
        self.assertEqual(lib.includesAcknowledgements, False)
        self.assertEqual(lib.componentSha1, "dead")
        self.assertEqual(lib.version, "1.6")

        self.assertEqual(lib.general_information.report_id, "112233")
        self.assertEqual(lib.general_information.reviewed_by, "TG")
        self.assertEqual(lib.general_information.component_name, "MyComp")
        self.assertEqual(lib.general_information.community, "Me")
        self.assertEqual(lib.general_information.component_version, "1.2.3")
        self.assertEqual(lib.general_information.component_hash, "DEADBEEF")
        self.assertEqual(lib.general_information.link_component_management, "https://anylink.com")
        self.assertEqual(lib.general_information.link_scan_tool, "https://anothertools.com")
        self.assertEqual(lib.general_information.component_id_type, "package-url")
        self.assertEqual(lib.general_information.component_id, "pkg:npm/%40angular/animation@12.3.1")
        self.assertEqual(lib.general_information.component_release_date, "2023-12-23")

        self.assertEqual(lib.assessment_summary.general_assessment, "abc")
        self.assertEqual(lib.assessment_summary.critical_files_found, "None")
        self.assertEqual(lib.assessment_summary.dependency_notes, "yes")
        self.assertEqual(lib.assessment_summary.export_restrictions_found, "yes")
        self.assertEqual(lib.assessment_summary.usage_restrictions_found, "yes")
        self.assertEqual(lib.assessment_summary.additional_notes, "xyz")

        self.assertEqual(len(lib.licenses), 1)
        license = lib.licenses[0]
        self.assertEqual(license.license_text, "some text")
        self.assertEqual(license.name, "Apache Software License, Version 2.0")
        self.assertEqual(license.spdx_identifier, "Apache-2.0")
        self.assertEqual(license.type, "global")
        self.assertEqual(len(license.acknowledgements), 1)
        self.assertEqual(license.acknowledgements[0], "Apache NOTICE file...")
        self.assertEqual(len(license.tags), 1)
        self.assertEqual(license.tags[0], "OSS")
        self.assertEqual(len(license.files), 1)
        self.assertEqual(license.files[0], "license1.txt")
        self.assertEqual(len(license.hashes), 1)
        self.assertEqual(license.hashes[0], "12AB")

        self.assertEqual(len(lib.copyrights), 1)
        copyright = lib.copyrights[0]
        self.assertEqual(copyright.text, "Copyright (c) by me")
        self.assertEqual(len(copyright.files), 1)
        self.assertEqual(copyright.files[0], "copyright1.txt")
        self.assertEqual(len(copyright.hashes), 1)
        self.assertEqual(copyright.hashes[0], "12CD")

        self.assertEqual(len(lib.obligations), 1)
        obligation = lib.obligations[0]
        self.assertEqual(obligation.text, "you have to")
        self.assertEqual(obligation.topic, "obligation")
        self.assertEqual(len(obligation.licenses), 1)
        self.assertEqual(obligation.licenses[0], "AGPL-9.0")

        self.assertEqual(len(lib.tags), 2)
        lib.tags.append("t1")
        lib.tags.append("OSS")

        self.assertEqual(len(lib.export_restrictions), 1)
        export_restriction = lib.export_restrictions[0]
        self.assertEqual(export_restriction.export_restriction_text, "ECCN=N")
        self.assertEqual(export_restriction.export_restriction_comment, "This is no fake!")
        self.assertEqual(len(export_restriction.files), 1)
        self.assertEqual(export_restriction.files[0], "export_restriction1.txt")
        self.assertEqual(len(export_restriction.hashes), 1)
        self.assertEqual(export_restriction.hashes[0], "12EF")

        self.assertEqual(len(lib.external_ids), 1)
        external_id = lib.external_ids[0]
        self.assertEqual(external_id.key, "category")
        self.assertEqual(external_id.value, "fun")

        self.assertIsNotNone(lib.irrelevant_files)
        self.assertEqual(len(lib.irrelevant_files.files), 1)
        self.assertEqual(lib.irrelevant_files.files[0], "ir1.txt")
        self.assertEqual(len(lib.irrelevant_files.hashes), 1)
        self.assertEqual(lib.irrelevant_files.hashes[0], "12AB")

        self.assertEqual(lib.comment, "some comment")


if __name__ == "__main__":
    APP = CliFileTest()
    APP.test_write_file()
