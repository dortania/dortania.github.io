---
layout: post
title: "Acidanthera Updates: May 2023"
date: 2023-05-10 12:00:00 +0200
categories: Hackintosh updates
---

* [Acidanthera Updates: A message from PMheart](#acidanthera-updates-a-message-from-pmheart)
* [Changelogs](#changelogs)

# Acidanthera Updates: A message from PMheart

Hello folks! We are late, but 2023.05 releases are worth waiting.

First, OpenCore 0.9.2 brings significant improvements on `GopBurstMode` thanks to @mikebeaton: guard checks which ensure that it is not arbitrarily turned on; compatibility with non-standard GOP implementations; fix for potential hang on DEBUG builds; and even support for natively supported cards. The other fixes and improvements cannot be neglected either: @CaseySJ introduces a new kext quirk `DisableIoMapperMapping` which resolves conflicts in AppleVTD. As well, @vit9696 ensures that single user mode is disabled when Apple Secure Boot is enabled. Following the fix of `ThirdPartyDrives` on macOS 13.3 and above, `ExternalDiskIcons` also functions correctly now, thanks to @fusion71au. The `Builtin` text renderer receives various updates, together with the new `InitialMode`. Also, `LogModules` now supports a new `?` filter for matching non-standard log lines. Last but not least, `AppleCpuPmCfgLock` is enabled back on macOS 13, to patch the injected `AppleIntelCPUPowerManagement` kext. There are also other minor improvements. Please review the full changelog below.

Lilu 1.6.5 can now detect Recovery and Installer mode on macOS 13, too. Thus, it is essential to upgrade together with plugin kexts.

As always, we continue to appreciate contributions to AppleALC database, including ALC1220 layout-id 18 for Gigabyte Z490 Aorus Master by hgsshaanxi, and layout-id 21 for ALC298 on X270 by MKjanek32. There are bundled in AppleALC 1.8.2.

RestrictEvents 1.1.1 fixes `f16c` patch misreporting other `hw.optional` features.

Last but not least, BrcmPatchRAM 2.6.6 integrates firmware for legacy BCM20702A1, thanks to @chapuza.

Enjoy,

— PMheart

# Changelogs

#### [OpenCorePkg 0.9.2](https://github.com/acidanthera/OpenCorePkg/releases)

* Added `DisableIoMapperMapping` quirk, thx @CaseySJ
* Fixed disabling single user mode when Apple Secure Boot is enabled
* Improved guard checks for `GopBurstMode` on systems where it's not needed
* Improved compatibility of `GopBurstMode` with some very non-standard GOP implementations
* Fixed possible hang with `GopBurstMode` enabled on DEBUG builds
* Enabled `GopBurstMode` even with natively supported cards, in EnableGop firmware driver
* Fixed inability to patch force-injected kexts
* Fixed `ExternalDiskIcons` quirk on macOS 13.3+, thx @fusion71au
* Fixed various recent reversions and some longer-standing minor bugs in `Builtin` text renderer
* Applied some additional minor optimizations to `Builtin` text renderer
* Implemented `InitialMode` option to allow fine control over text renderer operating mode
* Added support for `ConsoleMode` text resolution setting to `Builtin` renderer
* Fixed regression for ACPI quirks `RebaseRegions` and `SyncTableIds`
* Updated build process to provide stable and bleeding-edge versions of `EnableGop`
* Implemented minor improvements in `PickerMode` `Apple`
* Improved filtering algorithm for `LogModules` and added `?` filter for matching non-standard log lines
* Fixed crash when gathering system report on virtualised CPUs
* Fixed unnecessary warning when first booting with emulated NVRAM
* Enabled `AppleCpuPmCfgLock` quirk on macOS 13

#### [AppleALC 1.8.2](https://github.com/acidanthera/AppleALC/releases)

* Added ALC1220 layout-id 18 for Gigabyte Z490 Aorus Master by hgsshaanxi
* Fixed LayoutId 21 for ALC298 on X270 by MKjanek32

#### [RestrictEvents 1.1.1](https://github.com/acidanthera/RestrictEvents/releases)

* Fixed `f16c` patch misreporting other `hw.optional` features

#### [BrcmPatchRAM 2.6.6](https://github.com/acidanthera/BrcmPatchRAM/releases)

* Added firmware for legacy BCM20702A1 (thx @chapuza)

#### [Lilu 1.6.5](https://github.com/acidanthera/Lilu/releases)

* Fixed macOS 13+ recovery and installer detection
