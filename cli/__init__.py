# -------------------------------------------------------------------------------
# (c) 2019-2022 Siemens AG
# All Rights Reserved.
# Author: thomas.graf@siemens.com
#
# Licensed under the MIT license.
# SPDX-License-Identifier: MIT
# -------------------------------------------------------------------------------

__version__ = (1, 3)

# isort: skip_file
from .CLI import (  # noqa: F401
    CliFile,
    CliCopyright,
    CliExportRestriction,
    CliLicense,
    CliObligation,
)
from .license_tools import LicenseTools  # noqa: F401
