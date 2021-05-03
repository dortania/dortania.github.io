---
layout: post
title:  "Acidanthera Updates: May 2021"
date:   2021-05-03 14:45:00 -0400
categories: Hackintosh updates
---

* [A message from vit9696](#a-message-from-vit9696)
* [Dortania Updates](#dortania-updates)
* [Changelogs](#changelogs)

# A message from vit9696

This nice May evening brings us to another point in the Acidanthera chronology. To our surprise, it is not as minor as we initially expected. We were able to deliver not just the bug fixes but also features and more importantly we built certain design concepts that will help us go over the next steps.

Our primary objective was to continue investigating the new Z590 platform, and our belief at the time is that we succeeded in going over all the major nuances. Till the Dortania guides are updated you can use a separate [blog post](https://dortania.github.io/hackintosh/updates/2021/04/24/rocket-lake.html) covering all the caveats and our findings to work around them. In addition to Z590, we summarized our knowledge regarding NVMe SSD compatibility and provided a [list](https://github.com/dortania/bugtracker/issues/192) compiled by [@Andrey1970AppleLife](https://github.com/Andrey1970AppleLife) to help with the choice. We are very grateful to all the volunteers who provided the data, thank you! Eventually, the list will find its way to the Dortania guides, one way or the other.

After the previous OpenCore release brought numerous changes to the OpenCanopy interface, we discovered minor discrepancies in the implementation and addressed them accordingly. The mouse cursor should now move properly over the whole screen area, new power management buttons became optional, arrow keys will wrap around the boot entry list, and the version string can now be shown in the bottom right corner similar to the textual user interface. All thanks to [@MikeBeaton](https://github.com/MikeBeaton) and [@mhaeuser](https://github.com/mhaeuser).

When we introduced Apple Secure Boot last year we mentioned that while it is quite fast, the signature verification process can still be further optimized on newer platforms. Thanks to [@MikhailKrichanov](https://github.com/MikhailKrichanov) this actually happened and we were able to win up to a second during the boot time on Intel 3rd generation CPUs and newer with the `EnableVectorAcceleration` quirk enabled. This setting should be harmless even on unsupported CPUs, so we recommend keeping it enabled in case further acceleration features are added to the bootloader. The other OpenCore changes of this time are: NVIDIA graphics output support for legacy Mac Pro computers, utility binaries for Linux, updated EDK II codebase, and recent Mac EFI firmware versions.

On the kext side, we fixed IntelMausi loading on macOS 10.11, Lilu kernel patcher functioning on macOS 10.7, and NVMeFix support on macOS 11.3. Since more and more users will now opt with the `MacPro7,1` model, we provided a full explanation on why the memory misconfigured warning happens in the [reference manual](https://github.com/acidanthera/OpenCorePkg/commit/5db7147293e952fbdd9c3168631b0f75a9c09b81#diff-ff76194142498a223908566484df3ed947764eace1ae6104347516807422c9acR5332-R5346) and two workarounds of your choice: a custom plist sample and an update to RestrictEvents, which provides the natural About Mac user interface regardless of the Mac model. RestrictEvents now also allows customizing the CPU description and NVMeFix makes it possible to enable ASPM on Macs with limited device property access. SMCSuperIO EC sensors became more powerful and include bug fixes to Intel NUCs and the fan reading support on certain laptops sharing the design concept. Last but not least, MaciASL and the bundled ACPI compilers are now built with Apple Silicon support and no longer require Rosetta to run.

———Vit

# Dortania Updates

This month's been a big release cycle for us including many long-awaited features for [OpenCore Legacy Patcher](https://github.com/dortania/OpenCore-Legacy-Patcher/)! These include:

* Public Beta Support for Legacy Graphics Acceleration Patches thanks to [@ASentientBot](https://asentientbot.github.io/)
  * Including Nvidia's Tesla and Fermi, AMD/ATI's TeraScale 1 and Intel's Ironlake and Sandy Bridge graphics
  * [Current Issues](https://github.com/dortania/OpenCore-Legacy-Patcher/issues/108)
* Sidecar support for models with Metal-based Intel iGPUs
  * Based off our new [SidecarFixup Extension](https://github.com/khronokernel/SidecarFixup)
* AppleALC Support for 2011 and older Models
  * No longer relying on root patching for audio support
* Add El Capitan era Wifi card support
  * First of any patcher for Big Sur
* Windows 10 PCI Allocation patches for UEFI
  * Allowing better Audio and eGPU support on Sandy and Ivy Bridge Macs
* Support for Native Macs, allowing better 3rd Party Hardware support
  * Includes 3rd Party NVMe Patches, allowing for up-to 90% power reduction at idle on non-Apple drives
  * Sidecar Support for models excluded by Apple

Overall we're extremely happy with the progress made, and with macOS 12 a little over a month away we eagerly await to see what else Apple has for us to fix. Hope everyone enjoys the new releases!

———Khronokernel

# Changelogs

#### [OpenCore 0.6.9](https://github.com/acidanthera/OpenCorePkg/releases)

- Fixed out-of-sync cursor movement rectangle when loading e.g. CrScreenshotDxe
- Updated underlying EDK II package to edk2-stable202102
- Applied consistent enforcement of required minimum Apple OEM Apple Event protocol version
- Changed CustomDelays to less surprising boolean setting with failsafe of false
- Changed key repeat failsafes and sample values to Apple OEM values
- Changed PointerSpeedMul failsafe to Apple OEM value
- Updated docs to include configuration of key repeat settings with and without KeySupport
- Prevented 'set default' UI when action not permitted by security config
- Added `ForgeUefiSupport` quirk to workaround legacy EFI 1.x firmwares compatibility
- Added `ReloadOptionRoms` quirk to force-load Option ROMs on PCI devices
- Added `OC_ATTR_USE_MINIMAL_UI` to allow running pickers with no Shutdown and Restart buttons
- Added display of OpenCore version number to OpenCanopy as well as builtin picker, depending on existing ExposeSensitiveData bit
- Added support for case-insensitive argument handling in the UEFI tools
- Added vector acceleration of SHA-512 and SHA-384 hashing algorithms, thx @MikhailKrichanov
- Fixed wraparound when using arrow keys in OpenCanopy
- Updated builtin firmware versions for SMBIOS and the rest
- Added bundled Linux versions for userspace utilities
- Fixed fallback SMBIOS `Manufacturer` value to `NO DIMM` for empty slots
- Fixed assertions when running OpenCanopy with low resolution, will fallbacks to builtin now

#### [IntelMausi 1.0.6](https://github.com/acidanthera/IntelMausi/releases)

- Fixed loading on 10.11 and earlier (regressed in 1.0.5)

#### [VirtualSMC 1.2.3](https://github.com/acidanthera/VirtualSMC/releases)

- Fixed Intel NUC EC sensors not showing proper values on some platforms
- Added `generic` EC sensor type
- Added EC fan monitoring support on `HP Pavilion 14 CE2072NL`, thx @1alessandro1

#### [AppleALC 1.6.0](https://github.com/acidanthera/AppleALC/releases)

- Added `use-layout-id` property to use `layout-id` as is on Macs
- Added `use-apple-layout-id` property to use `apple-layout-id` as `layout-id` on Macs
- Fixed CS4206 and ALC885 support for legacy Macs
- Improvement ALC289 layout-id 87 for Alienware m15 by GitNaufal
- Added ALC1220 layout-id 98 for Mi Gaming Notebook Creator by Xsixu
- Added ALC1220 layout-id 100 for Hasee_G8-CU7PK by R-a-s-c-a-l

#### [VoodooPS2 2.2.3](https://github.com/acidanthera/OpenCorePkg/releases)

- Added `DisableDeepSleep` to workaround ACPI S3 wakes on some Synaptics touchpads

#### [NVMeFix 1.0.7](https://github.com/acidanthera/NVMeFix/releases)

- Fixed symbol solving on macOS 11.3
- Added `-nvmefaspm` boot argument to force ASPM L1 on all NVMe SSDs

#### [RestrictEvents 1.0.1](https://github.com/acidanthera/RestrictEvents/releases)

- Disabled `MacPro7,1` RAM & PCI Expansion Slot UIs
- Disabled `MacBookAir` memory view restrictions
- Added CPU brand string patch

#### [MaciASL 1.6.1](https://github.com/acidanthera/MaciASL/releases)

- Enabled codesigning and notarisation
- Added native ARM builds for iasl compilers
- Updated iasl compiler versions

#### [Lilu 1.5.3](https://github.com/acidanthera/Lilu/releases)

- Fixed kernel patcher support on 10.7
