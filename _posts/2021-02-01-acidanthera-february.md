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

It is nice to meet you with the first actually made in 2021 release. This time we have a handful changes to share with.
 
As some of you noticed this time we slightly postponed the deadline from the usual, and the primary reason behind this was to be able to include some imminent changes in OpenCore. After some long and tiring work with the PE/COFF loader [@mhaeuser](https://github.com/mhaeuser) (ex Download-Fritz) finally wrote a formal proof of its most critical properties. As we plan to later include it in EDK II and essentially in every new UEFI firmware, we now launch a second testing phase by embedding the up-to-date version in OpenCore. For the bootloader, the most important changes are the fixes for certain potential memory corruptions and enhanced APFS driver signature verification, provided as an extension to the base code. Our technically-inclined users may also find the [original paper](https://github.com/mhaeuser/ISPRASOpen-SecurePE) to be an interesting read.
 
The only more important thing to security is what the end-user interacts with, at least for some :P. This is why [@mhaeuser](https://github.com/mhaeuser) continued his OpenCanopy project introducing item scrolling with a large amount of boot options, background image support, which can also be used as a logo through transparency and background colour, and relaxed image dimensions, which of course are well-documented in the PDF spec following our usual standards. Marginal usability improvements also cover [@PMheart's](https://github.com/PMheart) additions to ocvalidate, which many found really helpful, and [@Goldfish64's](https://github.com/Goldfish64) audio configuration additions to SysReport. Besides that, we got two new drivers: OpenHfsPlus and OpenPartitionDxe. OpenHfsPlus is a tireless effort by [@shchuko](https://github.com/shchuko), who continued [@gsomlo's](https://github.com/gsomlo) and [@nms42's](https://github.com/nms42) work by finishing a poison-free non-GPL HFS+ driver. While it is still inferior to Apple's driver, its speed is clearly better than VBoxHfs, which is now deprecated. OpenPartitionDxe on the other hand improves compatibility with legacy macOS recoveries.
 
Sometimes the changes are not dictated by the necessity to improve things on our end or even our bugs, but rather flaws in the design & code of the other parties. This release includes three changes that happened due to exactly this kind of issues. One of them is the result of Apple’s APFS design, which does not track trimmed areas, resulting in essentially broken trim support for a vast amount of third-party SSDs. The discovery and an ugly workaround are described in the [SetApfsTrimTimeout section](https://github.com/acidanthera/OpenCorePkg/blob/master/Docs/Configuration.pdf) thanks to [@lvs1974's](https://github.com/lvs1974) efforts. The second issue is a design flaw of the older SMBIOS specifications, which caused confusion of how UUIDs can be read and written. While no changes are needed for the existing users, some new users might benefit from the improvements in dmidecode and the new [SetApfsTrimTimeout option](https://github.com/acidanthera/OpenCorePkg/blob/master/Docs/Configuration.pdf). Last but not least was a discovery that some firmwares disable support for UEFI driver loading, even with UEFI Secure Boot disabled. This obviously violates the UEFI specification, but [Microsoft](https://github.com/badstorm/surface-pro-7-opencore/issues/9) thinks differently, breaking the entire loading of OpenCore. If any Microsoft Surface firmware developers are reading this, it will help if you provide a comment on the matter, since even the provided workaround by transitioning to the app only uncovered further issues.
 
Besides OpenCore, our kexts also got notable updates. AppleALC got legacy Mac support, thanks to [@khronokernel](https://github.com/khronokernel), SMCDellSensors got fan control improvements, thanks to [@lvs1974](https://github.com/lvs1974), and on the Lilu side, we added a few helper APIs that show how one can perform basic userspace patches in Big Sur. This was used in WhateverGreen to improve MacPro5,1 compatibility. This makes it all for today; we are all very glad to hear your support.
 
——Vit

# Dortania Updates

A new year and a whole lot of changes from us and Acidanthera! As Vit mentioned earlier, BootProtect has now been reworked into LaucherOption and we've updates the Post Install Guide accordingly. This also includes a new section just for those updating, in cases where people may be a bit overwhelmed with the Configuration.pdf:

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
- Fixed multiple flaws in EFI image loading, APFS driver in particular
- Fixed NVRAM `system-id` being accidentally stored in Little Endian format
- Added `UseRawUuidEncoding` to choose SMBIOS UUID encoding style
- Updated builtin firmware versions for SMBIOS and the rest

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
