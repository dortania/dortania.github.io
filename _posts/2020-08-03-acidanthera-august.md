---
layout: post
title:  "Acidanthera Updates: August 2020"
date:   2020-08-03 15:00:00 -0700
categories: Hackintosh updates
---

* [A message from vit9696](#a-message-from-vit9696)
* [Changelogs](#changelogs)
* [Dortania Updates](#dortania-updates)
* [Guide Updates](#guide-updates)

# A message from vit9696

Nice to meet you this summer again. By skipping a month we hoped to push in a small vacation for our team members, yet, with Big Sur as it was, there was no room for it to happen. While these two months were very bright for the new changes, they also helped us to assess the previous release and reconsider some processes.

Our greatest achievement in June is that we discovered no issues in OpenCore 0.5.9 requiring to stay on a previous release. To make issue handling even more transparent, from now on we will publish the [OpenCore Errata document](https://github.com/acidanthera/OpenCorePkg/blob/master/Docs/Errata/Errata.pdf) containing notable issues and their workarounds. Thanks to Dortania Team and @dhinakg in particular this and several other documents are now available in [HTML format](https://dortania.github.io/docs) as well. And that is not all, with Dortania we have also launched a [community tracker](https://github.com/dortania/bugtracker/issues) to unify non-Acidanthera issues and a [regression-testing cellar](https://dortania.github.io/builds) containing binary pre-release versions of Acidanthera products on per-commit basis since Spring.

Let us get back to macOS 11. Big Sur is a big change, maybe not as big to do a major version increase, but it contains numerous under the hood changes that are yet to evolve. With this release we literally had to reimplement the kext injection from the ground. It is an entirely new state of the art piece of code we are very proud about with @Download-Fritz. As a consequence of this change, Lilu and its whole plugin system got a very serious rewrite as well. Lilu became noticeably more performant and flexible, though not all its APIs are available at the moment in 11.0. For example, one of such APIs, the userspace patcher, needs a rewrite, which we do not have the resources for at the moment. Today a number of our products received basic compatibility updates to support Big Sur, and today macOS Big Sur remains being an early beta and a part of a transitioning period. Please do not rush with it if your environment is important for you.

Extending our speech about the compatibility, we would like to say one important thing. We care. When we welcome the new Mac users that no longer can receive the updates. When we invest resources into OpenDuetPkg with @Goldfish64 to improve the support of older BIOS systems. When we implement the missing pieces of an advanced battery management driver and enable FAN configuration with @lvs1974. When we redo the Intel GPU reintegration with @07151129. When we implement [macOS native integration of Intel Wireless](https://github.com/usr-sse2/Black80211-Catalina) into [itwlm](https://github.com/OpenIntelWireless/itlwm) with @usr-sse2. We continue to interact with the community and accept patches from the outside, and we are looking forward to doing more fun stuff.

— Vit

# Changelogs

#### [OpenCore 0.6.0](https://github.com/acidanthera/OpenCorePkg/releases)

* Fixed sound corruption with AudioDxe
* Fixed icon choice for Apple FW update in OpenCanopy
* Fixed APFS driver loading on Fusion Drive
* Added Comet Lake HDA device code
* Fixed audio stream position reporting on non-Intel platforms
* Added `Firmware` mode to `ResetSystem` to reboot into preferences
* Replaced `BlacklistAppleUpdate` with `run-efi-updater` NVRAM variable
* Fixed reset value and detection in `FadtEnableReset` ACPI quirk
* Fixed freezes during boot option expansion with PXE boot entries
* Updated underlying EDK II package to edk2-stable202005
* Added `ProvideMaxSlide` quirk to improve laptop stability, thx @zhen-zen
* Fixed slide choice on platforms when 0 slide is unavailable, thx @zhen-zen
* Fixed assertions caused by unaligned file path access in DEBUG builds
* Renamed `ConfigValidity` utility to `ocvalidate` for consistency
* Added `GlobalConnect` for APFS loading to workaround older firmware issues
* Added 11.0 support for `AvoidRuntimeDefrag` Booter quirk
* Fixed 11.0 lapic kernel quirk as of DP1
* Improved boot selection scripts for macOS without NVRAM
* Added UGA protocol compatibility in `ProvideConsoleGop` quirk
* Added `UgaPassThrough` option to support UGA protocol over GOP
* Added `AppleFramebufferInfo` protocol implementation and override
* Fixed serial initialisation when file logging is disabled
* Fixed FSBFrequency reporting on Meron and similar CPUs
* Fixed incorrect volume icon dimension requirements in OpenCanopy
* Added preview version of KernelCollection injection code
* Fixed ACPI reset register detection in DxeIpl
* Added MacBookPro16,4 model code
* Updated builtin firmware versions for SMBIOS and the rest
* Fixed OSXSAVE reporting when emulating CPUID on newer CPUs
* Added `SerialInit` option to perform serial initialisation separately
* Fixed OpenDuetPkg booting on Intel G33 with SATA controller in RAID mode
* `PlatformInfo` `Automatic` for all models
* Fixed 32-bit OpenDuetPkg booting on machines with over 4 GBs of RAM
* Fixed delays with OpenDuetPkg booting with certain SATA controllers in IDE mode
* Fixed display name for some high core count i9 CPUs like 7920X
* Fixed SSDT-EC-USBX

#### [BT4LEContinuityFixup 1.1.5](https://github.com/acidanthera/BT4LEContinuityFixup)

* Fix an issue in routing for method __ZN25IOBluetoothHostController25SetControllerFeatureFlagsEj
* Added constants for 11.0 support

#### [NVMeFix 1.0.3](https://github.com/acidanthera/NVMeFix)

* Fix re-enabling APST after sleep (1.0.2 regression)
* Added constants for 11.0 support (no full compatibility provided)

#### [VoodooInput 1.0.7](https://github.com/acidanthera/VoodooInput/releases)

* Allowed to set finger type externally to fix swiping desktops when holding a dragged item
* Added a message to allow client to set gesture orientation when rotating a touchscreen (thx @Goshin)

#### [VoodooPS2 2.1.6](https://github.com/acidanthera/VoodooPS2/releases)

* Fix Command key being pressed after disabling the keyboard and trackpad with Command-PrtScr key combo
* Added a message to allow other kexts to disable the keyboard

#### [AppleALC 1.5.1](https://github.com/acidanthera/AppleALC/releases)

* Set MinKernel Catalina for 400 Series
* Added constants for 11.0 support
* Added 400 series 0x6c8 and 0x2c8 controller patch (thanks @lvs1974)
* Added ALC295 layout-id 24 for HP Pavilion / OMEN-2 by zty199
* Update CA0132 layout-id 7, 4, 2, 1 by wern-apfel
* Added IDT92HD95 layout-id 11 by wern-apfel
* Added Icelake Smart Sound Technology Audio Controller
* Fix Headphone NodeID，Add SPDIFOut NodeID，ALC255 layout-id 20 for DELL 7447 by was3912734
* Added ALC290 layout-id 15 for HP m6 n015dx by MacPeet
* Added ALC285 layout-61 for Lenovo Yoga C740 by fewtarius
* Added CA0132 LayoutID 99 - 5.1 channel for Alienware-M17X-R4 by DalianSky
* Added ALC289 layout-id 11 for alienware m17r2 by leeoem

#### [VirtualSMC 1.1.5](https://github.com/acidanthera/VirtualSMC/releases)
 
* Improved CHLC key value reporting
* Fixed B0PS and B0St key size to resolve broken fully charged state
* Fixed sometimes stuck battery update thx to @zhen-zen
* Added workaround for kBRemainingCapacityCmd exceeding kBFullChargeCapacityCmd
* Added preliminary 11.0 support
* Fixed SMCProcessor model detection warning
* Fixed legacy smc tool value calculation
* Fixed running smcread on 11.0 without IOKit framework
* Added a new plugin SMCDellSensors for Temp/FAN monitor/control
* Added basic SMCBatteryManager compatibility with 11.0
* Fixed crashes when trying to read CLKT key

#### [HibernationFixup 1.3.4](https://github.com/acidanthera/HibernationFixup)

* Improve auto-hibernate feature: correct next wake time disregarding the current sleep phase.
* Added constants for 11.0 support.

#### [WhateverGreen 1.4.1](https://github.com/acidanthera/WhateverGreen/releases)

* Added `igfxmetal=1` boot argument (and `enable-metal` property) to enable Metal on offline IGPU
* Fixed applying patches on CometLake IGPUs, thx @apocolipse
* Added constants required for 11.0 update
* Added the use of RPS control for all the command streamers on IGPU (disabled via `igfxnorpsc=1`)
* Add `-igfxvesa` to disable Intel Graphics acceleration.
* Fix black screen on igfx since 10.15.5
* Add workaround for rare force wake timeout panics on Intel KBL and CFL.
* Add Intel Westmere graphics support.

#### [Lilu 1.4.6](https://github.com/acidanthera/Lilu/releases)

* Added preliminary definitions for 11.0 support
* Temporarily disabled user patcher for 11.0
* Added `external-audio` property to ignore PCI audio cards
* Added in-memory symbol solving for 11.0
* Fixed accidentally solving stabs instead of normal symbols
* Added device publishing API to monitor device startup
* Added DeviceInfo caching for improved performance
* Added implicit slotted (medium) patches in KC mode to reduce patch size

#### [CPUFriend 1.2.1](https://github.com/acidanthera/CPUFriend)

* Added constants for 11.0 support

#### [AirportBrcmFixup 2.0.8](https://github.com/acidanthera/AirportBrcmFixup)

* Added constants for 11.0 support
* Property 'pci-aspm-default' with value 0 is not required for Broadcom BCM4350 chipset (with non-apple subsystem-vendor-id), 
since now it is injected/corrected and method IOPCIFamily::setASPMState called for provider to disable ASPM immediately.
* Add required dependencies into OSBundleLibraries section
* Remove injectors for AirPortBrcm4360 and AirPortBrcmNIC from main Info.plist and move them into separate plugins AirPortBrcm4360_Injector and 
AirPortBrcmNIC_Injector (kexts with plist only).
Under 10.16 (Big Sur) plugin AirPortBrcm4360_Injector.kext must be blocked by MaxKernel 19.9.9 or just removed, otherwise it will block loading of AirPortBrcmNIC
since class AirPortBrcm4360 is unsupported.
* Check whether brcmfx-driver value is incorrect (if specified value is unsupported in current osx system)
* Support boot-arg and property `brcmfx-aspm` to override value used for pci-aspm-default 

#### [DebugEnhancer 1.0.1](https://github.com/acidanthera/DebugEnhancer)

* Added constants for 11.0 support

#### [BrcmPatchRAM 2.5.4](https://github.com/acidanthera/BrcmPatchRAM)

* Added inject BCM2070 - BCM943224HMB, BCM943225HMB Combo

# Dortania Updates

With great efforts from one of our members, DhinakG, we're proud to announce Dortania's build site:

* https://dortania.github.io/builds/

What this site is meant is to be an easy to access list of all of Acidanthera's kexts and tools with the newest commits being built and posted here. Currently it's still in beta and would love for people to contribute via [PRs](https://github.com/dortania/build-repo), and there's plans to expand past Acidanthera-only tools.

# Guide Updates

Some of you may have noticed since our last update that the site has gone through a redesign and rewrite. The laptop guide has been merged into the desktop guide to create a unified install guide and post-install has been separated to a dedicated site.

We've also added a basic guide on macOS 11 (Big Sur) installs however we won't be providing proper support til official release.

* [OpenCore Install Guide](https://dortania.github.io/OpenCore-Install-Guide/)
* [OpenCore Post-Install](https://dortania.github.io/OpenCore-Post-Install/)

— Khronokernel
