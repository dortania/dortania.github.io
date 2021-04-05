---
layout: post
title:  "Acidanthera Updates: April 2021"
date:   2021-04-07 15:00:00 -0700
categories: Hackintosh updates
---

* [A message from vit9696](#a-message-from-vit9696)
* [Dortania Updates](#dortania-updates)
* [Changelogs](#changelogs)

# A message from vit9696

Eventually

# Dortania Updates

@khronokernel

# Changelogs

#### [OpenCore 0.6.8](https://github.com/acidanthera/OpenCorePkg/releases)
- Switched to VS2019 toolchain for Windows builds
- Reduced legacy boot install interaction effort
- Increased OpenCanopy rendering performance
- Added OpenCanopy Shut Down and Restart buttons
- Reduced OpenCanopy mouse pointer input lag
- Fixed that cursor bounds could be different from OpenCanopy's
- Improved builtin picker rendering performance
- Added Memory Type decoding for SMBIOS in `Automatic` mode
- Properly support setting custom entries as default boot options
- Fixed creating log file when root file system is not writable
- Fixed `DisableSingleUser` not being enabled in certain cases
- Added `ForceBooterSignature` quirk for Mac EFI firmware
- Fixed OpenCanopy sometimes cutting off shown boot entries
- Further improved CPU frequency calculation on legacy CPUs
- Fixed SMBIOS SMC version encoding sequence
- Added TSC frequency reading from Apple Platform Info
- Added TSC frequency reading for Apple devices with nForce chipsets
- Added `Base` and `BaseSkip` lookup for ACPI patches
- Fixed ACPI table magic corruption during patching
- Fixed unnatural OpenCanopy and FileVault 2 cursor movement
- Fixed OpenCanopy interrupt handling causing missed events and lag
- Improved OpenCanopy double-click detection 
- Reduced OpenCanopy touch input lag and improved usability
- Improved keypress responsiveness in OpenCanopy and builtin pickers
- Improved non-repeating key detection in OpenCanopy and builtin pickers
- Fixed Escape preventing OpenCanopy fade up until released, on some systems
- Fixed fast repeat then stall issue with key handling on some PS/2 systems
- Added accurate Shift+Enter/Shift+Index detection when using PollAppleHotKeys
- Added 'set default' indicator to builtin picker
- Replaced VerifyMsrE2 with ControlMsrE2 also allowing unlock on some firmwares
- Fixed OpenCanopy flicker when refreshing the entry view
- Added OpenCanopy TAB navigation support
- Added OpenCanopy graphical password interface
- Added OpenCanopy pulsing animation to signal timeout
- Added OpenCanopy 'set default' indicator
- Fixed OpenCanopy not aborting timeout on pointer click
- Fixed OpenCanopy intro animation not scaling with UIScale
- Add OpenCanopy boot entry label scrolling (fixes missing long labels)
- Added tabbable Shutdown and Restart buttons to builtin picker
- Fixed in-firmware shutdown for some systems running OpenDuet
- Added Zero as alias hotkey for Escape, to force show picker if hidden
- Added =/+ key as alias for CTRL to set default OS
- Added additional support for configuring correct key repeat behaviour with KeySupport mode
- Fixed CPU multiplier detection on pre-Nehalem Intel CPUs
- Fixed incorrect handling of multiple processors and processor cache in SMBIOS
- Matched default Apple boot picker cursor start position
- Updated OpenShell `devices` command to support misaligned device names returned by some Apple firmware
- Added `(dmg)` suffix to DMG boot options in OpenCanopy
- Added identifiers for Rocket Lake and Tiger Lake CPUs
- Added PickerAudioAssist 'disk image' indication
- Fixed PickerAudioAssist indications played twice in rare cases
- Improved OpenCanopy pointer acceleration
- Added more precise control on `AppleEvent` protocol properties and features
- Added dynamic keyboard protocol installation on CrScreenshotDxe
- Support starting UEFI tools with argument support (e.g. `ControlMsrE2`) without arguments from picker
- Fixed OpenCanopy font height calculation, may reject previously working fonts and mitigate memory corruption
- Fixed incorrect identification of Xeon E5XXX/E5-XXXX and Xeon WXXXX/W-XXXX CPUs
- Added RSDP, RSDT, and XSDT handling to `NormalizeHeaders` ACPI quirk

#### [NVMeFix 1.0.6](https://github.com/acidanthera/NVMeFix/releases)
- Added APST workaround for Kingston A2000

#### [AppleALC 1.5.9](https://github.com/acidanthera/AppleALC/releases)
- Added CS4206 layout-id 24 and 60
- Added 500 Series (0xF0C8 Z590 + Intel 10 Gen) PCH HD Audio Controller
- Added 500 Series (0x43C8 Z590 + Intel 11 Gen) PCH HD Audio Controller
- Added ALC289 layout-id 87 for Alienware m15 by GitNaufal
- Added ALC289 layout-id 15 for Dell 7730 Precision CM240 by MacPeet
- Added ALC897 layout-id 69 for MSI-Z490-A Pro by mathcampbell
- Added IDT 92HD95 layout-id 14 for LenovoG710 by Svilen88
- Added ALC235 layout-id 18 for asrock 310 bb by viorel78
- Added controller patch for 100 Series (8086:A170) by dhinakg

#### [Lilu 1.5.2](https://github.com/acidanthera/Lilu/releases)
- Fixed AZAL recognition as GPU audio on certain AMD platforms (thx to wkpark)
- Added external GPU disabling API with device and kernel selection via properties
- Added identifiers for Rocket Lake and Tiger Lake CPUs
- Added API to disable builtin GPU (IGPU)
- Reduced hardware presence bruteforce to a more sensible value

#### [HibernationFixup 1.4.0](https://github.com/acidanthera/HibernationFixup/releases)
- Auto hibernation: added possibility to disable power event kStimulusDarkWakeActivityTickle in kernel, so this event cannot be a trigger for switching from dark wake to full wake.
Can be turned on via bit `DisableStimulusDarkWakeActivityTickle=128` in boot-arg `hbfx-ahbm`.
- Support options in NVRAM (GUID = E09B9297-7928-4440-9AAB-D1F8536FBF0A or LiluReadOnlyGuid)

#### [WhateverGreen 1.4.9](https://github.com/acidanthera/WhateverGreen/releases)
- Added per-GPU disabling API: inject `disable-gpu` to disable
- Added per-GPU disabling kernel version specification: inject `disable-gpu-min` / `disable-gpu-max` to select kernel version to disable (inclusive range)
- Added IGPU disabling API: inject `disable-gpu` to disable or use `-wegnoigpu` boot argument
- Optimised Rocket Lake startup as IGPU is unsupported

#### [BrcmPatchRAM 2.5.8](https://github.com/acidanthera/BrcmPatchRAM/releases)
- Added BCM94360Z3 identifiers for injection

#### [VoodooInput 1.1.2](https://github.com/acidanthera/VoodooInput/releases)
- Improved touch state abstraction

#### [MaciASL 1.6.0](https://github.com/acidanthera/MaciASL/releases)
- Updated iasl compiler versions
- Fixed exceptions generated when performing certain tasks

#### [VirtualSMC 1.2.2](https://github.com/acidanthera/VirtualSMC/releases)
- Improve manual fan control in SMCDellSensors (SMM access is enabled even if audio is played)
- Fixed sensor DEBUG logging with `-liludbgall` argument
- Improved startup performance when probing SuperIO chips by splitting vendors
- Added SuperIO device activation when it is disabled on probe
- Added support for Nuvoton NCT6796D-E (0xD42A)
- Added support for ITE IT8987 (requires DEBUG firmware, not available for public)
- Added Intel NUC monitoring (requires manual configuration via `ec-device`, see `EmbeddedControllers.md`)
