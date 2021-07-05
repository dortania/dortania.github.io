---
layout: post
title:  "Acidanthera Updates: July 2021"
date:   2021-07-05 14:45:00 -0400
categories: Hackintosh updates
---

* [A message from vit9696](#a-message-from-vit9696)
* [Changelogs](#changelogs)

# A message from vit9696

It’s nice to see us moving forward with another macOS iteration bringing stabilization to a major overhaul we saw last year. macOS 12 is an all-around positive change from what we experienced since it fixed a fair number of bugs and brought rather few deprecations, bringing several new features on the surface and changing little in the background. Another thing to come was Windows, which a number of our users rely on, and its new version with new system requirements.

As most of you noticed, OpenCore 0.7.0 works just fine with both macOS 12 and Windows 11 without any special changes in normal circumstances. With macOS, some minor nuances needed to be addressed. Some quirks broke (e.g. `ProvideCurrentCpuInfo` or `PowerTimeoutKernelPanic`) and we fixed them. SMBIOS identifiers were also updated and we synced our database. OpenCanopy flavour recommendations were updated in addition to fixing some issues spotted with certain setups thanks to the attentive eyes of [@MikeBeaton](https://github.com/MikeBeaton). To help identifying and diagnosing the hardware on newer hardware setups [@PMheart](https://github.com/PMheart) included CPU MSR and PCI device information in the SysReport OpenCore functionality.

For Windows 11 we provided [a document](https://www.applelife.ru/posts/947082), outlining the requirements and the potential paths to work around them, hopefully avoiding any future misunderstanding. Besides that, we created a new tool, named `TpmInfo`, which helps everyone understand Intel hardware capabilities in regards to firmware TPM. Time will show whether we can find the resources to emulate certain features requested by Windows 11 in OpenCore, but it is not our priority at the moment, since roughly any post-Skylake system is compatible and only 8-year-old systems will optionally need emulation. As a reminder, please note, that any system needs to have _UEFI Secure Boot_ functionality enabled to properly support Windows 11. OpenCore has fully supported this for quite some time, and all the instructions are already included in the corresponding section of the OpenCore reference manual. We will later release a Dortania guide that is easier to follow. 

On the kernel side, there were several really important changes. Lilu got a brand new kext patcher, which unifies the approach for all the operating systems from macOS 10.6 to macOS 12, avoiding many hacks we had earlier and making our QC more reliable. As usual, all the plugins will need to be updated to support macOS 12, and we have already made changes in most of our own plugins, which are also included in this update. Many plugins are now also supported on macOS 10.6 (in 64-bit mode), including AppleALC, VirtualSMC, SMCBatteryManager, and WhateverGreen. All of this comes as a result of enormous work by [@Goldfish64](https://github.com/Goldfish64). After some research with [@dhinakg](https://github.com/dhinakg) we were able to find a solution for Bluetooth issues on macOS 12, which landed as a standalone kext named BlueToolFixup. To keep more continuity features available on an as-is basis [@khronokernel](https://github.com/khronokernel) brought more patches to SidecarFixup, making it widen the support of AirPlay to Mac, Universal Control, and so on.

This is all for today, a complete changelog is provided below.
———Vit

# Changelogs

#### [OpenCore 0.7.1](https://github.com/acidanthera/OpenCorePkg/releases)

- Added `SyncTableIds` quirk to sync modified table OEM identifiers
- Added CPU Info (MSRs) dumping to `SysReport`
- Updated builtin firmware versions for SMBIOS and the rest
- Fixed `PowerTimeoutKernelPanic` on macOS 12
- Fixed transparency click detection on OpenCanopy boot entries
- Added PCI device info dumping to `SysReport`
- Fixed `SetApfsTrimTimeout` on macOS 12
- Documented requirement for SetDefault.icns width to match Selector.icns width
- Added explicit warn and safe fallback to builtin picker on failure to match the above
- Added VSCode source level IDE debug config example to debug docs
- Added other minor debug docs updates
- Fixed incorrect timeout of built-in picker on IA32
- Added support for custom kernels on ESP partition
- Fixed DEBUG ASSERT on pressing change entry keys with single boot entry in OpenCanopy
- Added recommended `Apple12` and `Windows11` flavours
- Added `TpmInfo` tool to DEBUG TPM status
- Fixed incorrect OpenCanopy initial display when default entry beyond right of screen
- Fixed `ProvideCurrentCpuInfo` MSR patch on macOS 12

#### [Lilu 1.5.4](https://github.com/acidanthera/Lilu/releases)

- Allow loading on macOS 12 without `-lilubetaall` (With adapted for macOS 12 plug-ins)
- Added guarding for address slot usage to avoid potential kernel routing overflow
- Allow using medium size function routing in the kernel
- Added medium size function routing for `Long` mode as they are functionally equivalent
- Added `matchSharedCachePath` API to support dyld cache matching on macOS 12
- Added `_kmod` hooking for kext listening to unify kext patcher logic
- Added zlib decompression API
- Fixed kernel patcher support on 64-bit 10.6
- Added new GPU switching API

#### [AppleALC 1.6.2](https://github.com/acidanthera/AppleALC/releases)

- Added constants for macOS 12 support
- Added 10.6 and 10.7 support in 64-bit mode

#### [VirtualSMC 1.2.5](https://github.com/acidanthera/VirtualSMC/releases)

- Added preliminary macOS 12 support
- Added macOS 10.6 support for SMCBatteryManager

#### [WhateverGreen 1.5.1](https://github.com/acidanthera/WhateverGreen/releases)

- Added constants required for macOS 12 update
- Added Intel Arrandale graphics support on 10.6 and 10.7 64-bit

#### [CPUFriend 1.2.4](https://github.com/acidanthera/CPUFriend/releases)

- Added constants for macOS 12 support

#### [RestrictEvents 1.0.3](https://github.com/acidanthera/RestrictEvents/releases)

- Added constants for macOS 12 support
- Rewrote `eficheck` restrictions to avoid slowdowns

#### [DebugEnhancer 1.0.3](https://github.com/acidanthera/DebugEnhancer/releases)

- Added constants for macOS 12 support

#### [SidecarFixup 1.0.2](https://github.com/acidanthera/SidecarFixup/releases)

- Added constants for macOS 12 support
- Fixed macOS 12 shared cache compatibility
- Unlock AirPlay to Mac, Universal Control and NightShift Functionality

#### [NVMeFix 1.0.9](https://github.com/acidanthera/NVMeFix/releases)

- Added constants for macOS 12 support
- Fixed macOS 12 compatibility

#### [BrcmPatchRAM 2.6.0](https://github.com/acidanthera/BrcmPatchRAM/releases)

- Added BlueToolFixup for macOS 12 compatibility

#### [IntelMausi 1.0.7](https://github.com/acidanthera/IntelMausi/releases)

- Added force WOL support (`mausi-force-wol` device property or `-mausiwol` boot argument)

#### [VoodooPS2 2.2.4](https://github.com/acidanthera/VoodooPS2/releases)

- Fixed incorrect command gate initialization causing panics

#### [AirportBrcmFixup 2.1.3](https://github.com/acidanthera/AirportBrcmFixup/releases)

- Added constants for macOS 12 support


