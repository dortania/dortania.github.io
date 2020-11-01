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

{Insert inspirational message}

- Vit

# Guide Updates

{Insert boring message}

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

#### [Lilu 1.4.9](https://github.com/acidanthera/Lilu/releases)

- Added the PCI GMCH Graphics Control register definition. (by 0xFireWolf)
- Added a new API to solve multiple symbols in one shot conveniently. (by 0xFireWolf)
- Added a new `RouteRequest` constructor to work with function pointers without additional type castings. (by 0xFireWolf)

#### [AppleALC 1.5.4](https://github.com/acidanthera/AppleALC/releases)

- Improved Ice Lake controller patches by fewtarius
- Added verb sending functionality from userspace by black-dragon74

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
