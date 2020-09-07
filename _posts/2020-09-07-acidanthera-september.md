---
layout: post
title:  "Acidanthera Updates: September 2020"
date:   2020-09-07 15:00:00 -0700
categories: Hackintosh updates
---

* [A message from vit9696](#a-message-from-vit9696)
* [Guide Updates](#guide-updates)
* [Changelogs](#changelogs)

# A message from vit9696

The summer is over and I am glad to meet you all in the beginning of autumn. Some of you might not remember but today is a very important day for the team. Exactly one year ago on 7 September OpenCore went out of a developer preview stage. Now we have accomplished many goals and created a mature product that is fast, functional, and easy to use. We continue to move forward with all our products and do the best to explore the opportunities in front of us.

One of the important parts of all our pursuits has always been interacting with the community. By making it convenient for the fellow engineers to contribute we enabled the opportunity to not only breed the new features from the inside but also let them to be offered from the outside. For instance, [AppleALC](https://github.com/acidanthera/AppleALC) is one of the greatest examples of such community collaboration we were able to achieve. This release includes Ice Lake IGPU patches by [@0xFireWolf](https://github.com/0xFireWolf) in [WhateverGreen](https://github.com/acidanthera/WhateverGreen), battery supplement information by [@zhen-zen](https://github.com/zhen-zen) in [SMCBatteryManager](https://github.com/acidanthera/VirtualSMC), much improved hotkey handling by [@varahash](https://github.com/varahash) in [OpenCore](https://github.com/acidanthera/OpenCorePkg/), and several other changes all provided externally.

Many will agree that doing laptop support is a non-trivial thing. There are many differences in both hardware and firmware across even very similar models. For us it means that we will never be able to cover all the peculiarities. In most cases you will be all alone with your issue and your only option will be to debug the driver yourself. Even so, we try to do what is practical. For example, [itlwm](https://github.com/usr-sse2/itlwm) IO80211Family integration I announced earlier is continuing to move forward and [@usr-sse2](https://github.com/usr-sse2) was able to achieve considerable progress with WPA Enterprise you will find in the upcoming commits. [AirportBrcmFixup](https://github.com/acidanthera/AirportBrcmFixup) was also improved quite a bit by [@lvs1974](https://github.com/lvs1974) bringing better compatibility with older operating systems and resolving some long-standing issues with exotic setups. [HibernationFixup](https://github.com/acidanthera/HibernationFixup) also got better.

Now to OpenCore. With 0.6.1 we managed to fit what we have planned long ago: macOS Snow Leopard support and Apple Secure Boot. When [@Goldfish64](https://github.com/Goldfish64) said he is adding Snow Leopard support, we immediately realized that this is a challenge. Nevertheless we all supported that initiative as much as we could, as macOS 10.6 is very dear to us. This release is the first release to showcase our efforts: macOS 10.6 will install and launch at top notch speeds as you always expect from OpenCore. Not only we fully support the installation but we are first to implement the fastest available kernel caching with fuzzy matching easily beating Chameleon performance.

Apple Secure Boot is a thing that makes sure that your Apple operating system is correctly installed and is not corrupted by a drive failure for instance. Before OpenCore it was only available to Macs with T2 and now, thanks to [@Download-Fritz](https://github.com/Download-Fritz) efforts, it is supported on any UEFI compatible firmware letting the developers and security researchers understand the boot flow of modern Apple Hardware. While it is just a preview and it is yet to undergo the security audit, you can already try it along with UEFI Secure Boot.

Enjoy the new features and see you soon.

— Vit

# Guide Updates

This month we've actually had numerous updates to the guides including adding the [Apple secure boot](https://dortania.github.io/OpenCore-Post-Install/) guide and even expanding our config guides to include even more hardware generations:

* Sandy Bridge(Both mobile and desktop)
* Ivy Bridge-E(HEDT and server)

And we also have plans to expand for UEFI based secure boot and adding Nehalem guides, however due to time constraints this will likely be added with next month's release. We really hope you enjoy the updated guides to go along side 0.6.1!

* [OpenCore Install Guide](https://dortania.github.io/OpenCore-Install-Guide/)
* [OpenCore Post-Install](https://dortania.github.io/OpenCore-Post-Install/)

— Khronokernel

# Changelogs

#### [OpenCore 0.6.1](https://github.com/acidanthera/OpenCorePkg/releases)

* Improved recognition of early pressed hotkeys, thx @varahash
* Made DMG loading support configurable via `DmgLoading`
* Added iMac20,1 and iMac20,2 model codes
* Fixed display name for older Xeon CPUs like Xeon E5450
* Added Comet Lake-LP HDA device code
* Fixed OS boot selection on SATA controllers with legacy OPROMs
* Fixed RSDP ACPI table checksum recalculation
* Added immutablekernel loading support for 10.13+
* Fixed solving some symbols to zero in 11.0 kext inject
* Reduced OpenCanopy size by restricting boot management access
* Added `BuiltinText` variant for `TextRenderer` for older laptops
* Fixed `SyncRuntimePermissions` creating invalid MAT table
* Added EFI FAT image loading support (macOS 10.8 and earlier)
* Added 64-bit cacheless kext injection and patching support (macOS 10.9 and earlier)
* Added 64-bit mkext kext injection and patching support (macOS 10.6 and earlier)
* Fixed XNU hook matching non-kernel files
* Updated builtin firmware versions for SMBIOS and the rest
* Fixed patching of ACPI tables in low memory
* Fixed macOS 11.0 DMG recovery loading without hotplug
* Fixed `XhciPortLimit` quirk on 10.12.6 and possibly other versions
* Fixed `IncreasePciBarSize` quirk on 10.11.5 and possibly other versions
* Fixed `LapicKernelPanic` quirk on 10.8.5 and possibly other versions
* Fixed hard-lock caused by EHCI SMI in OpenDuetPkg
* Added preview UEFI Secure Boot compatibility
* Added `FuzzyMatch` option to support fuzzy kernelcache matching on 10.6 and earlier
* Added `KernelArch` option to specify architecture preference on older kernels
* Added `KernelCache` option to specify kernel caching preference for older kernels
* Added `Force` section to provide support for injecting drivers in older macOS
* Changed kernel driver injection to happen prior to kernel driver patching
* Added `Arch` filtering option to `Add`, `Block`, `Force`, and `Patch` sections
* Added `DisableLinkeditJettison` quirk to workaround 11.0b5 kernel panics
* Added debugging of missing fields in the configuration

#### [AppleALC 1.5.2](https://github.com/acidanthera/AppleALC/releases)

* Added missing layout7.xml for CA0132
* Added 400 series 0xA3F0 controller patch by goomadao
* Added ALCS1200A layout-id 11 for MAG-Z490-TOMAHAWK by owen0o0
* Added ALC269 layout-id 128 for Laptop NS4SL01 by ryahpalma
* Added ALCS1200A layout-id 50 for Gigabyte B460M Aorus Pro by VanXNF
* Added ALC280 layout-id 17 for Dell Optiplex 9020 SFF by pkendall64
* Added ALC236 layout-id 14 for Lenovo 330S by erinviegas
* Added ALC887 layout-id 12 for ASUS H81M-D by VanXNF
* Added ALCS1200A layout-id 49 for Asrock Z490M-ITX by VanXNF
* Added ALC269 layout-id 23 for Thinkpad T430 with fixed micophone inputlevel by haotiangood
* Added ALC245 layout-is 11 and 12 for Lenovo by soto2080
* Added ALC245 layout-id 13 for HP Omen 15 2020 by lunjielee
* Added ALC287 layout-id 11 for HP Omen 15 2020 by lunjielee

#### [VirtualSMC 1.1.6](https://github.com/acidanthera/VirtualSMC/releases)
 
* Added battery supplement info, thx @zhen-zen
* Fix audio lags in Safari caused by reading SMM in SMCDellSensors plugin
* Fix module version for SMCDellSensors, SMCBatteryManager and SMCLightSensor
* Optimised floating point sensor key reading with fewer arithmetic operations
* Improved SMCProcessor CPU power consumption by relaxing core synchronisation
* Fix key sensor key enumeration on Macmini8,x and MacBookPro models

#### [HibernationFixup 1.3.5](https://github.com/acidanthera/HibernationFixup)

* Postpone RTC wake in AppleRTC::setupDateTimeAlarm according to current standby/autopoweroff delay (if auto-hibernate feature and standby/autopoweroff is on) in order to avoid earlier wake.

#### [WhateverGreen 1.4.2](https://github.com/acidanthera/WhateverGreen/releases)

* Fixed `disable-external-gpu` (`-wegnoegpu`) on some systems
* Disabled RPS control patch by default due to a bug in 10.15.6 IGPU drivers
* Replaced `igfxnorpsc=1` with `igfxrpsc=1` to opt-in RPS control patch
* Support all valid Core Display Clock (CDCLK) frequencies to avoid the kernel panic of "Unsupported CD clock decimal frequency" on Intel ICL platforms. (by @0xFireWolf)
* Fix the kernel panic caused by an incorrectly calculated amount of DVMT pre-allocated memory on Intel ICL platforms. (by @0xFireWolf)

#### [Lilu 1.4.7](https://github.com/acidanthera/Lilu/releases)

* Added more platform headers for plugin compilation
* Fixed symbol chainloading regression in 1.4.6

#### [AirportBrcmFixup 2.0.9](https://github.com/acidanthera/AirportBrcmFixup/releases)

* boot-arg and property `brcmfx-aspm` supports special value `255` in order to skip logic disabling APSM for 0x14e4:0x43a3 (DW1820A). It can be used if you have masked pin 53 (CLKREQ#) and APSM L0|L1 is working.
* Improve service matching (the old implementation could cause hangs on boot)

#### [MaciASL 1.5.8](https://github.com/acidanthera/MaciASL/releases)

* Fixed parse error
