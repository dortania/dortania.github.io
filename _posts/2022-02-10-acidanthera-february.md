---
layout: post
title: "Acidanthera Updates: February 2022"
date: 2022-02-10 12:00:00 -0500
categories: Hackintosh updates
---

* [A message from vit9696](#a-message-from-vit9696)
* Changelogs (coming soon!)

*Note: This post was originally supposed to go up on 2022-02-07. We are sorry for the delay.*

# A message from vit9696

Good evening,

We have just released one more stability upgrade:

* Thanks to @mikebeaton, OpenCore will finally work correctly with SIP values, OpenLinuxBoot will no longer crash on partially valid setups, and AudioDxe will work as normal with older macOS versions.
* @Goldfish64 updated RestrictEvents to work with older macOS versions and also fixed its configuration abilities, making them more logical.
* With the help of @Sergey-Galan and others, more codec controller patches were updated to the new format, resolving some HDMI issues in AppleALC.
* @mikebeaton also updated alc-verb to more closely resemble hda-verb behaviour in Linux to increase the interoperability.
* AirportBrcmFixup was updated by @lvs1974 to be more stable on macOS 12.1+.
* @Ph-FrX fixed several backlight issues in WhateverGreen on Ice Lake platforms.

While that makes it for today, we are currently working on improving bootloader security and reliability.

Stay safe,

— Vit

# Changelogs

#### [OpenCore 0.7.8](https://github.com/acidanthera/OpenCorePkg/releases)

#### [Lilu 1.6.0](https://github.com/acidanthera/Lilu/releases)

#### [FeatureUnlock 1.0.6](https://github.com/acidanthera/FeatureUnlock/releases)

#### [WhateverGreen 1.5.7](https://github.com/acidanthera/WhateverGreen/releases)

#### [gfxutil 1.83b](https://github.com/acidanthera/gfxutil/releases)

#### [RestrictEvents 1.0.7](https://github.com/acidanthera/RestrictEvents/releases)

#### [AirportBrcmFixup 2.1.4](https://github.com/acidanthera/AirportBrcmFixup/releases)

#### [CpuTscSync 1.0.6](https://github.com/acidanthera/CpuTscSync/releases)

#### [AppleALC 1.6.9](https://github.com/acidanthera/AppleALC/releases)
