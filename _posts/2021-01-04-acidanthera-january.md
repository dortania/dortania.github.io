---
layout: post
title:  "Acidanthera Updates: January 2021"
date:   2021-01-04 15:00:00 -0700
categories: Hackintosh updates
---

* [A message from vit9696](#a-message-from-vit9696)
* [Dortania Updates](#dortania-updates)
* [Changelogs](#changelogs)

# A message from vit9696

{Inspirational message}

——Vit

# Dortania Updates

{Inspirational message}

——Khronokernel

# Changelogs

#### [OpenCore 0.6.5](https://github.com/acidanthera/OpenCorePkg/releases)

* Fixed installing OpenDuet on protected volumes
* Updated underlying EDK II package to edk2-stable202011
* Updated builtin firmware versions for SMBIOS and the rest
* Fixed macrecovery server protocol compatibility
* Added basic audio assistant support in OpenCanopy
* Added compiled ACPI samples to the package
* Fixed timer resolution restoration at boot time
* Fixed memory capacity when using custom SMBIOS memory config
* Removed no longer required `DeduplicateBootOrder` quirk
* Fixed macserial crashes when processing invalid serials
* Fixed macserial issues when processing 2021 year serials
* Added advanced error checking in ocvalidate utility
* Added `SetupDelay` to configure audio setup delay
* Reworked LogoutHook.command to support older macOS
* Implemented MP3 audio decoding for audio assistant support
* Added support for `PickerVariant` for more theme variants
* Added `OC_ATTR_HIDE_THEMED_ICONS` `PickerAttribute` for Time Machine

#### [RestrictEvents 1.0.0](https://github.com/acidanthera/RestrictEvents/releases)

* Initial release

#### [WhateverGreen 1.4.6](https://github.com/acidanthera/WhateverGreen/releases)

* Backlight registers fix replaces the previous Coffee Lake backlight fix and is now available on Intel Ice Lake platforms.
* Boot argument `igfxcflbklt=1` as well as device property `enable-cfl-backlight-fix` are deprecated and replaced by `-igfxblr` and `enable-backlight-registers-fix`.
* Add max pixel clock override through `-igfxmpc` boot argument or `enable-max-pixel-clock-override` and `max-pixel-clock-frequency` device properties
* Moved PNLF samples to OpenCore

#### [IntelMausi 1.0.5](https://github.com/acidanthera/NVMeFix/releases)

* Merged changes from 2.5.3d1
* Updated e1000e sources from Linux upstream branch
* Solved high-load throttling problem for I219 family
* Add support for new I219 Cannon-Point family devices
    * I219-LM13
    * I219-V13
    * I219-LM14
    * I219-V14
    * I219-LM15
    * I219-V15
    * I219-LM16
    * I219-V16
    * I219-LM17
    * I219-V17
    * I219-LM18
    * I219-V18
    * I219-LM19
    * I219-V19

#### [NVMeFix 1.0.5](https://github.com/acidanthera/IntelMausi/releases)

* Fixed quirks enabling per controller
* Fixed initialisation on 10.15+

#### [CPUFriend 1.2.3](https://github.com/acidanthera/CPUFriend/releases)

* Improved path handling in generator scripts

#### [VoodooPS2 2.2.0](https://github.com/acidanthera/VoodooPS2/releases)

* Added VoodooRmi compatibility to allow external touchpad resets

#### [AppleALC 1.5.6](https://github.com/acidanthera/AppleALC/releases)

* Improved `alc-verbs` availability checking
* Add Realtek ALC256 layout-id 67 for Dell OptiPlex 7080
* Add ALC222 layout-id 11 for HP EliteDesk 800 G6 Mini
* Add ALC256 layout-id 69 Xiaomi Pro Enhanced 2019

#### [HibernationFixup 1.3.9](https://github.com/acidanthera/HibernationFixup/releases)

* Auto hibernation: properly handle transition from dark wake to full wake
* Extend method emuVariableIsDetected in order to use EfiRuntimeServices if nvram cannot be accessed in standard way

#### [dmidecode 3.3a](https://github.com/acidanthera/dmidecode/releases)

* Update to 3c111e4f with SMBIOS 3.3 improvements
