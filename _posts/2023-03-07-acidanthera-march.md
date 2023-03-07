---
layout: post
title: "Acidanthera Updates: March 2023"
date: 2023-03-07 10:00:00 +0100
categories: Hackintosh updates
---

* [Acidanthera Updates: A message from PMheart](#acidanthera-updates-a-message-from-pmheart)
* [Changelogs](#changelogs)

# Acidanthera Updates: A message from PMheart

Hello. Sorry guys! I have been sick and busy moving, hence I skipped the February 2023 message.

While there is not much listed in the changelog, OpenCore 0.9.0 has improvements on graphics thanks to @mikebeaton, including verbose boot log appearance, versioning information for the `EnableGop UI` tool, and AMD support and GOP offset auto-detection, with which macOS 10.11+ gets support for the EnableGop vBIOS insertion script. As well, the quirk `ProvideCurrentCpuInfo` now supports macOS 13.3 DP. Lastly, we included precompiled EDK-II EfiRom and GenFfs in Utilities/BaseTools with OpenCore releases.

For many years, AppleALC 1.8.0 enlarges its codec and layout database again with new and improved support for ALC274 (layout-id 28), ALC256 (layout-id 95), and ALC236 (layout-id 55) thanks to contributions from @Tweakkinn, @Floron, and @8DireZ3.

As a minor improvement, MaciASL 1.6.4 deletes broken URLs patches.

In the wake of stability, VirtualSMC 1.3.1 includes a tiny fix for `smcread -l` output.

VoodooPS2 2.3.4 introduces two fixes: device count detection when ps2rst=0 is set, and handleClose not being called by VoodooInput, thanks to @1Revenger1.

Last but not least, Lilu 1.6.4 adds AMD IGPU detection.

Enjoy,

— PMheart

# Changelogs

#### [OpenCorePkg 0.9.0](https://github.com/acidanthera/OpenCorePkg/releases)

* Resolved issues with verbose boot log appearing over picker graphics
* Added version number to EnableGop UI section, so tool builders can track it
* Added `ProvideCurrentCpuInfo` support for macOS 13.3 DP
* Added AMD support, GOP offset auto-detection and macOS 10.11+ support to EnableGop vBIOS insertion script
* Included precompiled EDK-II `EfiRom` and `GenFfs` in `Utilities/BaseTools` with OpenCore releases

#### [AppleALC 1.8.0](https://github.com/acidanthera/AppleALC/releases)

* Fixed ALC274 layout-id 28 in/out 3.5mm jacks audio by Tweakkinn
* Added ALC256 layout-id 95 for Honor MagicBook Pro HBB-WAH9 by Floron
* Added ALC236 layout-id 55 for HP-240G8 by 8DireZ3

#### [MaciASL 1.6.4](https://github.com/acidanthera/MaciASL/releases)

* Deleted broken URLs patches

#### [VirtualSMC 1.3.1](https://github.com/acidanthera/VirtualSMC/releases)

* Fixed `smcread -l` output

#### [VoodooPS2 2.3.4](https://github.com/acidanthera/VoodooPS2/releases)

* Fixed device count detection when ps2rst=0 is set
* Fixed handleClose not being called by VoodooInput

#### [Lilu 1.6.4](https://github.com/acidanthera/Lilu/releases)

* Added AMD IGPU detection
