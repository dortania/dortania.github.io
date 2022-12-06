---
layout: post
title: "Acidanthera Updates: December 2022"
date: 2022-12-06 17:00:00 +0100
categories: Hackintosh updates
---

* [Acidanthera Updates: A message from PMheart](#acidanthera-updates-a-message-from-pmheart)
* [Changelogs](#changelogs)

# Acidanthera Updates: A message from PMheart

Prior to a nice Christmas and New Year vacation, we slightly updated some of our projects.

To begin with, OpenCore 0.8.7 introduced several minor changes primarily in the GUI. With some reverse engineering from @mikebeaton, and additional helpful input from @cdf and @tsialex, we have now added support for Apple builtin picker on models GPUs without Mac-EFI support, and now the selected entry can be successfully launched using `BootKicker.efi` or `PickerMode` `Apple`. As well, @dakanji updated spoof proof UEFI 2.x checking to OpenVariableRuntimeDxe. After some discussion, we introduced `Misc -> Boot -> HibernateSkipsPicker` not to show picker if waking from macOS hibernation, as a boolean value, in lieu of string settings. @Shaneee fixed TSC/FSB for AMD CPUs in ProvideCurrentCpuInfo; and @mikebeaton removed unwanted clear screen when launching non-text boot entry. We would also like to thank @dreamwhite who helped created the `com.apple.recovery.boot` folder hiearchy in our macrecovery script.

@Goldfish64 created daemons for each userspace function replacing hvutil and added Guest Services integration service support, together with the fix of high storage latency when heaving network I/O is occurring. These changes are included in MacHyperVSupport 0.9.3.

In FeatureUnlock 1.1.1, @khronokernel resolved patch regression on `Macmini8,1` and `iPad` models.

Thanks to @nikey22's contribution, W7170M/S7100X ID is now included in WhateverGreen 1.6.2. In addition, @Andrey1970AppleLife, @dreamwhite, @perez987, and @unChiled helped produce a more readable version of README documentation.

After months of silence, @lvs1974 made HibernationFixup 1.4.7 respect parameters `standbydelaylow`, `standbydelayhigh`, `highstandbythreshold` set via pmset utility, and introduced a new bit in hbfx-ahbm boot-arg: `DoNotOverrideWakeUpTime` = 64, to let macOS decide when wake for standby sleep maintenance.

Starting with VoodooPS2 2.3.2, a new boot argument `ps2kbdonly=1` is introduced by @Kethen to prevent touchpad line from being disabled on reboot.

For AppleALC 1.7.7, we appreciate @littlesum contributing a new layout-id 68 for ALC256 for nuc9.

Enjoy,

— PMheart

# Changelogs

#### [OpenCorePkg 0.8.7](https://github.com/acidanthera/OpenCorePkg/releases)

* Removed unwanted clear screen when launching non-text boot entry
* Fixed TSC/FSB for AMD CPUs in ProvideCurrentCpuInfo, thx @Shaneee
* Added `Misc` -> `Boot` -> `HibernateSkipsPicker` not to show picker if waking from macOS hibernation
* Changed macrecovery to download files into `com.apple.recovery.boot` by default, thx @dreamwhite
* Supported Apple builtin picker (using `BootKicker.efi` or `PickerMode` `Apple`) when running GPUs without Mac-EFI support on units such as the MacPro5,1 (thx @cdf, @tsialex)
* Enabled `PickerMode` `Apple` to successfully launch selected entry
* Enabled `BootKicker.efi` to successfully launch selected entry (via reboot) (thx @cdf)
* Added spoof proof UEFI 2.x checking to OpenVariableRuntimeDxe, thx @dakanji

#### [AppleALC 1.7.7](https://github.com/acidanthera/AppleALC/releases)

* Added ALC256 layout-id 68 for nuc9 by littlesum

#### [FeatureUnlock 1.1.1](https://github.com/acidanthera/FeatureUnlock/releases)

* Resolved Macmini8,1 patch regression from 1.1.0
* Resolved iPad Sidecar patch regression from 1.1.0
  * Applicable if host model did not require Sidecar patch

#### [MacHyperVSupport 0.9.3](https://github.com/acidanthera/MacHyperVSupport/releases)

* Created daemons for each userspace function replacing hvutil
* Added support for host to guest file copy (Guest Services integration service)
* Fixed very high storage latency when heaving network I/O is occurring

#### [WhateverGreen 1.6.2](https://github.com/acidanthera/WhateverGreen/releases)

* Added W7170M/S7100X ID

#### [HibernationFixup 1.4.7](https://github.com/acidanthera/HibernationFixup/releases)

* Respect parameters `standbydelaylow`, `standbydelayhigh`, `highstandbythreshold` set via pmset utility
* Introduce a new bit in hbfx-ahbm boot-arg: `DoNotOverrideWakeUpTime` = 64, to let macOS decide when wake for standby sleep maintenance

#### [VoodooPS2 2.3.2](https://github.com/acidanthera/VoodooPS2/releases)

* Added ps2kbdonly=1 argument not to disable touchpad line on reboot, thx @Kethen
