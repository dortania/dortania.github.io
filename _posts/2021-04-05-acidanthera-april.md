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

On a charming evening in the beginning of April it may be interesting to discuss how our work is accepted by a wider audience. For us, the engineers, the primary focus will unavoidably be the people we know, and quite often these people work in similar spheres. However, as history says, it is still important not to lose contact with the normal humans. Sane normal humans may well be obsessed by technology but they think in more rational categories. What I imply is when an overwhelming change happens under the hood with the core parts being rewritten from scratch, making things far better: more compatible, faster, filled with practical though not so common features, the usual reaction is "it’s great to see things improving steadily bit by bit". A completely different picture is seen when a user-visible change happens. Be it just a single icon on the page, the reaction will be a furore of "what a huge difference it makes".

This is funny but realistic. And since all of us love having fun and value good looking things, we did exactly that. You asked and we delivered. With this release OpenCanopy was rewritten along with the builtin picker and in fact it redefined how all the user input is handled. @Andrey1970AppleLife, @mhaeuser, and @MikeBeaton did a great job on this, planning, designing, writing code, testing, and repeating from scratch, over and over again, and I can guess some of the artists will definitely call this the year of the OpenCanopy desktop :P. It got a whole lot better: gained the ability to shutdown or reboot and started to feature fancy animations like boot entry label scrolling. It even received a fully graphical password input UI to protect advanced setups from tampering, revived the ability to show disk image suffixes with full voice assistance, acquired a visual indication for various keyboard actions like tabbing or holding control to set the default boot entry, what not. Of course all of this comes with 4K support and more than acceptable FPS even on low-end setups.

Another big news is that the new Intel Desktop CPU generation landed. This state of the art all in one solution provides incredible flexibility and finally replaces the well established toolset of an iron, a solderer, and a blowtorch. With an average user it will reduce the cryptography computation times by more than a light-year and will guarantee immediate response tolerance. Besides that, it can seriously be used as a central processor unit, and it still manages to run macOS without a hitch against its will as long as you forget about the graphics. With @vandroiy2013 we spent a few productive evenings conducting all kinds of tests and provided all the basic updates to the bootloader and kexts to ensure immediate compatibility. The early writeup is already [published](https://applelife.ru/posts/933615) and at this time we are expanding our knowledge and providing all the information to the folks at Dortania to write more helpful documentation.

And this is not all. Every week we hang a conscript for the crowd to see and ponder about someone who who did not read the ACPI specification and destroyed a Windows installation. Implementing OS-specific ACPI patching would have been a great idea as an April Fools joke, but it is not happening since we don’t have a good sense of humour. But instead we are giving out something better: a way to lookup a device, a method, or a field and apply patches relative to it. Just like you normally do for your kernel and kext patches. This piece of work, initially prototyped by @koralexa and @Ubsefor, is quite mighty, and though still in beta, may ease building of a bunch of existing and new laptop setups. As usual it provides a standalone utility named ACPIe for debugging purposes.

While these are the grand features, there surely are more to add to the list. One day a user came to our bugtracker and asked to monitor a NUC. We did not quite get the idea at first, you just launch them, but after we reread it for a second time we realised that it was just a mere precedent of no hardware documentation available to accomplish this. This lasted for a while until somebody provided us with what we needed… only to realise that the hardware does not support reading fans or temperatures at all via any standardised interface. And the datasheet has no information on the non-standard one, period. We felt a little disappointed and accidentally added a new class of SuperIO sensors to SMCSuperIO (a VirtualSMC plugin): EC sensors. These sensors are unfortunately hardware specific and documented roughly nowhere. As a result it is not only very hard to add them but it needs to be done for every piece of hardware. Even so, along with @joedmru and @osy after a heavy reverse-engineering session, we prototyped a solution for Intel NUCs and today we have small hopes that various engineers will follow our experience and submit patches for their own hardware into our codebase. Not necessarily just for the EC sensors.

Besides that, there are many minor changes. HibernationFixup and SMCDellSensors became more configurable thanks to [@lvs1974](https://github.com/lvs1974). [@Goldfish64](https://github.com/Goldfish64) fixed various server board issues including dual-processor SMBIOS support and various ACPI bugfixes. We polished the UI for MaciASL and updated iasl compilers to more recent versions with @Moorre. We updated AppleALC and WhateverGreen to include RocketLake features like per-GPU disabling and several controller patches. There are several changes for legacy Macs that resolve CPU frequency calculation and integrate better with their ecosystem, and for all the rest you will have to look over the changelogs, which have about right size this day.

———Vit

# Dortania Updates

It's been a relatively slow month for us here at Dortania. It's been fairly quiet on the guide front, so we've been working on our [OpenCore Legacy Patcher](https://github.com/dortania/OpenCore-Legacy-Patcher/) for unsupported Macs, quashing quite a few bugs, such as fixing a black screen issue on MacBookPro9,1 , preventing the SMC updater from running, and fixing a MacPro5,1 graphics issue. We've also been working on adding new features, including configurable SMBIOS spoofing, debug builds, and codesigning and notarization.

Our biggest update this month is that we've been making great progress on adding GPU acceleration support for older machines to our patcher. Thanks to the invaluable work of [@ASentientBot](https://asentientbot.github.io/), we've been able to get acceleration on quite a bunch of machines, including machines with unsupported NVIDIA, AMD, and Intel graphics. However, there's still a lot of work to do as there are quite a few issues, and we're hard at work fixing them. You can track our progress here:

* [Legacy GPU status tracker](https://github.com/dortania/OpenCore-Legacy-Patcher/issues/108)

Although we're not looking for testers at this time, we do appreciate any ways you can contribute, including [contributing patches or code improvements](https://github.com/dortania/OpenCore-Legacy-Patcher/pulls), [reporting issues](https://github.com/dortania/OpenCore-Legacy-Patcher/issues), or [supporting us with hardware donations](https://dortania.github.io/OpenCore-Legacy-Patcher/DONATE.html).

———dhinakg

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
