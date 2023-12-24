# -------------------------------------------------------------------------------
# (c) 2022-2023 Siemens AG
# All Rights Reserved.
# Author: thomas.graf@siemens.com
#
# Licensed under the MIT license.
# SPDX-License-Identifier: MIT
# -------------------------------------------------------------------------------

import unittest

from cli_support import CliFile, CliLicense
from cli_support.license_tools import LicenseTools


class LicenseToolTest(unittest.TestCase):
    TESTFILE1 = "tests/fixtures/CLIXML_MIT_simple.xml"
    TESTFILE2 = "tests/fixtures/CLIXML_COMPLETE_simple.xml"
    TESTFILE3 = "tests/fixtures/CLIXML_Licenses_source_shipping.xml"
    TESTFILE4 = "tests/fixtures/CLIXML_Licenses_multi.xml"

    def test_get_global_license(self) -> None:
        cli = CliFile()
        cli.read_from_file(self.TESTFILE2)

        actual = LicenseTools.get_global_license(cli)
        self.assertIsNotNone(actual)
        if actual:  # for mypy
            self.assertEqual("MIT", actual.spdx_identifier)
            self.assertEqual("MIT License", actual.name)

    def test_get_non_global_licenses(self) -> None:
        cli = CliFile()
        cli.read_from_file(self.TESTFILE2)

        actual = LicenseTools.get_non_global_licenses(cli)
        self.assertIsNotNone(actual)
        self.assertEqual(1, len(actual))
        self.assertEqual("Apache-2.0", actual[0].spdx_identifier)

    def test_has_license(self) -> None:
        cli = CliFile()
        cli.read_from_file(self.TESTFILE2)

        actual = LicenseTools.has_license(cli, "MIT")
        self.assertTrue(actual)

        actual = LicenseTools.has_license(cli, "Apache-2.0")
        self.assertTrue(actual)

        actual = LicenseTools.has_license(cli, "GPL-2.0")
        self.assertFalse(actual)

        actual = LicenseTools.has_license(cli, "XYZ")
        self.assertFalse(actual)

    def test_is_source_code_shipping_license(self) -> None:
        actual = LicenseTools.is_source_code_shipping_license("MIT")
        self.assertFalse(actual)

        actual = LicenseTools.is_source_code_shipping_license("GPL-2.0")
        self.assertTrue(actual)

        actual = LicenseTools.is_source_code_shipping_license("LGPL-2.1")
        self.assertTrue(actual)

        actual = LicenseTools.is_source_code_shipping_license("CDDL-1.1")
        self.assertTrue(actual)

        actual = LicenseTools.is_source_code_shipping_license("CDDL-1.2")
        self.assertTrue(actual)

        actual = LicenseTools.is_source_code_shipping_license("EPL-1.0")
        self.assertTrue(actual)

        actual = LicenseTools.is_source_code_shipping_license("EUPL-1.0")
        self.assertTrue(actual)

        actual = LicenseTools.is_source_code_shipping_license("MPL-1.1")
        self.assertTrue(actual)

        actual = LicenseTools.is_source_code_shipping_license("MPL-2.0")
        self.assertTrue(actual)

        actual = LicenseTools.is_source_code_shipping_license("MS-RL")
        self.assertTrue(actual)

        actual = LicenseTools.is_source_code_shipping_license("ECOS-1.1")
        self.assertTrue(actual)

    def test_is_multi_license(self) -> None:
        actual = LicenseTools.is_multi_license("MIT")
        self.assertFalse(actual)

        actual = LicenseTools.is_multi_license("MIT or GPL-2.0")
        self.assertTrue(actual)

        actual = LicenseTools.is_multi_license("MIT AND GPL-2.0")
        self.assertTrue(actual)

        actual = LicenseTools.is_multi_license("MULTI: MIT / GPL-2.0")
        self.assertTrue(actual)

        actual = LicenseTools.is_multi_license("DUAL: MIT, GPL-2.0")
        self.assertTrue(actual)

    def test_is_do_not_use_license(self) -> None:
        license = CliLicense()
        license.type = "RED"
        actual = LicenseTools.is_do_not_use_license(license)
        self.assertTrue(actual)

        license.type = "OTHER_RED"
        actual = LicenseTools.is_do_not_use_license(license)
        self.assertTrue(actual)

        license.type = "OTHERRED"
        actual = LicenseTools.is_do_not_use_license(license)
        self.assertTrue(actual)

        license.type = "OTHERWHITE"
        actual = LicenseTools.is_do_not_use_license(license)
        self.assertFalse(actual)

    def test_has_multi_license(self) -> None:
        cli = CliFile()
        cli.read_from_file(self.TESTFILE1)
        actual = LicenseTools.has_multi_license(cli)
        self.assertFalse(actual)

        cli = CliFile()
        cli.read_from_file(self.TESTFILE4)
        actual = LicenseTools.has_multi_license(cli)
        self.assertTrue(actual)

    def test_has_do_not_use_files(self) -> None:
        cli = CliFile()
        cli.read_from_file(self.TESTFILE2)
        actual = LicenseTools.has_do_not_use_files(cli)
        self.assertFalse(actual)

        cli = CliFile()
        cli.read_from_file(self.TESTFILE3)
        actual = LicenseTools.has_do_not_use_files(cli)
        self.assertTrue(actual)

    def test_has_source_code_shipping_license(self) -> None:
        cli = CliFile()
        cli.read_from_file(self.TESTFILE3)
        actual = LicenseTools.has_source_code_shipping_license(cli)
        self.assertTrue(actual)

        cli = CliFile()
        cli.read_from_file(self.TESTFILE1)
        actual = LicenseTools.has_source_code_shipping_license(cli)
        self.assertFalse(actual)

    def test_license_has_not_readme_tag(self) -> None:
        cli = CliFile()
        cli.read_from_file(self.TESTFILE3)
        actual = LicenseTools.license_has_not_readme_tag(cli.licenses[2])
        self.assertTrue(actual)

        actual = LicenseTools.license_has_not_readme_tag(cli.licenses[1])
        self.assertFalse(actual)

    def test_component_has_not_readme_tag(self) -> None:
        cli = CliFile()
        cli.read_from_file(self.TESTFILE1)
        actual = LicenseTools.component_has_not_readme_tag(cli)
        self.assertFalse(actual)

        cli = CliFile()
        cli.read_from_file(self.TESTFILE3)
        actual = LicenseTools.component_has_not_readme_tag(cli)
        self.assertTrue(actual)
