---
layout: post
title: "Acidanthera Updates: October 2022"
date: 2022-10-04 10:15:00 -0400
categories: Hackintosh updates
---

* [Acidanthera Updates: A message from PMheart](#acidanthera-updates-a-message-from-pmheart)
* [Changelogs](#changelogs)

# Acidanthera Updates: A message from PMheart

Having experienced a chilling September, October comes after a nice weekend. Following iOS 16, macOS Ventura is coming soon.

As usual, there are no critical updates to OpenCore 0.8.5, as recent beta versions of macOS 13 tend to be stable. To begin with, @Andrey1970AppleLife updated builtin firmware versions which might be useful for the official macOS update. Then, several more updates regarding Hyper-V, including the correction for CPU objects that are exclusively available in Windows Server 2022, and extra hot-adding/removing device path expansion support, have been carried out by @Goldfish64. As well, we improved verbose logging for kernel patching, which can be useful for developers to filter patcher status. That's it.

@Goldfish64 pushed a bunch of updates to MacHyperVSupport 0.9.2: The issue with control key pressing has been fixed, together with DMA allocation problems and another one with buffer overrun in network packet sending; VMBus implemenations get improved; intermittent hangs storage and network drivers are addressed. Finally, he added support for storage disk hot-adding/removing and that for guest restart via Restart-VM; time synchronization support for the guest machine has landed as well.

Thanks to the hard work of @dhinakg and @khronokernel, those CPU models without AVX2.0 support can boot normally by installing the Apple Silicon Cryptex (OS.dmg) with the help of the new Lilu plugin - CryptexFixup. Still, this breaks delta updates ([ref](https://github.com/acidanthera/bugtracker/issues/2080)), and we are looking forward to patches and contributions to this.

For VoodooPS2, we would like to give credits to @diepeterpan who fixed disabled keyboard after reboot. Users with the common problems can now enjoy VoodooPS2 2.3.1. Also, @lalithkota improved compatibility with BCM43142A0 on macOS Big Sur in BrcmPatchRAM 2.6.4.

Enjoy,

— PMheart

# Changelogs

#### [OpenCorePkg 0.8.5](https://github.com/acidanthera/OpenCorePkg/releases)

* Updated builtin firmware versions for SMBIOS and the rest
* Moved CPU objects that exist only in Windows Server 2022 into SSDT-HV-DEV-WS2022.dsl
* Updated Hyper-V device path expansion to support hot add/remove of disks
* Improved verbose logging during kernel patching

#### [BrcmPatchRAM 2.6.4](https://github.com/acidanthera/BrcmPatchRAM/releases)

* Improve compatibility with BCM43142A0 on macOS Big Sur (thx lalithkota)

#### [VoodooPS2 2.3.1](https://github.com/acidanthera/VoodooPS2/releases)

* Fixed disabled keyboard after reboot

#### [CryptexFixup 1.0.0](https://github.com/acidanthera/CryptexFixup/releases)

* Initial release

#### [MacHyperVSupport 0.9.2](https://github.com/acidanthera/MacHyperVSupport/releases)

* Fixed crash when control key is pressed under macOS 10.4
* Fixed DMA allocations under macOS 10.4 and 10.5
* Refactored and cleaned up VMBus core logic and integration services
* Fixed crash caused by a buffer overrun in network packet sending
* Fixed intermittent hangs in storage and network drivers
* Added support for storage disk addition and removal while VM is running
* Added support for guest restart via Restart-VM
* Renamed hvshutdown daemon to hvutil to support all userspace-side functions
* Added guest time synchronization support
* Added support for "Type clipboard text" function
