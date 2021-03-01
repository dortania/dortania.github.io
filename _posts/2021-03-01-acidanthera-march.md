---
layout: post
title:  "Acidanthera Updates: March 2021"
date:   2021-03-01 15:00:00 -0700
categories: Hackintosh updates
---

* [A message from vit9696](#a-message-from-vit9696)
* [Dortania Updates](#dortania-updates)
* [Changelogs](#changelogs)

# A message from vit9696

Hello everyone,

Today we are making a logical step forward in improving the compatibility of less popular configurations throughout the stack:

* As our Mac user quantity expands we continue to provide special options dedicated for them in particular. Thanks to [@PMheart](https://github.com/PMheart) and [@Bmju](https://github.com/) we got things like `GopPassThrough` option, OEM serial handling, the ability to reuse firmware features, and other SMBIOS values. Certain Macs that started to have trouble booting on with 0.6.7 should now also work fine.
* Another hardware range we needed better support for is brand new hardware. After over a month of remote debugging, we were able to identify the problem with memory mapping on Microsoft Surface and several other laptops and successfully fixed it.
* For the legacy hardware we resolved multiple issues related to displayed and actual CPU frequency rounding, particularly for the CPUs with a fractional multiplier. [@nms42](https://github.com/nms42) also provided patches to avoid NVIDIA kernel log spam in Big Sur. As a bonus OpenCore can now activate HPET support on legacy Intel machines.

Besides that, we published new utilities like `acdtinfo` and `ocpasswordgen` to help to analyze kext installations and set OpenCore password correspondingly. In addition to that [@mhaeuser](https://github.com/mhaeuser) fixed a long-standing bug with version reporting through NVRAM which may have resulted in extra flash wear. VoodooPS2 received NumLock key support thx to [@chilledHamza](https://github.com/chilledHamza) and VoodooInput got overall code simplification thx to [@zen-shen](https://github.com/zen-shen).

While this is clearly not all and certain features were left behind for better testing, we hope that a considerable portion of the userbase will find their long-standing bugs fixed as a consequence.

——Vit

# Dortania Updates

A new month for us with many of changes and improvements over at Acidanthera. With Dortania, we've added a fair number of improvements to our guides including documentation on OpenCore's password system as well as `ocvalidate` info thanks to [@dreamwhite](https://github.com/dreamwhite)!

Looking over to future changes in Dortania, we'd like to notify users of a potentially [large scale issue of `XhciPortLimit` in macOS 11.3 Beta 2(20E5186d) and newer](https://github.com/acidanthera/bugtracker/issues/1514). The specific issue regards users who have this quirk enabled and have not mapped their USB ports, as macOS 11.3 will now boot-loop for many users on installs, updates as well as regular OS boots. We've already prepped a [PR](https://github.com/dortania/OpenCore-Install-Guide/pull/238/files) to help warn users as well as provide work-arounds to this situation like hosting recovery images.

* Note: Users who have `XhciPortLimit` disabled need not worry, however please ensure you've [mapped your USB ports](https://dortania.github.io/OpenCore-Post-Install/usb/) before updating

Currently we expect 11.3 to be released to the public sometime this week or the coming weeks, so when these changes hit the public we will be merging the changes. Additionally, whenever there are new reports of `XhciPortLimit` being fixed, we will be updating the guide to ensure users know. For users who'd like to aid in the patches, you can find the binaries of [11.3 Beta 1 and Beta 2 kexts ](https://github.com/acidanthera/bugtracker/issues/1514) as well as the source for [XhciPortLimit Patches](https://github.com/acidanthera/OpenCorePkg/blob/cbd2fa3ad306c123f2acaed5d2277bacfd48917b/Library/OcAppleKernelLib/CommonPatches.c#L527-L740).

——Khronokernel

# Changelogs

#### [OpenCore 0.6.7](https://github.com/acidanthera/OpenCorePkg/releases)

- Fixed ocvalidate return code to be non-zero when issues are found
- Added `OEM` values to `PlatformInfo` in `Automatic` mode
- Improved CPU frequency calculation on Haswell and earlier
- Fixed issues when applying certain patches
- Added `SSN` (and `HW_SSN`) variable support
- Added onscreen early logging in DEBUG builds for legacy firmware
- Added workaround for firmware not specifying DeviceHandle at bootstrap
- Added support for R/O page tables in `SetupVirtualMap` quirk
- Added OEM preservation for certain Apple SMBIOS tables
- Fixed switching to graphics mode when entering OpenCanopy
- Fixed installing Apple FB Info protocol when no GOP exists
- Fixed abort timeout sound in OpenCanopy on key press
- Added `GopPassThrough` option to support GOP protocol over UGA
- Fixed CPU speed rounding for certain Xeon and Core 2 CPUs
- Removed `KeyMergeThreshold` as it never functioned anyway
- Added `acdtinfo` utility to lookup certain products
- Fixed `FSBFrequency` calculation with fractional multiplier
- Fixed showing core count for some AMD CPUs
- Added `ResetTrafficClass` to reset TCSEL to T0 on legacy HDA
- Fixed default boot entry selection without timeout for builtin picker
- Added ocpasswordgen utility to generate OpenCore password data
- Added `ActivateHpetSupport` quirk to activate HPET support
- Fixed `opencore-version` reporting the incorrect version in rare cases

#### [WhateverGreen 1.4.7](https://github.com/acidanthera/WhateverGreen/releases)

- Fixed debug messages from cursor manipulation with NVIDIA GPUs on macOS 11

#### [VirtualSMC 1.2.1](https://github.com/acidanthera/VirtualSMC/releases)

- Fix version publishing for VirtualSMC and plugins

#### [VoodooPS2 2.2.2](https://github.com/acidanthera/VoodooPS2/releases)

- Added NumLockSupport & NumLockOnAtBoot

#### [VoodooInput 1.1.1](https://github.com/acidanthera/VoodooInput/releases)

- Remove angle calculation

#### [AppleALC 1.5.8](https://github.com/acidanthera/AppleALC/releases)

- Improved resource packaging by stripping optional tags

#### [BrcmPatchRAM 2.5.7](https://github.com/acidanthera/BrcmPatchRAM/releases)

- Added BCM94360Z4 identifiers for injection

