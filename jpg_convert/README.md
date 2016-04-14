# jpeg conversion tool

This tool uses [jpegtran](http://jpegclub.org/jpegtran/) to mass compress a
directory tree containing JPEG images. They are compressed using '-progressive'.

Usage:

```
jpg_convert.py source/path dest/path
```

Where:

* `source/path` is the path to the source JPEGs
* `dest/path` is the path where the destination JPEGs will reside

The tool will attempt to create the same directory structure in the dest as was
found in the source.
