# Distro Overview

A **distribution** (commonly shortened to **distro**) can be though of as a "flavor" of GNU/Linux. While all GNU/Linux distros, by definition, use Linux as a kernel, they may differ in installation processes, prepackaged software, release model, and many other things. Some distros are better suited for some purposes than others. **This is an overview of common GNU/Linux distros. This is not a complete list of all GNU/Linux distros.**

**Contents:**
1. Arch Linux
2. Red Hat Enterprise Linux
3. Fedora Linux
4. Debian Linux
5. Ubuntu Linux
6. Pop!\_OS
7. Kali Linux
8. elementaryOS

## Arch Linux

(I use Arch btw.)

[Website](https://www.archlinux.org/)

Arch Linux is a distribution of Linux known for its **minimalism, simplicity, and rolling release model.**

By default, Arch Linux does not come with a prepackaged window manager or desktop environment. In fact, **it comes with only the minimum amount of prepackaged software.** This allows Arch Linux to be minimalistic, simplistic, versatile, free of bloat, and be tailored by each user for their own usage. **Arch Linux is not typically recommended for beginners.**

Arch Linux operates on a rolling release model. This means that the latest updates are always available to the user to be installed *at their own discretion.* By default, packages are managed using pacman (package manager) and can be installed from either the official Arch Linux Repositories or from the Arch User Repositories.

**Arch Linux excels most at being a personal operating system for GNU/Linux users who want to tailor their operating system for their own tastes and purposes.**

## Red Hat Enterprise Linux

[Website](https://www.redhat.com/en/technologies/linux-platforms/enterprise-linux)

Red Hat Enterprise Linux (aka RHEL) is a distribution of Linux known for being **commercially viable.**

RHEL is supported by Red Hat, Inc. and is much more suited to enterprise applications that require commercial support, stability, security, and readiness for mass deployment in commercial environments. RHEL is much more prevalent in servers, mainframes, supercomputers, and workstations.

RHEL operates on a version release model, meaning that versions are packaged, tested, and shipped out to users. Packages are managed using RPM (RPM Package Manager). 

**RHEL excels most in commercial environments and is not meant to be a personal desktop operating system for the average Joe.**

## Fedora Linux

[Website](https://getfedora.org/)

Fedora is a distribution of Linux similar to RHEL but is much more **community-focused and tailored to regular, non-enterprise users.**

Different editions of Fedora exist that tailor to desktops, servers, and cloud computing devices. Fedora is also supported by Red Hat through their sponsorship of the Fedora Project, but is again much more tailored to regular users than RHEL. By default, Fedora uses a GNOME desktop environment.

Fedora operates on a version release model similar to RHEL. Packages are also managed using RPM.

**Fedora excels most in personal desktop environments for users who are already comfortable using Linux.**

## Debian Linux

[Website](https://www.debian.org/)

Debian Linux is a distribution of Linux known for **free/libre and open source software and stability.**

Debian is tailored to both desktops and servers. The project is supported by the community-driven Debian Project. There are many other distributions of Linux that are based off of Debian. By default, Debian uses GNOME or KDE as desktop environments.

Debian operates on a version release model and packages are managed using dpkg (Debian package) and APT (Advanced Package Tool).

**Debian excels most in personal desktop environments for users who are already comfortable using Linux.**

## Ubuntu Linux

[Website](https://ubuntu.com/)

Ubuntu is perhaps the most popular and well known distribution of Linux known for **user-friendliness and working out of the box.**

Ubuntu is supported by Canonical has editions tailored to desktops, servers, and IoT devices. There are both infrequent long-term support (LTS) versions and frequent non-LTS versions available. By default, Ubuntu uses GNOME as a desktop environment.

Ubuntu operates on a version release model. Ubuntu is based on Debian and as such, also uses dpkg/APT to manage packages.

**Ubuntu excels most in personal/server environments for users who are looking for a user-friendly, simple, and easy Linux experience.**

## Pop!\_OS

[Website](https://pop.system76.com/)

Pop!\_OS is a younger Linux distribution known for **user-friendliness, working out of the box, and being tailored towards makers.**

Pop!\_OS is supported by System76, a respected manufacturer of Linux machines. It is built on top of Ubuntu and is also on a similar version system in which they release LTS versions of their OS as well as non-LTS versions of their OS. By default, they also use GNOME as a desktop environment.

The distribution operates on a version release model. It uses dpkg/APT to manage packages.

**Pop!\_OS excels most as a personal operating system for users who may want all of the features and qualities of Ubuntu, but also use their computer create and make things.**

## Kali Linux

[Website](https://www.kali.org/)

Kali Linux is a Debian-based distribution of Linux tailored towards **digital forensics and penetration testing.**

Kali Linux is supported by Offensive Security, a reputable and respected company specializing in computer security and training, well known for being the authority behind the OSCP certification. It is **prepackaged with a wide array of common tools used in security.** Kali Linux is a special operating system in that **Kali is not meant to be installed.** Instead, users are encouraged to flash a Kali Linux image onto a USB drive or set up a virtual machine, and then use Kali Linux inside of a live environment. By default, XFCE is used as the default desktop environment.

The distribution operates on a version release model and uses dpkg/APT to manage packages.

**Kali Linux excels most in security environments for professionals and is not meant to be used as a daily driver. Kali Linux is meant to be run as a live or virtual operating system.**

## elementaryOS

[Website](https://elementary.io/)

elementaryOS is an Ubuntu-based distribution of Linux known for **user-friendliness, working out of the box, and low learning curve.**

elementaryOS is supported by Elementary, Inc. and is tailored towards personal desktops as a user-friendly operating system. It uses Pantheon as the default desktop environment and is often times compared to MacOS in terms of aesthetic appeal

The distribution operates on a long-term support model and uses dpkg/APT to manage packages.

**elementaryOS excels most in personal desktop environments for non-technical users who want to use a Linux operating system while having the lowest possible learning curve.**

## Conclusion

This was just an overview of common Linux distributions. Ultimately, it actually doesn't matter what distribution you choose as long as you're comfortable with it. There's a great video by Luke Smith called *"How to choose a Linux distro: Stop Thinking!"* that you can check out [here](https://www.youtube.com/watch?v=3zpgQpdy_fI).

For beginners, it is recommended that you use Linux inside of a virtual machine before committing to a single or dual boot installation of Linux. Some distributions of Linux have steeper learning curves than others, and a virtual machine can allow you to make mistakes in controlled, safe, and reversible environment.

After choosing and installing a Linux distribution, it may be desirable for you to start learning how to interact with the system via the command line interface.
