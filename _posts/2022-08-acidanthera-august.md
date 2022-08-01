TODO
---
layout: post
title: "Acidanthera Updates: January 2022"
date: 2022-01-11 13:30:00 -0500
categories: Hackintosh updates
---

* [A message from PMheart](#a-message-from-PMheart)
* [Changelogs](#changelogs)

# A message from PMheart

Howdy! We wish you enjoyed this summer as life is getting back to normal. It has been a while since the last message from @vit9696 in [February 2022](https://dortania.github.io/hackintosh/updates/2022/02/10/acidanthera-february.html), but the monthly greeting is back now.

In addition to the fix for one of the most important OpenCore quirks, `AvoidRuntimeDefrag`, in our July 2022 release, the new updates to OpenCore (again by @mhaeuser) make it possible to load the Kernel Collection on macOS Ventura beta 3 and above. Thanks to @savvamitrofanov's hard work, we have integrated the ext4 file system driver into OpenCore. In addition, @Goldfish64 fixed `OSBundleLibraries_x86_64` handling and a crash when using kext blocking for cacheless injection, and another issue with FAT binary architechure selection. Furthermore, he added macOS 10.4 and 10.5 support to `AllowRelocationBlock` Booter quirk, and CPU cache info injection for macOS 10.4 to `ProvideCurrentCpuInfo` quirk. @mikebeaton brought another significant code refactoring for NVRAM operations by introducing `OpenVariableRuntimeDxe`, so now it is possible to specify drivers which need to be loaded before NVRAM initialisation. What's more, he made various improvements to AudioDxe, including the new `--force-device` and `--codec-setup-delay` options, the removal of default codec connection delay, as well as the change of unit (from microseconds to milliseconds) in `Audio` -> `SetupDelay`. Brought by the same author, @mikebeaton contributed a new option named `--show-csr` to the ToggleSipEntry tool for toggling SIP boot menu, and fixed a rare assertion caused by label animation initialisation in OpenCanopy. Last but not least, RsaTool is no longer dependant on macOS system SSL thanks to @dhinakg.

When it comes to Lilu, @mhaeuser addressed the kernel panic on macOS Ventura beta 3 and above by fixing the segment name for the new Kernel Collection. Although a small change, without his contribution, all Lilu plugins would have stopped working. As well, @Goldfish64 disabled EFI64 runtime APIs when `-legacy` is used on 32-bit kernels.

Although there are not many updates to our AppleALC v1.7.4 release, @wern-apfel corrected the pincofig data for ALC294 with `layout-id` 15, and @Ardhi9696 contributed a new audio data with `layout-id` 25 for ALC1220 on MSI GE73 Raider RGB 8RF.

While Apple removed support for Skylake in macOS 13, it is easy to spoof it as Kaby Lake. Building off the preliminary support in WhateverGreen v1.6.0, v1.6.1 addressed HEVC playback problems thanks to @abenraj and @dhinakg. However, further investigation is required for a proper solution to the intermittent flickering, which we wish to include in the next release.

Enjoy the last spot of summer,

— PMheart

# A message from dhinakg
*Eventually™️*

Build repo changes

TODO

# Changelogs

TODO
