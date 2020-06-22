---
layout: post
title:  "macOS Big Sur has been revealed!"
date:   2020-06-22 9:00:00 -0600
categories: Hackintosh updates
---

So today at WWDC Apple unveiled the next version of macOS, macOS 10.16 Big Sur!

## The major thing on your mind

ARM Macs have been dropped.

## Prerequisites:

* Running OpenCore
   * Clover *may* get support but not out of the box, the reason OpenCore works is that its prelinker is OS agnostic, and any built-in patches
* `-lilubetaall` in boot-args
   * Reason for this is Lilu does not support beta versions of macOS out of the box, this means we need to both force Lilu and all its plugin's to load. That's where this boot argument comes in
   * Lilu will likely be updated in the coming weeks to support 10.16 natively
* 16GB USB drive
   * Apple's been slowly growing the installer files
* macOS 10.16 installer, couple ways to get this:
   * gibMacOS and select `4. developer`
      * Once downloaded, run `BuildmacOSInstallApp.command` as our installer will be in pieces
      * After that's finished, move the installer into your applications folder to make running the next step a bit easier
   * Install the `macOS Developer Beta Access Utility` then download
      * once installed, you'll notice a new update in System Preferences -> Software Update

## Preparing the installer

Next you'll want to format the USB as follows:
* Name: MyVolume
* Format: Mac OS Extended (HFS+)
* Scheme: GUID Partition map

Once this is done, next open up terminal and run the following:

```
sudo /Applications/Install\ macOS\ 10.16\ Beta.app/Contents/Resources/createinstallmedia --volume /Volumes/MyVolume
```

## Preparing our boot drive

Something you should never do is install a developer beta on-top of your existing install, unless you're ok with crying for a couple days. Luckily APFS has a neat feature to add dynamic volumes making partitioning much easier, where you don't need to specify a certain size and can easily remove them:

![](/images/posts/2020-06-08/disk-utility.png)

## QnA

> Kexts were removed for macOS, will this finally kill hackintoshes?

No this won't kill hackintoshes, but lets go over what is exactly happening to better understand where we need to worry:

* 3rd party kexts will be moved from kernel to user space
* Apple will still have kexts for their own use
* Library/Extensions is likely to be removed

So with this info, we'll need to establish some things on how both macOS and the rootkits we use to boot on PC hardware work:

* macOS has a bundle of kexts called the prelinked kernel, this is what every mac requires to boot macOS
* OpenCore uses this prelinked kernel to inject kexts
* Clover on the other hand uses ancient XNU code that's no longer used in macOS since 10.7, it's more than likely this code will be removed as Apple removes SLE/LE

