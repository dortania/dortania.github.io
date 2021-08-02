---
layout: post
title: "Acidanthera Updates: August 2021"
date: 2021-08-02 14:45:00 -0400
categories: Hackintosh updates
---

* [A message from vit9696](#a-message-from-vit9696)
* [Dortania Updates][#dortania-updates]
* [Changelogs](#changelogs)

# A message from vit9696

With the vacation season ongoing we continue to deliver minor updates to all the products improving overall stability and compatibility.

We understand the importance of security, and this is why all our products are built with security in mind. With this release OpenCore becomes even more tamper resistant by introducing [stack canary](https://en.wikipedia.org/wiki/Buffer_overflow_protection) support thanks to @MikhailKrichanov. Furthermore, we fixed macOS 12 Apple Secure Boot compatibility. As a side measure, we deprecated Apple Secure Boot support for macOS 10.15 and older with the default preferences. The primary reason is due to these operating systems not having advanced protective measures such as root volume authentication like in macOS 11 and above. To continue using Apple Secure Boot with older operating systems one will need to specify `j137` in the `SecureBootModel` parameter, yet this value will not work with macOS 12. Similarly to Apple Secure Boot, APFS driver verification requirements were also bumped to macOS 11 and newer, and thus require one to change `MinDate` and `MinVersion` in the APFS section if older macOS versions need to be launched.

On the kernel side @Goldfish64 pioneered with 32-bit kernel extension support, expanding Lilu, VirtualSMC, and SMCBatteryManager compatibility to macOS 10.4 and above. We will continue to expand older macOS compatibility to help the developers test their software on various configurations. WhateverGreen got device-id spoofing support for AMD cards, letting newer RX 6900 GPUs run without a hassle. RestrictEvents became more configurable and received minor enhancements for better compatibility with macOS 10.15 and older.

— Vit

# Dortania Updates

WIP

# Changelogs

#### [OpenCore 0.7.2](https://github.com/acidanthera/OpenCorePkg/releases)

* Fixed OSBundleLibraries/OSBundleLibaries64 handling
* Added `GraphicsInputMirroring` to fix lost keystrokes in some non-Apple graphical UEFI apps
* Added support for stack canaries (security cookies / stack guards)
* Fixed unintialised memory access in AudioDxe causing audio playback failure
* Changed `Default` Apple Secure Boot model to `x86legacy` for better security and compatibility
* Increased default APFS `MinDate` and `MinVersion` to macOS Big Sur for better security
* Updated builtin firmware versions for SMBIOS and the rest
* Improved SSDT-PNLF compatibility with Windows and newer graphics
* Fixed CLANGPDB OpenCore builds by shortening OC magic

#### [Lilu 1.5.5](https://github.com/acidanthera/Lilu/releases)

* Added a variant of `KernelPatcher::findAndReplace` that requires both `find` and `replace` buffers to have the same length.
* Added support for macOS 10.4 and newer

#### [AppleALC 1.6.3](https://github.com/acidanthera/AppleALC/releases)

*

#### [VirtualSMC 1.2.6](https://github.com/acidanthera/VirtualSMC/releases)

* Added macOS 10.4 support for VirtualSMC and SMCBatteryManager

#### [WhateverGreen 1.5.2](https://github.com/acidanthera/WhateverGreen/releases)

* Added `device-id` spoofing support for AMD graphics

#### [FeatureUnlock 1.0.3](https://github.com/acidanthera/FeatureUnlock/releases)

* Rename project from SidecarFixup to FeatureUnlock

#### [HibernationFixup 1.4.2](https://github.com/acidanthera/HibernationFixup/releases)

* Use method routeMultipleLong instead of routeMultiple in order to avoid conflict with future versions of CpuTscSync

#### [MacHyperVSupport 0.6.0](https://github.com/acidanthera/MacHyperVSupport/releases)

* Added constants for macOS 12 support
* Enable loading on 32-bit macOS 10.6 and 10.7
