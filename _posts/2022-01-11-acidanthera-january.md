---
layout: post
title: "Acidanthera Updates: January 2022"
date: 2022-01-11 13:30:00 -0500
categories: Hackintosh updates
---

* [A message from vit9696](#a-message-from-vit9696)
* [Changelogs](#changelogs)

# A message from vit9696

Welcome to 2022! We are glad to meet you with this year's first update of our products. After getting the well deserved rest, which lasts a bit longer in Russia than the winter holidays in several other countries, we tried to push all the fixes for the most annoying issues.

Lilu now works correctly with some third-party plugins on macOS Catalina and older after introducing a regression by the December update. Thanks to @Goshin for their time and patience tracking this down. RestrictEvents now also blocks the unreadable disk popup and enables the memory configuration view on all models thanks to @Goldfish64. @khronokernel additionally included new abilities for Hypervisor spoofing used in OCLP on legacy Macs.

AppleALC got controller patch improvements following the Z690 series as well as the new audio resources. gfxutil was fixed to support Apple Silicon as well as parse legacy Mac device paths, thanks to @joevt. FeatureUnlock also includes fixes for the AirPlay to Mac support introduced in the previous release.

As for OpenCore, it got two major changes. First is the audio driver reengineering, which allowed for support of many more audio controllers including Apple hardware, thanks to @mikebeaton, and second is the quirk we created to activate the efficiency cores on Intel Alder Lake. More details on Intel Alder Lake are provided in a [separate post](https://dortania.github.io/hackintosh/updates/2022/01/09/alder-lake.html).

Have a nice winter,

— Vit

# Changelogs

#### [OpenCore 0.7.7](https://github.com/acidanthera/OpenCorePkg/releases)

- Fixed rare crash caused by register corruption in the entry point
- Added `ProvideCurrentCpuInfo` support for Intel Alder Lake
- Fixed typo in `Cpuid1Data` recommendations for Intel Rocket Lake and newer
- Updated builtin firmware versions for SMBIOS and the rest
- Updated underlying EDK II package to edk2-stable202111
- Resolved crashes in QEMU with AudioDxe
- Added AudioDxe settings caching (avoids non-needed setup delays)
- Added DisconnectHda quirk to allow UEFI sound on Apple hardware and others
- Added workarounds for bugs in QEMU `intel-hda` driver to allow UEFI sound in QEMU
- Implemented multi-channel (e.g. bass+main speaker; speakers+headphones) UEFI sound with `AudioOutMask`
- Fixed AudioDxe startup stalls when Nvidia HDA audio is present
- Resolved AudioDxe disabling sound in Windows on some firmware
- Added pointer polling period tuning in the builtin AppleEvent implementation
- Added pointer device list tuning in the builtin AppleEvent implementation
- Added VREF handling to support UEFI sound on more Apple hardware
- Updated audio output channel detection to support UEFI sound on more Apple hardware
- Added manual GPIO config (use `--gpio-setup` AudioDxe driver argument for UEFI sound on Apple hardware)
- Switched UEFI audio levels to decibel gain to allow accurate matching of saved macOS volume levels
- Separated settings for minimum audio assist volume and minimum audible volume

#### [RestrictEvents 1.0.6](https://github.com/acidanthera/RestrictEvents/releases)

- Fixed memory view restrictions for `MacBookAir` and `MacBookPro10` not being correctly disabled
- Disabled `The disk you inserted was not readable by this computer` message popup
- Added Content Caching support for systems exposing `kern.hv_vmm_present` via `-revasset`
- Lowered OS requirement for `-revsbvmm` to macOS 11.3

#### [FeatureUnlock 1.0.5](https://github.com/acidanthera/FeatureUnlock/releases)

- Fixed AirPlay to Mac UDM patching regression

#### [AppleALC 1.6.8](https://github.com/acidanthera/AppleALC/releases)

- Replace patch for 500 Series(0x43C8) PCH HD Audio
- Added ALC269-VC for Samsung NP540U4E #752 by @majonez
- Added ALC1220A layout 8 for MSI z490i unify by @viorel78
- Added front panel connections in ALC892 layout 23 for ASRock B365 Pro4 by @TheHackGuy
- Removed redundant 8086:A171 controller patches by @al3xtjames
- Fixed wakeconfigdata for ALC236 LayoutID 36 by @volcbs
- Fixed Combo jack for CX8200 layout-id 80 by @vivzero
- Added ALC897 layout 11 for GIGABYTE Z590M

#### [WhateverGreen 1.5.6](https://github.com/acidanthera/WhateverGreen/releases)

- Fixed deprecated code in unfairgva

#### [Lilu 1.5.9](https://github.com/acidanthera/Lilu/releases)

- Fixed memory corruption when mixing cs_validate_range/page mid/long routes (thx @Goshin)
- Enforced all routes to be slotted after one slotted route
- Refactored all internal routes to use new RouteRequest API
- Deprecated routeFunction APIs as they are dangerous to use for multiple routes

#### [gfxutil 1.82b](https://github.com/acidanthera/gfxutil/releases)

- Fixed handling of Mac EFI malformed paths, thx @joevt
- Added Apple Silicon support
