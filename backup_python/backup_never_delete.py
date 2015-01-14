#coding=utf-8
# This is a small python script to help you synchronize two folders
# Compatible with Python 2.x and Python 3.x

# Adapted from
# http://xalexchen.github.io/blog/blog/2013/10/18/sync-tow-folders-by-python/
 

import filecmp, shutil, os, sys
 
SRC = "\\\\SOURCE_SERVER_NAME\\folder\\folder"
DEST = "X:\\DEST_NAME\\also_folder"
 
IGNORE = ['Thumbs.db', '.DS_Store', 'DS_Store']
 
def get_cmp_paths(dir_cmp, filenames):
    return ((os.path.join(dir_cmp.left, f), os.path.join(dir_cmp.right, f)) for f in filenames)
 
def sync(dir_cmp):
    """
    for f_left, f_right in get_cmp_paths(dir_cmp, dir_cmp.right_only):
        if os.path.isfile(f_right):
            os.remove(f_right)
        else:
            shutil.rmtree(f_right)
        print('delete %s' % f_right.encode("utf-8"))  
    """
    for f_left, f_right in get_cmp_paths(dir_cmp, dir_cmp.left_only+dir_cmp.diff_files):
        if os.path.isfile(f_left):
            print('copying %s' % f_left.encode("utf-8"), end="",flush=True)
            shutil.copy2(f_left, f_right)
            print('   DONE')
        else:
            print('copying %s' % f_left.encode("utf-8"), end="",flush=True)
            shutil.copytree(f_left, f_right)
            print('   DONE')
        #print('copy %s' % f_left)
    for sub_cmp_dir in dir_cmp.subdirs.values():
        sync(sub_cmp_dir)
 
def sync_files(src, dest, ignore=IGNORE):
    if not os.path.exists(src):
        print('Please check the source directory was exist')
        print('Sync file failure !!!')
        return
    if os.path.isfile(src):
        print('We only support for sync directory but not a single file,one file please do it by yourself')
        print('Sync file failure !!!')
        return
    if not os.path.exists(dest):
        os.makedirs(dest)    
    dir_cmp = filecmp.dircmp(src, dest, ignore=IGNORE)
    sync(dir_cmp)
    print('Sync file finished!')
 
if __name__ == '__main__':
    src, dest = SRC, DEST
    if len(sys.argv) == 3:
        src, dest = sys.argv[1:3]
    sync_files(src, dest)
