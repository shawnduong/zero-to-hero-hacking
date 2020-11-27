# EXIF Data

EXIF, short for **Exchangeable Image File Format**, is a **standard for embedding metadata into audio or photo files.** EXIF data is often reviewed during digital forensics operations in order to gain more information about the file itself and by extension, the individuals and/or devices that produced the data.

EXIF is most commonly associated with JPG, TFF, and WAV formats. However, many tools used to view EXIF data can also be used to view non-EXIF metadata in other file formats. This article deals purely with EXIF metadata and EXIF-compatible file formats.

## Types of Metadata Supported

EXIF supports many types of metadata, including (but not limited to):
- Description
- Geolocation
- Date and time of capture
- Capture device
- Capture device settings

## Viewing EXIF Metadata

EXIF metadata can be viewed using the `exiftool` command-line utility. To view the EXIF metadata of a particular file, simply pass the path to the file as an argument.

```
$ exiftool <path>
```

For example, consider the following image located at `images/exif_sample.jpg`:

![](./images/exif_sample.jpg)

To view the EXIF metadata of this file, the following command can be run:

```
$ exiftool images/exif_sample.jpg
```

This command returns a large quantity of output. The most interesting lines of data that may pop out to a digital forensics specialist are:

```
Make                            : NIKON
Camera Model Name               : COOLPIX P6000
Software                        : Nikon Transfer 1.1 W
Modify Date                     : 2008:11:01 21:15:07
Date/Time Original              : 2008:10:22 16:28:39
Create Date                     : 2008:10:22 16:28:39
Nikon Capture Version           : COOLPIX P6000V1.0
File Source                     : Digital Camera
Scene Type                      : Directly photographed
GPS Latitude Ref                : North
GPS Longitude Ref               : East
GPS Altitude Ref                : Above Sea Level
GPS Time Stamp                  : 14:27:07.24
GPS Satellites                  : 06
GPS Img Direction Ref           : Unknown ()
GPS Map Datum                   : WGS-84
GPS Date Stamp                  : 2008:10:23
GPS Date/Time                   : 2008:10:23 14:27:07.24Z
GPS Latitude                    : 43 deg 28' 2.81" N
GPS Longitude                   : 11 deg 53' 6.46" E
GPS Position                    : 43 deg 28' 2.81" N, 11 deg 53' 6.46" E
```

Looking at this, it becomes very apparent why EXIF metadata can be invaluable to a digital forensics expert. Imagine for a moment that you're a digital forensics specialist investigating a threatening photo. If the sender forgot to scrub the EXIF metadata, then you can learn a lot about them including when they captured the photo, what device they used to capture the photo, and the GPS coordinates of where the photo was captured.
