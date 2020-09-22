---
layout: post
title:  "What's new in macOS 11, Big Sur!"
date:   2020-09-15 7:00:00 -0600
categories: Hackintosh updates
---

* What has changed on the surface
  * A whole new iOS-like UI
  * macOS Snapshotting
  
* What has changed under the hood
  * New kext cache system: KernelCollections!

* What’s new in the Hackintosh scene?
  * Dortania: a new Organization has appeared

It's that time of year again, and we've got a new version of macOS on our hands! This year we've finally jumped of the 10.xx naming scheme and now going to 11! And with, a lot has changed under the hood in macOS.

As with [previous years](https://dortania.github.io/hackintosh/updates/2019/10/07/catalina.html), we'll be going over what's changed in macOS and what you should be aware of.

# What has changed on the surface

## A whole new iOS-like UI

Love it or hate it, we've got a new UI more reminiscent of iOS 14 with hints of skeuomorphism as a call back to previous mac UIs which have subtle details in the icons

## macOS Snapshotting

A feature initially baked into APFS back in 2017 with the release of macOS 10.13, High Sierra, now macOS's main System volume has become both read-only and snapshotted. What this means is:

* 3rd parties have a much more difficult time modifying the system volume, allowing for greater security
* OS updates can now be installed while you're using the OS, similar to how iOS handles updates
* Time Machine can now more easily perform back ups, without file inconsistencies with HFS Plus while you were using the machines

However there are a few things to note with this new enforcement of snapshotting:

* OS snapshots are not calculated as used space, instead being labeled as purgeable space
* Disabling macOS snapshots for the root volume with break software updates, and can corrupt data if one is applied


# What has changed under the hood

Quite a few things actually! Both in good and bad ways unfortunately.


## New Kernel Cache system: KernelCollections!

So for the past 9 years, macOS has been using the Prelinked Kernel as a form of Kernel and Kext caching. And with macOS Big Sur's new Read-only, snapshot based system volume, a new version of caching has be developed: KernelCollections!

How this differs to previous OSes:

* Kexts can no longer be hot-loaded, instead requiring a reboot to load with `kmutil`
* The Secure Boot and standard kernel are now one(ie. no more Immutable Kernel)
* Symbols are no longer required

The last point is the most important part, as this is what we use for kext injection in OpenCore. Currently Apple has left symbols in place seemingly for debugging purposes however this is a bit worrying as Apple could outright remove symbols in later versions of macOS.







# What’s new in the Hackintosh scene?

## Dortania: a new Organization has appeared

As many of you have probably noticed, a new Organization focusing on documenting the hackintoshing process has appeared. Originally under my alias, Khronokernel, I started to transition my guides over to this new family as a way to concentrate the vast amount of information around hackintoshes to both ease users and give a single trusted source for information. 

We work quite closely with the community and developers to ensure information's correct, up-to-date and of the best standards. While not perfect in every way, we hope to be the go-to resource for reliable hackintosh information.

And for the times our information is either outdated, missing context or generally needs improving, we have our bug tracker to allow the community to more easily bring attention to issues and speak directly with the authors:

* [Dortania's Bugtracker](https://github.com/dortania/bugtracker)


