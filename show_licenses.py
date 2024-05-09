# -------------------------------------------------------------------------------
# (c) 2019-2022 Siemens AG
# All Rights Reserved.
# Author: thomas.graf@siemens.com
#
# Licensed under the MIT license.
# SPDX-License-Identifier: MIT
# -------------------------------------------------------------------------------

"""
Show all licenses and copyrights of a component

call syntax

show_licenses filename
"""

import sys
from typing import Any, List

from colorama import Fore, init

import cli_support

# initialize colorama
init()


class ShowLicenses():
    """Application class"""
    def __init__(self) -> None:
        self.cli_filename: str = ""
        self.global_license_list: List[str] = []

    @classmethod
    def print_license_list(cls, license_list: List[str]) -> None:
        """Displays the licenses color-coded"""
        for lic in license_list:
            color = Fore.RESET
            check = lic.upper()
            if "GPL" in check:
                color = Fore.LIGHTYELLOW_EX

            if "EPL" in check:
                color = Fore.LIGHTYELLOW_EX

            if "MPL" in check:
                color = Fore.LIGHTYELLOW_EX

            if "CDDL" in check:
                color = Fore.LIGHTYELLOW_EX

            if "CPL" in check:
                color = Fore.LIGHTYELLOW_EX

            print("  " + color + lic)

        print(Fore.RESET)

    def process_cli_file(self, cli_filename: str) -> None:
        """Processes a single CLI file"""
        clifile = cli_support.CLI.CliFile()

        try:
            clifile.read_from_file(cli_filename)
        except OSError as ex:
            print(Fore.LIGHTRED_EX)
            print("    Error reading CLI file: " + cli_filename)
            print("    Error '{0}' occurred. Arguments {1}.".format(ex.errno, ex.args))
            print(Fore.RESET)
            return

        license_list: List[str] = []
        for lic in clifile.licenses:
            license_list.append(lic.name)
            if lic.name not in self.global_license_list:
                self.global_license_list.append(lic.name)

    def process_commandline(self, argv: Any) -> Any:
        """Reads the command line arguments"""
        if len(argv) < 2:
            sys.exit(
                Fore.LIGHTRED_EX +
                "  No CLI file specified!" +
                Fore.RESET)

        self.cli_filename = argv[1]

    def main(self) -> None:
        """Main method()"""
        print("\nShow all licenses and copyrights of a component:\n")
        self.process_commandline(sys.argv)

        self.global_license_list = []
        self.process_cli_file(self.cli_filename)
        self.print_license_list(self.global_license_list)


if __name__ == '__main__':
    APP = ShowLicenses()
    APP.main()
