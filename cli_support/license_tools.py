# -------------------------------------------------------------------------------
# (c) 2019-2022 Siemens AG
# All Rights Reserved.
# Author: thomas.graf@siemens.com
#
# Licensed under the MIT license.
# SPDX-License-Identifier: MIT
# -------------------------------------------------------------------------------

from typing import List, Optional

from .CLI import CliFile
from .cli_license import CliLicense


class LicenseTools:
    """Tools for license and CLI file processing."""

    NOT_README_TAG = "NOT_README_OSS"
    NON_FUNCTIONAL_TAG = "NON_FUNCTIONAL"
    NON_USED_DUAL_LICENSE_TAG = "NOT_USED_DUAL_LICENSE"
    MANUAL_CHECK_NEEDED_TAG = "MANUAL_CHECK_NEEDED"

    @staticmethod
    def get_global_license(clifile: CliFile) -> Optional[CliLicense]:
        """Determines the global license."""
        for lic in clifile.licenses:
            if lic.type.upper() == "GLOBAL":
                return lic

        return None

    @staticmethod
    def get_non_global_licenses(clifile: CliFile) -> List[CliLicense]:
        """Gets the non global licenses."""
        result: List[CliLicense] = []
        for lic in clifile.licenses:
            if lic.type.upper() != "GLOBAL":
                result.append(lic)

        return result

    @staticmethod
    def has_license(clifile: CliFile, spdx_identifier: str) -> bool:
        """Determines whether the specified component has the
        specified license."""
        for lic in clifile.licenses:
            if lic.spdx_identifier.upper() == spdx_identifier.upper():
                return True

        return False

    @staticmethod
    def is_source_code_shipping_license(spdx_identifier: str) -> bool:
        """Determines whether this is a license where the source code needs to
        be ready to be shipped to customers.
        Please note that this is a very simplified approach."""
        licenseUpper = spdx_identifier.upper()
        if "GPL" in licenseUpper:  # includes LGPL
            return True
        if "CDDL" in licenseUpper:
            return True
        if "EPL" in licenseUpper:
            return True
        if "ECOS" in licenseUpper:
            return True
        if "EUPL" in licenseUpper:
            return True
        if "MPL" in licenseUpper:
            return True
        if "MS-RL" in licenseUpper:
            return True

        return False

    @staticmethod
    def is_multi_license(spdx_identifier: str) -> bool:
        """Determines whether the licenses is a dual/multi license."""
        licenseUpper = spdx_identifier.upper()
        if "DUAL" in licenseUpper:
            return True
        if "TRIPLE" in licenseUpper:
            return True
        if "QUADRUPLE" in licenseUpper:
            return True
        if "MULTI" in licenseUpper:
            return True
        if " OR " in licenseUpper:
            return True
        if " AND " in licenseUpper:
            return True

        return False

    @staticmethod
    def is_do_not_use_license(license: CliLicense) -> bool:
        """Determines whether this license is a 'do not use' license."""
        typeUpper = license.type.upper()
        if typeUpper == "OTHER_RED":
            return True
        if typeUpper == "OTHERRED":
            return True
        if typeUpper == "RED":
            return True

        return False

    @staticmethod
    def has_multi_license(clifile: CliFile) -> bool:
        """Determines whether this component has at least one multi license."""
        for lic in clifile.licenses:
            if LicenseTools.is_multi_license(lic.spdx_identifier):
                return True

        return False

    @staticmethod
    def has_do_not_use_files(clifile: CliFile) -> bool:
        """Determines whether this component has at least one
        'do not use' license/file."""
        for lic in clifile.licenses:
            if LicenseTools.is_do_not_use_license(lic):
                return True

        return False

    @staticmethod
    def has_source_code_shipping_license(clifile: CliFile) -> bool:
        """Determines whether this component has at least one license
        where the source code needs to get shipped."""
        for lic in clifile.licenses:
            if LicenseTools.is_source_code_shipping_license(lic.spdx_identifier):
                return True

        return False

    @staticmethod
    def license_has_not_readme_tag(license: CliLicense) -> bool:
        """Determines whether the specified item has a
        'not for Readme_OSS' tag."""
        for tag in license.tags:
            if tag.upper() == LicenseTools.NOT_README_TAG:
                return True

        return False

    @staticmethod
    def component_has_not_readme_tag(clifile: CliFile) -> bool:
        """Determines whether the specified item has a
        'not for Readme_OSS' tag."""
        for tag in clifile.tags:
            if tag.upper() == LicenseTools.NOT_README_TAG:
                return True

        return False
