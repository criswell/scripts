# Simple MD5 checker

This script will run through a directory tree containing files with MD5
checksums and compare them to their respective files. It will report on errors
it finds.

If there is no problem with the files, there will be no output.

## Usage

```
Usage: md5chk ROOT_PATH
Where ROOT_PATH is the path to check.

md5chk will spider its way through ROOT_PATH looking for *.md5 and *.md5sum
files. It wil then compare them to similarly named files in the same directory.

This program expects files and their MDS5 checksums to be of the following
pattern:

   file.foo.bar
   file.foo.bar.md5

or:

   file.foo.bar
   file.foo.nar.md5sum

Will output a list of files which do not match their MD5 checksums, as well as
a list of any MD5 checksum files without matching files.

If no output, then you can assume there were no problems.
```


