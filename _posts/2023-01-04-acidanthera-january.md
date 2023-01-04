---
layout: post
title: "Acidanthera Updates: January 2023"
date: 2023-01-04 17:00:00 +0100
categories: Hackintosh updates
---

* [Acidanthera Updates: A message from PMheart](#acidanthera-updates-a-message-from-pmheart)
* [Changelogs](#changelogs)

# Acidanthera Updates: A message from PMheart

Happy belated new year!

OpenCore 0.8.8 includes several practical fixes: Synchronising with upstream, @savvamitrofanov updated the EDK II package to `edk2-stable202211`. As well, @Andrey1970AppleLife provided us with the latest firmware and keyboard layout information. On Apple Silicon, the prebuilt mtoc binary is now universal, together with fixed OpenDuet build and new secure PE/COFF loader. The ocvalidate tool now allows duplicate tool if FullNvramAccess is different, authored by @mikebeaton. As for the kernel patching engine, @Goldfish64 fixed blocking entries not being processed if one was skipped due to `Arch`. In addition, he also fixed intermittent prelinking failures caused by XML corruption when kext blocking is enabled. @vit9696 also changed the logic of picker hiding: now the magic Acidanthera sequence from OpenCore files is removed, and `.contentVisibility` file is added to hide and disable boot entries. For better Duet debugging, QemuBuild.command supports Linux thanks to @MikhailKrichanov's effort. Last but not least, @Goldfish64 added SD card device path support for boot device selection.

Having hibernated for nearly two years, VoodooInput 1.1.3 is revived with trackpoint logic improvements by @1Revenger1, seperated X and Y axis, higher solution. The addition of divisor for scroll and mouse movement also makes the Voodoo projects better ones. One more thing, @kprinssu worked around crashes with USB devices on macOS 13.

In FeatureUnlock 1.1.2, @khronokernel added AirPlay to Mac unlocking inside Control Center.app.

With continuous contributions to our AppleALC database, new layout configurations for ALC255, ALC1220, ALCS1220A, and 700 series PCH HD Audio have been added thanks to @juniorcaesar, @CaseySJ, and @dreamwhite; these are added to AppleALC 1.7.8.

Included in WhateverGreen 1.6.3, @nikey22 added various GPU identifiers from different Macs, together with the new property `disable-telemetry-load` which disables iGPU telemetry loading by @Goldfish64.

VoodooPS2 2.3.3 fixed scrolling and button issues, as well as DynamicEWMode problem on Lenovo ThinkPad Laptops, thanks to @1Revenger1.

@al3xtjames added Raptor Lake CPU model as of Lilu 1.6.3.

Enjoy,

— PMheart

# Changelogs

#### [OpenCorePkg 0.8.8](https://github.com/acidanthera/OpenCorePkg/releases)

* Updated underlying EDK II package to edk2-stable202211
* Updated AppleKeyboardLayouts.txt from macOS 13.1
* Updated builtin firmware versions for SMBIOS and the rest
* Updated ocvalidate to allow duplicate tool if FullNvramAccess is different
* Fixed `Kernel` -> `Block` entries not being processed if one was skipped due to `Arch`
* Fixed intermittent prelinking failures caused by XML corruption when kext blocking is enabled
* Removed magic Acidanthera sequence from OpenCore files used for picker hiding
* Added `.contentVisibility` to hide and disable boot entries
* Added Linux support to QemuBuild.command used for Duet debugging
* Built in new secure PE/COFF loader
* Added prebuilt mtoc universal binary with Apple Silicon support
* Corrected OpenDuet build on Apple Silicon
* Added SD card device path support for boot device selection

#### [VoodooInput 1.1.3](https://github.com/acidanthera/VoodooInput/releases)

* Added trackpoint logic improvements by @1Revenger1
* Seperated X and Y axis
* Switched to higher resolution (400)
* Added divisor for scroll and mouse movement
* Workaround crashes with USB devices on macOS 13, thx @kprinssu

#### [AppleALC 1.7.8](https://github.com/acidanthera/AppleALC/releases)

* Added ALC255 layout-id 69 for Acer Aspire 3 A315-56-327T by juniorcaesar
* Added ALC1220 layout-id 20 for Gigabyte B550 Vision D by CaseySJ
* Added ALCS1220A layout-id 15 for Asus ROG Strix X570-F Gaming by CaseySJ
* Added 700 series PCH HD Audio by dreamwhite

#### [FeatureUnlock 1.1.2](https://github.com/acidanthera/FeatureUnlock/releases)

* Added AirPlay to Mac unlocking inside Control Center.app
  * Applicable for systems with `kern.hv_vmm_present` set to `1` in macOS Ventura 

#### [MacHyperVSupport 0.9.3](https://github.com/acidanthera/MacHyperVSupport/releases)

* Created daemons for each userspace function replacing hvutil
* Added support for host to guest file copy (Guest Services integration service)
* Fixed very high storage latency when heaving network I/O is occurring

#### [WhateverGreen 1.6.3](https://github.com/acidanthera/WhateverGreen/releases)

* Added various GPU identifiers from different Macs
* Added `disable-telemetry-load` to disable iGPU telemetry loading that may cause a freeze during startup on certain laptops such as Chromebooks.

#### [VoodooPS2 2.3.3](https://github.com/acidanthera/VoodooPS2/releases)

* Fixed rapidly opening pages in browsers while scrolling with the trackpoint
* Fixed buttons on various trackpads (especially those without trackpoints attached)
* Fixed DynamicEWMode problem on Lenovo ThinkPad Laptops (acidanthera/bugtracker#890)

#### [Lilu 1.6.3](https://github.com/acidanthera/Lilu/releases)

* Added Raptor Lake CPU definitions
