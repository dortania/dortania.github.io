---
layout: post
title:  "Acidanthera Updates: November 2020"
date:   2020-11-02 15:00:00 -0700
categories: Hackintosh updates
---

* [A message from vit9696](#a-message-from-vit9696)
* [Guide Updates](#guide-updates)
* [Changelogs](#changelogs)

# A message from vit9696

Welcome back. Today we are pleased to announce one more autumn software iteration in preparation for Big Sur. Based on our experience with the seeds, I believe I can safely admit that we are ready for it. Even so, I advise everyone not to rush and instead skip a couple of point releases before transitioning your primary installation. The amount of changes within the operating system itself has affected application developers a lot more than us, and naturally it will take time before all the software has been updated to work correctly in Big Sur.

With the November update we made further improvements in Apple Secure Boot support. The latest additions to Big Sur let us discover genuine issues in the implementation that were not critical to previous macOS versions. We fixed these problems and published the [ACDT0133PRU](https://github.com/acidanthera/bugtracker/blob/master/DOCUMENTS.md) note to explain the nuances to the general audience. We expect that its contents will soon appear in Dortania guides in some way. For improved security and stability we recommend all the users to enable Apple Secure Boot.

In addition to that, we resolved some long-standing problems with hardware configuration. In the current OpenCore version one can find SMBIOS memory property customization and Intel IGPU resolution patching for legacy systems contributed by [@Goldfish64](https://github.com/Goldfish64). We also included an [ACPI table](https://github.com/acidanthera/OpenCorePkg/blob/master/Docs/AcpiSamples/SSDT-UNC.dsl) required by some X99 platforms for macOS 11 to function researched by [@RemB](https://github.com/remb). On the kext side, [@lvs1974](https://github.com/lvs1974) updated [SMCDellSensors](https://github.com/acidanthera/VirtualSMC) to improve Bluetooth audio stability, and [@black-dragon74](https://github.com/black-dragon74) contributed custom verb sending to [AppleALC](https://github.com/acidanthera/AppleALC/releases). Additionally [@0xFireWolf](https://github.com/0xFireWolf) continued the refactoring of IGPU patches in [WhateverGreen](WhateverGreen) and added automatic link rate calculation.

— Vit

# Guide Updates

This month we've taken a bit of a step back in regards to the install guide, and pivoted our time towards [post-install guide](https://dortania.github.io/OpenCore-Post-Install/) updates before things get too hectic with Big Sur's imminent release. The main things we've been working on:

* [Legacy Intel Patching](https://dortania.github.io/OpenCore-Post-Install/gpu-patching/legacy-intel/)
  * GMA series supported
* [Legacy Nvidia Patching](https://dortania.github.io/OpenCore-Post-Install/gpu-patching/nvidia-patching/)
  * Tesla through Fermi series supported
* [More in-depth WhateverGreen Patching](https://dortania.github.io/OpenCore-Post-Install/gpu-patching/intel-patching/)
  * Sandy bridge and newer supported
  
We know that documentation on legacy hardware can be quite difficult to find as more and more sites go offline, and even more challenging finding credible information from that era where users would throw anything at the wall till it sticks. So to ease users wanting to breath new life into older hardware or ditch Chameleon and Clover, we dedicated quite a bit of time and resources into documenting support for older GPUs. And thanks to the efforts of [@1Revenger1](https://github.com/1Revenger1/), we now have an amazing utility to help calculate NVCAP values for legacy Nvidia GPUs by simply importing your VBIOS into [NVCAP-Calculator](https://github.com/1Revenger1/NVCAP-Calculator).

Additionally, we've also begun work on a new guide to breath new life into legacy Macs. This guide focuses on setting up a Mac no longer supported by the latest OS, and installing OpenCore with little to no modifications to the file system. This allows for native OS updates, full features such as SIP and APFS snapshots allowing for a near-identical experience to a supported Macs. The guide is still a work in progress, as legacy GPU acceleration and AppleHDA patching are still being worked on, however this is the only way to get certain Macs like iMac11,x and MacBookPro6,x to boot Big Sur at all. You can read more about this new guide here:

* [OpenCore for Legacy Macs](https://dortania.github.io/OpenCore-For-Legacy-Macs/)

And as mentioned before, Big Sur's release is just around the corner. Unfortunately quite a bit has changed with the software catalogue so we do want to warn users in advance that gibMacOS may not fully support Windows or Linux initially (however macOS-based installers will still be fully supported). You may find [macrecovery.py](https://github.com/acidanthera/OpenCorePkg/tree/master/Utilities/macrecovery) to be a more reliable solution if there's issues with Big Sur and gibMacOS. If this does occur, please be patient while things would be patched up to accomodate the potential new GDMF update system, we will be updating the guides regularly with new information on Big Sur installs as it comes out.

We hope you enjoy the updates to the guides, and we'll be seeing you in a few weeks with a new Big Sur update thread on all things to watch out for with the release!

— Khronokernel

# Changelogs

#### [OpenCore 0.6.3](https://github.com/acidanthera/OpenCorePkg/releases)

- Added support for xml comments in plist files
- Updated underlying EDK II package to edk2-stable202008
- Provide fallbacks for NULL memory SMBIOS strings
- Fixed `BOOTx64.efi` and `BOOTIA32.efi` convention
- Fixed SMBIOS handling with multiple memory arrays
- Fixed memory array handle assignment on empty slots
- Fixed CPUID patching on certain versions of macOS 10.4.10 and 10.4.11
- Fixed incorrect core/thread counts on Pentium M processors
- Added `SSDT-UNC.dsl` ACPI sample to resolve X99 issues, thx @RemB
- Updated builtin firmware versions for SMBIOS and the rest
- Increased slide allocation reserve to 200 MB for Big Sur beta 10
- Fixed assert when trying to enable direct renderer on blit-only GOP
- Added support for custom memory properties
- Fixed intermittent 32-bit prelinking failures caused by improper Mach-O expansion
- Fixed failures in cacheless injection dependency resolution
- Fixed detection issues with older Atom CPUs
- Fixed `ScanPolicy` NVMe handling on MacPro5,1
- Fixed I/O issues on platforms incapable of reading over 1MB at once
- Fixed plist-only kext injection in Big Sur
- Add `ForceResolution` option for enabling non-default resolutions
- Fixed Ps2MouseDxe not properly loading under OpenDuetPkg
- Added workaround for read-only errors on some X299 boards
- Added support for `x86legacy` Secure Boot model
- Added missing Secure Boot NVRAM variables required by 11.0
- Added setting of `system-id` NVRAM variable
- Added `ForceSecureBootScheme` quirk for virtual machines
- Fixed kernel and ACPI patches failing to replace last bytes of memory

#### [Lilu 1.4.9](https://github.com/acidanthera/Lilu/releases)

- Added the PCI GMCH Graphics Control register definition. (by 0xFireWolf)
- Added a new API to solve multiple symbols in one shot conveniently. (by 0xFireWolf)
- Added a new `RouteRequest` constructor to work with function pointers without additional type castings. (by 0xFireWolf)

#### [AppleALC 1.5.4](https://github.com/acidanthera/AppleALC/releases)

- Improved Ice Lake controller patches by fewtarius
- Added verb sending functionality from userspace by black-dragon74
- Added ALC235 (display as ALC233) layout-id 35 for Lenovo Qitian M420-D046(C) by crysehillmes
- Added ALC892 layout-id 100 for MSI Z370-A PRO by GeorgeWan
- Added ALCS1200A layout-id 51 for for ASROCK Z490 Steel Legend by GeorgeWan
- Added ALC662 layout-id 66 for Lenovo Qitian M415-D339 by static-host
- Fixed ALC285 layout-Id 21 for X1C6 (by @fewtarius)
- Added ALC272 layout-id 12 for Lenovo Y470 by amu_1680c
- Added patch CX20751/2 by vasishath to fix internal mic gain adjustment (this fix microphone volume slider in system preferences)
- Added ALC230 layout 13 & 20 Jack Sense and EAPD support and add WakeConfigData to layout 13
- Added ALC290 layout-id 10 for HP Envy 15t-k200 w/ Beats Audio 2.1 by temp1122-sys

#### [WhateverGreen 1.4.4](https://github.com/acidanthera/WhateverGreen/releases)

- Extended the maximum link rate fix: Now probe the rate from DPCD automatically and support Intel ICL platforms. (by @0xFireWolf)
- Fixed an issue that LSPCON driver causes a page fault if the maximum link rate fix is not enabled. (by @0xFireWolf)

#### [VirtualSMC 1.1.8](https://github.com/acidanthera/VirtualSMC/releases)

- Reduce audio lags in SMCDellSensors
 
#### [AirportBrcmFixup 2.1.1](https://github.com/acidanthera/AirportBrcmFixup/releases)

- Fix an issue with posponed matching (method IOTimerEventSource::timerEventSource could fail)

#### [HibernationFixup 1.3.7](https://github.com/acidanthera/HibernationFixup/releases)

- Refactoring, setup next RTC wake manually if IOPMrootDomain::setMaintenanceWakeCalendar was not called before sleep
- Force next sleep if maintanence wake type is detected (RTC/SleepService/Maintenance)

#### [VoodooPS2 2.1.8](https://github.com/acidanthera/VoodooPS2/releases)

- Added support for receiving input form other kexts
- Fixed dynamic coordinate refresh for ELAN v3 touchpads

#### [BrightnessKeys 1.0.1](https://github.com/acidanthera/BrightnessKeys/releases)

- Recovered support for macOS 10.11-10.14
- Added message capability for sending key to primary keyboard and palm rejection
