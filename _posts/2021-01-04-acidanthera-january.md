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

Happy New Year everyone! We hope that you have had and perhaps still have some calm holidays and are ready to check-in for a small but important update we prepared. We begin this year under the slogan of stability and usability improvements, and this time we have done really well to help you maintain your setup.

To begin with, [@PMheart](https://github.com/PMheart) wrote an absolutely overwhelming update to [ocvalidate utility](https://github.com/acidanthera/OpenCorePkg/tree/master/Utilities/ocvalidate). As some of you may already know, ocvalidate is an OpenCore configuration checking tool that reports issues that are clear violations of the specification, i.e. semantic mistakes in the configuration. [@PMheart](https://github.com/PMheart) added many semantical checks that allow not only finding missing fields or wrong field types, but also various inconsistencies, incorrect values, duplicate entries, and many more. Hopefully, ocvalidate will continue to ensure a cleaner configuration for everyone. Other than that, several other utilities like [dmidecode](https://github.com/acidanthera/dmidecode), [macserial, macrecovery, and LogoutHook](https://github.com/acidanthera/OpenCorePkg/tree/master/Utilities) got their own updates with special thanks going to [@roddy20](https://github.com/roddy20) for still caring about older hardware.

It has been quite some time since we made changes to [OpenCanopy](https://github.com/acidanthera/OpenCorePkg), so this update brings small but important changes to its audio-visual experience. From now on you can utilize prefixes for the icon packs, and as a result, a new Modern icon pack was bundled as a built-in addendum thanks to [@Andrey1970AppleLife](https://github.com/Andrey1970AppleLife). We are continuing to make the artists' lives better, and hopefully, this change will make their experience even more smooth. In addition, we also brought audio assistant support to OpenCanopy and re-encoded the audio files, significantly reducing their size.

The road to Big Sur was not quite smooth for some, and this update brings a few more compatibility improvements. [NVMeFix](https://github.com/acidanthera/NVMeFix) got initial macOS 11 support, noticeably reducing laptop power consumption, and MacPro7,1 users got a new [RestrictEvents kext](https://github.com/acidanthera/RestrictEvents), resolving issues with the memory misconfiguration notifications. Last but not least, [@savvamitrofanov](https://github.com/savvamitrofanov) spent quite some time exploring the issues in [IntelMausi](https://github.com/acidanthera/IntelMausi) and he was eventually able to resolve many speed issues and Wake on Lan problems for some machines. While we still recommend the [upstream version](https://github.com/Mieze/IntelMausiEthernet) and provide no support for our variant, perhaps the changes made are useful for further development.

——Vit

# Dortania Updates

Happy new year to everyone from Dortania! As we're coming off the holidays, we wanted to take a look back at what's happened in the community over the past year.

Late March last year we had the release of macOS 10.15.4, where we got official support for Comet and Ice Lake CPUs. Overall Comet Lake's introduction was quite smooth however Ice Lake's iGPU drivers needed more work done to ensure stable operations with consumer PCs. Not too long after, [@0xFireWolf](https://github.com/0xFireWolf) and others in the community had adapted WhateverGreen into fully supporting Ice Lake's iGPUs.

Soon after in early April, we started working on a new organization to centralize Hackintosh documentation as well as allowing more users to join in and contribute. Initially, most of the guides on Dortania were hosted under my alias, khronokernel, meaning the work was heavily tied to me. But with Dortania, this new organization, we were able to bring in a much larger contributor base allowing us to expand and improve the quality of our sites. 

From there came June and Apple's WWDC event. Here we were introduced to both macOS 11, Big Sur as well as Apple's transition away from Intel towards their in-house silicon. While the public was all eyes on the death of x86 in macOS, here in the community we had much bigger fish to fry. From Apple's new kernel cache system, to the snapshot-based system volume and reworked framework caching system, there was much to be done. Before Big Sur's release, Acidanthera had almost all of the most important issues resolved.

Overall it's been quite a roller coaster, but we're still committed to supporting Hackintoshes till the end. While the popularity in building a hack will go down, we know many of you are still around to learn and to tinker. And for those enthusiasts, we're more than happy to continue writing.

And for my final words, I wanted to dedicate a bit of this in memory of my late father, Volodymyr Grymalyuk. A man passionate about his work, I inherited a lot of your drive and passion for your work, I am truly honored to be your son and hope for a safe passage in the after-life.

——Mykola Grymalyuk (Khronokernel)

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

#### [IntelMausi 1.0.5](https://github.com/acidanthera/IntelMausi/releases)

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

#### [NVMeFix 1.0.5](https://github.com/acidanthera/NVMeFix/releases)

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
