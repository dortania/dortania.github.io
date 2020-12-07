---
layout: post
title:  "Acidanthera Updates: December 2020"
date:   2020-12-07 15:00:00 -0700
categories: Hackintosh updates
---

* [A message from vit9696](#a-message-from-vit9696)
* [Dortania Updates](#dortania-updates)
* [Changelogs](#changelogs)

# A message from vit9696

Hello. First of all, we would like to congratulate you with the beginning of the holiday season. Autumn provided us with a refreshing experience thanks to the Apple Silicon presentation, and just like everyone else we were quite pleased with Apple Silicon real-world task performance. Out of interest we performed several tests on Macmini9,1 and concluded that it performs almost on par with i7 8700k when compiling LLVM, and outperforms pretty much any AMD or Intel CPU when compiling OpenCore, which build system depends heavily on single-core performance. If you want more details, check [this post](https://applelife.ru/posts/909181) for the commands and numbers. To ensure smooth transitioning we updated most of the applications and tools to compile and execute on Apple Silicon. However, despite all that effort I should say that for the nearest future Intel platform will remain our primary target, and we will continue polishing our software as needed.

While this is not quite true for volunteer open-source projects, there still is some sense in the common saying that the greater popularity inevitably leads to the greater responsibility. Since OpenCore now gets well over 100,000 downloads monthly, we tried to eliminate the technical debt in most commonly mentioned areas. One of these areas was Boot Option handling in the firmwares. Many firmwares have absolutely terrific bugs and badly violate the UEFI specification, creating genuine security vulnerabilities. Unfortunately, popular OEMs, like ASUS, continue to ignore all the reports. Trying to do at least something, we included a large number of workarounds for such firmwares with [@Download-Fritz](https://github.com/Download-Fritz) in OpenCore 0.6.4. So far this resolved all the issues we encountered. Check [this page](https://github.com/acidanthera/bugtracker/issues/1222#issuecomment-739241310) for the upgrade steps and issue details if you think you may be affected or use `BootProtect`.

Additionally, we discovered that macOS 11 broke the ability to disable third-party firmware upgrades via NVRAM, causing installation issues on platforms with some Macmini or Mac Pro firmware identifiers. This was addressed by `BlacklistAppleUpdate` UEFI quirk. We also improved several other quirks responsible for properly booting macOS Big Sur in Safe Mode (`EnableSafeModeSlide`), installing macOS before Mountain Lion (`AllowRelocationBlock`), and securing your environment in specific situations (`DisableSingleUser`). Due to a constant demand in perfect user experience, we made it possible to disable mouse control and allowed per-volume icons in OpenCanopy. Furthermore, Boot Chime sound can now be controlled through macOS Big Sur preferences, and advanced users can create manual bootloader patches thanks to [@PMHeart](https://github.com/PMHeart).

Other projects also received minor but important changes. [VoodooInput](https://github.com/acidanthera/VoodooInput/) now supports trackpoint information, which we plan to later use for reducing the code duplication across different trackpad projects. [HibernationFixup](https://github.com/acidanthera/HibernationFixup/) got further improvements in automatic hibernation. [Lilu](https://github.com/acidanthera/Lilu/) and [SMCDellSensors](https://github.com/acidanthera/VirtualSMC/) got stability fixes specific to Big Sur, and [SMCBatteryManager](https://github.com/acidanthera/VirtualSMC/) provided some tuning to the recent extended supplement information addition. [WhateverGreen](https://github.com/acidanthera/WhateverGreen/) now also runs in Safe Mode resolving black screen issues on platforms requiring AGDP patches. Thanks to [@Dhinakg](https://github.com/Dhinakg) and [@zhen-zen](https://github.com/zhen-zen), from this release onwards all the projects are built with GitHub Actions, which so far provided not only faster build times, but also build artifacts, which let you test your contributions through the official build suite.

——Vit

# Dortania Updates

This month has been a fairly quiet commit cycle for us on the guides, and thanks to this bit of peace we here at Dortania have been able to dedicate more time to some smaller projects. The project we've been hard at work on this month has been our [OpenCore Legacy Patcher](https://github.com/dortania/Opencore-Legacy-Patcher). 

The goal of this tool is simple:

* Allow Mac machines dropped by Apple to run newer versions of macOS
* And ensure all of this is kept in memory, allowing for all security features compared to other basic patchers

Because of this philosophy, we've gained a lot of features most patchers cannot compare to. This includes:

* Native OTA updates
* Full SIP, AMFI, Gatekeeper and other macOS secuirty features
* Full FileVault 2 support
* APFS Snapshotting
* Native IO80211 usage for many broadcom cards
* Only current way to boot Arrandale, Lynnfield and Clarkdale Macs
  * ie. iMac11,1, iMac11,2, iMac11,3, MacBookPro6,1, MacBookPro6,2, MacBookPro6,3
 
We hope that the community can also use our tools to the fullest potential, and we want to give some big thanks to Acidanthera for the countless hours, days, months and years spent working on tools used in our project such as OpenCorePkg, Lilu, WhateverGreen, etc 

——Khronokernel

# Changelogs

#### [OpenCore 0.6.4](https://github.com/acidanthera/OpenCorePkg/releases)

- Added `BlacklistAppleUpdate` to fix macOS 11 broken update optout
- Dropped HII services from OpenDuet improving size and performance
- Fixed patching of injected kexts in mkext
- Added support for launching from relative paths
- Added direct path passing for tools via `RealPath`
- Allowed launching tools and entries in text mode via `TextMode`
- Updated builtin firmware versions for SMBIOS and the rest
- Fixed ACPI patches not applying if tables are in locked memory
- Fixed `EnableSafeModeSlide` on macOS 11
- Added `AllowRelocationBlock` quirk for older macOS and safe mode
- Fixed CPU frequency calculation on AMD 19h family
- Updated recovery_urls
- Fixed `DisableSingleUser` quirk when Apple Secure Boot is enabled
- Added `BootstrapShort` to workaround buggy Insyde firmwares
- Changed `Bootstrap(Short)` to choose dynamic entry (requires NVRAM reset)
- Avoided `Boot` prefix in `RequestBootVarRouting` to workaround AMI issues
- Added bootloader patch support in `Booter` `Patch` section
- Fixed startup hang on firmwares allowong reentrance for timer functions
- Made pointer control optional for OpenCanopy via `PickerAttributes`
- Added support for `StartupMute` variable in `PlayChime`
- Added support for per-volume icons for APFS on Preboot
- Removed HII dependency from OpenUsbKbDxe driver
- Fixed undefined behavior in OpenDuet causing random crashes and hangs

#### [Lilu 1.4.5](https://github.com/acidanthera/Lilu/releases)

- Fixed Apple HDEF detection made by NVIDIA
- Fixed race-condition in select kext detection during patching (thx to lvs1974)

#### [AppleALC 1.5.5](https://github.com/acidanthera/AppleALC/releases)

- Fixed kext loading issues on 10.8 and similar operating system
- Added a requirement to inject `alc-verbs` or use `alc-verbs=1` argument for custom verbs
- Added ALC255 layout-id 66 for Dell Optiplex7060/7070MT(Separate LineOut) by Dynamix1997
- Fixed Jack Sense and EAPD on ALC 236 layout ID 14 by erinviegas
- Added VIA VT2021 layout-id 13 support for all 3 analog lineOUTs on Gigabyte GA-Z77X-D3H (rev. 1.0) by enrysan0
- Added ALC283 layout-id 13 for (Alldo)Cube Mix Plus by Aldo97
- Fix PinConfigs ALC662v3 for Lenovo M415-D339
- Added ALC295 layout-id 22 for HP Spectre x360 by aleixjf
- Added ALC285 layout-id 71 for Spectre x360 ap0xxx by jpuxdev
- Added ALC221 layout-id 88 for HP ProDesk 400 G2 Desktop Mini PC by dragonbbc
- Added CX8200 layout-id 80 for LG Gram 17 17z990 by rdmitry0911
- Added ALC269 layout-id 91 for Chuwi CoreBox by Luca1991
- Modify CX20632 layout-id 20 - Added Mic support and outputs mute controls - HP EliteDesk 800 G4/G5 mini by sisumara
- Added ALC671 layout-id 16 for Fujitsu Q558 by sisumara
- Added `-dev` option to alc-verb to support sending commands to all codecs

#### [WhateverGreen 1.4.5](https://github.com/acidanthera/WhateverGreen/releases)

- Enabled loading in safe mode (mainly for AGDP fixes)
- Resolved an issue that the maximum link rate fix is not working properly on Intel Comet Lake platforms. (Thanks @CoronaHack)
- Allowed enabling `igfxrpsc` on Comet Lake
- Fixed failed to route IsTypeCOnlySystem warning from Skylake to Ice Lake

#### [VirtualSMC 1.1.9](https://github.com/acidanthera/VirtualSMC/releases)

- Improve manual fan control in SMCDellSensors (use control registers 0x35a3 and 0x34a3 to cover more Dell models)
- Fix processKext in SMCDellSensors (could be called multiple times for the same kext since flag Reloadable was set)
- Reduce audio lags in SMCDellSensors when USB audio device is used
- Allow not injecting TB0T SMC key when it is unavailable in SMCBatteryManager
 
#### [AirportBrcmFixup 2.1.2](https://github.com/acidanthera/AirportBrcmFixup/releases)

- Do not patch airport drivers missing in the system (set of available drivers depends on the system version). 
For systems with manually added airport drivers this behaviour can be overridden by boot-arg or property `brcmfx-alldrv`

#### [HibernationFixup 1.3.8](https://github.com/acidanthera/HibernationFixup/releases)

- Improve auto hibernation: immediate hibernate if standbydelaylow / autopoweroffdelay is 0, fast resume after hibernate, code cleanup

#### [VoodooPS2 2.1.8](https://github.com/acidanthera/VoodooPS2/releases)

- Disabled PrntScr remap by default, see `SSDT-PrtSc-Remap.dsl` for example to re-enable it
- Disabled Command and Option remap by default, see `SSDT-Swap-CommandOption.dsl` for example to re-enable it

#### [VoodooInput 1.0.9](https://github.com/acidanthera/VoodooInput/releases)

- Add trackpoint device from VoodooTrackpoint

#### [MaciASL 1.5.9](https://github.com/acidanthera/MaciASL/releases)

- Updated iasl compiler versions
- Updated icons for Big Sur UI
- Updated bundled iasl compilers
- Compatibility with macOS 10.8 or older is not guaranteed
- Fixed crashes when processing certain ACPI files
- Fixed DSDT fetch error on Apple Silicon
