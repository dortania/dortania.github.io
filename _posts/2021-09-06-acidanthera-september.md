---
layout: post
title: "Acidanthera Updates: September 2021"
date: 2021-09-06 19:00:00 -0400
categories: Hackintosh updates
---

* [A message from vit9696](#a-message-from-vit9696)
* [Changelogs](#changelogs)

# A message from vit9696

This month completes the vacation season, and this time we have something special to present. For a long time Linux support was a grey area in OpenCore. It worked and we fixed the reported issues when it did not. However, one needed to perform a fair amount of work to make Linux natively display in the OpenCore boot pickers, whether built-in or the shiny OpenCanopy. This fall, this is finally changing.

With OpenCore 0.7.3, we present a preview version of the OpenLinuxBoot.efi driver, which delivers first-class Linux support for OpenCore without any chainloading required like GRUB or rEFInd. @MikeBeaton did a really great job on this. His driver supports all sorts of distributions, including [blspec](https://systemd.io/BOOT_LOADER_SPECIFICATION) compatibility, automatic detection of other installation types / schemes, and even manual configuration for particularily peculiar setups. There is a comprehensive section on how to use it in the reference manual, as well as in the discussion for the [PR](https://github.com/acidanthera/OpenCorePkg/pull/282). While we have had positive experiences so far, we must still warn you that the driver has just landed and is still in a beta stage.

Among other bootloader changes there are several stability fixes, new quirks for older hardware courtesy of @mhaeuser, and security revampments by @MikhailKrichanov. As for the drivers, WhateverGreen got a long awaited backlight smoothing support for the Intel GPUs thanks to @0xFireWolf. After months of hard work from @Goldfish64 AppleALC and VirtualSMC are now available on 32-bit macOS versions up to 10.4 for the first time. To add more, VoodooPS2 also received support for the touchpad muxers thanks to @1Revenger1.

— Vit

# Changelogs

#### [OpenCore 0.7.3](https://github.com/acidanthera/OpenCorePkg/releases)

* Improved SSDT-PNLF compatibility with CFL+ graphics
* Fixed OpenCanopy performance loss due to redrawing introduced in 0.6.9
* Added pattern-based automatic variable initialisation for better security
* Updated underlying EDK II package to edk2-stable202108
* Updated Apple Secure Boot variables for `x86legacy`
* Updated Linux variants in Flavours.md
* Implemented Boot Entry Protocol, allowing plug-in boot entry drivers
* Added StringBuffer and FlexArray libraries
* Updated Drivers to support arguments (requires config.plist update, see samples)
* Added OpenLinuxBoot driver: OC-native Linux autodetect and boot without chaining via GRUB
* Fixed overlong boot entry names breaking text flow in builtin menu
* Added `ForceOcWriteFlash` UEFI quirk to enable writing OC system variables

#### [Lilu 1.5.6](https://github.com/acidanthera/Lilu/releases)

* Added the circular buffer API.
* Added convenient helpers to check a value (available as of C++17).
* Added the `OSObjectWrapper` API to wrap a non-`OSObject` value.

#### [AppleALC 1.6.4](https://github.com/acidanthera/AppleALC/releases)

* Added 10.4 and 10.5 support, and 10.6 and 10.7 support in 32-bit mode
* Update STAC9200 layout-id 11 to support 10.4 to 10.6
* Added STAC9205 layout-id 11 for Dell Inspiron 1520 and Latitude D630
* Fixed crash on GPUs without digital audio support introduced in 1.6.1
* Added ALC623 layout-id 21 for Lenovo M70T by Andres ZeroCross
* Seperated Laptop/Desktop patches for 8086:A171 to fix HDMI audio on Intel NUC
* Added ALC236 layout-id 36 for Lenovo Ideapad 510s 14isk by volcbs
* Added ALC235 layout-id 12 for Dell Optiplex 7040 MT by wern-apfel
* Improved CA0132 layout-id 7 by removing not needed MuteGPIO by wern-apfel
* Added ALC235 layout-id 8 for Intel NUC 8 by wern-apfel
* Added ALC269 layout-id 69 for MSI GF63 Thin 9SEXR  by Vorshim92
* Added ALC289 layout-id 93 for XPS 9500 4k by sweet3c
* Added ALC892 layout-id 32 for custom G4/G5mod

#### [VirtualSMC 1.2.7](https://github.com/acidanthera/VirtualSMC/releases)

* Fixed build settings for 32-bit
* Added EC fan monitoring support on `HP OMEN Laptop 15-ek0xxx`, thx @lunjielee
* Added `fan0-dividend` to support more EC fan monitors

#### [WhateverGreen 1.5.3](https://github.com/acidanthera/WhateverGreen/releases)

Note: This release requires Lilu v1.5.6 or later.

* Added `no-gfx-spoof` to avoid forcing `device-id` values from PCI I/O.
* Added the backlight smoother submodule that makes brightness transitions smoother on Intel IVB+ platforms. (by @0xFireWolf)
* MMIO Register Access submodules are now available on Intel IVB+ platforms. (by @0xFireWolf)
* Improved ASUS-made AMD R9 380 GPU identification
* Fixed `applbkl` property with `<00 00 00 00>` value failing to disable backlight patches

#### [HibernationFixup 1.4.3](https://github.com/acidanthera/HibernationFixup/releases)

* Use method routeMultipleLong instead of routeMultiple in order to avoid conflict with DebugEnhancer

#### [DebugEnhancer 1.0.4](https://github.com/acidanthera/DebugEnhancer/releases)

* Use method routeMultipleLong instead of routeMultiple in order to avoid conflict with HibernationFixup

#### [VoodooPS2 2.2.5](https://github.com/acidanthera/VoodooPS2/releases)

* Added support for touchpads with multiplexors

#### [RestrictEvents 1.0.4](https://github.com/acidanthera/RestrictEvents/releases)

* Fixed dual-core CPU spoofing on macOS 10.14 and earlier
* Allow preserving MP7,1 UI through `revnopatch` in NVRAM or boot-args
* Skip leading spaces for automatically received CPU names

#### [CpuTscSync 1.0.4](https://github.com/acidanthera/CpuTscSync/releases)

* Added constants for macOS 12 support
* Added macOS 12 compatibility for CPUs with `MSR_IA32_TSC_ADJUST` (03Bh)
