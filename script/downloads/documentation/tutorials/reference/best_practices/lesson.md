Use the [latest version of Circos](/software/download/circos/) and read
[Circos best
practices](/documentation/tutorials/reference/best_practices/)—these list
recent important changes and identify sources of common problems.

If you are having trouble, post your issue to the [Circos Google
Group](https://groups.google.com/group/circos-data-visualization) and [include
all files and detailed error logs](/support/support/). Please do not email me
directly unless it is urgent—you are much more likely to receive a timely
reply from the group.

Don't know what question to ask? Read [Points of View: Visualizing Biological
Data](https://www.nature.com/nmeth/journal/v9/n12/full/nmeth.2258.html) by
Bang Wong, myself and invited authors from the [Points of View
series](https://mk.bcgsc.ca/pointsofview).

# 12 — Circos Reference

## 1\. Best Practices

This is a very important document—well worth reading. Chances are if you have
asked a question in the [Google Group](https://groups.google.com/group/circos-
data-visualization), I have sent you to read this first.

Follow these tips to avoid common errors and to increase the legibility and
modularity of your configuration files.

### runtime

#### configuration dump

The configuration file is passed through several parsing steps, which import
files, merge blocks, and replace values. To see the configuration data
structure that Circos will use, use `-cdump`.

    
    
    > circos -cdump
    ...
    $VAR1 = {
              anglestep => 0.5,
              anti_aliasing => 1,
              ...
            };
    

The format is a Perl data structure, with `{}` indicating a hash and `[]` a
list.

The configuration dump is long. To obtain a list of a specific block, provide
the block name.

    
    
    > circos -cdump ideogram
    $VAR1 = {
              fill => 1,
              radius => '0.90r',
              spacing => {
                           default => '0.005r'
                         },
              stroke_color => 'dgrey',
              stroke_thickness => '2p',
              thickness => '20p'
            };
    

To list parameters that match a regular expression,

    
    
    > circos -cdump block:regex
    > circos -cdump :regex
    

See [Runtime Parameter
Tutorial](/documentation/tutorials/configuration/runtime_parameters/) for
details.

#### temporarily altering parameters

You can change any configuration parameter without editing the configuration
file by using the `-param` flag. The syntax here is `-param
BLOCK/.../PARAMETER=VALUE`. For example,

    
    
    > circos -param ideogram/show=no -param image/radius=2000p
    

This is useful to toggle things on/off for testing. For example, to turn all
<plot> tracks off,

    
    
    > circos -param plots/show=no
    

This is the equivalent of adding the following to the configuration file

    
    
    <plots>
    
    show = no
    
     <plot>
     ...
     </plot>
    
     ...
    
    </plots>
    

See [Runtime Parameter
Tutorial](/documentation/tutorials/configuration/runtime_parameters/) for
details.

#### debugging

Circos can produce debug messages from different components of the code. By
default you will see only summary debug messages and, if your image takes more
than 30 seconds to create, you will see timing information.

This is set by the `debug_group` and `debug_auto_timer_report` parameters in
`etc/housekeeping.conf`.

To include messages from other parts of the code, use `debug_group`.

    
    
    # include file I/O messages
    > circos -debug_group io
    

To get a list of debug groups,

    
    
    > circos -debug_group
    

See [Debugging Tutorial](/documentation/tutorials/configuration/debugging/)
for details.

### configuration

#### templates

Do not write your configuration files from scratch.

Do not use the configuration of the `example/` as a template. It is quite
complex.

Use the [Quick Start Tutorials](/documentation/tutorials/quick_start) as
templates for your configuration file.

#### configuration defaults

Some files are conventionally included from the Circos distribution directory.
Do not copy them outside of the Circos directories, unless you need to alter
them.

    
    
    etc/colors_fonts_patterns.conf
    etc/housekeeping.conf
    etc/image.conf
    data/karyotype/*
    

The contents of these files often change with new versions.

#### color, font and pattern includes

Colors, fonts and patterns should be imported from
`etc/colors_fonts_patterns.conf`.

    
    
    # circos.conf
    <<include etc/colors_fonts_patterns.conf>>
    

This file, which can be found in `etc/` in the distribution, automatically
brings in `etc/colors.conf`, `etc/fonts.conf`, and `etc/patterns.conf`, which
you do not need to import individually.

Make sure that you're not defining colors twice by using this file _and_
importing from `etc/colors.conf`.

#### defining your own colors

Circos comes with a large number of predefined colors. The best way to add
your own is to append new color definitions to the <colors> block as follows

    
    
    # circos.conf
    
    # your own colors will be merged and overwrite
    # any default color definitions included in
    # the <colors> block from 
    # etc/colors_fonts_patterns.conf
    <colors>
    myred  = 211,121,111
    myblue = 85,143,190
    </colors>
    
    # color, font, pattern defaults -- this is required
    <<include etc/colors_fonts_patterns.conf>>
    

The <colors> block imported from `etc/colors_fonts_patterns.conf` will be
merged with the one you've added. The order in which these appear in the
configuration file does not matter.

See [Configuration File
Tutorial](/documentation/tutorials/configuration/configuration_files) for
details.

#### track defaults

Every track type has some default variables set. To see these, look in
`etc/track/*` in the Circos distribution. To undefine a parameter

    
    
    <plot>
    type = tile
    # removes the definition of this parameter
    stroke_thickness = undef
    ...
    </plot>
    

If you don't like the idea of these defaults, you can either comment the
`track_defaults` parameter in `etc/housekeeping.conf`, or better yet undefine
it in your configuration by overwriting the parameter (see below about doing
this).

    
    
    <<include etc/housekeeping.conf>>
    track_defaults* = undef
    

#### overwriting parameters

Circos has many different parameters and keeping track of them can initially
be a challenge. I suggest that you import default values, as done in the
tutorials, by including configuration snippets from the Circos distribution.

For example, the <image> block, which defines output file location, size,
color, etc, is populated conveniently by importing `etc/image.conf`,

    
    
    # circos.conf
    <image>
    <<include etc/image.conf>>
    </image>
    

Sometimes you'll want to redefine some of the parameters set by the included
file. To do this, use the `*` suffix syntax

    
    
    # circos.conf
    <image>
    <<include etc/image.conf>>
    file*   = myfile.png
    radius* = 1000p
    </image>
    

The value of any parameter named `p` will be overwritten by the value of `p*`.
Similarly, `p**` overwrites the value of code (p*), and so on. This is
particularly useful if you want to adjust some system parameters temporarily

    
    
    # circos.conf
    <<include etc/housekeeping.conf>>
    anti_aliasing* = no
    

See [Configuration File
Tutorial](/documentation/tutorials/configuration/configuration_files) for
details.

### file organization

#### file paths

Use a separate directory for each Circos image. Put configuration files in
`etc/` and data in `data/`. For an example, see the `example/` directory,
included in the Circos distribution.

Here's what a typical Circos project directory might look like,

    
    
     cancer_snp/
      etc/ 
       circos.conf
       ticks.conf
       ideogram.conf
       ...
      data/
       cnv.txt
       genes.txt
       ...
    

#### file names

Circos will automatically look for `circos.conf` as the main configuration
file. Therefore, I suggest you name your file to this. If you have a one-to-
one mapping between directory and image, there won't be any ambiguity. It is
better to name the directory after the project, rather than configuration
file. For example, instead of

    
    
     circos/
      circos_cancersnp.conf
      ...
    

I suggest

    
    
     circos/
      cancer_snp/
       etc/
        circos.conf
    

By having your configuration file named `circos.conf`, you can quickly run
Circos like this

    
    
    # switch to the image project directory
    > cd cancer_snp
    > ls
    data/
    etc/ 
    
    # Circos will automatically look for circos.conf in several locations (including etc/),
    # You don't need to use the command-line flag "-conf etc/circos"
    > circos
    ...
    > ls
    data/
    etc/
    circos.png
    circos.svg
    

#### output files

The default location of the output file is the same as directory of the
configuration file. This is set in `etc/image.generic.conf`

    
    
    dir = conf(configdir)
    

If you want to change the name of the output file, use `-outputfile` and
`-outputdir`.

    
    
    # ./snp.png
    > circos -outputfile snp.png
    # /tmp/snp.png
    > circos -outputfile snp.png -outputdir /tmp
    # /tmp/circos.png
    > circos -outputdir /tmp
    

#### relative file names

As much as possible, avoid the use of absolute path names in the configuration
files. Relative paths will be interpreted relative to your current directory.
If Circos cannot find the file, it will look in a few other places, such as
relative to the path of the configuration file as well as the Circos
distribution.

For example, if you have

    
    
     /user/bob/circos/cancersnp/
      etc/
       circos.conf
      data/
       snp.txt
    

Then in `circos.conf` you only need

    
    
    file = data/snp.txt
    

and not

    
    
    file = /user/bob/circos/cancersnp/data/snp.txt
    

Avoiding the use of absolute paths will make your Circos project files
portable.

#### how Circos locates files

When a file name is defined using a relative path, Circos will attempt to look
for it various places, constructed by combining three paths.

    
    
    dir1/dir2/dir3
    
    where
    
    dir1 = current_directory | configuration_directory | circos_binary_directory
    dir2 = . | .. | ../.. | ../../../
    dir3 = . | etc | data
    

For example, some of the possible search locations are

    
    
    current_directory/../
    current_directory/../data
    current_directory/../etc
    current_directory/../../
    current_directory/../../data
    current_directory/../../etc
    configuration_directory/
    circos_binary_directory/../../etc
    

It's important to realize that this automatic searching is happening. You can
see it in action by using the `-debug_group io` command-line flag. For
example, here I am running the example, found in `example/`, from `~/tmp`
directory

    
    
    >: cd ~/tmp
    > circos -debug_group io -conf ~/work/circos/svn/example/etc/circos.conf
    ...
    # here Circos is trying to find the data/mm.bundle.txt file
    # try relative to current directory
    debuggroup io 6.31s trying /home/martink/tmp/data/mm.bundle.txt
    debuggroup io 6.31s trying /home/martink/tmp/etc/data/mm.bundle.txt
    debuggroup io 6.31s trying /home/martink/tmp/data/data/mm.bundle.txt
    debuggroup io 6.31s trying /home/martink/tmp/../data/mm.bundle.txt
    debuggroup io 6.31s trying /home/martink/tmp/../etc/data/mm.bundle.txt
    debuggroup io 6.31s trying /home/martink/tmp/../data/data/mm.bundle.txt
    debuggroup io 6.31s trying /home/martink/tmp/../../data/mm.bundle.txt
    debuggroup io 6.31s trying /home/martink/tmp/../../etc/data/mm.bundle.txt
    debuggroup io 6.31s trying /home/martink/tmp/../../data/data/mm.bundle.txt
    debuggroup io 6.31s trying /home/martink/tmp/../../../data/mm.bundle.txt
    debuggroup io 6.31s trying /home/martink/tmp/../../../etc/data/mm.bundle.txt
    debuggroup io 6.31s trying /home/martink/tmp/../../../data/data/mm.bundle.txt
    # try relative to configuration directory
    debuggroup io 6.31s trying /home/martink/work/circos/svn/example/etc/data/mm.bundle.txt
    debuggroup io 6.31s trying /home/martink/work/circos/svn/example/etc/etc/data/mm.bundle.txt
    debuggroup io 6.31s trying /home/martink/work/circos/svn/example/etc/data/data/mm.bundle.txt
    debuggroup io 6.31s trying /home/martink/work/circos/svn/example/etc/../data/mm.bundle.txt
    # found it!
    debuggroup io 6.31s data/mm.bundle.txt found in /home/martink/work/circos/svn/example/etc/../data/mm.bundle.txt
    

### input files

#### karyotype files

If you are using reference genomes, use the karyotype files that come bundled
in the distribution in `data/karyotype`.

    
    
    karyotype = data/karyotype/karyotype.human.txt
    

Avoid unnecessary duplication and do not copy these files to your working
directories. If you have custom karyotype files that you use often, place them
in a central location.

    
    
    karyotype = /path/to/my/karyotype/custom.txt
    

If you are plotting multiple genomes, it's best to keep their karyotype files
separate and then specify them as a list.

    
    
    karyotype = data/karyotype/karyotype.human.txt,data/karyotype/karyotype.mouse.txt
    

See [Data Files Tutorial](/documentation/tutorials/configuration/data_files/)
for details.

#### link files

Use the one-line link format instead of the two line format.

    
    
    # YES
    hs1 100 200 hs5 500 750 id=5
    
    # NO
    link001 hs1 100 200 id=5
    link001 hs5 500 750 id=5
    

See [Data Files Tutorial](/documentation/tutorials/configuration/data_files/)
for details.

### <plot> and <link> blocks

#### <link> does not require a block name

In old versions these blocks required names. This is no longer needed.

    
    
    # YES
    <link>
     ...
    
    # NO
    <link segdup>
     ...
    

#### global parameters

If all your <plot> or <link> blocks share the same parameters, place them in
the parent <plots> or <links> block.

    
    
    <plots>
    
    color = black
    
    <plot>
     # color inherited from outer block
     ...
    </plot>
    
    <plot>
     # color inherited from outer block
     ...
    </plot>
    
    <plot>
     # override color 
     color = blue
     ...
    </plot>
    
    </plots>
    

### data

#### cytogenetic bands

You can add cytogenetic bands to your ideograms, as described in the
[Ideograms Tutorial](/documentation/tutorials/ideograms/karyotypes/). These
are regional annotations that (a) cover the ideogram entirely and (b) do not
overlap. If you attempt to use the cytogenetic band functionality for other
data, make sure that they meet these criteria.

Do not use the band function for showing genomic annotations like repeats or
genes. Instead, use <plot> block of `type=highlight`.

    
    
    <plot>
    type = highlight
    file = repeats.txt
    r0   = dims(ideogram,radius_inner)
    r1   = dims(ideogram,radius_outer)
    </plot>
    

#### matching data and display resolution

When drawing data on a 3 Gb genome, it is easy to quickly exceed the
resolution of the output medium. Consider that a typical 3,000 x 3,000 pixel
Circos image will have an ideogram circumference of about 6,000 pixels. The
size of each pixel will be about 0.5 Mb on the genome.

If your data is sampled more finely than this, you will not see any structure
in it because multiple data points will be assigned to the same pixel. In
general, if you have more than 10,000 data points in any track, consider
downsampling.

When drawing images on full mamallian genomes, I suggest starting with 5 Mb
data bins. You can use the `tools/resample` script to resample your data. This
script is designed for moderate data sizes. If you have millions of data
points, you're better off using something like
[bedtools](https://code.google.com/p/bedtools/).

For guidelines about matching data and output resolution, see [Limits of Human
Visual Acuity and Consequences on Sequence
Visualization](https://mk.bcgsc.ca/vizbi/2012/resolution/resolution.pdf).

### rules

#### importance parameter

Rules no longer require the `importance` parameter. They are evaluated in the
order that they appear in the configuration file. The parameter is only used
if you want the rules to be evaluated in some other order.

#### `_FIELD_` syntax is deprecated

Rules should use `var(FIELD)` syntax, not `_FIELD_`. For example,

    
    
    # YES
    condition = var(chr) eq "hs1"
    
    # NO
    condition = _CHR_ eq "hs1"
    

