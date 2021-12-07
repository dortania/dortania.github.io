---
layout: post
title: "Acidanthera Updates: December 2021"
date: 2021-12-06 23:50:00 -0500
categories: Hackintosh updates
---

* [A message from vit9696](#a-message-from-vit9696)
* [Changelogs](#changelogs)

# A message from vit9696

Good evening,

As some of you already noticed, winter is coming. However, unlike the streets freezing and getting covered with snow, the development here starts to accelerate. This time we worked hard to get better support for Intel Alder Lake, about which we are going to give a separate post. Other than that, we addressed a few unpleasant bugs that affected certain legacy systems in a pretty bad manner.

First, Intel Alder Lake. This required a substantial amount of changes in OpenCore and kexts, and we believe it is possible that more changes might happen in the future. OpenCore currently recognises the 12th CPU generation by Intel and includes several ACPI samples that make the bring-up process smoother. We also adjusted some quirks like `ProvideConsoleGop` to workaround ASUS firmware specialties. Thanks to @R-a-s-c-a-l, AppleALC was updated to support Z690's audio controller, although we have not been able to test this ourselves yet. We also crafted a pilot version of the CpuTopologySync driver, allowing the use of efficiency cores in macOS. I thank @vandroiy2013 for spending days and nights debugging this piece of hardware, giving smart ideas, and all in all helping me understand the caveats.

Thanks to @Goldfish64, OpenCore now supports higher resolution mode-set on old NVIDIA GPUs through the BiosVideo driver. OpenCore will also let one automatically select the display scaling depending on the connected screen, which eases the ability to swap monitors. To switch to this new option one will need to perform an NVRAM reset, and @PMheart also updated ocvalidate to ensure that new settings have appropriate values. Label scrolling glitches were also fixed in OpenCanopy thanks to @mikebeaton and @mhaeuser. We hope that the overall rendering experience will be a little better with this update.

`ProtectUefiServices` will no longer crash certain Dell computers thanks to @al3xtjames and `FadtEnableReset` will make sure Dell computers reboot thanks to @Goldfish64 again. `ScanPolicy` can now handle old Samsung NVMe drives, which are exposed as PCI drives, not NVMe. Thanks to @mikebeaton, legacy Macs can get virtual machine support not just in macOS through `EnableVmx` quirk. After @mikhailkrichanov's updates GCC builds are functional again.

Lilu got crash fixes on 10.15 and older. With the recent efforts of @khronokernel and @dhinakg, FeatureUnlock received updated patches for macOS 12.1 and minor performance improvements. @lvs1974 additionally pushed some compatibility fixes into SMCDellSensors.

That makes it for this evening.

— Vit

# Changelogs

#### [OpenCore 0.7.6](https://github.com/acidanthera/OpenCorePkg/releases)

- Fixed stack canary support when compiling with GCC
- Added automatic scaling factor detection
- Explicitly restricted `ResizeAppleGpuBars` to 0 and -1
- Fixed OpenCanopy long labels fade-out over graphics background
- Fixed `ProvideConsoleGop` not disabling blit-only modes (e.g. on Z690)
- Fixed Alder Lake SMBIOS CPU model information
- Added XCPM CPU power management ACPI table for Intel Alder Lake
- Updated draw order to avoid graphics tearing in OpenCanopy
- Fixed handling PCI device paths with logical units in ScanPolicy
- Added `ReconnectGraphicsOnConnect` option for enabling alternative UEFI graphics drivers
- Added BiosVideo.efi driver to use with `ReconnectGraphicsOnConnect`
- Changed `FadtEnableReset` to avoid unreliable keyboard controller reset
- Added `EnableVmx` quirk to allow virtualization in other OS on some Macs
- Upgraded `ProtectUefiServices` to prevent GRUB shim overwriting service pointers when chainloading with Secure Boot enabled
- Removed deprecated SSDT-PNLFCFL
- Fixed handling of zero-sized Memory Attributes Table

#### [Lilu 1.5.8](https://github.com/acidanthera/Lilu/releases)

- Fixed kernel panic on macOS 10.15 and earlier introduced in 1.5.7
- Added Alder Lake CPU model support
- Added shared patcher instance grabbing API

#### [AppleALC 1.6.7](https://github.com/acidanthera/AppleALC/releases)

- Added 600-series controller patch by @R-a-s-c-a-l
- Added ALC282 layout-id 69 for Lenovo IdeaPad Z510 by hoseinrez
- Added ALC285 layout-id 66 for for Lenovo Legion S740 15-IRH by @R-a-s-c-a-l
- Fix PinConfigs Device and Port in ALC662v3 by static-host
- Added ALC269 layout-id 25 for Medium Akoya p6653 by hua0512
- Added ALC235 layout-id 13 for Deskmini H470 by dumk1217
- Added ALC283 layout-id 12 for ThinkCentre M73(10AX) ALC283 by dumk1217
- Added ALC285 layout-id 88 for Yoga S740 by frozenzero123
- Fix ALC256 layout-id 67 unable to change the built-in Speaker Volume through the hotkey after unplugging the headphone by @R-a-s-c-a-l
- Fix ALC298 layout-id 11 wake data for Alienware 17 R4 by RockJesus
- Added ALC282 layout-id 30 for Soarsea S210H by Jokerman1991
- Added ALC662 layout-id 19 for MSI X79A-GD65 by @wy414012

#### [VirtualSMC 1.2.8](https://github.com/acidanthera/VirtualSMC/releases)

- Do not override CPU proximity SMC key in SMCDellSensors + minor fixes in logic

#### [FeatureUnlock 1.0.4](https://github.com/acidanthera/FeatureUnlock/releases)

- Fixed AirPlay to Mac support with macOS 12.1
- Refactored patch sets to only patch model families
- Resolved rare OS-side crashing from Sidecar patching
- Added AssetCache patch for `kern.hv_vmm_present` usage
- Disabled iPad/Sidecar exemption by default
  - Patch set does not work on devices running iOS 14 or newer
- Added additional boot-args for specific patch disabling

#### [DebugEnhancer 1.0.5](https://github.com/acidanthera/DebugEnhancer/releases)

- Support boot-arg `-dbgenhiolog` to redirect IOLog output to kernel vprintf

#### [CpuTopologySync 1.0.0](https://github.com/acidanthera/CpuTopologySync/releases)

- *Initial release 🎉*