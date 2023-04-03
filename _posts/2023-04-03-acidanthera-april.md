---
layout: post
title: "Acidanthera Updates: April 2023"
date: 2023-04-03 17:35:00 +0200
categories: Hackintosh updates
---

* [Acidanthera Updates: A message from PMheart](#acidanthera-updates-a-message-from-pmheart)
* [Changelogs](#changelogs)

# Acidanthera Updates: A message from PMheart

Embracing a warm spring, we published our 2023.04 releases.

OpenCore 0.9.1 brings better support for legacy graphic cards together with bug fixes. To begin with, @corpnewt fixed a minor printing bug in ocvalidate which led to the failure of message printing. @mikebeaton made VS Code debugging easier by providing sample config for gdb. As well, he implemented `GopBurstMode` quirk for faster GOP operation on older firmware; now `SysReport` will also include GOP memory caching reports. Thanks to @vit9696's discovery, we also integrated the new patch for `ThirdPartyDrives` quirk on macOS 13.3 and above. Last but not least, @Andrey1970AppleLife has always continuously updated builtin firmware versions.

macOS Ventura introduced a new check for Continuity Camera which is only available on Kaby Lake and above. FeatureUnlock 1.1.4 patches this restriction to make it possible everywhere thanks to @khronokernel.

Users' consistent maintenance to AppleALC database has been integrated into AppleALC 1.8.1 as well. We would like to thank @lgh07711, @DalianSky, @Pinokyo-H, @wern-apfel, and @imoize, for their contibutions to the configurations of ALC293, Alder Lake PCH-P High Definition Audio Controller (0x51C8), ALC269, ALC623, ALC295, and ALC255 respectively.

To investigate NSS issues, @lvs1974 updated AirportBrcmFixup to 2.1.7 to dump debugging logs from the methods `AirPort_BrcmNIC::setTX_NSS`, `AirPort_BrcmNIC::getTX_NSS`, and `AirPort_BrcmNIC::getNSS`.

As of RestrictEvents 1.1.0, it is possible to disable `hw.optional.f16c` on macOS 13.3 and above. This is particularly useful on Ivy Bridge CPUs where AVX 2.0 instructions are not present, resulting in CoreGraphics.framework crash.

We appreciate @AsdMonio who fixed `board-id` length calculation for legacy Mac models where it is shorter. This is now integrated into BrcmPatchRAM 2.6.5.

In BrightnessKeys 1.0.3, @ChefKissInc added support for certain laptops including AMD ones where `kIOACPILegacyPanel` is used.

Thanks to @1Revenger1, one of the primary authors of our VoodooPS2 project, version 2.3.5 removed `actAsTrackpad` and related logic; and on Elan Touchpads, Trackpoint logic is now powered by VoodooInput.

Enjoy,

— PMheart

# Changelogs

#### [OpenCorePkg 0.9.1](https://github.com/acidanthera/OpenCorePkg/releases)

* Fixed long comment printing for ACPI patches, thx @corpnewt
* Added sample config for VS Code source level debugging with `gdb`
* Updated builtin firmware versions for SMBIOS and the rest
* Added GOP memory caching report to `SysReport`
* Implemented `GopBurstMode` quirk for faster GOP operation on older firmware
* Fixed `ThirdPartyDrives` quirk on macOS 13.3 and above

#### [FeatureUnlock 1.6.4](https://github.com/acidanthera/FeatureUnlock/releases)

* Added Continuity Camera unlocking for pre-Kaby Lake CPUIDs

#### [AppleALC 1.8.1](https://github.com/acidanthera/AppleALC/releases)

* Added ALC293 layout-id 31 for Hasee Z7-CT7NA by lgh07711
* Added Alder Lake PCH-P High Definition Audio Controller (0x51C8) by DalianSky
* Added ALC269 layout-id 111 for minisforum NAG6 by DalianSky
* Added ALC623 layout-id 13 for Lenovo ThinkCentre M720e with internal speaker by Pinokyo-H
* Added ALC295 layout-id 11 for ZenBook UX581 by wern-apfel
* Added ALC255 layout-id 37 for Acer Nitro 5 AN515-52-73Y8 by imoize

#### [AirportBrcmFixup 2.1.7](https://github.com/acidanthera/AirportBrcmFixup/releases)

* Override methods AirPort_BrcmNIC::setTX_NSS, AirPort_BrcmNIC::getTX_NSS and AirPort_BrcmNIC::getNSS to investigate NSS issues. Original method is called, and debug version of kext (with boot-arg -brcmfxdbg) prints info into log

#### [RestrictEvents 1.1.0](https://github.com/acidanthera/RestrictEvents/releases)

* Added `hw.optional.f16c` disabling for macOS 13.3+
  * Resolves CoreGraphics.framework invoking AVX2.0 code paths on Ivy Bridge CPUs
  * Configurable via `revpatch`'s `f16c` argument

#### [BrcmPatchRAM 2.6.5](https://github.com/acidanthera/BrcmPatchRAM/releases)

* Fixed legacy Mac compatibility (thx @AsdMonio)

#### [BrightnessKeys 1.0.3](https://github.com/acidanthera/BrightnessKeys/releases)

* Added legacy panel support in ACPI (thx @ChefKissInc)

#### [VoodooPS2 2.3.5](https://github.com/acidanthera/VoodooPS2/releases)

* Removed actAsTrackpad and related logic
* Fix Trackpoints connected to Elan Touchpads
* Use VoodooInput Trackpoint logic for Elan Touchpads
