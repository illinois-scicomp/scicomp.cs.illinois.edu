https://stackoverflow.com/questions/4493525/rsync-what-means-the-f-on-rsync-logs

YXcstpoguax  path/to/file
|||||||||||
||||||||||╰- x: The extended attribute information changed
|||||||||╰-- a: The ACL information changed
||||||||╰--- u: The u slot is reserved for future use
|||||||╰---- g: Group is different
||||||╰----- o: Owner is different
|||||╰------ p: Permission are different
||||╰------- t: Modification time is different
|||╰-------- s: Size is different
||╰--------- c: Different checksum (for regular files), or
||              changed value (for symlinks, devices, and special files)
|╰---------- the file type:
|            f: for a file,
|            d: for a directory,
|            L: for a symlink,
|            D: for a device,
|            S: for a special file (e.g. named sockets and fifos)
╰----------- the type of update being done::
             <: file is being transferred to the remote host (sent)
             >: file is being transferred to the local host (received)
             c: local change/creation for the item, such as:
                - the creation of a directory
                - the changing of a symlink,
                - etc.
             h: the item is a hard link to another item (requires
                --hard-links).
             .: the item is not being updated (though it might have
                attributes that are being modified)
             *: means that the rest of the itemized-output area contains
                a message (e.g. "deleting")


>f+++++++++ some/dir/new-file.txt
.f....og..x some/dir/existing-file-with-changed-owner-and-group.txt
.f........x some/dir/existing-file-with-changed-unnamed-attribute.txt
>f...p....x some/dir/existing-file-with-changed-permissions.txt
>f..t..g..x some/dir/existing-file-with-changed-time-and-group.txt
>f.s......x some/dir/existing-file-with-changed-size.txt
>f.st.....x some/dir/existing-file-with-changed-size-and-time-stamp.txt
cd+++++++++ some/dir/new-directory/
.d....og... some/dir/existing-directory-with-changed-owner-and-group/
.d..t...... some/dir/existing-directory-with-different-time-stamp/
