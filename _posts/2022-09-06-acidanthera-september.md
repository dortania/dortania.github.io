---
layout: post
title: "Acidanthera and Dortania Updates: September 2022"
date: 2022-09-06 00:30:00 -0400
categories: Hackintosh updates
---

* [Acidanthera Updates: A message from PMheart](#acidanthera-updates-a-message-from-pmheart)
* [Dortania Updates: A message from dhinakg](#dortania-updates-a-message-from-dhinakg)
* [Changelogs](#changelogs)

# Acidanthera Updates: A message from PMheart

With the heatwave moving away in Europe, we are finally approaching the fall. And it's also about time to embrace the new OS updates coming this month and/or in October.

Compared to OpenCore 0.8.3, the changes introduced in 0.8.4 are fairly minor. Following @mikebeaton's groundbreaking work on NVRAM, our mission is finalised by syncing the checks for `LoadEarly` in ocvalidate and the addition of the new option `FullNvramAccess` allowing direct access to NVRAM. When it comes to Hyper-V support, @Goldfish64 brought the new `SSDT-HV-DEV.dsl` for better compatibility with older macOS versions on Windows 10 and newer; in addition, he fixed a `SysReport` crash on Pentium 4 systems, and another crash on an`ExitBootServices` call while using DEBUG builds and file logging. For developers, @mhaeuser made a new ProcessKernel utility for testing kext injection by reading users' config, making tests easier; in addition, @mikebeaton fixed 32-bit userspace build support on macOS. With basic set of NetworkPkg drivers with HTTP boot support included in OpenCore, we can start working on a new EFI tool which downloads and boots macOS Recovery, replacing [macrecovery](https://github.com/acidanthera/OpenCorePkg/tree/master/Utilities/macrecovery). Last but not least, we updated the [zlib library](https://zlib.net) to 1.2.12, and @savvamitrofanov made characters invisible on password input in ocpasswordgen. We would also like to thank @dreamwhite for his constant and solid work to defeat all warnings in our Pythhon scripts.

@Goldfish64 brought a bunch of changes to MacHyperVSupport, providing a more seamless experience for Hyper-V users. These include PCI passthrough support, a fix for IOPCIBridge crash on macOS 12 and newer, and a new `hvshutdown` daemon for Hyper-V shutdown requests. As well, macOS 10.4 and 10.5 support has been added, together with the standardisation of boot arguments.

For VoodooPS2, in spite of small changes, we fixed variable shadowing to make the code more consistent.

We would also like to thank @hgsshaanxi and @Feartech for their contributions to our AppleALC codec database for ALC222, ALC235, and ALC255 (3234). Also, without @vandroiy2013's consistent maintainance, the AppleALC project would not even have been alive.

Thanks to the developers of dmidecode, our fork has been updated to upstream a1a2258f with Apple Silicon support by @vit9696.

It is a pity that no further progress has been made for Skylake users spoofing as Kaby Lake. We are looking forward to contributions reviving the support for Skylake.

Enjoy our updates and macOS Ventura,

— PMheart

# Dortania Updates: A message from dhinakg

Hi everyone! Nothing much for this month. We're slowly progressing on merging in PRs and pushing some updates to the guides before I start working on reorganizing the install guide as mentioned in the [previous post](2022-08-02-acidanthera-dortania-august.md).

Enjoy the last vestiges of summer,

— Dhinak

# Changelogs

#### [OpenCorePkg 0.8.4](https://github.com/acidanthera/OpenCorePkg/releases)

* Added checks for `Driver` -> `LoadEarly` in ocvalidate
* Added `FullNvramAccess` option for tools which require direct access to NVRAM
* Replaced `SSDT-HV-CPU.dsl` with `SSDT-HV-DEV.dsl` for compatiblity with older macOS versions on Windows 10 and newer
* Updated builtin zlib library to 1.2.12
* Changed ocpasswordgen not to print characters on password input
* Added ProcessKernel utility for testing kext injection based on configs
* Fixed crash while using `SysReport` on Pentium 4 systems
* Fixed crash after ExitBootServices() is called while using DEBUG builds and file logging
* Fixed 32-bit userspace build support on macOS (use High Sierra 10.13 and below)
* Added basic set of NetworkPkg drivers with HTTP boot support

#### [MacHyperVSupport 0.9.1](https://github.com/acidanthera/MacHyperVSupport/releases)

* Added initial PCI passthrough support
* Fix crash related to IOPCIBridge on 12.0 and newer
* Added support for macOS 10.4 and 10.5
* Added hvshutdown daemon to support shutdowns from Hyper-V
* Standardized boot arguments

#### [VoodooPS2 2.3.0](https://github.com/acidanthera/VoodooPS2/releases)

* Fixed variable shadowing

#### [AppleALC 1.7.5](https://github.com/acidanthera/AppleALC/releases)

* Added ALC222 layout-id 12 for Lenovo Tianyi 510s-07IMB Desktop PC by hgsshaanxi
* Added ALC235 layout-id 36 for Lenovo Tianyi 510 pro-18ICB Desktop PC by hgsshaanxi
* Added ALC255(3234) layout-id 22 for Asus N752VX by Feartech by feartech

#### [dmidecode 3.4a](https://github.com/acidanthera/dmidecode/releases)

* Synced with dmidecode a1a2258f
* Added Apple Silicon support
