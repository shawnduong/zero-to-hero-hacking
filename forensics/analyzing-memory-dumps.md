# Analyzing Memory Dumps

A **memory dump** is a copy of a system's computer memory at a particular time. Memory dumps are incredibly useful for analyzing the state of a system and can be used to detect malware, discover running processes, detect network connections, and discover many other key pieces of information that may be valuable to a digital forensics investigation.

Memory dumps may range in size depending on the region or regions of memory included in the dump. The most common memory dumps found in digital forensics investigations are usually **complete memory dumps**, which include *all* the memory being used by a system. Besides a complete memory dump, another type of memory dump is a **kernel memory dump**, which are similar to complete memory dumps *except* for the fact that they *exclude* user applications.

## Types of Information

Learning how to analyze memory dumps may give an investigator access to a variety of information, including (but not limited to):
- The operating system and version.
- Running programs and processes.
- Data stored in the clipboard.
- Data belonging to currently active programs.
- Data belonging to the filesystem itself.
- A rough sketch of the desktop at the time of capture.
- A list of active network connections.

## Analyzing a Memory Dump with Volatility

[Volatility](https://www.volatilityfoundation.org/) is an open source memory forensics framework that is known for being immensely powerful, thorough, and reliable. It can be interacted with through the command line and comes with many tools pre-packaged.

The sample memory dump used in this article is [joshua1.vmem](https://web.archive.org/web/20150110164058/https://dl.dropboxusercontent.com/u/55819714/joshua1.zip). Credits to Jesse Kornblum.

The most basic syntax for Volatility is:

```
$ volatility -f <dump> <action>
```

Let's start off by discovering some basic information about this memory dump. We can do this using the `imageinfo` option.

```
$ volatility -f joshua1.vmem imageinfo
Volatility Foundation Volatility Framework 2.6.1
INFO    : volatility.debug    : Determining profile based on KDBG search...
          Suggested Profile(s) : Win7SP1x64, Win7SP0x64, Win2008R2SP0x64, Win2008R2SP1x64_24000, Win2008R2SP1x64_23418, Win2008R2SP1x64, Win7SP1x64_24000, Win7SP1x64_23418
                     AS Layer1 : WindowsAMD64PagedMemory (Kernel AS)
                     AS Layer2 : FileAddressSpace (/home/skat/dl/joshua1.vmem)
                      PAE type : No PAE
                           DTB : 0x187000L
                          KDBG : 0xf8000283f0a0L
          Number of Processors : 4
     Image Type (Service Pack) : 1
                KPCR for CPU 0 : 0xfffff80002840d00L
                KPCR for CPU 1 : 0xfffff880009ea000L
                KPCR for CPU 2 : 0xfffff88003164000L
                KPCR for CPU 3 : 0xfffff880031d5000L
             KUSER_SHARED_DATA : 0xfffff78000000000L
           Image date and time : 2013-03-23 02:08:37 UTC+0000
     Image local date and time : 2013-03-22 19:08:37 -0700
```

Based off of this, we can estimate that it's almost certainly a Windows system. The image was taken 2013-03-23 at 02:08:37 UTC+0. Volatility also suggests some profiles to us, which will be very important for the steps to follow. Digital forensics tools may approach the same problem in different ways to account for differences in operating systems. Specifying a profile helps Volatility account for these differences and adjust accordingly.

From here on out, we can get much more accurate results by specifying the profile by setting the `--profile` parameter.

```
$ volatility --profile=<profile> -f <dump> <action>
```

Let's advance in our investigation now and try to get a list of all processes by using the `pslist` option.

(The following output is cropped for the sake of this article.)

```
$ volatility --profile=Win7SP1x64 -f joshua1.vmem pslist
Volatility Foundation Volatility Framework 2.6.1
Offset(V)          Name                    PID   PPID   Thds     Hnds   Sess  Wow64 Start                          Exit                          
------------------ -------------------- ------ ------ ------ -------- ------ ------ ------------------------------ ------------------------------
0xfffffa8000c9fb30 System                    4      0     97      535 ------      0 2013-03-23 01:59:42 UTC+0000                                 
0xfffffa8001d89b30 smss.exe                248      4      2       32 ------      0 2013-03-23 01:59:42 UTC+0000                                 
0xfffffa80029f8b30 csrss.exe               344    336      9      425      0      0 2013-03-23 01:59:52 UTC+0000                                 
0xfffffa8002a4eb30 csrss.exe               380    372      8      117      1      0 2013-03-23 02:00:05 UTC+0000                                 
0xfffffa8002a54b30 wininit.exe             388    336      3       80      0      0 2013-03-23 02:00:05 UTC+0000                                 
0xfffffa8002a66b30 winlogon.exe            416    372      6      130      1      0 2013-03-23 02:00:05 UTC+0000                                 
...
```

Since this is just a sample memory dump, there's not many exciting things going on. We can also see the process list as a tree using the `pstree` option.

(The following output is cropped for the sake of this article.)

```
$ volatility --profile=Win7SP1x64 -f joshua1.vmem pstree
Volatility Foundation Volatility Framework 2.6.1
Name                                                  Pid   PPid   Thds   Hnds Time
-------------------------------------------------- ------ ------ ------ ------ ----
 0xfffffa8002a54b30:wininit.exe                       388    336      3     80 2013-03-23 02:00:05 UTC+0000
. 0xfffffa8002ae8b30:services.exe                     476    388     13    227 2013-03-23 02:00:13 UTC+0000
.. 0xfffffa8001e41730:svchost.exe                     904    476     15    312 2013-03-23 02:00:49 UTC+0000
... 0xfffffa8002e9bb30:dwm.exe                        956    904      4     76 2013-03-23 02:05:57 UTC+0000
.. 0xfffffa8002112b30:taskhost.exe                   2400    476     10    172 2013-03-23 02:07:34 UTC+0000
.. 0xfffffa8000c637d0:svchost.exe                     788    476     16    311 2013-03-23 02:02:32 UTC+0000
...
```

If we're analyzing a memory dump of a machine known or suspected to have malware, it may be worth checking out `malfind`. While `malfind` usually has a high false positive rate, it's still worth checking out in order to be as thorough as possible with our investigation.

(The following output is cropped for the sake of this article.)

```
$ volatility --profile=Win7SP1x64 -f joshua1.vmem malfind
Volatility Foundation Volatility Framework 2.6.1
Process: svchost.exe Pid: 1100 Address: 0x2770000
Vad Tag: VadS Protection: PAGE_EXECUTE_READWRITE
Flags: CommitCharge: 128, MemCommit: 1, PrivateMemory: 1, Protection: 6

0x02770000  20 00 00 00 e0 ff 07 00 0c 00 00 00 01 00 05 00   ................
0x02770010  00 42 00 50 00 30 00 70 00 60 00 00 00 00 00 00   .B.P.0.p.`......
0x02770020  48 8b 45 28 c7 00 00 00 00 00 c7 40 04 00 00 00   H.E(.......@....
0x02770030  00 48 8b 45 28 48 8d 40 08 48 89 c2 48 8b 45 20   .H.E(H.@.H..H.E.

0x02770000 2000             AND [EAX], AL
0x02770002 0000             ADD [EAX], AL
0x02770004 e0ff             LOOPNZ 0x2770005
0x02770006 07               POP ES
0x02770007 000c00           ADD [EAX+EAX], CL
0x0277000a 0000             ADD [EAX], AL
0x0277000c 0100             ADD [EAX], EAX
0x0277000e 0500004200       ADD EAX, 0x420000
0x02770013 50               PUSH EAX
...
```

Something that's really great if we're taking a more offensive position during an investigation is to dump the password hashes using `hashdump`.

```
$ volatility --profile=Win7SP1x64 -f joshua1.vmem hashdump
Volatility Foundation Volatility Framework 2.6.1
Administrator:500:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0:::
Guest:501:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0:::
falken:1000:aad3b435b51404eeaad3b435b51404ee:a5c21848e6a6f81e797d73731ba359ba:::
```

Before we continue our investigation, let's recap on what we've done so far:
- We have **determined the operating system.**
- We have **discovered when the memory dump was captured.**
- We have **discovered all processes that were available at the time of the dump.**
- We have **inspected the machine for potential malware.**
- We have **dumped the system's password hashes.**

We've done a lot so far, but this is barely scratching the surface! All of this is basic information about a system. Let's start gearing our investigation more specifically towards the target user themselves now.

One great place to look for data is in the system **clipboard.** We might find some very useful information here, such as copied passwords or messages. We can extract data from the clipboard in memory using the `clipboard` option.

```
$ volatility --profile=Win7SP1x64 -f joshua1.vmem clipbo
ard
Volatility Foundation Volatility Framework 2.6.1
Session    WindowStation Format                         Handle Object             Data                                              
---------- ------------- ------------------ ------------------ ------------------ --------------------------------------------------
```

Unfortunately, nothing was found on the clipboard. Again, this is just a very basic sample memory dump that we are analyzing and so there's not many interesting things happening on the system.

Normally, we would check for connections at this point in order to see if the user was making connections to any remote destinations. This might be useful for malware analysis in order to detect C2 servers or to see if any data was being potentially exfiltrated. This can be done using `connscan` and `connections`. However, this is not supported for the memory dump that we are currently analyzing.

```
$ volatility --profile=Win7SP1x64 -f joshua1.vmem connsc
an
Volatility Foundation Volatility Framework 2.6.1
ERROR   : volatility.debug    : This command does not support the profile Win7SP1x64
$ volatility --profile=Win7SP1x64 -f joshua1.vmem connections
Volatility Foundation Volatility Framework 2.6.1
ERROR   : volatility.debug    : This command does not support the profile Win7SP1x64
```

Let's move on then. Something that can be incredibly useful is scanning the system for files, which can be done through `filescan`.

(The following output is cropped for the sake of this article.)

```
Offset(P)            #Ptr   #Hnd Access Name
------------------ ------ ------ ------ ----
0x000000003d7001c0     16      0 -W-rwd \Device\HarddiskVolume2\Windows\winsxs\Catalogs\f7cb979fd0964eb0fda39e4640d169f37b1ec66b8bb6c7f42a5aaa4e2eccf4f2.catg
0x000000003d700310     16      0 -W-rwd \Device\HarddiskVolume2\Windows\winsxs\Catalogs\34bf547c2d4f73ede50d74d9b9392b39c786685309ccfc84c729c01aa5f0446b.catg
0x000000003da26d00      1      1 R--r-d \Device\HarddiskVolume2\Windows\System32\en-US\crypt32.dll.mui
0x000000003da29b20     16      0 RWD--- \Device\HarddiskVolume2\Windows\System32\catroot\{F750E6C3-38EE-11D1-85E5-00C04FC295EE}\WUClient-SelfUpdate-ActiveX~31bf3856ad364e35~amd64~~7.6.7600.256.cat
0x000000003da2d220     14      0 R--rwd \Device\HarddiskVolume2\Windows\System32\sysclass.dll
0x000000003da2e790     16      0 R--r-- \Device\HarddiskVolume2\Windows\winsxs\Manifests\amd64_microsoft.windows.gdiplus_6595b64144ccf1df_1.1.7601.17514_none_2b24536c71ed437a.manifest
0x000000003da2f070      2      0 RWD--- \Device\HarddiskVolume2\Windows\inf\WmiApRpl\WmiApRpl.h
0x000000003da30b40     16      0 R--r-- \Device\HarddiskVolume2\Windows\winsxs\Manifests\amd64_microsoft.windows.c..-controls.resources_6595b64144ccf1df_5.82.7600.16385_en-us_ba5641d1849f93bc.manifest
...
```

We can end up with a *lot* of data so regex and `grep` will definitely help us out here! Note that these are just the file *locations* and their *contents* **may not necessarily be accessible from a memory dump alone.**

In order to access the contents of whatever files *are* accessible through a memory dump, we can use the `dumpfiles` option. In order to use this, we will also need to set the `--dump-dir` parameter.

```
$ mkdir dump
$ volatility --profile=Win7SP1x64 -f joshua1.vmem dumpfiles --dump-dir=dump
Volatility Foundation Volatility Framework 2.6.1
DataSectionObject 0xfffffa8001a56440   4      \Device\clfsKtmLog
SharedCacheMap    0xfffffa8001a56440   4      \Device\clfsKtmLog
DataSectionObject 0xfffffa800288f790   4      \Device\clfs\Device\HarddiskVolume1\$Extend\$RmMetadata\$TxfLog\$TxfLog
SharedCacheMap    0xfffffa800288f790   4      \Device\clfs\Device\HarddiskVolume1\$Extend\$RmMetadata\$TxfLog\$TxfLog
DataSectionObject 0xfffffa8001c3a8c0   4      \Device\HarddiskVolume2\Windows\System32\LogFiles\WMI\RtBackup\EtwRTEventLog-Application.etl
SharedCacheMap    0xfffffa8001c3a8c0   4      \Device\HarddiskVolume2\Windows\System32\LogFiles\WMI\RtBackup\EtwRTEventLog-Application.etl
DataSectionObject 0xfffffa8001c30f20   4      \Device\HarddiskVolume2\Windows\System32\LogFiles\WMI\RtBackup\EtwRTEventLog-System.etl
...
```

After the file dump is complete, you can access the *successfully* extracted *available* files in the dump directory you specified.

We've covered a lot in this article so far, but this barely starts the journey into memory forensics and tools such as Volatility. You can consult the Volatility documentation for a full list of built-in features in addition to consulting the internet for useful modules.

Let's conclude the article here. In another article, we will visit specific actions that would be done during a real-life digital forensics investigation. We'll visit more advanced and exciting topics related to memory forensics such as memory forensics on a malware-infected computer, the computer of a suspected cybercriminal, and more. Many exciting things lie ahead in the realm of digital forensics!
