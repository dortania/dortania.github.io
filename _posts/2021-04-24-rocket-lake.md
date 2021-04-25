---
layout: post
title:  "Intel Z590 compatibility with macOS"
date:   2021-04-24 14:45:00 -0400
categories: Hackintosh updates
---
As I mentioned earlier in the monthly release notes blogpost, over the last weeks we did a great job with @vandroiy2013 in testing Intel Z590 with Comet Lake (10th generation) and Rocket Lake (11th generation) CPUs. While our experience was generally positive it was still full of unexpected caveats and nuances, so below we tried to write a summary, while our colleagues from Dortania integrate the discovered knowledge into more complete guides. All the discoveries are logically structured into sections depending on the hardware or software part. Most things do not differ from Z490, so we skipped this stuff.

_Please keep in mind that up to the moment we tested only two ASUS motherboards and although the described issues should normally apply to the other vendors, we can neither guarantee that we spotted them all, nor say that we performed all the tests even at the boards we had at hand._

#### BIOS

The overall BIOS impression is really messy. The firmware are actively worked on, and while this continues you can expect all kind of glitches and performance loss. While the firmware has not bricked for us yet, we had numerous black screens, especially when doing performance tuning and overclocking. The good news is that firmware updates gradually provided better stability and noticeably improved performance, so we strongly advise to keep the BIOS up-to-date for the next months at the very least.

* Apple RTC checksum writes still cause firmware configuration corruption, and as a result `DisableRtcChecksum` is still needed. So far we have not observed issues on the EfiBoot level, but using `rtc-blacklist` to exclude the Apple checksum area in UEFI as well will not hurt. Just for a reminder, `AWAC` still cannot be turned off, and thus enabling `RTC` still needs an SSDT.
* GOP performance is terrible in some BIOS versions. For unknown reasons both IGPU and dGPU (multiple Polaris and Navi cards) have vey slow rendering in UEFI and XNU kernel 1st stage regardless of the CPU generation. This was mostly addressed by the firmware updates, but in our opinion verbose boot is still visually a bit slower than older boards. Fortunately it does not affect booted macOS performance anyhow.
* XMP is completely broken in early BIOS versions. In most cases the motherboard will simply not boot without a CMOS reset. BIOS updates got that fixed, yet manual overclocking does not seem to be working as stable as in Z490.
* Sometimes the firmware randomly switches the GPU slot to PCIe x8 or x1 with no software solution but with a simple replug resolving the problem. We failed to find a logical explanation, yet always checking the lane count is by all means reasonable anyway.
* PCIe 4.0 ports work just fine and deliver PCIe 4.0 speeds with newer SSDs and GPUs. However, dynamically resizable BARs are unsupported by macOS and should always be disabled.

#### CPU tuning

CPU-related things to keep in mind when booting with Z590:

