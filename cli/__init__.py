# -------------------------------------------------------------------------------
# (c) 2019-2022 Siemens AG
# All Rights Reserved.
# Author: thomas.graf@siemens.com
#
# Licensed under the MIT license.
# SPDX-License-Identifier: MIT
# -------------------------------------------------------------------------------

__version__ = (1, 3)

from .CLI import (  # noqa
    CliObligation,
    CliFile,
    CliLicense,
    CliCopyright,
    CliExportRestriction,
)

from .license_tools import LicenseTools  # noqa
