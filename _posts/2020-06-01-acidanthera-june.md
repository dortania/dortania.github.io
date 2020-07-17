---
layout: post
title:  "Acidanthera Updates: June 2020"
date:   2020-06-01 15:00:00 -0700
categories: Hackintosh updates
---

# A message from vit9696

The previous release we published in May was an important step forward in stabilisation of all our products and an anniversary for OpenCore. This release marks the end of the long-lasting repository reorganisation period for all our UEFI products and delivers some very important features to ease your life.

Firstly, the debugging. While troubleshooting is not something you need often, when you do, it is crucial to have proper instruments. An iPhone camera is by all means a great debugging tool, but it is even greater when you do not have to use it. In the latest OpenCore version in addition to EfiBoot debug logging we implemented macOS kernel panic decoding and saving right onto ESP volume. After enabling this in the configuration you will automatically get text representation of all saved macOS kernel panics right after rebooting, which you can later symbolicate with the included `kpdescribe` utility if necessary.

Secondly, boot management. We understand that some people need multiboot support with Windows, sometimes even on the same drive your macOS installation exists. In the latest OpenCore version we reworked boot management from the ground to provide first-class Windows support. This was a tough decision, but it is here and brings better performance and compatibility. In addition to that with the help of the new bootstrap mechanism we were able to mostly resolve duplicated boot entries on ASUS APTIO V boards.

