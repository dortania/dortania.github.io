---
layout: post
title:  "What's new in macOS 11, Big Sur!"
date:   2020-11-12 7:00:00 -0600
categories: Hackintosh updates
---

* [Reddit Thread](https://www.reddit.com/r/hackintosh/comments/jsziec/whats_new_in_macos_11_big_sur/)

It's that time of year again, and we've got a new version of macOS on our hands! This year we've finally jumped off the 10.xx naming scheme and now going to 11! And with that, a lot has changed under the hood in macOS.

As with [previous years](https://dortania.github.io/hackintosh/updates/2019/10/07/catalina.html), we'll be going over what's changed in macOS and what you should be aware of as a macOS and Hackintosh enthusiast.

* [Has Nvidia Support finally arrived?](#has-nvidia-support-finally-arrived)
* [What has changed on the surface](#what-has-changed-on-the-surface)
  * [A whole new iOS-like UI](#a-whole-new-ios-like-ui)
  * [macOS Snapshotting](#macos-snapshotting)
  * [Broken Kexts in Big Sur](#broken-kexts-in-big-sur)
* [What has changed under the hood](#what-has-changed-under-the-hood)
  * [New Kernel cache system: KernelCollections!](#new-kernel-cache-system-kernelcollections)
  * [New Kernel Requirements](#new-kernel-requirements)
    * [Secure Boot Changes](#secure-boot-changes)
    * [No more symbols required](#no-more-symbols-required)
  * [Broken Kexts in Big Sur](#broken-kexts-in-big-sur)
  * [MSI Navi installer Bug Resolved](#msi-navi-installer-bug-resolved)
  * [New AMD OS X Kernel Patches](#new-amd-os-x-patches)
  * [Other notable Hackintosh issues](#other-notable-hackintosh-issues)
    * [Several SMBIOS have been dropped](#several-smbios-have-been-dropped)
    * [Dropped hardware](#dropped-hardware)
    * [Extra long install process](#extra-long-install-process)
    * [X79 and X99 Boot issues](#x79-and-x99-boot-issues)
	* [Asus Z97 failing Stage 2 Installation](#asus-z97-failing-stage-2-installation)
    * [New RTC requirements](#new-rtc-requirements)
    * [SATA Issues](#sata-issues)
    * [Legacy GPU Patches currently unavailable](#legacy-gpu-patches-currently-unavailable)
* [What’s new in the Hackintosh scene?](#whats-new-in-the-hackintosh-scene)
  * [Dortania: a new organization has appeared](#dortania-a-new-organization-has-appeared)
  * [Dortania's Build Repo](#dortania-s-build-repo)
  * [True legacy macOS Support!](#true-legacy-macos-support)
  * [Intel Wireless: More native than ever!](#intel-wireless-more-native-than-ever)
  * [Clover's revival? A frankenstein of a bootloader](#clovers-revival-a-frankenstein-of-a-bootloader)
  * [Death of x86 and the future of Hackintoshing](#death-of-x86-and-the-future-of-hackintoshing)
* [Getting ready for macOS 11, Big Sur](#getting-ready-for-macos-11-big-sur)

# Has Nvidia Support finally arrived?

![](https://github.com/dortania/GPU-Buyers-Guide/blob/master/WebDrivers.gif?raw=true)

Sadly every year I have to answer the obligatory question, no there is no new Nvidia support. Currently [Nvidia's Kepler line](https://dortania.github.io/GPU-Buyers-Guide/modern-gpus/nvidia-gpu.html) is the only natively supported gen.

However macOS 11 makes some interesting changes to the boot process, specifically moving GPU drivers into stage 2 of booting. Why this is relevant is due to Apple's initial reason for killing off Web Drivers: Secure boot. What I mean is that secure boot cannot work with Nvidia's Web Drivers due to how early Nvidia's drivers have to initialize at, and thus Apple refused to sign the binaries. With Big Sur, there could be 3rd party GPUs however the chances are still super slim but slightly higher than with 10.14 and 10.15.

# What has changed on the surface

## A whole new iOS-like UI

Love it or hate it, we've got a new UI more reminiscent of iOS 14 with hints of skeuomorphism(A somewhat subtle call back to previous mac UIs which have neat details in the icons)

You can check out Apple's site to get a better idea:

* [Apple's Big Sur Preview](https://www.apple.com/macos/big-sur-preview/)

## macOS Snapshotting

A feature initially baked into APFS back in 2017 with the release of macOS 10.13, High Sierra, now macOS's main System volume has become both read-only and snapshotted. What this means is:

* 3rd parties have a much more difficult time modifying the system volume, allowing for greater security
* OS updates can now be installed while you're using the OS, similar to how iOS handles updates
* Time Machine can now more easily perform backups, without file inconsistencies with HFS Plus while you were using the machines

However there are a few things to note with this new enforcement of snapshotting:

* OS snapshots are not calculated as used space, instead being labeled as purgeable space
* Disabling macOS snapshots for the root volume with break software updates, and can corrupt data if one is applied


# What has changed under the hood

Quite a few things actually! Both in good and bad ways unfortunately.

* [New Kernel cache system: KernelCollections!](#new-kernel-cache-system-kernelcollections)
* [New Kernel Requirements](#new-kernel-requirements)
  * [Secure Boot Changes](#secure-boot-changes)
  * [No more symbols required](#no-more-symbols-required)
* [Broken Kexts in Big Sur](#broken-kexts-in-big-sur)
* [MSI Navi installer Bug Resolved](#msi-navi-installer-bug-resolved)
* [New AMD OS X Kernel Patches](#new-amd-os-x-patches)
* [Other notable Hackintosh issues](#other-notable-hackintosh-issues)
  * [Several SMBIOS have been dropped](#several-smbios-have-been-dropped)
  * [Dropped hardware](#dropped-hardware)
  * [Extra long install process](#extra-long-install-process)
  * [X79 and X99 Boot issues](#x79-and-x99-boot-issues)
  * [New RTC requirements](#new-rtc-requirements)
  * [SATA Issues](#sata-issues)

## New Kernel Cache system: KernelCollections!

So for the past 15 years, macOS has been using the Prelinked Kernel as a form of Kernel and Kext caching. And with macOS Big Sur's new Read-only, snapshot based system volume, a new version of caching has be developed: KernelCollections!

How this differs to previous OSes:

* Kexts can no longer be hot-loaded, instead requiring a reboot to load with `kmutil`
* [All kernels now support Secure Boot(ie. no more dedicated `immutablekernel`)](#secure-boot-changes)
  * Now all Macs will have some form of basic Secure Boot support
* [Symbols are no longer required](#no-more-symbols-required)

### Secure Boot Changes

With regards to Secure Boot, now all officially supported Macs will also now support some form of Secure Boot even if there's no T2 present. This is now done in 2 stages:

* macOS will now always verify the ECID value to the secure boot manifest files(if present)
  * On T2's this ECID value is burned into the chip
  * On regular Macs, the first 8 bytes of your SystemUUID value
  * On Hackintoshes, this will either be automatically generated by your SystemUUID value or [manually added with a cryptographically secure random number generator](https://dortania.github.io/OpenCore-Post-Install/universal/security/applesecureboot.html)
* OS Snapshots are now verified on each boot to ensure no system volume modifications occurred
  * apfs.kext and AppleImage4.kext verify the integrity of these snapshots

While technically these security features are optional and can be disabled after installation, many features including OS updates will no longer work reliably once disabled. This is due to the heavy reliance of snapshots for OS updates, as mentioned above and so we highly encourage all users to ensure at minimum `SecureBootModel` is set to `Default` or [higher](https://dortania.github.io/OpenCore-Post-Install/universal/security/applesecureboot.html).

* **Note**: ApECID is not required for functionality, and can be skipped if so desired.
* **Note 2**: OpenCore 0.6.3 or newer is required for Secure Boot in Big Sur.

### No more symbols required

This point is the most important part, as this is what we use for kext injection in OpenCore. Currently Apple has left symbols in place seemingly for debugging purposes however this is a bit worrying as Apple could outright remove symbols in later versions of macOS. But for Big Sur's cycle, we'll be good on that end however we'll be keeping an eye on future releases of macOS.

## New Kernel Requirements

With this update, the `AvoidRuntimeDefrag` Booter quirk in OpenCore broke. Because of this, the macOS kernel will fall flat when trying to boot. Reason for this is due to `cpu_count_enabled_logical_processors` requiring the MADT (APIC) table, and so OpenCore will now ensure this table is made accessible to the kernel. Users will however need a build of OpenCore 0.6.0 with commit [`bb12f5f`](https://github.com/acidanthera/OpenCorePkg/commit/9f59339e7eb8c213e84551df0fdbf9905cd98ca4) **or newer** to resolve this issue.

Additionally, both [Kernel Allocation requirements](https://github.com/acidanthera/OpenCorePkg/commit/c8bf19dc807548ba938a1e67a014531d647355b6) and [Secure Boot have also broken with Big Sur](https://github.com/acidanthera/OpenCorePkg/commit/1b0041493d4693f9505aa6415d93079ea59f7ab0) due to the new caching system discussed above. Thankfully these have also been resolved in OpenCore 0.6.3.


To check your OpenCore version, run the following in terminal:

```sh
nvram 4D1FDA02-38C7-4A6A-9CC6-4BCCA8B30102:opencore-version
```

If you're not up-to-date and running OpenCore 0.6.3+, see here on how to upgrade OpenCore: [Updating OpenCore, Kexts and macOS](https://dortania.github.io/OpenCore-Post-Install/universal/update.html)

## Broken Kexts in Big Sur

Unfortunately with the aforementioned KernelCollections, some kexts have unfortunately broken or have been hindered in some way. The main kexts that currently have issues are anything relying on Lilu's userspace patching functionality:

* [WhateverGreen's](https://github.com/acidanthera/WhateverGreen) [DRM](https://dortania.github.io/OpenCore-Post-Install/universal/drm.html) and `-cdfon` patches
  * Most of WhateverGreen's functions are still working as they're kernelspace based
* [MacProMemoryNotificationDisabler](https://github.com/IOIIIO/MacProMemoryNotificationDisabler)
* [SystemProfilerMemoryFixup](https://github.com/Goldfish64/SystemProfilerMemoryFixup)

Thankfully most important kexts rely on kernelspace patcher which is now in fact working again.

## MSI Navi installer Bug Resolved

For those receiving boot failures in the installer due to having an MSI Navi GPU installed, macOS Big Sur has finally resolved this issue!

## New AMD OS X Kernel Patches

For those running on AMD-Based CPUs, you'll want to also update your kernel patches as well since patches have been rewritten for macOS Big Sur support:

* [AMD OSX Kernel Patches](https://github.com/AMD-OSX/AMD_Vanilla)

## Other notable Hackintosh issues

* [Several SMBIOS have been dropped](#several-smbios-have-been-dropped)
* [Dropped hardware](#dropped-hardware)
* [Extra long install process](#extra-long-install-process)
* [X79 and X99 Boot issues](#x79-and-x99-boot-issues)
* [Asus Z97 failing Stage 2 Installation](#asus-z97-failing-stage-2-installation)
* [New RTC requirements](#new-rtc-requirements)
* [SATA Issues](#sata-issues)

### Several SMBIOS have been dropped

Big Sur dropped a few Ivy Bridge and Haswell based SMBIOS from macOS, so see below that yours wasn't dropped:

* iMac14,3 and older
  * Note iMac14,4 is still supported
* MacPro5,1 and older
* MacMini6,x and older
* MacBook7,1 and older
* MacBookAir5,x and older
* MacBookPro10,x and older

If your SMBIOS was supported in Catalina and isn't included above, you're good to go! We also have a more in-depth page here: [Choosing the right SMBIOS](https://dortania.github.io/OpenCore-Install-Guide/extras/smbios-support.html)

For those wanting a simple translation for their Ivy and Haswell Machines:

* iMac13,1 should transition over to using iMac14,4
* iMac13,2 should transition over to using iMac15,1
* iMac14,2 and iMac14,3 should transition over to using iMac15,1
  * Note: AMD CPUs users should transition over to MacPro7,1
* iMac14,1 should transition over to iMac14,4

### Dropped hardware

Currently only certain hardware has been officially dropped:

* "Official" Consumer Ivy Bridge Support(U, H and S series)
  * These CPUs will still boot without much issue, but note that no Macs are supported with consumer Ivy Bridge in Big Sur.
  * Ivy Bridge-E CPUs are still supported thanks to being in MacPro6,1
* Ivy Bridge iGPUs slated for removal
  * HD 4000 and HD 2500, however currently these drivers are still present in 11.0.1
  * Similar to Mojave and Nvidia's Tesla drivers, we expect Apple to forget about them and only remove them in the next major OS update next year
* BCM4331 and BCM43224 based Wifi cards.
  * See [Wireless Buyers guide](https://dortania.github.io/Wireless-Buyers-Guide/) for potential cards to upgrade to.
  * Note, while AirPortBrcm4360.kext has been removed in Big Sur, support for the 4360 series cards have been moved into AirPortBrcmNIC.kext, which still exists.
  * For work-arounds, see here: [Legacy Wireless Kexts](https://github.com/khronokernel/IO80211-Patches)

### Extra long install process

Due to the new snapshot-based OS, installation now takes some extra time with sealing. If you get stuck at `Forcing CS_RUNTIME for entitlement`, **do not shutdown**. This will corrupt your install and break the sealing process, so please be patient:

![](https://github.com/dortania/OpenCore-Install-Guide/blob/master/images/extras/big-sur/readme/cs-stuck.jpg?raw=true)

### X79 and X99 Boot issues

With Big Sur, IOPCIFamily went through a decent rewriting causing many X79 and X99 boards to fail to boot as well as panic on IOPCIFamily. To resolve this issue, you'll need to disable the unused uncore bridge:

* [SSDT-UNC](https://github.com/acidanthera/OpenCorePkg/blob/master/Docs/AcpiSamples/SSDT-UNC.dsl)

You can also find prebuilts here for those who do not wish to compile the file themselves:

* [Dortania's Pre-Built SSDTs](https://dortania.github.io/Getting-Started-With-ACPI/ssdt-methods/ssdt-prebuilt.html)

### Asus Z97 failing Stage 2 Installation

With Big Sur, there's a higher reliance on native NVRAM for installation otherwise the installer will get stuck in a reboot loop. To resolve this you'll need to either:

* Install Big Sur on another machine, then transfer the drive
* Fix the motherboard's NVRAM

For the latter, see here: [Haswell ASUS Z97 Big Sur Update Thread](https://www.reddit.com/r/hackintosh/comments/jw7qf1/haswell_asus_z97_big_sur_update_and_installation/)

### New RTC requirements

With macOS Big Sur, AppleRTC has become much more picky on making sure your OEM correctly mapped the RTC regions in your ACPI tables. This is mainly relevant on Intel's HEDT series boards, I documented how to patch said RTC regions in OpenCorePkg:

* [SSDT-RTC0-RANGE](https://github.com/acidanthera/OpenCorePkg/blob/master/Docs/AcpiSamples/SSDT-RTC0-RANGE.dsl)

For those having boot issues on X99 and X299, this section is super important; you'll likely get stuck at `PCI Configuration Begin`. You can also find prebuilts here for those who do not wish to compile the file themselves:

* [Dortania's Pre-Built SSDTs](https://dortania.github.io/Getting-Started-With-ACPI/ssdt-methods/ssdt-prebuilt.html)

### SATA Issues

For some reason, Apple removed the AppleIntelPchSeriesAHCI class from AppleAHCIPort.kext. Due to the outright removal of the class, trying to spoof to another ID (generally done by SATA-unsupported.kext) can fail for many and create instability for others.
  * A partial fix is to block Big Sur's AppleAHCIPort.kext and inject Catalina's version with any conflicting symbols being patched. You can find a sample kext here: [Catalina's patched AppleAHCIPort.kext](https://github.com/dortania/OpenCore-Install-Guide/blob/master/extra-files/CtlnaAHCIPort.kext.zip)
  * This will work in both Catalina and Big Sur so you can remove SATA-unsupported if you want. However we recommend setting the MinKernel value to 20.0.0 to avoid any potential issues.

### Legacy GPU Patches currently unavailable

Due to major changes in many frameworks around GPUs, those using [ASentientBot's](https://forums.macrumors.com/members/1135186/) legacy GPU patches are currently out of luck. We either recommend users with these older GPUs stay on Catalina until further developments arise or buy an [officially supported GPU](https://dortania.github.io/GPU-Buyers-Guide/)

# What’s new in the Hackintosh scene?

* [Dortania: a new organization has appeared](#dortania-a-new-organization-has-appeared)
* [Dortania's Build Repo](#dortania-s-build-repo)
* [True legacy macOS Support!](#true-legacy-macos-support)
* [Intel Wireless: More native than ever!](#intel-wireless-more-native-than-ever)
* [Clover's revival? A frankenstein of a bootloader](#clovers-revival-a-frankenstein-of-a-bootloader)
* [Death of x86 and the future of Hackintoshing](#death-of-x86-and-the-future-of-hackintoshing)

## Dortania: a new organization has appeared

As many of you have probably noticed, a new organization focusing on documenting the hackintoshing process has appeared. Originally under my alias, [Khronokernel](https://github.com/khronokernel), I started to transition my guides over to this new family as a way to concentrate the vast amount of information around Hackintoshes to both ease users and give a single trusted source for information. 

We work quite closely with the community and developers to ensure information's correct, up-to-date and of the best standards. While not perfect in every way, we hope to be the go-to resource for reliable Hackintosh information.

And for the times our information is either outdated, missing context or generally needs improving, we have our bug tracker to allow the community to more easily bring attention to issues and speak directly with the authors:

* [Dortania's Bugtracker](https://github.com/dortania/bugtracker)

## Dortania's Build Repo

For those who either want to run the lastest builds of a kext or need an easy way to test old builds of something, Dortania's Build Repo is for you!

* [**Build Repo**](https://dortania.github.io/builds/)

Kexts here are built right after commit, and currently supports most of Acidanthera's kexts and some 3rd party devs as well. If you'd like to add support for more kexts, feel free to PR: [Build Repo source](https://github.com/dortania/build-repo)

## True legacy macOS Support!

As of OpenCore's latest versioning, 0.6.2, you can now boot every version of x86-based builds of OS X/macOS! A huge achievement on [@Goldfish64](https://github.com/Goldfish64)'s part, we now support every major version of kernel cache both 32 and 64-bit wise. This means machines like Yonah and newer should work great with OpenCore and you can even relive the old days of OS X like OS X 10.4!

And Dortania guides have been updated accordingly to accommodate for builds of those eras, we hope you get as much enjoyment going back as we did working on this project!

## Intel Wireless: More native than ever!

Another amazing step forward in the Hackintosh community, near-native Intel Wifi support! Thanks to the endless work on many contributors of the [OpenIntelWireless project](https://github.com/OpenIntelWireless/), we can now use Apple's built-in IO80211 framework to have near identical support to those of Broadcom wireless cards including features like network access in recovery and control center support.

For more info on the developments, please see the itlwm project on GitHub: [itlwm](https://github.com/OpenIntelWireless/itlwm)

* Note, native support requires the AirportItlwm.kext and [SecureBootModel enabled on OpenCore](https://dortania.github.io/OpenCore-Post-Install/universal/security/applesecureboot.html). Alternatively you can force IO80211Family.kext to ensure AirportItlwm works correctly.
* Airdrop support currently is also not implemented, however is actively being worked on.

## Clover's revival? A frankestien of a bootloader

As many in the community have seen, a new bootloader popped up back in April of 2019 called [OpenCore](https://github.com/acidanthera/OpenCorePkg). This bootloader was made by the same people behind projects such as [Lilu](https://github.com/acidanthera/Lilu), [WhateverGreen](https://github.com/acidanthera/WhateverGreen), [AppleALC](https://github.com/acidanthera/AppleALC) and many other extremely important utilities for both the Mac and Hackintosh community. OpenCore's design had been properly thought out with security auditing and proper road mapping laid down, it was clear that this was to be the next stage of hackintoshing for the years we have left with x86.

And now lets bring this back to the old crowd favorite, [Clover](https://github.com/CloverHackyColor/CloverBootloader/). Clover has been having a rough time of recent both with the community and stability wise, with many devs jumping ship to OpenCore and Clover's stability breaking more and more with C++ rewrites, it was clear Clover was on its last legs. Interestingly enough, the community didn't want Clover to die, similarly to how Chameleon lived on through Enoch. And thus, we now have the [Clover OpenCore integration project](https://github.com/CloverHackyColor/CloverBootloader/tree/opencore_integration)(Now merged into Master with r5123+).

The goal is to combine OpenCore into Clover allowing the project to live a bit longer, as Clover's current state can no longer boot macOS Big Sur or older versions of OS X such as 10.6. As of writing, this project seems to be a bit confusing as there seems to be little reason to actually support Clover. Many of Clover's properties have [feature-parity in OpenCore](https://github.com/dortania/OpenCore-Install-Guide/tree/master/clover-conversion) and trying to combine both C++ and C ruins many of the features and benefits either languages provide. The main feature OpenCore does not support is macOS-only ACPI injection, however the reasoning is covered here: [Does OpenCore always inject SMBIOS and ACPI data into other OSes?](https://dortania.github.io/OpenCore-Install-Guide/why-oc.html#does-opencore-always-inject-smbios-and-acpi-data-into-other-oses)

## Death of x86 and the future of Hackintoshing

With macOS Big Sur, a big turning point is about to happen with Apple and their Macs. As we know it, Apple will be shifting to in-house designed Apple Silicon Macs(Really just ARM) and thus x86 machines will slowly be phased out of their lineup within 2 years. 

What does this mean for both x86 based Macs and Hackintoshing in general? Well we can expect about 5 years of proper OS support for the iMac20,x series which released earlier this year with an extra 2 years of security updates. After this, Apple will most likely stop shipping x86 builds of macOS and hackintoshing as we know it will have passed away.

For those still in denial and hope something like ARM Hackintoshes will arrive, please consider the following:

* We have yet to see a true iPhone "Hackintosh" and thus the likely hood of an ARM Hackintosh is unlikely as well
  * There have been successful attempts to get the iOS kernel running in virtual machines, however much work is still to be done
* Apple's use of "Apple Silicon" hints that ARM is not actually what future Macs will be running, instead we'll see highly customized chips *based* off ARM
  * For example, Apple will be heavily relying on hardware features such as [W^X](https://en.wikipedia.org/wiki/W%5EX), kernel memory protection, Pointer Auth, etc for security and thus both macOS and Applications will be dependant on it. This means hackintoshing on bare-metal(without a VM) will become extremely difficult without copious amounts of work
  * Also keep in mind Apple Silicon will no longer be UEFI-based like Intel Macs currently are, meaning a huge amount of work would also be required on this end as well

So while we may be heart broken the journey is coming to a stop in the somewhat near future, hackintoshing will still be a time piece in Apple's history. So enjoy it now while we still can, and we here at Dortania will still continue supporting the community with our guides till the very end!

# Getting ready for macOS 11, Big Sur

This will be your short run down if you skipped the above:

* Lilu's userspace patcher is broken
  * Due to this many kexts will break:
      * DiskArbitrationFixup
      * MacProMemoryNotificationDisabler
      * SidecarEnabler
      * SystemProfilerMemoryFixup
      * NoTouchID
      * WhateverGreen's DRM and -cdfon patches
* Many Ivy Bridge and Haswell SMBIOS were dropped
  * See above for what SMBIOS to choose
* Ivy Bridge iGPUs are to be dropped
  * Currently in 11.0.1, these drivers are still present
* BCM4331 and BCM43224 support was dropped
  * Solution listed here: [Legacy Wireless Kexts](https://github.com/khronokernel/IO80211-Patches)
* X79 and X99 require SSDT-UNC
  * See above how to make it
* X99 and X299 requires SSDT-RTC0-RANGE
  * See above how to make it
* Asus Z97 needing to fix NVRAM
  * See above
* AMD CPUs need their kernel patches updated
  * See above for new patches
* OpenCore 0.6.3 or newer is required to boot
* Latest releases of all your kexts

For the last 2, see here on how to update: [Updating OpenCore, Kexts and macOS](https://dortania.github.io/OpenCore-Post-Install/universal/update.html)

In regards to downloading Big Sur, OpenCore Install Guide has been updated to utilise macrecovery.py for Windows and Linux users. macOS users can still use GibMacOS.

And as with every year, the first few weeks to months of a new OS release are painful in the community. We **highly** advise users to stay away from Big Sur for first time installers. The reason is that we cannot determine whether issues are Apple related or with your specific machine, so it's best to install and debug a machine on a known working OS before testing out the new and shiny.

For more in-depth troubleshooting with Big Sur, see here: [OpenCore and macOS 11: Big Sur](https://dortania.github.io/OpenCore-Install-Guide/extras/big-sur/)
