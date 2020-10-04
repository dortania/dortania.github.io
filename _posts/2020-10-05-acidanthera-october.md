---
layout: post
title:  "Acidanthera Updates: October 2020"
date:   2020-10-05 15:00:00 -0700
categories: Hackintosh updates
---

* [A message from vit9696](#a-message-from-vit9696)
* [Guide Updates](#guide-updates)
* [Changelogs](#changelogs)

# A message from vit9696

{Insert inspirational message}

— Vit

# Guide Updates

Just like with last month, we've expanded our guide support once again! Specifically we've now added support for almost every native Intel CPU generation including:

* Yonah, Conroe and Penryn
* Lynnfield and Clarkdale
* Clarksfield and Arrandale
* Nehalem and Westmere

In addition to more legacy support hardware wise, we've also expanded our DuetPkg support to Windows, added more OS X install methods including 10.4 and much more info on legacy quirks in OpenCore. This is all thanks to the rigorous work from [@goldfish64](https://github.com/Goldfish64) and [@vit9696](https://github.com/vit9696) on adding more legacy support to OpenCore itself!

We had quite a bit fun going back and messing with older versions of OS X and even experience some versions for the first time. I made a mini thread about my hardware here: [One box, every x86 install! HP DC 7900](https://www.reddit.com/r/hackintosh/comments/j0d6t0/one_box_every_x86_install_hp_dc_7900/)

* [OpenCore Install Guide](https://dortania.github.io/OpenCore-Install-Guide/)

— Khronokernel

# Changelogs

#### [OpenCore 0.6.2](https://github.com/acidanthera/OpenCorePkg/releases)

- Updated builtin firmware versions for SMBIOS and the rest
- Added `ProcessorType` option to `Generic` allowing custom CPU names
- Fixed `UnblockFsConnect` option not working with APFS JumpStart
- Added IA32 binary variant to the release bundles
- Fixed improper handling of cacheless kexts without an Info.plist
- Fixed improper calculation of kext startup address for blocking
- Added mkext 32-bit kext injection (10.4-10.6)
- Added cacheless 32-bit kext injection (10.4-10.7)
- Added 32-bit kernel/kext patching/blocking support
- Fixed issues loading 10.7 EfiBoot
- Added `Type` to `ReservedMemory` to fulfil hibernation hack needs
- Added workaround to displaying `Preboot` instead of `Macintosh HD`
- Added prelinkedkernel 32-bit kext injection (10.6-10.7)
- Added `SystemMemoryStatus` to override memory replacement on some models
- Added older Pentium CPU recognition in SMBIOS 
- Added `ExtendBTFeatureFlags` to properly set `FeatureFlags` for Bluetooth (which substitutes BT4LEContinuityFixup) 
- Added `MinKernel`/`MaxKernel` to CPUID emulation and `DummyPowerManagement`
- Fixed `-legacy` not being added in `KernelArch` `Auto` mode
- Fixed `i386-user32` not forcing `i386` on macOS 10.7 on X64 firmwares
- Fixed `i386-user32` being incorrectly enabled in macOS 10.4, 10.5, and 10.7
- Disabled prelinked boot for macOS 10.4 and 10.5 in `KernelCache` `Auto` mode
- Fixed `macserial` compatibility with iMac20,x serials and other models from 2020
- Added `LegacyCommpage` quirk to improve pre-SSSE3 userspace compatibility
- Fixed legacy SATA HDDs displaying as external drives in the picker

### [Lili 1.4.8](https://github.com/acidanthera/Lilu/releases)

- Added MacKernelSDK with Xcode 12 compatibility
- Removed `kern_atomic.hpp` due to MacKernelSDK implementation
- Acidanthera MacKernelSDK is now required for all plugins
- Fixed Lilu loading on macOS 10.6 (not all APIs will be functional)
- Fixed plugin debug log not working with Lilu disabled

#### [AppleALC 1.5.3](https://github.com/acidanthera/AppleALC/releases)

- Fix ALCS1200A lost ID 11 by owen0o0
- Added MacKernelSDK with Xcode 12 compatibility

#### [WhateverGreen 1.4.3](https://github.com/acidanthera/WhateverGreen/releases)

- Added CFL and CML P630
- Added MacKernelSDK with Xcode 12 compatibility
- Fixed loading on macOS 10.11 and earlier

#### [VirtualSMC 1.1.7](https://github.com/acidanthera/VirtualSMC/releases)

- Added MacKernelSDK with Xcode 12 compatibility
- Fixed SMCDellSensors loading on macOS 10.8
- Added VirtualSMC support for 10.6 (most plugins require newer versions)
- Fixed rare kernel panic in SMCSuperIO
 
#### [AirportBrcmFixup 2.1.0](https://github.com/acidanthera/AirportBrcmFixup/releases)

- Add pci14e4,4331, pci14e4,4353  and pci14e4,4357  into AirPortBrcmNIC_Injector.kext  (in 11.0 only AirPortBrcmNIC can support these devices)
- Added MacKernelSDK with Xcode 12 compatibility
- Fixed macOS 10.8 compatibility (without ASPM support)

#### [HibernationFixup 1.3.6](https://github.com/acidanthera/HibernationFixup/releases)

- Postpone RTC wake in AppleRTC::setupDateTimeAlarm according to current standby/autopoweroff delay (if auto-hibernate feature and standby/autopoweroff is on)
in order to avoid earlier wake.

#### [RTCMemoryFixup 1.0.7](https://github.com/acidanthera/RTCMemoryFixup/releases)

- Added MacKernelSDK with Xcode 12 compatibility

#### [CPUFriend 1.2.2](https://github.com/acidanthera/CPUFriend/releases)

- Added MacKernelSDK with Xcode 12 compatibility

#### [DebugEnhancer 1.0.2](https://github.com/acidanthera/DebugEnhancer/releases)

- Added MacKernelSDK with Xcode 12 compatibility

#### [NVMeFix 1.0.4](https://github.com/acidanthera/NVMeFix/releases)

- Added MacKernelSDK with Xcode 12 compatibility

#### [IntelMausi 1.0.4](https://github.com/acidanthera/IntelMausi/releases)

- Added MacKernelSDK with Xcode 12 compatibility
- Added IntelSnowMausi variant for 10.6-10.8

#### [BrcmPatchRAM 2.5.5](https://github.com/acidanthera/BrcmPatchRAM/releases)

- Initial MacKernelSDK and Xcode 12 compatibility
- Added bundled BrcmPatchRAM.kext to the binaries

#### [VoodooInput 1.0.7](https://github.com/acidanthera/VoodooInput/releases)

- Initial MacKernelSDK and Xcode 12 compatibility

#### [VoodooPS2 2.1.7](https://github.com/acidanthera/VoodooPS2/releases)

- Initial MacKernelSDK and Xcode 12 compatibility
- Added support for select ELAN touchpads by BAndysc and hieplpvip
- Added constants for 11.0 support

#### [CpuTscSync 1.0.3](https://github.com/acidanthera/CpuTscSync/releases)

- Added MacKernelSDK with Xcode 12 compatibility

#### [BrightnessKeys 1.0.0](https://github.com/acidanthera/BrightnessKeys/releases)

- Initial release