---
layout: post
title:  "Acidanthera Updates: February 2021"
date:   2021-02-01 15:00:00 -0700
categories: Hackintosh updates
---

* [A message from vit9696](#a-message-from-vit9696)
* [Dortania Updates](#dortania-updates)
* [Changelogs](#changelogs)

# A message from vit9696

{Insert message}

——Vit

# Dortania Updates

A new year and a whole of changes from us and Acidanthera! As Vit mentioned earlier, BootProtect has now been reworked into LaucherOption and we've updates the Post Install Guide accordingly. This also includes a new section just for those updating, in cases where people may be a bit overwhelmed with the Configuration.pdf:

* [Updating Bootstrap in 0.6.6](https://dortania.github.io/OpenCore-Post-Install/multiboot/bootstrap.html#updating-bootstrap-in-0-6-6)

Besides the main user facing changes with Dortania, I've taken a bit of time to experiment with Apple's latest silicon. Specifically emulating older versions of Mac OS X and macOS on an M1 MacBook Pro and even on iOS devices. You can read a bit more about my experiment here(even ended up with a geekbench single core of [68!](https://browser.geekbench.com/v5/cpu/6070899)):

* [Virtualizing OpenCore and x86 macOS on Apple Silicon (and even iOS!)](https://khronokernel.github.io/apple/silicon/2021/01/17/QEMU-AS.html)

——Khronokernel

# Changelogs

#### [OpenCore 0.6.6](https://github.com/acidanthera/OpenCorePkg/releases)

- Added keyboard and pointer entry scroll support in OpenCanopy
- Added background image support in OpenCanopy
- Fixed selector boot option choice in OpenCanopy
- Relaxed selector dimensions for OpenCanopy
- Added `MaxBIOSVersion` option to `Generic`
- Fixed MLB verification feature in macrecovery
- Replaced `VBoxHfs` driver with `OpenHfsPlus`
- Added audio codec dumping to `SysReport`
- Fixed compatibility with page protection for all binaries
- Fixed crashes in OpenUsbKbDxe when handling unsupported devices
- Removed `HdaCodecDump` application in favor of `SysReport`
- Added `SetApfsTrimTimeout` to tune APFS trim command
- Changed `OpenCore.efi` to application to improve FW compatibility
- Added `DisableSecurityPolicy` UEFI quirk to workaround driver loading
- Added support for ranged widget connections in AudioDxe
- Fixed supplying non-RT `SetVirtualAddressMap` for non-macOS systems
- Fixed using `SystemUuid` from `DataHub` in non-Automatic mode for `SMBIOS`
- Dropped failsafe defaults from `Generic` to match non-Automatic mode
- Replaced `BootProtect` with `LauncherOption` and `LauncherPath`
- Added `OpenPartitionDxe` with Apple Partition Management scheme
- Improved ocvalidate checks in `Misc`, `NVRAM`, and `UEFI` sections

#### [Lilu 1.5.1](https://github.com/acidanthera/Lilu/releases)

- Added `lilu_os_memmem` and `lilu_os_memchr` APIs
- Added `getSharedCachePath` API to obtain current cache path
- Added `LIKELY`/`UNLIKELY` macros

#### [WhateverGreen 1.4.7](https://github.com/acidanthera/WhateverGreen/releases)

- Implemented `unfairgva` device property (use `<01 00 00 00>` value for MP5,1 to enable streaming DRM)

#### [VirtualSMC 1.2.0](https://github.com/acidanthera/VirtualSMC/releases)

- Improve manual fan control in SMCDellSensors (switch off manual control before going to sleep), rename control boot-args (start with -dell)

#### [VoodooPS2 2.2.1](https://github.com/acidanthera/VoodooPS2/releases)

- Fix issue with registering of services matched by property name "RM,deliverNotifications". It solves issue with broadcasting timestamp for the last pressed key and handling of QuietTimeAfterTyping [see bug #1415](https://github.com/acidanthera/bugtracker/issues/1415) 

#### [VoodooInput 1.1.0](https://github.com/acidanthera/VoodooInput/releases)

- Eliminate leftover scaling of physical dimensions by x10

#### [AppleALC 1.5.7](https://github.com/acidanthera/AppleALC/releases)

- Add support for legacy Macs
- Added ALC289 layout-id 99 for Dell XPS 13 9300 by DalianSky
- Added ALC225 layout-id 90 for Dell Inspiron 5379 by fast900
- Added ALC274 layout-id 28 working speakers/mic Maingear Element 3 (TongFang 17 Barebone) by 343iChurch
- Added ALC256 layout-id 77 for Asus x430_s4300FN by fangf2018
- Added ALC256 layout-id 88 for Asus x430_s4300FN by fangf2018
- Fix Mic for ALC221 layout-id 88 HP ProDesk 400 G2 Desktop Mini PC
- Added ALC897 layout-id 66 for ASUS_PRIME_B460M-K by Dynamix1997

#### [BrcmPatchRAM 2.5.6](https://github.com/acidanthera/BrcmPatchRAM/releases)

- Added inject Laird BT851 Bluetooth 5.0 USB dongle
- Added legacy Bluetooth injection kext

#### [dmidecode 3.3b](https://github.com/acidanthera/dmidecode/releases)

- Update to a4b31b2b
