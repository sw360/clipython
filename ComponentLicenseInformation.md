# Component License Information (CLI)

Component License Information and is used to automatically process license information of
third party software components.

This file format has been developed at Siemens many years ago. The goal was to have a
machine readable file that contains information about the copyrights, export restrictions,
licenses, and license obligations that apply to a specific open source or commercial software
component.

CLI files can be created by [FOSSology](https://www.fossology.org). At Siemens they are stored
in a central database, [SW360](https://www.eclipse.org/sw360/). Additional tools can pull
these CLI files from SW360, for additional license compliance checks or to create the license
documentation that needs to get forwarded to customer, aka. `ThirdPartyNotices` or `Readme_OSS`.

Technically, the CLI file format is based on XML.

## What does CLI file specification cover?

General component information

* Licenses - all licenses found in the scan and relevant for the component
* Copyrights - all copyrights found
* Obligations - obligations take from the *current* obligation database at the time the
  CLI file was generated
* Export restrictions - export restrictions found during the source code scan
* Irrelevant files - files that may contains licensing information but are not relevant for the
* use of the component (test files, (build) tools, documentation)

Examples of CLI file can be found in the folder test/testfiles.

## Comparison to SPDX or why do we need another file format?

When the CLI file format was developed only an early version of SPDX was available.  
But already at the point of time it was obvious that SPDX had a slightly different mindset.
SPDX wanted to have far more possibilities to describe the license and copyright findings
of a source code scan. There wars also no intention to include information about export control
related findings or information about license obligations. The goal of CLI is to have a concise
description of all this information.

A more detailed specification, including an XML schema definition is available on request.
