# -------------------------------------------------------------------------------
# (c) 2022 Siemens AG
# All Rights Reserved.
# Author: thomas.graf@siemens.com
#
# Licensed under the MIT license.
# SPDX-License-Identifier: MIT
# -------------------------------------------------------------------------------

import unittest

from cli_support import CliFile


class CliFileTest(unittest.TestCase):
    TESTFILE1 = "test/testfiles/CLIXML_MIT_simple.xml"
    TESTFILE2 = "test/testfiles/CLIXML_COMPLETE_simple.xml"

    def test_constructor(self):
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
        self.assertEqual(0, len(lib.irrelevant_files))
        self.assertIsNotNone(lib.export_restrictions)
        self.assertEqual(0, len(lib.export_restrictions))

    def test_read_from_file_simple(self):
        lib = CliFile()
        lib.read_from_file(self.TESTFILE1)
        self.assertEqual(self.TESTFILE1, lib.filename)
        self.assertEqual("TestFile1", lib.component)
        self.assertEqual("john.doe@cli.com", lib.creator)
        self.assertEqual("2022-03-08", lib.date)
        self.assertEqual("/srv/fotransfer/repository/report", lib.baseDoc)
        self.assertEqual("SpdxToCliConverter", lib.toolUsed)
        self.assertEqual("12345", lib.componentId)
        self.assertEqual("false", lib.includesAcknowledgements)
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
        self.assertEqual(0, len(lib.irrelevant_files))

        self.assertIsNotNone(lib.export_restrictions)
        self.assertEqual(0, len(lib.export_restrictions))

    def test_read_from_file_complete(self):
        lib = CliFile()
        lib.read_from_file(self.TESTFILE2)
        self.assertEqual(self.TESTFILE2, lib.filename)
        self.assertEqual("TestFile2", lib.component)
        self.assertEqual("john.doe@cli.com", lib.creator)
        self.assertEqual("2022-03-09", lib.date)
        self.assertEqual("/srv/fotransfer/repository/report", lib.baseDoc)
        self.assertEqual("SpdxToCliConverter", lib.toolUsed)
        self.assertEqual("12345", lib.componentId)
        self.assertEqual("false", lib.includesAcknowledgements)
        self.assertEqual("5243c0eac8c674732802731670657c93855f4071", lib.componentSha1)
        self.assertEqual("1.5", lib.version)

        self.assertIsNotNone(lib.licenses)
        self.assertEqual(2, len(lib.licenses))
        self.assertEqual("MIT License", lib.licenses[0].name)
        self.assertEqual("MIT License", lib.licenses[0].name)
        self.assertEqual("MIT License", lib.licenses[0].name)
        self.assertEqual("MIT License", lib.licenses[0].name)

        self.assertIsNotNone(lib.copyrights)
        self.assertEqual(1, len(lib.copyrights))

        self.assertIsNotNone(lib.obligations)
        self.assertEqual(3, len(lib.obligations))

        self.assertIsNotNone(lib.tags)
        self.assertEqual(2, len(lib.tags))

        self.assertIsNotNone(lib.irrelevant_files)
        self.assertEqual(0, len(lib.irrelevant_files))

        self.assertIsNotNone(lib.export_restrictions)
        self.assertEqual(1, len(lib.export_restrictions))