Thirdly, the instrumentation. [@PMHeart](https://github.com/PMheart) recovered our old OpenCore config checking utility, and it is now included right in the package to let you find obvious mistakes in the configuration. New ConfigValidity provides more helpful diagnostic messages and is also available for Windows. While currently it is very basic, we hope that it will evolve in the future. In addition to ConfigUtility several other instruments gained Windows support, and we also updated `dmidecode` with the latest changes from upstream and improved the formatting.

Fourthly, the interface. While not vital, a graphical interface is a nice thing to have, and [@usr-sse2](https://github.com/usr-sse2) worked hard to provide definite font-rendering and HiDPI screen support in the latest update to OpenCanopy. While OpenCanopy is still a preview and lacks some features compared to the builtin text interface like screen reading support, it is evolving with the time and getting important features and bugfixes like basic hotkey handling or seamless integration with EfiBoot or Shell. Other than that we were also able to resolve the input problem on some AMD firmwares.

Lastly, the recently released 10th generation platform. We tested some boards and can confirm that all the products received basic compatibility. Yet, even if there are not any problems on our side, there is quite an amount of issues in Z490 firmwares. For example, on the ASUS board we had Multi-Monitor functionality was broken, XMP made the system unbootable, and XHCI SSDT violated ACPI specification at its best. Even so, while we strongly recommend not to rush trying the new platform, for more advanced engineers we implemented a preview version of ACPI and SMBIOS table dumping right in OpenCore to ease the migration.

In the end I would like to express my sincere gratitude to Acidanthera and WWHC teams for their enthusiasm and professionalism, which make all of this possible. See you in August as Acidanthera takes a short summer vacation.

— Vit

# Changelogs

#### [OpenCore 0.5.9](https://github.com/acidanthera/OpenCorePkg/releases)

* Added full HiDPI support in OpenCanopy
* Improved OpenCanopy font rendering by using CoreText
* Fixed light and custom background font rendering
* Added `Boot####` options support in boot entry listing
* Removed `HideSelf` by pattern recognising `BOOTx64.efi`
* Added `BlacklistAppleUpdate` to avoid Apple FW updates
* Fixed accidental tool and NVRAM reset booting by default
* Fixed unrecognised select `com.apple.recovery.boot` entries
* Changed NVRAM reset not to erase `BootProtect` boot options
* Improved boot performance when picker UI is disabled
* Enforced the use of builtin picker when external fails
* Fixed warnings for empty NVRAM variables (e.g. rtc-blacklist)
* Added `ApplePanic` to store panic logs on ESP root
* Fixed `ReconnectOnResChange` reconnecting even without res change
* Fixed OpenCanopy showing internal icons for external drives
* Fixed OpenCanopy launching Shell with text over it
* Added partial hotkey support to OpenCanopy (e.g. Ctrl+Enter)
* Added builtin text renderer compatibility with Shell page mode
* Fixed `FadtEnableReset` with too small FACP tables and some laptops
* Fixed CPU detection crash with QEMU 5.0 and KVM accelerator
* Removed `RequestBootVarFallback` due to numerous bugs
* Added `DeduplicateBootOrder` UEFI quirk
* Removed `DirectGopCacheMode` due to being ineffective
* Fixed assertions on log exhaustion causing boot failures
* Fixed builtin text renderer failing to provide ConsoleControl
* Fixed compatibility with blit-only GOP (e.g. OVMF Bochs)
* Fixed ignoring `#` in DeviceProperty and NVRAM `Delete`
* Renamed `Block` to `Delete` in `ACPI`,`DeviceProperties`, and `NVRAM`
* Added MacBookPro16,2 and MacBookPro16,3 model codes
* Added PCI device scanning policy support (e.g. VIRTIO)
* Improved playback performance in AudioDxe
* Updated builtin firmware versions for SMBIOS and the rest
* Added improved CPU type detection for newer CPU types
* Added ConfigValidity utility and improved config validation
* Added serial port initialisation for serial debug logging
* Disabled empty debug log file creation to avoid ESP cluttering
* Added `TscSyncTimeout` quirk to workaround debug kernel assertions
* Added first-class Windows support to bless model
* Fixed `LapicKernelPanic` kernel quirk on 10.9
* Added prebuilt version of `CrScreenshotDxe` driver
* Fixed Hyper-V frequency detection compatibility
* Added `SysReport` option for DEBUG builds to dump system info
* Fixed crashes on some AMD firmwares when performing keyboard input

#### [AppleALC 1.5.0](https://github.com/acidanthera/AppleALC/releases)

* Update ALC283 layout-id 88 by xiaoleGun
* Fixed accidental reading of `alc-layout-id` on non-Apple firmwares
* Add patch to fix internal mic gain adjustment Conexant CX8050
* Move ALC255 layout-id 7 to layout-id 86
* Added ALC257 layout-id 86 for Lenovo T480 by armenio
* Fixed can't activate mute problem Conexant CX8070 layout-id 15 by lietxia
* Added ALC255 layout-id 20 for DELL 7447 by was3912734. Add Subwoofer drive.
* Added ALC662 layout-id 18 for MP67-DI/ESPRIMO Q900 by ryahpalma
* Added ALC256 layout-id 19 for Matebook X Pro 2019 by Durian-Life
* Added ALC256 layout-id 76 (4CH) for Matebook X Pro 2019 by Durian-Life

#### [VirtualSMC 1.1.4](https://github.com/acidanthera/VirtualSMC/releases)
 
 * Fixed incorrect revision reporting on T2 models (e.g. Macmini8,1)

#### [RTCMemoryFixup 1.0.6](https://github.com/acidanthera/RTCMemoryFixup/releases)

* Fix reading of key rtc-blacklist from NVRAM (only 4 bytes could be read)
* rtcfx_exclude can be combined with rtc-blacklist

#### [IntelMausi 1.0.3](https://github.com/acidanthera/IntelMausi/releases)

* Merged changes from 2.5.1d1

#### [dmidecode 3.2c](https://github.com/acidanthera/dmidecode/releases)

* Update to 5b3c8e99 with SMBIOS 3.2 improvements

#### [WhateverGreen 1.4.0](https://github.com/acidanthera/WhateverGreen/releases)

* Added 0x3EA6, 0x8A53, 0x9BC4, 0x9BC5, 0x9BC8 IGPU device-id
* Fixed `framebuffer-conX-alldata` patching regression
* Added `disable-hdmi-patches` device property alias to `-igfxnohdmi`

#### [Lilu 1.4.5](https://github.com/acidanthera/Lilu/releases)

* Fixed newer CPU generation detection
* Added failsafe versions of CML framebuffers

#### [VoodooInput 1.0.6](https://github.com/acidanthera/VoodooInput/releases)

* Reduced memory consumption and CPU usage
* Fixed dragging issues on some touchpads

#### [VoodooPS2 2.1.5](https://github.com/acidanthera/VoodooPS2/releases)

* Upgraded to VoodooInput 1.0.6
* Added logo + print scr hotkey to disable trackpad

# Guide Updates

While not made by Acidanthera, both the OpenCore Desktop and Laptop Guides have been updated with 0.5.9 support. And the desktop guide getting early Comet Lake-S support:

* [OpenCore Install Guide](https://dortania.github.io/OpenCore-Install-Guide/)

— Khronokernel
