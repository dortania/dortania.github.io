---
layout: post
title: "Acidanthera Updates: November 2022"
date: 2022-11-07 21:00:00 +0100
categories: Hackintosh updates
---

* [Acidanthera Updates: A message from PMheart](#acidanthera-updates-a-message-from-pmheart)
* [Changelogs](#changelogs)

# Acidanthera Updates: A message from PMheart

Embracing the final release of macOS Ventura and following Halloween, we entered November 2022.

Overall speaking, OpenCore 0.8.6 brings several groundbreaking changes. To begin with, @mikebeaton updated the LogoutHook script for the compatibility with earlier versions of macOS and brought the capability of automatic installation as launch daemon/logout hook on Yosemite and above. As well, @mikebeaton fixed a recursive loop crash and early logging failure, and resolved wake-from-sleep failure on EFI 1.1 systems. After months of hard work, @mhaeuser has brought the most impressive feature in this release, dwell-clicking, to our bootloader. As always, @Andrey1970AppleLife ensures that firmware/SMBIOS info is up-to-date.

After nearly one year of hibernation, MaciASL got a minor improvement where line number breaking during scroll has been fixed, thanks to @SkyrilHD.

For AppleALC 1.7.6, we would like to thank @anderson-suga, @andreszerocross, @mishurov, and @RockJesus for their contributions to our audio configuration database.

In CryptexFixup 1.0.1, @khronokernel added support for in-OS macOS installation via Install macOS.app on Big Sur and newer. As well, he refactored model patch set detection, and replaced the previously unused boot argument `-disable_uni_control` with `-disable_sidecar_mac` in FeatureUnlock 1.1.0. Last but not least, in RestrictEvents 1.0.9, the new `revblock` userspace processes blocking is added, together with `displaypolicyd` blocking for genuine `MacBookPro9,1/10,1`, `mediaanalysisd` for Metal 1 GPUs on Ventura, and conditional blocking for PCIe/memory notifications on `MacPro7,1` SMBIOS.

Enjoy,

— PMheart

# Changelogs

#### [OpenCorePkg 0.8.6](https://github.com/acidanthera/OpenCorePkg/releases)

* Updated NVRAM save script for compatibilty with earlier macOS (Snow Leopard+ tested)
* Updated NVRAM save script to automatically install as launch daemon (Yosemite+) or logout hook (older macOS)
* Fixed maximum click duration and double click speed for non-standard poll frequencies
* Added support for pointer dwell-clicking
* Fixed recursive loop crash at first non-early log line on some systems
* Fixed early log preservation when using unsafe fast file logging
* Updated builtin firmware versions for SMBIOS and the rest
* Resolved wake-from-sleep failure on EFI 1.1 systems (including earlier Macs) with standalone emulated NVRAM driver
* Updated macrecovery commands with macOS 12 and 13, thx @Core-i99
* Updates SSDT-BRG0 with macOS-specific STA to avoid compatibility issues on Windows, thx @Lorys89
* Fixed memory issues in OpenLinuxBoot causing crashes on 32-bit UEFI firmware

#### [MaciASL 1.6.3](https://github.com/acidanthera/MaciASL/releases)

* Fix line number breaking during scroll, thanks to @SkyrilHD

#### [AppleALC 1.7.6](https://github.com/acidanthera/AppleALC/releases)

* Added ALC298 layout-id 33 for surface laptop 1gen by Rockjesus.cn
* Added ALC255 layout-id 23for Acer Aspire A515-54G by anderson-suga
* Added ALC897 combo jack mic layout-id 22 for CHUWI CoreBook X by mishurov
* Added ALC897 layout-id 21 for OPS Computer by Andres ZeroCross

#### [CryptexFixup 1.0.1](https://github.com/acidanthera/CryptexFixup/releases)

* Allow in-OS Install macOS.app usage on Big Sur and newer

#### [FeatureUnlock 1.1.0](https://github.com/acidanthera/FeatureUnlock/releases)

* Refactored model patch set detection
  * Implemented proper VMM detection for AirPlay to Mac on Ventura
  * Avoids unnessary patching on supported models (ex. NightShift on 2012+)
* Removed unused `-disable_uni_control` boot argument
  * Was non-functional previously, use `-disable_sidecar_mac` instead

#### [RestrictEvents 1.0.9](https://github.com/acidanthera/RestrictEvents/releases)

* Added `revblock` for user configuration of blocking processes
* Added additional process blocking:
  * `gmux` * block displaypolicyd on Big Sur+ (for genuine MacBookPro9,1/10,1)
  * `media` * block mediaanalysisd on Ventura+ (for Metal 1 GPUs)
  * `pci` * block PCIe & memory notifications (for MacPro7,1 SMBIOS)
    * Previous unconditional
  * `auto` * same as `pci`, set by default
