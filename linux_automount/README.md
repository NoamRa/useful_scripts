# Linux Automount
These two scripts use udev rules to mount HDD on RHEL5. 
It was designed to solve the need to manualy mount the drives to folders select folders. The drive's model, manufacturer and volume are disregarded. as long as it's detected as a USB storage device and is connected by USB, it will be picked up by udev whick will run a bash script.
The script will then check to see if the first desired folder is empty. If not, it will continue to the next folder on the list.