* RKL requires CML `CPUID` virtualization for booting.
* Both CML and RKL CPUs are XCPM-compatible. However, stock XCPM frequency vectors will generally halve the performance, and need to be replaced with [custom ones](https://github.com/dortania/bugtracker/issues/190) through CPUFriend.
* On RKL CPUs Intel Power Gadget shows slightly incorrect frequencies and also randomly crashes macOS on S3 wake, making its installation strongly undesired.
* On ASUS boards a fairly standard Nuvoton SuperIO is installed and is thus fully supported by SMCSuperIO (e.g. fans, voltages). Each board requires a profile to interpret the values of course.

While not strictly related to macOS, very few people would use the configurations at Intel stock values, so here are some extras:

* RKL CPUs are very very hot and power-consuming. In case overclocking is done, testing normal multicore load with e.g. Cinebench and `AVX-512` with e.g. OCCT for at least half an hour each in WIndows is an absolute must. Note, that AIDA64 incorrectly reports throttling when `AVX-512` frequency lowering is in effect as of now.
* For us ASUS automatic overclocking resulted in terribly high CPU voltage (+1.5V), and we had to use negative offsetting to get adequate temperatures. The good news is that after a reasonable amount of experiments with the BIOS 4.9 GHz on all cores under `AVX-512`  should be doable by roughly any liquid cooling, even 240mm.
* Benchmark values between macOS and Windows are roughly the same as long as CPU power management functions correctly and customised frequency vectors are installed.

#### Graphics support

Since there is no sane reason to use an IGPU-inclusive Mac model with not working IGPU, CPUFriend is generally required. IM201 vectors generally fit as they provide up to 4 GHz stepping. IPG detects the CPUs and shows their temperatures and load as well.

* CML IGPU works fine without connectors as a video decoding accelerator for Polaris. Using CML IGPU exclusively will require manual connector patching. We did not test that thoroughly as IGPU-only configurations are prone to errors.
* RKL IGPU is unsupported and will likely never be. Booting with RKL IGPU enabled with or without connectors results in boot failure (black screen). Can be disabled by WEG in macOS exclusively through injecting `disable-gpu` into an `IGPU` device. This can let other systems use IGPU acceleration to off-load tasks.
* DRM support (both streaming and purchased media) will not work with any IGPU, but will work fine with IMP11 or MP71 Mac models and a dGPU (e.g. Polaris, Navi).

#### Audio support

There are two board types in regards to sound support:
1. Standard Realtek HDA based boards (commonly ALC889 and ALC1220).
2. Realtek USB audio based boards (commonly ALC4080 and ALC4082).

For the first type the solution is to use AppleALC to patch AppleHDA as usual. Surprisingly, depending on the CPU different audio controller ID is provided: 0xF0C8 for CML and 0x43C8 RKL. We have no idea why that happens since HDA controller is a part of the chipset, but hopefully these two identifiers are all we will face. Both are present in the latest AppleALC release. We tested speakers, phones, and a microphone on ALC889 and observed no issues.

For the second type no patching is required, but AppleALC is still necessary for digital audio support (HDMI, DP). Automatic device switching and S/PDIF works without issues as well. By default USB audio will cause macOS to immediately wake after sleep. The fix is explained in the USB section below.

#### USB support

The amount of USB ports does not fit the 26 port limit (2.0 + 3.x) just as usual. Without the plist-only kext describing every USB port in most cases even the basic macOS Installer will be uncontrollable through the mouse and keyboard regardless of the port limit quirks. To workaround it creating a plist-only kext with just the first 26 USB 2.0 and USB 3.x devices is highly recommended. Such an action should be enough to get the mouse, the keyboard, and the USB media work in at least some ports to perform the installation and configure all the devices properly.

To workaround this immediate S3 wake issue caused the audio controller the USB port it is connected to (commonly `HS02` on ASUS, yet can easily be found in the I/O Registry) needs to be given an internal type via the USB port plist kext (`UsbConnector` → `255`). Afterwards the board should sleep just fine. To resolve the issue with USB wake not lighting the screen [USBWakeFixup](https://github.com/osy/USBWakeFixup) is still needed.

We are yet to test the current levels produced by the ports, but charging the devices works fine at the very least. So far no disconnections across the S3 sleep-wake cycles were spotted. Broadcom Bluetooth from BCM94360CS2 connected to the NGFF slot can be controlled from BIOS and works natively. This actually is an improvement as on Z390 and Z490 boards with the Broadcom combo modules we only had Wi-Fi working from the NGFF slot and not the Bluetooth.

#### Networking

Most boards come with either 1 Gbps or 2.5 Gbps Intel LAN. The former works with IntelMausi and the latter works out of the box with AppleIntelI210Ethernet but requires a `device-id` injection of `<F2150000>` and a kext patch. This is all the same as with the CML boards. Additionally, with macOS 11.4 Beta 1, Apple has opened up AppleIntelI210Ethernet to supporting a larger array of devices including the i225-V NIC found on most higher end boards. This requires no `device-id` injection or kext patch. For 11.3 and older, see below kernel patch:

```
Base:       __Z18e1000_set_mac_typeP8e1000_hw
Find:       F2150000
Replace:    F3150000
Identifier: com.apple.driver.AppleIntelI210Ethernet
```

The preinstalled Wi-Fi cards (Intel AX210) are generally not (yet) compatible with OpenIntelWireless and need to be replaced. The amount of space behind the cover does not let using an Apple original module in the NGFF slot with higher-end boards, but one should be able to fit the BCM94360NG or some others. The use of non-original modules is a trial and error as usual, unfortunately.

#### Power cycle

* ACPI S3 (sleep) works just fine, but requires some effort with the USB stack as described above. This is especially true when USB audio is used. Interestingly Polaris wake up issues in combination with LG 4K HDR screens common on older boards are back. With Z590 it may be required to power the screen before wake. Otherwise replug or programmatic input switch may be needed to avoid black screen after wake.
* ACPI S4 (hibernation) is a no go. For us the firmware simply did not POST after waking from S4. We observed black screen and OpenCore was not reached up until two hard reboots with a normal boot to follow.
* Authenticated restart and seamless update installation work fine with (and without) File Vault 2 full disk encryption. RTC patches are needed, at least for ASUS.

#### Conclusion

Our overall impression with Z590 is mixed, but so far we have not found any issues that we could not resolve or at least workaround, maybe except the RKL IGPU drivers. We are yet to test special things, like Intel Thunderbolt controller, but despite no firmware patches as of yet, there exist reports with storage devices working without too much hassle almost out of the box. All our products were updated to provide basic support and the whole standard operating system range (macOS, Windows, and Linux) work fine.

———Vit