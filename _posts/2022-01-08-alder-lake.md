---
layout: post
title: "Intel Z690 compatibility with macOS"
date: 2022-01-08 19:30:00 -0500
categories: Hackintosh updates
---
Last year, when I presented the Z590 nuances here on Dortania ([main paper](https://dortania.github.io/hackintosh/updates/2021/04/24/rocket-lake.html), [amendments](https://dortania.github.io/hackintosh/updates/2021/06/07/acidanthera-june.html), [sample configuration](https://github.com/dortania/bugtracker/issues/221)), I was rather worried that with the introduction of Intel Z690 architecture we will be out of luck. Today I am confident that it is not the case. While it is far from perfect and while it is harder to make Alder Lake run on the kernel side, after several days of experiments with @vandroiy2013 we were able to make it. Here comes what one needs to be aware of when building a Z690-based setup. As usual, the previous knowledge of Z490 and Z590 still applies, and I strongly advise you to acquaint yourself with these platforms first.

_Please keep in mind that up to this moment we have only tested one ASUS motherboard and although the described issues should normally apply to the other vendors, we can neither guarantee that we spotted them all, nor say that we performed all the tests even with the board we had at hand._

#### BIOS

Given that we waited a bit longer for a news post this time, Alder Lake firmware were updated to be more acceptable.

- Apple RTC issues are finally resolved at least in ASUS boards. While one still obviously needs an AWAC SSDT table, `DisableRtcChecksum` or `RTCMemoryFixup.kext` are no longer required.
- CFG Lock may not be configurable in preferences on ASUS boards. This is an obvious BIOS bug, although it may not cause boot failures. We had to unlock it manually through the Shell method described in OpenCore Reference Manual. Unlocking with ControlMsrE2 was unsuccessful, but we did not investigate it much.
- XMP works at least with DDR5 we had at hand, but there were reports of no issues with DDR4 as well. While macOS does not name DDR5 as DDR5 in the profiler, this nuance is purely cosmetic.
- We did not have PCIe 5.0 hardware to ensure optimal performance, but there were no issues with PCIe 4.0 and 3.0 including Resize Bar support handled by the `ResizeAppleGpuBars` quirk.
- We did not have native Thunderbolt support in our board, but Z690 Thunderbolt firmware is also part of the main firmware, and thus can hardly be modified. Flashed PCIe cards should work fine though.
- ASUS boards have a new aggregate GOP instance, which causes black screen during macOS first stage. This is addressed in the `ProvideConsoleGop` quirk starting with OpenCore 0.7.6.
- Most firmware dropped `Processor`-based CPU definition in ACPI and switched to `Device`-based definition, which is not recognised by macOS. To workaround this one needs to use the `SSDT-PLUG-ALT` ACPI table.

#### CPU tuning

Unlike the previous generation, only Alder Lake CPUs are supported in Z690 boards. Furthermore, the new CPUs utilise a heterogenous architecture, similarly to [big.LITTLE](https://en.wikipedia.org/wiki/ARM_big.LITTLE) found in ARM. There is a trade-off between using different core kinds and getting better multicore performance and sticking with performance cores. In case you enable the efficiency cores be aware: 
- All cores are to support the same instruction set on x86, which means AVX-512 is disabled.
- Ring bus frequency is lowered to match the efficiency cores (3.6 vs 5.0), which slowdowns the overall performance.
- XNU scheduler does not distinguish core types in macOS and will work no better than current Windows 10 in terms of core assignment.
- More patches are required for XNU when using the efficiency cores, though handled automatically by the `ProvideCurrentCpuInfo` quirk starting with OpenCore 0.7.7.
- Enabling the efficiency cores will require [RestrictEvents](https://github.com/acidanthera/RestrictEvents) CPU name spoofing functionality due to large core count.

As for the issues not related to the hybrid architecture:

- Alder Lake CPUs also require `CPUID` virtualisation to boot.
- Partial XCPM compatibility is available, but frequency vector tuning will be [required](https://github.com/dortania/bugtracker/issues/190).
- Thermal management works. While Intel Power Gadget is rather buggy and not recommended in production, it mostly works, so do SuperIO and SMCProcessor.

#### Audio and graphics

Just like Z590, Z690 boards support USB and analog audio. Analog audio patches were contributed by @R-a-s-c-a-l and are present starting with AppleALC 1.6.7. USB audio is supported by AppleALCU out of the box. Please note that USB audio may need separate firmware updates provided by the motherboard vendor (like on ASUS Z590 series, which initially had sporadic crackling noise).

Builtin IGPU is not supported by macOS starting with Rocket Lake. In case it is needed for other operating systems, it is recommended to disable it with `class-code` = `<FF FF FF FF>`. This applies to all uses of `disable-gpu`, which has been proven to be unreliable. One can also disable it in firmware preferences. Discrete GPUs are supported without any limitations including DRM and digital audio.

#### USB

No change from Z590:

- Needs usual care with port mapping to get working sleep support.
- [USBWakeFixup](https://github.com/osy/USBWakeFixup) is needed to fix keyboard wakeup support, but may cause [compatibility issues](https://github.com/osy/USBWakeFixup/issues/14) with Bluetooth.
- Overclocking RAM is known to cause USB issues, but we were unable to spot anything negative with XMP so far.

#### Networking and wireless

- Intel 2.5 Gbps adapters work out of the box through the DEXT drivers at least on ASUS boards.
- Intel Wi-Fi works with AirportItlwm, but we had wake-up issues at the time we tested it. The issue is tracked [here](https://github.com/OpenIntelWireless/itlwm/issues/519).
- Intel Bluetooth works with IntelBluetoothFirmware in macOS 11, but may not be functional in macOS 12. The issue is tracked [here](https://github.com/OpenIntelWireless/IntelBluetoothFirmware/issues/369).

As usual we recommend replacing Intel wireless modules with Apple ones whenever possible.

#### Miscellaneous 

No change from Z590:

- S3 support works fine.
- FileVault 2 authenticated restart works fine.

To summarise, Intel Z690 looks like a solid upgrade which brings better performance per watt. We can still run macOS on it with acceptable efficacy.

— Vit
