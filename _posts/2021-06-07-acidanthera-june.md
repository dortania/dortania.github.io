---
layout: post
title:  "Acidanthera Updates: June 2021"
date:   2021-06-07 14:45:00 -0400
categories: Hackintosh updates
---

* [A message from vit9696](#a-message-from-vit9696)
* [Changelogs](#changelogs)

# A message from vit9696

Pleasure to meet you on this summer day. This release commemorates a second ten-version cycle for OpenCore, and we shall say that we are quite satisfied with the achievements we accomplished over the year. Big Sur support, a really tough thing, Apple Secure Boot, legacy platform support including 32-bit computers with macOS 10.4, a whole lot of visual improvements, hardware compatibility and performance fixes, documentation rewrite, usability refinements. We did way more than we planned, and are grateful to the support from our families, friends, who encouraged us and helped to find spare time, from the external contributors, who brought new features and helped to track the issues, from the community that started to build an ecosystem based on the entities we create. Thank you all for being here!

We have three major highlights for today, and our first is OpenCanopy. We worked hard to understand what the artists need from the user interface, and did our best to integrate it in a best possible way that does not contradict the OpenCore architecture. With this update a new icon concept lands in OpenCanopy. While previously the themes were limited to a small list of predefined icon names, newly introduced flavours allow arbitrary icon names that do not depend on OpenCore code and can be maintained by the community. For better understanding @MikeBeaton additionally wrote a [writeup](https://github.com/acidanthera/OpenCorePkg/blob/master/Docs/Flavours.md) explaining the caveats and defining the initial list. Besides that, we built a new home for all the artists: [OpenCanopy Gallery](https://dortania.github.io/OpenCanopy-Gallery). While still under development, OpenCanopy Gallery already hosts a few examples and is waiting for your contributions.

Next thing to discuss are virtual machines. Virtual machines are an essential part of our everyday workflow. Those who do not use them directly may be running them indirectly. It may be slightly uncommon knowledge but modern Windows runs itself as a [virtual machine](https://docs.microsoft.com/windows-hardware/design/device-experiences/oem-vbs). What it means for the end-user is that every modern operating system comes with a virtualisation stack. Linux and macOS come with accelerators: Hypervisor.framework and KVM accordingly. There needs to be third-party software that can utilise these mechanisms to run virtual machines, like VMware or QEMU. Windows comes with an all-in-one solution — Hyper-V. Since the amount of Windows users continues to grow, we agreed that being able to install macOS with the builtin hypervisor on Windows is a must. With thus release Goldfish64 implemented all the basics in MacHyperVSupport.

Last but not least are our continuing tests of the Z590 platform. As more boards continue to go through our hands, we discover more new issues or let's say possibilities:
- Since most Z590 boards have USB audio, we built a light version of our audio supplement driver — AppleALCU. This driver only has digital audio patches and is recommended for these setups.
- Many ASUS boards for some reason fail to enable ASPM on the NVMe SSDs and GPUs. As a result one needs to inject `pci-aspm-default` with `<02 00 00 00>` value into the relevant devices and their parent bridges, when not observing the lower 2 bits, to fix the bug.
- Disabling the `IGPU` via  `disable-gpu` property may not be sufficient as it may happen late. This may result in broken sleep or DRM issues. To workaround that one can inject `class-code` with `<FF FF FF FF>` value and `name` with `"unused"` value.
- ASMedia USB HUB used in ASUS boards to split the USB ports (e.g. 1 to 4) may immediately wake the system after sleep when working in USB 3.x mode for the first sleep attempt. This one looks extremely random and may be a bug of certain particular boards, but at the very least one can force it in 2.0 mode as a workaround.

That's all for the highlights, see below for a complete changelog and have a nice evening.

———Vit

# Changelogs

#### [OpenCore 0.7.0](https://github.com/acidanthera/OpenCorePkg/releases)

- Fixed NVRAM reset on firmware with write-protected `BootOptionSupport`
- Improved direct GOP renderer performance for certain cases
- Added support for display rotation in direct GOP renderer
- Fixed handling multinode device paths in LoadedImage and elsewhere
- Changed OpenCanopy image directory to support directory prefixes
- Changed OpenCanopy preferred image set to `Acidanthera\GoldenGate`
- Removed `<BOOTPATH>.icns` and `<TOOLPATH>.icns` support
- Added content flavour system allowing custom boot entry icons compatible across icon packs
- Added automatic flavour detection for macOS boot entries
- Added `ProvideCurrentCpuInfo` quirk to provide correct TSC/FSB for Hyper-V virtual machines
- Added Hyper-V device path expansion to allow setting default boot volume
- Added `Apple` variant of `GopPassThrough` to handle only `AppleFramebufferInfo` handles
- Fixed further kernel patches not being processed if a patch was skipped due to arch mismatch
- Added optional Toggle SIP system boot menu option
- Added `CsrUtil.efi` tool, similar to Apple `csrutil`
- Removed support for `<TOOLPATH>.lbl`/`.l2x` pre-drawn entry labels
- Fixed previous text not cleared before console mode tools and entries in OpenCanopy
- Fixed DEBUG build crashes with `GopPassThrough` and `UgaPassThrough`
- Added flavour for memory testing utilities
- Updated recommended `memtest86` config in sample `.plist` files
- Defined bootloader flavours
- Applied own flavour to OC build
- Added CPU topology fixes to `ProvideCurrentCpuInfo` quirk
- Updated OC default SIP disabled value
- Documented SIP values which affect macOS updates
- Added `csr-data` Apple NVRAM var to docs
- Fixed file alignment causing codesign issues with CLANGPDB images
- Replaced `AdviseWindows` with `AdviseFeatures` to support APFS


#### [RestrictEvents 1.0.2](https://github.com/acidanthera/RestrictEvents/releases)

- Fixed patching CPU brand string with 8 core configurations
- Fixed detecting CPU core count on some CPU models
- Added single-core CPU brand string spoofing support

#### [AppleALC 1.6.1](https://github.com/acidanthera/AppleALC/releases)

- Fixed broken data in CS4206's layout76.xml
- Added PathMapID 4206 and 8800 for ALC885's Layout 67 and 73
- Fixed broken data in ALC289's layout87.xml
- Fixed automatic resource formatting on build
- Fixed ALC885's Info.plist Platforms entry
- Added 400 Series (0xF1C8 Z490 + Intel 11 Gen) PCH HD Audio Controller
- Fixed `alc-verb` device indexing giving varying results over reboots
- Added device listing with indices via `-L`/`-l` in `alc-verb`
- Added AppleALCU kext variant for digital-only audio setup
- Disabled kext patching for verb support and delays when not requested
- FIxed replace count in `WhiskeyLake` HDA patches
- Separated Intel `WhiskeyLake` laptop and desktop patches
- Added ALC1220 layout-id 35 for MSI GP75 9SD by Win7GM
- Added ALC1200 (display as ALCS1200A) layout-id 69 for Asrock Z490M ITX/AC by Lorys89 & Vorshim92
- Added ALC293 layout-id 30 for HASEE ZX8-CT5DA by RushiaBoingBoing
- Added ALC255 layout-id 96 for dell 5559 by Bhavin
- Fix mute on Conxexant CX 20724 by Human7900
- Added ALC1220 layout-id 17 for Gigabyte Z490 Vision G manual SP/HP by NIBLIZE
- Added ALC255 layout-id 82 for minisforum U820 by daliansky
- Added ALC282 layout-id 21 for TinyMonster ECO by DalianSky

#### [NVMeFix 1.0.8](https://github.com/acidanthera/NVMeFix/releases)

- Fixed applying quirks based on the disk name and serial
- Make Kingston A2000 quirk specific to S5Z42105

#### [VirtualSMC 1.2.4](https://github.com/acidanthera/VirtualSMC/releases)

- Added support for NCT6683D series

#### [BrightnessKeys 1.0.2](https://github.com/acidanthera/BrightnessKeys/releases)

- Fixed potential null pointer dereference crash

#### [WhateverGreen 1.5.0](https://github.com/acidanthera/WhateverGreen/releases)

- Fixed AMD WX-4170 name for 67E0 device id
- Added NVIDIA driver error logging with `-ngfxdbg`

#### [SidecarFixup 1.0.1](https://github.com/acidanthera/SidecarFixup/releases)

- Fixed excessive memory comparison
- Fixed boot argument handling on Secure Boot enabled macOS

#### [BrcmPatchRAM 2.5.9](https://github.com/acidanthera/BrcmPatchRAM/releases)

- Added BCM94352Z identifiers for injection

#### [MacHyperVSupport 0.5](https://github.com/acidanthera/MacHyperVSupport/releases)


#### [gfxutil 1.81b](https://github.com/acidanthera/gfxutil/releases)

- Improved compatibility with older EFI device paths having invalid trailing node (0xFF)

#### [UEFIGraphicsFB 1.0.0](https://github.com/acidanthera/UEFIGraphicsFB/releases)

- Initial release




