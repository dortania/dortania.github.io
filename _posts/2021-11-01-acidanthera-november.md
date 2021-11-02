---
layout: post
title: "Acidanthera Updates: November 2021"
date: 2021-11-01 12:00:00 -0400
categories: Hackintosh updates
---

* [A message from vit9696](#a-message-from-vit9696)
* [Changelogs](#changelogs)

# A message from vit9696

Good evening,

Considering all the effort spent on making our projects feature-rich and stable, we have long awaited the monthly changelist to decrease in size and contain less ground-breaking adjustments. While we have not reached this state yet, this release is a great example of our shift to a new strategy. The main changes are dictated by three factors: macOS changes, hardware releases, and security enhancements we continue to pursue.

The updates to OpenCore include a long-awaited feature: Resizable BAR configuration for GPUs. Resizable BAR is a PCI specification feature which allows control of the amount of video memory visible from the CPU. While macOS does support this feature, it limits the supported BAR sizes by 1 GB and seems to be unstable with BARs above 256 MB. If both your GPU and your firmware support Resizable BAR, setting `ResizeAppleGpuBars` to `0` will update GPU registers to their defaults when booting macOS and fix the hangs on newer boards. The [updated reference manual](https://github.com/acidanthera/OpenCorePkg/blob/0.7.5/Docs/Configuration.pdf) includes all the relevant details for the technically inclined. Among the other improvements are recovery image signature checking in `macrecovery` by @jspraul and @zhangyoufu, ensuring that the image is not corrupted and comes directly from Apple, and minor OpenLinuxBoot improvements by @MikeBeaton, resolving an annoying hang with some distributions.

As for kernel driver changes, after the Bluetooth stack overhaul in macOS 12, we are still trying to get things in line. Thanks to contributions from @dhinakg, @usr-sse2, @williambj1, and @zxystd, BlueToolFixup makes most devices work on any Mac model with on-off support. Please note that Continuity and AirDrop features may not function correctly [for the time being](https://github.com/acidanthera/bugtracker/issues/1821) on macOS 12. Other than that, with @lvs1974 we extended Lilu APIs to support trampoline routing on macOS 10.15 and earlier, which fixed an unpleasant regression in HibernationFixup and CpuTscSync causing boot or sleep wake failures. @kingo132 added PWM backlight control for AMD 5000-series to WhateverGreen and @0xFireWolf resolved some flickering issues on Ice Lake GPUs. Thanks to @1Revenger1, VoodooPS2 got a bugfix for the recently added muxing code, which caused some devices to crash on sleep wake.

This is all for the highlights, we hope you enjoy macOS 12 on your non-production systems. Besides that, while we are moderately excited about the imminent release of Intel Alder Lake, we use this message as a reminder that this platform is not supported and may actually have architectural incompatibilities with macOS.

— Vit

# Changelogs

#### [OpenCore 0.7.5](https://github.com/acidanthera/OpenCorePkg/releases)

- Revised OpenLinuxBoot documentation
- Supported Linux ostree boot layout
- Fixed external drive icons for Boot Entry Protocol
- Added GPU Resize BAR quirks to reduce BARs on per-OS basis
- Fixed OpenLinuxBoot hang bug after correct detection of some distros
- Added DMG signature check during download, thx @jspraul and @zhangyoufu
- Updated builtin firmware versions for SMBIOS and the rest
- Updated recovery downloading commands to include macOS 11 and 12

#### [Lilu 1.5.7](https://github.com/acidanthera/Lilu/releases)

- Added address slot support for all 64-bit macOS version

#### [AppleALC 1.6.6](https://github.com/acidanthera/AppleALC/releases)

- Added ALC256 layout-id 24 for Intel NUC NUC10i5FNH by Andres ZeroCross
- Added Conexant CX11970 (CX8400) layout-id 13 for Acer Swift 3 SF31* (Ice Lake) by m0d16l14n1
- Added ALCS1200A layout-id 7 for B550M Gaming Carbon WIFI by Kila2
- Try to solve wake up mute for GP75 9SD by Win7GM
- Added ALC256 layout-id 33 for Huawei Matebook D15 MRC-W10 by im1ke
- Added ALC892 layout-id 23 for ASRock B365 Pro4 by TheHackGuy
- Fixed ALC221 layout-id 11 for HP6300/8300 rear line-in jack by adding DSP functions by aloha-cn

#### [WhateverGreen 1.5.5](https://github.com/acidanthera/WhateverGreen/releases)

- Changed the default delay of optimizing display data buffer allocations from 0 to 1 second to fix the issue that both internal and external displays flicker on some Ice Lake-based laptops. (Thanks @m0d16l14n1)
- Disabled the black screen fix on Ice Lake platforms as it is only applicable to SKL/KBL/CFL/CML platforms.
- Disabled the force complete modeset submodule on Ice Lake platforms as HDMI/DVI connections are not supported by the driver.
- Added AMD Radeon RX 5000 series PWM backlight control support. (Thanks to @kingo132)

#### [BrcmPatchRAM 2.6.1](https://github.com/acidanthera/BrcmPatchRAM/releases)

- Improved BlueToolFixup compatibility with macOS 12b10 (thx @dhinakg, @williambj1)
- Fixed bluetooth support on MBP15,4 and other similar boards (thx @dhinakg, @usr-sse2)
- Fixed bluetooth not working on macOS 12 after the first power cycle (thx @williambj1, @zxystd)

#### [VoodooPS2 2.2.7](https://github.com/acidanthera/VoodooPS2/releases)

- Fixed kernel panic after S3

#### [HibernationFixup 1.4.5](https://github.com/acidanthera/HibernationFixup/releases)

- When battery level is critical, try to put macOS into sleep/hibernate mode only once per minute.
