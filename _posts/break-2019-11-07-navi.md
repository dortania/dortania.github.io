---
layout: post
title:  "Radeon RX 5500 and 5500M support in 10.15.2 Beta 1"
date:   2019-11-07 7:00:00 -0600
categories: Hackintosh updates
---
 Well look at that, more Navi support in macOS. Though hopefully the installer screen has also been fixed for Navi GPUs, and quick reminder that users who experience black screen on Navi should add the boot flag `agdpmod=pikera` and have WEG version 1.3.4

 To check yourself, CD into S/L/E:

     grep -ir "7340" .

 PCI ID's can be found [here](https://pci-ids.ucw.cz/read/PC/1002)

 Edit: Well apparently we also got Navi 12 support hidden in there!
