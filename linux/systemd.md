# systemd

**systemd is a software suite that provides system and service managers for Linux systems.** Most Linux distributions today use systemd as a modern replacement for the older init system. systemd has been criticized for being too monolithic and in violation of the UNIX philosophy, but has also received praise for its low learning curve and ease of usage and management. Understanding systemd is important for effectively managing a modern Linux system.

## Overview

systemd contains many features. Only a handful of these features are of concern to regular users.

**systemctl** is a command-line utility that can be used to control the systemd system and service manager. **journalctl** is a command-line utility that can be used to access systemd logs. **Services** are managed by systemd and are applications and programs running in the background of a system. There are many more features of systemd that are not covered in a basic-level article such as this one.

## systemctl

As mentioned earlier, **systemctl can be used to control the systemd system and service manager.**

To **list running units**, run `systemctl` without any additional arguments.

```
$ systemctl
```

To **list failed units**, pass the `--failed` flag.

```
$ systemctl --failed
```

To **list all units**, pass the `--all` flag.

```
$ systemctl --all
```

To **view the status of the system**, pass the `status` option.

```
$ systemctl status
```

If you'd like to **view the status of a particular unit**, pass the `status` option as well as the name of the unit in question.

```
$ systemctl status <unit>
```

For example:

```
$ systemctl status sshd
```

In addition to displaying information about the system and services, `systemctl` can also be used to manage them. There are four main operations that can be done to a particular unit: start, enable, stop, and disable. While start/stop and enable/disable may sound similar, they are in fact different.

**Start** does exactly what it sounds like it does: it starts a unit. This unit will then run as expected. **Stop** is the opposite of start. It will stop a unit from running.

**Enable** may *seem* similar to start, but it is in fact different. Enable does not start a unit right away and does not spawn a daemon process. Enable merely marks a unit to start the next time its specified hook is met, whether this be at boot, sleep, or anything else supported by systemd. **Disable** is the opposite of enable. It will mark the unit to *not* start the next time its specified hook is met.

To start, stop, enable, or disable, pass either the `start`, `stop`, `enable`, or `disable` option as well as the unit in question.

```
# systemctl start <unit>
# systemctl stop <unit>
# systemctl enable <unit>
# systemctl disable <unit>
```

For example:

```
# systemctl start sshd
# systemctl stop sshd
# systemctl enable sshd
# systemctl disable sshd
```

This article covers creating custom units later on which can also be managed with systemctl using these same commands.

## journalctl

As mentioned earlier, **journalctl can be used to access systemd logs.**

To **view all logs**, run `journalctl` with no additional parameters.

```
$ journalctl
```

To **follow logs** as they come in, pass the `-f` flag.

```
$ journalctl -f
```

To **view logs from a particular PID**, you can pass an argument into the `_PID` parameter.

```
$ journalctl _PID=<PID>
```

For example:

```
$ journalctl _PID=1231
```

To **view logs from a particular ID**, you can pass an argument into the `_UID` parameter.

```
$ journalctl _UID=<ID>
```

For example:

```
$ journalctl _UID=1000
```

To **view logs from a particular program**, you can specify the path to the executable.

```
$ journalctl <path>
```

For example:

```
$ journalctl /bin/sh
```

To **view logs specifically from the kernel**, pass the `-k` flag.

```
$ journalctl -k
```

To **view logs specifically related to boot**, pass the `-b` flag.

```
$ journalctl -b
```

As usual, there is a lot more functionality to `journalctl` that isn't covered here. The `man` page of `journalctl` may be worth a read if you're interested in what more `journalctl` is capable of.

## Services

**Services** are one type of unit offered under systemd. **Services are applications and programs that can run in the background of a system.** For example, a web server like nginx can be a service that is managed by systemd using the systemctl commands covered earlier in this article.

You can also create your own custom services that can be managed by systemd. Service files should be placed in the `/etc/systemd/system/` directory and should have the extension `.service`.

The basic syntax of a service is:

```
[Unit]
Description=<DESCRIPTION>

[Service]
ExecStart=<COMMAND>

[Install]
WantedBy=<TARGET>
```

The `<TARGET>` can be thought of as the hook sought after by `systemctl enable`. For most services that hook to boot, `<TARGET>` is most commonly `multi-user.target`. For a full list of available targets, run:

```
$ systemctl list-units --type=target --all
```

After writing a service file, it can be managed using its filename just like any other systemd service.

For example, the following is a custom service file called `myService.service` that runs `myProgram` located at `/usr/local/bin/myProgram` and hooks onto `multi-user.target`.

```
[Unit]
Description=Run myProgram whenever starting up the system.

[Service]
ExecStart=/usr/local/bin/myProgram

[Install]
WantedBy=multi-user.target
```

It can then be enabled and started using systemctl.

```
# systemctl enable myService
# systemctl start myService
```

Services are an incredibly useful feature of systemd that allows you to automate just about everything on a system.
