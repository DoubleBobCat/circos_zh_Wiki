---
author: DoubleCat
date: 2025-04-11
layout: post
category: configuration
title: Runtime Parameters
---

### lesson
#### checking version
```    
    > circos -version
    circos | v 0.67-pre5 | 12 May 2014
```
#### checking for missing modules
```    
    > circos -modules
    ok       1.26 Carp
    ok       0.37 Clone
    ok       2.50 Config::General
    ok       3.33 Cwd
    ok      2.145 Data::Dumper
    ...
```
#### specifying the configuration file
All aspects of the image are controlled by the [plain-text configuration
file](/documentation/tutorials/configuration/configuration_files). I
conventionally name this file `circos.conf`, but you can use whatever name you
like.

This file is specified at run-time using the `-conf` flag an

```    
    > circos -conf myimage.conf
```
Using `circos.conf` is convenient because Circos will automatically attempt to
find a file of this name for its configuration.

```    
    # automatically search for circos.conf
    > circos
```
Circos will search each combination of the path `A/B/C` for the file where

  * `A` = `cwd`, location of `circos` script 
  * `B` = `. .. ../.. ../../..`
  * `C` = `. etc/ data/`

For example, the following will be searched (among others)

```    
    ./circos.conf
    ./etc/circos.conf
    ./../etc/circos.conf
```
To see a list of paths that are searched, use the `-debug_group` flag.

```    
    > circos -debug_group io
``````
#### adjusting output image location
Use `-outputdir` and `-outputfile` to change the output image location and
name. These parameters are typically set in the <image> block in the
configuration file with the `dir` and `file` parameters

```    
    <image>
    dir  = /path/to/your/output/directory
    file = yourimage.png
    ...
    </image>
```
but you can override them at the command-line

```    
    > bin/circos -conf etc/circos.conf 
                 -outputdir /path/to/your/output/directory 
                 -outputfile yourimage.png
```
#### dumping configuration values
To see all the internal configuration values, provide all parameters as you
would normally to generate the image but also add `-cdump`. You'll see a
formatted data structure of your image's configuration.

```    
    > circos ... -cdump
```
#### changing parameters on the command line
All configuration file parameters can be adjusted on the command line using
the `-param` flag. The syntax is

```    
    circos -param block1/block2/.../name=value
```
which will change the parameter `name` in the block <block1><block2>,
overriding any value already defined in the configuration file.

```    
    <block1>
     <block2>
     ...
      name
```
For example,

```    
    circos -param karyotype=myfile.txt ...
    circos -param image/radius=500p
    circos -param ideogram/show=no
```
You can undefine a parameter by changing its value to `undef`

```    
    circos -param chromosomes=undef
```
This will effectively remove the parameter from the configuration. There
should be no reason to have to do this but it is included in cases where you
want to avoid inheriting a parameter from the parent block in some cases.

The full list of shortcuts is

```    
    # check required modules
    modules
    
    # toggle options
    silent
    cdump
    debug
    help
    man
    version
    color_cache_rebuild
    color_cache_static
    
    # negatable toggle options (e.g. -png, -nopng)
    png
    svg
    warnings
    paranoid
    show_tick_labels
    show_ticks
    
    # options with arguments
    debug_group
    configfile
    outputdir
    outputfile
    
    # randomize all colors
    randomcolor
```
Use these as flags. For example,

```    
    circos -modules
    circos ... -nosvg
    circos ... -randomcolor
```### images
### configuration
