---
layout: post
title:  "NVRAM for all! 300 series users rejoice!"
date:   2020-01-20 7:00:00 -0600
categories: Hackintosh updates
---

So in the latest commit of OpenCorePkg, a new SSDT was added: [SSDT-PMC.dsl](https://github.com/acidanthera/OpenCorePkg/blob/master/Docs/AcpiSamples/SSDT-PMC.dsl).
What this SSDT does is bring back NVRAM for B360, B365, H310, H370, Z390, but why the hell did we have broken NVRAM to start with?

Well quite simple, Intel "forgot" to actually declare the FW chip as MMIO in ACPI and so XNU will ignore the MMIO region declared by the UEFI memory map. And so NVRAM SMM page fault'ed on unmapped page access, oh what fun!

>    So how do I use this SSDT?

Honestly quite simple, it requires no configuration and is plug-and-play. Plus its not tied to OpenCore, Clover users can run this as well. Do note that it requires LPCB in your `DSDT` but this is super common on Z390, you can verify by searching for `PCI0.LPCB`.

To compile in macOS:

* Grab [MaciASL](https://github.com/acidanthera/MaciASL/releases)
* Open the SSDT, `File -> Save As -> ACPI Machine Language`

To compile in Windows:

* Grab iasl: [Windows](https://acpica.org/sites/acpica/files/iasl-win-20180105.zip)
* Open Command Prompt and run: `path/to/iasl.exe path/to/SSDT-PMC.dsl`

To compile in Linux:

* Grab iasl: [Linux](http://amdosx.kellynet.nl/iasl.zip)
* Open Terminal and run: `path/to/iasl path/to/SSDT-PMC.dsl`

Once the file is compiled, you'll get the SSDT-PMC.**aml**. The extension is important as that's the compiled version, .dsl is just source code. Once you have the SSDT made, drop this into either EFI/CLOVER/ACPI/patched or EFI/OC/ACPI(remember to add it to the config as well if you run OpenCore)

For the lazy, I'll leave a precompiled file here: [SSDT-PMC.aml](https://github.com/khronokernel/Opencore-Vanilla-Desktop-Guide/blob/master/extra-files/SSDT-PMC.aml)

>    How do I get rid of my NVRAM emulation

Well Clover would like to give a quick "fuck you" first if you installed RC scripts, as you may need to mount Catalina as R/W with SIP off before you can even clean up its mess. What garbage do you need to clean? Well see the following:

* `/Volumes/EFI/EFI/CLOVER/drivers/UEFI/EmuVariableUefi-64.efi`
* `/Volumes/EFI/nvram.plist`
* `/etc/rc.clover.lib`
* `/etc/rc.boot.d/10.save_and_rotate_boot_log.local`
* `/etc/rc.boot.d/20.mount_ESP.local`
* `/etc/rc.boot.d/70.disable_sleep_proxy_client.local.disabled`
* `/etc/rc.shutdown.d/80.save_nvram_plist.local​`


For OpenCore users, all you need is to disable the following in your config:

* `Booter -> DisableVariableWrite -> False`
* `NVRAM -> LegacyEnable -> False`

And don't forget to delete the nvram.plist on the root of your EFI

>    How do I test if my NVRAM works?

Open up terminal and paste one line at a time:


    sudo -s
    sudo nvram -c 
    sudo nvram myvar=test
    exit


Then reboot and run this:

    nvram -p | grep -i myvar


If nothing returns then your NVRAM is not working. If a line containing `myvar test` returns, your NVRAM is working.

Note: `nvram -c` requires SIP to be off, an alternative is to wipe NVRAM at the boot menu. For clover, press F11. For OpenCore, select `CleanNvram`, reminder you'll need `Misc -> Security -> AllowNvramReset -> YES`.
