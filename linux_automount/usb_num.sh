#!/bin/bash

# This script should be called by udev when a USB mass storage device is connected
# if /mnt/usbdisk3 is empty, mount it there, otherwise check /mnt/usbdisk4.
# if both contain files/folders (and therefore mounted), do nothing.

# Input is the device name to mount such as 'sda1' or 'sdd3'
# In udev that input value is passed as %k.

# udev has no output. It will not print the 'echo' and 'ls' commands.

# Place the script in /usr/local/bin/ and make sure it has execute premissions.

DEVICE=$1

echo Trying to mount $DEVICE.

USBDISK3='/mnt/usbdisk3'
USBDISK4='/mnt/usbdisk4'
USBDISK5='/mnt/usbdisk5'

if [ `find $USBDISK3 -prune -empty` ] # check to see if there are any files or folders
then
    echo mounting to $USBDISK3
    mount /dev/$DEVICE $USBDISK3
    echo The content of $USBDISK3 is -
    ls $USBDISK3
else
    if [ `find $USBDISK4 -prune -empty` ] # check to see if there are any files or folders
    then
        echo mounting to $USBDISK4
        mount /dev/$DEVICE $USBDISK4
        echo The content of $USBDISK4 is -
        ls $USBDISK4
    else
        if [ `find $USBDISK5 -prune -empty` ] # check to see if there are any files or folders
        then
            echo mounting to $USBDISK5
            mount /dev/$DEVICE $USBDISK5
            echo The content of $USBDISK5 is -
            ls $USBDISK5
        fi
    fi
fi
