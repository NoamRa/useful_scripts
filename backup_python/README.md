# Backup - Non Destructive (Python)

This script copies a folder from source to destination, checks files for new versions and updates if necesary.

It's based on 
http://xalexchen.github.io/blog/blog/2013/10/18/sync-tow-folders-by-python/

Alterations -

The script will not delete files in the destination in case they were deleted from source. only adding and updating.
Fixed problems with non ASCII characters.
