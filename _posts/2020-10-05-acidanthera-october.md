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

We are very pleased to meet you this evening to present our latest achievements in the scene. This update is particularly remarkable for one reason: today, OpenCore becomes the only openly available bootloader capable of running any version of macOS released for Intel CPUs, spanning as early as macOS 10.4 to macOS 11 (which is currently in the late beta phase). Most importantly, the architecture we created allows us to perform a very clean integration both code-wise and configuration-wise, allowing the user to have a single configuration for every macOS version ever needed. My congratulations go to all who made this possible.

Last month we stated that collaboration is a primary goal for Acidanthera in every aspect, and today we present our next steps in this direction. If you use multiple macOS versions you might have noticed that some kexts may not always work on an older operating system if built with a newer Xcode version. This is because the macOS kernel SDK is version dependent and does not always respect the API and ABI differences in the kernel. Previously we used various workarounds available in most Acidanthera kexts which let us target macOS 10.8 and sometimes even lower, and now these workarounds are available to everyone as a standalone product: [MacKernelSDK](https://github.com/acidanthera/MacKernelSDK). This product lets you build kernel extensions with basically any recent Xcode version for basically any macOS version. It is very easy to integrate in your environment and all the kexts in Acidanthera have already been migrated, providing a great example to numerous popular third-party kexts migrating right now.
 
Another important side of the collaboration is the ability to share our code. Previously, we made it possible to build standalone drivers like [OcQuirks](https://github.com/ReddestDream/OcQuirks) (which provided a compatibility layer for legacy bootloaders) and we also shared our code with various projects for classic Mac Pros letting them work with most GPUs available on the market. This time, we shared our core code with a popular legacy bootloader named [Clover](https://github.com/CloverHackyColor/CloverBootloader), letting it launch recent versions of macOS. Surely, we understand that such a project will never be as stable, fast, or secure as the original; that goes without saying. However, the users are those who we actually value. and we understand that not all these users have completed the migration, and so as part of our goodwill, we give them an ability to postpone this a little longer. Take your time while we care for your productivity.

For the technical part of the story, I cannot miss the chance to shed a little light on some key changes. [@Goldfish64](https://github.com/Goldfish64) merged all the remarkable work dedicated to 32-bit macOS compatibility, making it possible to install basically any version from a clean image through the original installer, even with CPUs as far back as the Pentium 4. To our own surprise, most of the validation team members were pleased to report that the migration of their old machines went very smoothly. [@BAndysc](https://github.com/BAndysc) and [@hieplpvip](https://github.com/hieplpvip) contributed basic ELAN touchpad support to [VoodooPS2](https://github.com/acidanthera/VoodooPS2) with a large number of touchpads working out of the box and more issues currently being worked on. [@zhen-zen](https://github.com/zhen-zen) and [@usr-sse2](https://github.com/usr-sse2) contributed a new driver called [BrightnessKeys](https://github.com/acidanthera/BrightnessKeys) that greatly simplifies the process of ACPI editing for backlight hotkey handling. [@lvs1974](https://github.com/lvs1974) and [@PMHeart](https://github.com/PMHeart) made it possible to reimplement [BT4LEContinuityFixup](https://github.com/acidanthera/BT4LEContinuityFixup)'s functionality into all recent macOS versions as a part of an OpenCore quirk known as `ExtendBTFeatureFlags`. Finally, the advancements in Intel Wireless support by [@usr-sse2](https://github.com/usr-sse2) were also merged upstream and released as a part of the latest [alpha release](https://github.com/OpenIntelWireless/itlwm/releases).

Every release is a considerable amount of effort by a small team with the members spending a lot of their free time to make it possible. They write code, they write documentation, they run a lot of tests, and they help to maintain the repositories and reply on the [bugtracker](https://github.com/acidanthera/bugtracker). While it is not possible to mention everyone in the highlights, I use this ability to thank them all once more.

We hope you enjoy the new features and stay safe as the situation gets more serious outside.

- Vit

# Guide Updates

Just like with last month, we've expanded our guide support once again! Specifically we've now added support for almost every native Intel CPU generation including:

* Yonah, Conroe and Penryn
* Lynnfield and Clarkdale
* Clarksfield and Arrandale
* Nehalem and Westmere

In addition to more legacy support hardware wise, we've also expanded our DuetPkg support to Windows, added more OS X install methods including 10.4 and much more info on legacy quirks in OpenCore. This is all thanks to the rigorous work from [@Goldfish64](https://github.com/Goldfish64) and [@vit9696](https://github.com/vit9696) on adding more legacy support to OpenCore itself!

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

#### [Lilu 1.4.8](https://github.com/acidanthera/Lilu/releases)

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
