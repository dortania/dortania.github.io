---
layout: post
title: "Acidanthera and Dortania Updates: August 2022"
date: 2022-08-02 03:00:00 -0400
categories: Hackintosh updates
---

* [A message from PMheart](#a-message-from-PMheart)
* [A message from dhinakg](#a-message-from-dhinakg)
* [Changelogs](#changelogs)

# Acidanthera Updates: A message from PMheart

Howdy! We wish you enjoyed this summer as life is getting back to normal. It has been a while since the last message from @vit9696 in [February 2022](https://dortania.github.io/hackintosh/updates/2022/02/10/acidanthera-february.html), but the monthly greeting is back now.

In addition to the fix for one of the most important OpenCore quirks, `AvoidRuntimeDefrag`, in our July 2022 release, the new updates to OpenCore (again by @mhaeuser) make it possible to load the Kernel Collection on macOS Ventura beta 3 and above. Thanks to @savvamitrofanov's hard work, we have integrated the ext4 file system driver into OpenCore. In addition, @Goldfish64 fixed `OSBundleLibraries_x86_64` handling and a crash when using kext blocking for cacheless injection, and another issue with FAT binary architechure selection. Furthermore, he added macOS 10.4 and 10.5 support to the `AllowRelocationBlock` Booter quirk, and CPU cache info injection for macOS 10.4 to the `ProvideCurrentCpuInfo` quirk. @mikebeaton brought another significant code refactoring for NVRAM operations by introducing `OpenVariableRuntimeDxe`, so now it is possible to specify drivers which need to be loaded before NVRAM initialisation. What's more, he made various improvements to AudioDxe, including the new `--force-device` and `--codec-setup-delay` options, the removal of default codec connection delay, as well as the change of unit (from microseconds to milliseconds) in `Audio` -> `SetupDelay`. Brought by the same author, @mikebeaton contributed a new option named `--show-csr` to the ToggleSipEntry tool for toggling SIP boot menu, and fixed a rare assertion caused by label animation initialisation in OpenCanopy. Last but not least, RsaTool is no longer dependant on macOS system SSL thanks to @dhinakg.

When it comes to Lilu, @mhaeuser addressed the kernel panic on macOS Ventura beta 3 and above by fixing the segment name for the new Kernel Collection. Although a small change, without his contribution, all Lilu plugins would have stopped working. As well, @Goldfish64 disabled EFI64 runtime APIs when `-legacy` is used on 32-bit kernels.

Although there are not many updates to our AppleALC v1.7.4 release, @wern-apfel corrected the pinconfig data for ALC294 with `layout-id` 15, and @Ardhi9696 contributed new audio data with `layout-id` 25 for ALC1220 on MSI GE73 Raider RGB 8RF.

While Apple removed support for Skylake in macOS 13, it is easy to spoof it as Kaby Lake. Building off the preliminary support in WhateverGreen v1.6.0, v1.6.1 addressed HEVC playback problems thanks to @abenraj and @dhinakg. However, further investigation is required for a proper solution to the intermittent flickering, which we wish to include in the next release.

Enjoy the last spot of summer,

— PMheart

# Dortania Updates: A message from dhinakg

Hello everyone! It's been a while since I've posted one of these, and it's about time that I posted.

I'm happy to share that our [build repo](https://dortania.github.io/builds/) is now running on an M1 machine, drastically improving build times - 30-minute builds of OC are now 7 minutes! More plugins have also been added, and development on the build repo will continue in the future.

Let's jump to the crux of the matter though - the guides.

Many of you have probably been wondering why the install guide has remained on 0.7.8 for a while when we're up to 0.8.3 already. Albeit the changes between 0.7.8 and the latest version haven't been major, it has been a while since the guides have been getting updates. How come?

Well, the dortania team has not had as much time or as many active people as it once had. Mykola (khronokernel) has moved on to legacy Macs. And I no longer have the abundance of time I had while under a lockdown order.

Avery (@1Revenger1) and I, however, have been actively working to change this. First off, PMheart is helping out with maintaining the guides, recently reviewing a PR to the power management section of the post-install guide. In addition, we've finally been able to find some time to go through PRs and issues, and thanks to the help of several external contributors - @hkusdaryanto, @dreamwhite, @YuiiiPTChan, @Krazy-Killa, @thegermanguyben, and @extremegrief1 - we've been able to update the install guide to 0.8.3. The post-install guide does need updates for 0.8.3 too, but these are minor updates that will be completed in the near future. There are still many issues and updates that all of the guides need though.

This does raise the question - haven't the updates to OC been minor? Why has it been so hard to keep the install guide up to date?

Well, the answer lies in how the install guide is organized. Currently, it's organized by CPU generation, and all aspects of configuring your config.plist for that generation are covered in one page. However, this design leads to a humongous amount of copy and paste - there are 26 config pages as of current, and a lot of the core content is shared among the pages, but with different variations. This makes it incredibly difficult to change all the pages and ensure nothing is missed, and it also makes any PRs fairly difficult to review.

To combat this, we've come up with a new idea of organizing the guide: instead of by generation, by config.plist section. Each section of the config (ie. ACPI, Booter, DeviceProperties, Kernel) would be its own page, and shared configuration for several generations would be grouped on each page. This would significantly reduce the amount of repeated content and allow updates to the guide to be made much more easily. To better demonstrate, [here's a demo site](https://dortania.github.io/other/install-guide-reorganized-sample).

Alongside this, we'd also like to combine the current WiFi Buyers Guide, GPU Buyers Guide, and Anti-Hackintosh Buyers Guide into one guide to have compatibility info in one central place. This new guide would be called the Hackintosh Compatibility Guide.

We know that the best way to get feedback is to ask the users, so we're asking for public comment on these proposed changes. Please comment down in the comments below.

Thank you all,

— Dhinak (dhinakg)

# Changelogs

#### [OpenCorePkg 0.8.4](https://github.com/acidanthera/OpenCorePkg/releases)

* Added checks for `Driver` -> `LoadEarly` in ocvalidate

#### [Lilu 1.6.2](https://github.com/acidanthera/Lilu/releases)

* Fixed KC segment name, which also fixed kernel panic on macOS 13 b3
* Disable EFI64 runtime APIs when `-legacy` is used on 32-bit kernels

#### [AppleALC 1.7.4](https://github.com/acidanthera/AppleALC/releases)

* ALC294 layout-id 15 corrected incorrect pinconfig by wern-apfel
* Added ALC1220 layout-id 25 for MSI GE73 Raider RGB 8RF by Ardhi9696

#### [WhateverGreen 1.6.1](https://github.com/acidanthera/WhateverGreen/releases)

* Improved Skylake graphics spoofing support by removing profile 2 from VTSupportedProfileArray on macOS 13+, thanks @abenraj and @dhinakg

