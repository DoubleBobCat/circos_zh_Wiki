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

# 1 — Configuration and Installation

## 3\. Configuration Files - Syntax, Colors, Fonts and Units

[Lesson](/documentation/tutorials/configuration/configuration_files/lesson)
[Images](/documentation/tutorials/configuration/configuration_files/images)

If you are having trouble with installation of Perl or modules, use online
resources that explain the details of how to [download
Perl](https://www.perl.org/get.html), get it working
([Linux](https://learn.perl.org/installing/unix_linux.html), [Mac OS
X](https://learn.perl.org/installing/osx.html), Windows [[win32.perl.org
wiki](https://win32.perl.org/wiki/index.php?title=Main_Page<span class=syn-
comment>#Installing_Perl_on_Windows_for_the_First_Time.3F),
[ActiveState](https://perl.about.com/od/gettingstartedwithperl/ss/installperlwin.htm),
[Strawberry](https://damienlearnsperl.blogspot.com/2009/01/install-strawberry-
perl-your-windows.html)]), and how to [install
modules](https://www.cpan.org/modules/INSTALL.html)
([UNIX](https://perldoc.perl.org/perlmodinstall.html), [Windows](install perl
modules windows)). If you're still stuck, post your questions to the [Circos
group](https://groups.google.com/group/circos-data-visualization).

Try the [Active State Perl build for
Circos](https://platform.activestate.com/ReadyMade/Circos/distributions?platformID=78977bc8-0f32-519d-80f3-9043f059398c).
It includes all the necessary modules.

Need to install modules? See [A Guide to Installing
Modules](https://www.perlmonks.org/?node_id=621579) and [its corresponding
tutorial for Windows users](https://www.perlmonks.org/?node_id=434813).

Having trouble with libgd and GD? See the [Perl Monks libgd/GD
Tutorial](https://www.perlmonks.org/?node_id=621579), Shaun Jackman's
[Homebrew formula](https://groups.google.com/forum/#!topic/circos-data-
visualization/qOIjmy4_wnM), Wang's [install zlib/libpng/jpeg/freetype/libgd/GD
on Mavericks](https://wangqinhu.com/install-gd-on-mavericks/) as well as my
own guide for [installation of libpng, freetype, libgd and GD on Mac OS X
Mavericks](/documentation/tutorials/configuration/perl_and_modules/index.mhtml#circos-
libgd-gd). There are some [useful
threads](https://groups.google.com/forum/?hl=en&fromgroups=<span class=syn-
comment>#!topic/circos-data-visualization/MOdx0eKWDeQ) in the Google Group
about this.

Need to run Bash shell batch files in Windows? You'll need to install a [UNIX
command line shell](https://stackoverflow.com/questions/913912/bash-shell-for-
windows), like [Cygwin](https://www.cygwin.com).

Stumped by an error? A good strategy is to Google the error message (e.g.
[mkdir /usr/local/share/man: permission
denied](https://www.google.ca/search?hl=en&q=%2Fbin%2Fenv+not+found&sourceid=navclient-
ff&rlz=1B7GGLL_enCA396CA396&ie=UTF-8<span class=syn-
comment>#sclient=psy&hl=en&rlz=1B7GGLL_enCA396CA396&source=hp&q=mkdir+%2Fusr%2Flocal%2Fshare%2Fman:+permission+denied&aq=f&aqi=&aql=&oq=&pbx=1&fp=58653f3aee9cd59b))
to find the solution.

Want to learn more about Perl? Try [learn.perl.org](https://learn.perl.org/)
or read through the [Perl Journal
archive](https://mk.bcgsc.ca/books/sapj/tpj).

Circos generates static images. The image generation process is driven by a
central configuration file. This file usually imports other configuration
files, such as global color and font settings.

There is no interface to Circos. Workflow typically proceeds as follows

  * determining how the data is to be shown (this is the hard part) 
  * parsing data files into [Circos format](/documentation/tutorials/configuration/data_files)
  * constructing a configuration file, either from scratch or using one of the tutorials as template 
  * running Circos to create PNG and SVG files 
  * editing PNG/SVG files for publication (adding a legend, additional text labels, etc). 

## configuration syntax

Configuration files are parsed using
[Config::General](https://search.cpan.org/~tlinden/Config-General-2.50/)
module. All pertinent features are described below, but for those so inclined,
refer to this [module's man page](https://search.cpan.org/~tlinden/Config-
General-2.50/General.pm) to learn about the details of the syntax and parsing
of these files.

Settings are defined in configuration files using the format

    
    
    variable = value
    

Note that although [Config::General](https://search.cpan.org/~tlinden/Config-
General-2.50/) supports a whitespace as an assignment delimiter, Circos
requires that you use `=` for all definitions.

Some settings are grouped in blocks, to create a hierarchical structure.

    
    
    <ideogram>
     thickness = 30p
     fill      = yes
     ...
    </ideogram>
    

Some blocks can have multiple instances, such as data tracks. Typically, these
are enlosed in another block, here <links>.

    
    
    <links>
    
    <link>
     file      = data/set1.txt
     color     = black
     ...
    </link>
    
    <link>
     file      = data/set2.txt
     color     = red
     ...
    </link>
    
    </links>
    

Please ensure that all your configuration blocks are correctly terminated with
an appropriate close block tag.

    
    
    <ideogram>
    ...
    <ideogram> # <-- if this is missing, an error will result
    

## 4 ways to specify configuration parameters: global, track, data and rules

There are four places in which a configuration parameter can be specified.

In order of _increasing_ importance

  * globally for all data points in all plot tracks (in the <plots>or <links> block) 
  * locally for all data points in a given plot track (in the <plot> or <link> block) 
  * specifically for a single data point (in the data file) 
  * using a rule (in a <rule> block) 

A parameter set by a rule overrides any specified in the data file. A data
file parameter overrides any in a <plot> or <link> block, which in turn
override any global parameters in a <plots> or <links> block.

    
    
    <plots>
    
    # global parameter
    fill_color = white
    
    <plot>
    
    ... # other plot parameters, such as file, type, position, etc
    
    # local to this track - overrides the fill_color=white value
    fill_color = grey
    
    # in data.txt:
    #
    # ...
    # hs1 10 20 0.50 fill_color=dblue
    # ...
    # 
    # The data point will be purple, overriding both fill_color=red and fill_color=green values. 
    
    <rules>
    <rule>
    condition  = var(value) < 0.33
    # specific to data points matching the condition, overrides any previously specified
    # fill_color value, (global, local, data file)
    fill_color = orange
    </rule>
    </rules>
    
    </plot>
    
    </plots>
    

If you are plotting a large number of similar tracks (e.g. groups of
histograms, heat maps, etc), it is useful to apply global parameters where
possible. This is particularly effective when combined with [automated track
placement with track
counters](/documentation/tutorials/recipes/automating_tracks). In the example
below, each plot will be a heatmap with the same min/max value and color map.
Within individual <plot> blocks, only the parameters specific to that block
need to be specified.

    
    
    <plots>
    
    type  = heatmap
    min   = 0
    max   = 1
    # this color name is a list - see below about color lists
    color = spectral-4-div
    
    <plot>
    file = data.1.txt
    r1   = 0.6r
    r0   = 0.5r
    ...
    </plot>
    
    <plot>
    file = data.2.txt
    r1   = 0.7r
    r0   = 0.6r
    ...
    </plot>
    
    <plot>
    file = data.3.txt
    r1   = 0.8r
    r0   = 0.7r
    ...
    </plot>
    
    <plot>
    file = data.4.txt
    r1   = 0.9r
    r0   = 0.8r
    ...
    </plot>
    
    …
    
    </plots>
    

## external imports

Some settings never or rarely change, such as colors and fonts. To keep the
main configuration file modular, the files for these static values are
imported using the <<include ...>> directive.

Two files should always be imported from `etc/` in the Circos distribution.
These are

    
    
    # colors, fonts and fill patterns
    <<include etc/colors_fonts_patterns.conf>>
    # system and debug parameters
    <<include etc/housekeeping.conf>>
    

The `etc/colors_fonts_patterns.conf` file itself imports several files from
the Circos distribution.

    
    
    # etc/colors_fonts_patterns.conf
    
    <colors>
    import(etc/colors.conf)
    </colors>
    
    <fonts>
    import(etc/fonts.conf)
    </fonts>
    
    <patterns>
    import(etc/patterns.conf)
    </patterns>
    
    

Circos requires that these blocks be present and populated with definitions.

Conventionally, I store configuration for ideograms in an external file
(`ideogram.conf`) and for tick mark formatting (`ticks.conf`). The reason for
this is that these settings are fairly verbose, but are not related to a data
set. By importing ideogram and tick mark settings from an external file

    
    
    <<include ideogram.conf>>
    <<include ticks.conf>>
    

the main configuration file is kept more succinct. Moreover, if you are
creating multiple images with different data sets, you are likely to use the
same settings for ideogram and tick mark formats. Storing these settings
separately just makes sense.

Usually both `ideogram.conf` and `ticks.conf` are placed in the same directory
as `circos.conf`, so no path (relative or absolute) needs to be added to the
filename in the <<include >> directive.

If you have parameters that rarely change, consider creating external
configuration files for these.

You can use the <<include >> directive anywhere in the configuration file,
such as in plot blocks.

    
    
    <plot>
    file = data.4.txt
    r0 = 0.8r
    r1 = 0.9r
    <<include plotsettings.conf>>
    </plot>
    

Inclusion can be arbitrarily nested. In other words, included files can
themselves include others, and so on.

When you include a file using <<include CONFIG_FILE_PATH/CONFIG_FILE>>, Circos
will search the following paths for the file

  * relative to the location of `CONFIG_FILE`
  * relative to `CONFIG_FILE_PATH/etc`
  * `CIRCOS_PATH/etc`
  * `CIRCOS_PATH/../etc`
  * `CIRCOS_PATH/..`
  * `CIRCOS_PATH`

## dynamically evaluated parameters

In the configuration file, parameters are typically set to constants using the
syntax

    
    
    variable = value
    

For example,

    
    
    color = blue
    

There will be times when you'll want to specify the value of a configuration
parameter using the value or a function of another.

### accessing configuration values

Any parameter can be set to the value of another parameter using the syntax

    
    
    parameter2 = conf(parameter1)
    

or, for parameters which are found in blocks

    
    
    parameter2 = conf(block1,parameter1)
    parameter2 = conf(block1,block2,parameter1)
    ...
    

For example,

    
    
    track_color = blue
    <plots>
    <plot>
    color = conf(track_color)
    ...
    

When the configuration file is parsed, simple substitution is exhaustively
made until all `conf(parameter`) strings have been replaced by values.

Make sure that you include the full block path of the parameter when using
this syntax. Thus for

    
    
    <block1>
    <block2>
    parameter1 = ...
    </block2>
    </block1>
    

you would use `conf(block1,block2,parameter1`).

### performing operations on parameters

Any parameter can be written as Perl code and evaluated at run-time. To use
this feature, enclose the parameter in an `eval(`) function.

    
    
    thickness = eval(1+1)
    color     = eval("b"."l"."u"."e")
    

The `eval(`) feature is very useful when used to refer to and manipulate other
configuration parameters.

For example,

    
    
    track_color = blue
    track_width = 100
    track_start = 0.5
    
    <plots>
    <plot>
    
    # color=blue
    color = conf(track_color)
    # r0 = 0.5r
    r0    = eval(conf(track_start) . "r")
    # r1 = 0.5r+100p
    r1    = eval(conf(track_start) . "r" + conf(track_width) . "p")
    </plot>
    </plots>
    

If you are defining a parameter by a single `conf(parameter`) value, you do
not need `eval(`), since only a substitution is required. However, if you need
to manipulate this value (e.g. append a string, perform arithmetic), then
`eval(`) is required since the expression must be evaluated as code.

Because `eval(`)calls require that you write correct Perl syntax, the chance
of a mistake and therefore fatal error is high. Double check! It is common to
forget to quote text in these calls — verify that you are not using a value as
a bare word.

    
    
    ## OK
    x = eval( 1.05 . "r" )
    ## NOT OK - r is meant to be a string, but without quotes Perl will 
    ## interpret it as a bare word, producing an error
    x = eval( 1.05 . r )
    

Parameters with `eval(`) in <rule> blocks are evaluated independently for each
data point.

### Automated Counters

Circos keeps a running count of the tracks as they are drawn. You can use
these variables to fully automate track placement.

See [Automating Tracks](/documentation/tutorials/recipes/automating_tracks/).

## colors

By including the `etc/colors_fonts_patterns.conf` file in the main
configuration file

    
    
    # circos.conf
    <<include etc/colors_fonts_patterns.conf>>
    ...
    

you are including definitions for primary RGB and HSV colors. Also defined are
[Brewer palette colors](href=) and the conventional human chromosome color
palette. To learn more about Brewer palettes, see my [Color Palettes
Matter](https://mk.bcgsc.ca/brewer/talks/color-palettes-brewer.pdf)
presentation.

The `etc/colors.conf` file, which is included by
`etc/colors_fonts_patterns.conf`, itself includes these various color
definitions

    
    
    # etc/colors.conf
    
    # primary RGB colors
    ...
    
    # Brewer palettes
    # see etc/colors.brewer.conf
    <<include colors.brewer.conf>>
    
    # UCSC genome browser human chromosome colors
    # see etc/colors.ucsc.conf
    <<include colors.ucsc.conf>>
    
    # HSV pure colors
    # see etc/colors.hsv.conf
    <<include colors.hsv.conf>>
    

### using colors

Colors are referenced using their RGB values or their names (see below).

    
    
    # using RGB values
    color = 107,174,241
    
    # using name
    color = blue
    

When passing a color as an option in data files, the RGB values need to be
delimited by `(...)`. For example, if you want to add a color to a link

    
    
    # using a color name
    chr1 100 200 chr2 200 250 color=blue,thickness=2
    
    # using RGB value
    chr1 100 200 chr2 200 250 color=(107,174,241),thickness=2
    

### color names

Colors in Circos are defined by their RGB or HSV values and specified by a
name (e.g. red, orange, etc). Many named colors are pointers to Brewer palette
equivalents.

    
    
    # pure orange
    porange  = 255,127,0
    
    # dark pure orange
    dporange = 234,110,0
    
    # points to Brewer color...
    orange = oranges-7-seq-4
    
    # ...which is defined in colors.brewer.conf as
    oranges-7-seq-4 = 253,141,60
    

### color name syntax

Typically for a given color root name (e.g. orange), there are corresponding
shades of the color with prefixed `d` (dark), `l` (light). The light version
may be prefixed by one or more `v` (very). These shades point to a sequential
Brewer palette for the color. For example, oranges point to the 7-color
'oranges' Brewer palette

    
    
    vvlorange = oranges-7-seq-1
    vlorange  = oranges-7-seq-2
    lorange   = oranges-7-seq-3
    orange    = oranges-7-seq-4
    dorange   = oranges-7-seq-5
    vdorange  = oranges-7-seq-6
    vvdorange = oranges-7-seq-7
    

which is defined in `colors.brewer.conf` as

    
    
    oranges-7-seq-1 = 254,237,222 
    oranges-7-seq-2 = 253,208,162 
    oranges-7-seq-3 = 253,174,107 
    oranges-7-seq-4 = 253,141,60 
    oranges-7-seq-5 = 241,105,19 
    oranges-7-seq-6 = 217,72,1  
    oranges-7-seq-7 = 140,45,4 
    

If you want the pure, saturated version of the color, use the `p` prefix. For
example, `porange` is a pure bright orange.

    
    
    vvlporange = 255,182,106
    vlporange  = 255,164,82
    lporange   = 255,146,54
    porange    = 255,127,0
    dporange   = 234,110,0
    vdporange  = 213,92,0
    vvdporange = 193,75,0
    

Check `etc/colors` for the full list of colors.

I suggest that you try using the Brewer colors (e.g. `orange` vs `porange`),
because they are perceptually uniform. However, they will appear less punchy
and saturated than their pure equivalents. In particular, the Brewer reds may
appear pinkish and light when used on their own.

Experiment, but be aware of the perceptual aspects of color, which will
influence how your figure is perceived (see my [Color Palettes
Matter](https://mk.bcgsc.ca/jclub/biovis/brewer/colorpalettes.pdf)
presentation).

### Brewer colors

Brewer colors are categorized into one of three palette types: sequential,
diverging and qualitative. For a given palette type (e.g. sequential), there
are a variety of palettes (e.g. reds, greens, blues). Each palette is
available for various number of colors (e.g. 3, 4, 5, ...).

The syntax for a Brewer color name is `palettename-ncolors-palettetype-index`.
The palette names, for each type, are

    
    
    # sequential (-seq-) (3-9 colors)
    blues
    bugn
    bupu
    gnbu
    greens
    greys
    oranges
    orrd
    pubu
    pubugn
    purd
    purples
    rdpu
    reds
    ylgn
    ylgnbu
    ylorbr
    ylorrd
    
    # diverging (-div-) (3-11 colors)
    brbg
    piyg
    prgn
    puor
    rdbu
    rdgy
    rdylbu
    rdylgn
    spectral
    
    # qualitative (-qual-) (3-8 colors, some up to 12 colors)
    accent (3-8 colors)
    dark2 (3-8 colors)
    paired (3-12 colors)
    pastel1 (3-9 colors)
    pastel2 (3-8 colors)
    set1 (3-9 colors)
    set2 (3-8 colors)
    set3 (3-12 colors)
    

For example, purple-orange diverging 9-color palette colors are
`puor-9-div-1`, `puor-9-div-2`, ..., `puor-9-div-9`.

### HSV colors

You can use the HSV color space to define colors. To do so, specify the HSV
values as hsv(h,s,v). For example,

    
    
    red = hsv(0,1,1)
    

All pure HSV colors (s = 1, v = 1) are defined in `colors.hsv.conf`.

    
    
    hue000 = hsv(0,1,1)
    hue001 = hsv(1,1,1)
    ...
    hue359 = hsv(359,1,1)
    hue360 = hsv(360,1,1) # same as hue000
    

### unix colors

The file `etc/colors.unixnames.txt` defines a large number (700+) of named
colors, taken from UNIX's [rgb.txt
file](https://www.uize.com/examples/sortable-color-table.html). This file is
_not_ included by default.

Many definitions in this file duplicate definitions in `colors.conf` (e.g.
`colors.unixnames.txt` defines blue as 0,0,255 but in `colors.conf` it is
blues-7-seq-4, which is 107,174,214). Including `colors.unixnames.txt`
together with (colors.conf) will result in an error.

### colors with alpha channels (transparency)

You can assign an alpha channel value to a color (transparency) by including a
fourth component.

    
    
    # 0 < alpha < 1 
    # 0 opaque
    # 1 transparent
    red_faint = 255,255,255,0.8
    
    # or alpha 0-127
    # 0   opaque
    # 127 transparent
    red_also_faint = 255,255,255,102
    

You can use either the [0,1] range for the alpha value, or [0,127]. In both
cases, the right end of the interval corresponds to transparent. For example,
if alpha is in the range 0-127 then `a=0` corresponds to fully opaque, and
`a=127` to fully transparent.

Please see [Transparent
Link](/documentation/tutorials/recipes/transparent_links/) tutorial for
discussion about automating definition of these colors.

### full transparency

To create a fully transparent color (e.g. for an image with transparent
background), you'll need to define a color named `transparent`. A transparent
color still requires an RGB value (a strange artefact in gd implementation).
Choose an RGB value that you aren't using elsewhere. Typically something like
1,0,0 will be suitable.

    
    
    # in color.conf
    transparent = 1,0,0
    

The transparent color will be available using the name `transparent`. A
synonym `clear` is also provided. To use the transparent color (e.g. for
background),

    
    
    <image>
    ...
    background = transparent # 'clear' also works here 
    ...
    </image>
    

The names `transparent` and `clear` are reserved. Do not use these two color
names for other colors.

### color synonyms

You can include synonyms for colors, by defining one color using the name of
another color, instead of RGB or RGBA values.

    
    
    favourite        = green
    almost_favourite = orange
    ...
    green  = 51,204,94
    orange = 255,136,0
    

Be careful not to create infinite lookup loops — these produce an error.

    
    
    # don't do this
    favourite = green
    green     = favourite
    

### color lists

A color list can be defined by specifying a comma-delimited list of existing
colors

    
    
    red_list = dred,red,lred,vlred
    

or, more conveniently, a regular expression. The results will be sorted by the
value of any capture buffers. The order will be reasonable (numerically or
alphanumerically depending on the value of the capture buffer). If you want to
sort the matches in reverse, wrap the regular expression in `rev(`).

For example, to create a list of the 9-color spectral Brewer palette,

    
    
    spectral9 = spectral-9-div-(\d+)
    

and to create a reversed list

    
    
    spectral9r = rev(spectral-9-div-(\d+))
    

Color lists are used with [heat
maps](/documentation/tutorials/lessons/2d_tracks/heat_maps/).

### Brewer palette Lists

Lists for all [Brewer palettes](https://www.colorbrewer.org) are predefined
(see `etc/brewer.lists.conf`). For a given color set `name-ncolors-type-
index`, two lists are available

  * `name-ncolors-type` Brewer palette color list (e.g. `reds-8-seq = reds-8-seq-1,reds-8-seq-2,...`) 
  * `name-ncolors-type-rev` corresponding palette, with colors in reverse order (e.g. `reds-8-seq-rev = reds-8-seq-8,reds-8-seq-7,...`) 

For example, the 6-color Brewer palette lists that are defined are

    
    
    # sequential
    blues-6-seq
    bugn-6-seq
    bupu-6-seq
    gnbu-6-seq
    greens-6-seq
    greys-6-seq
    oranges-6-seq
    orrd-6-seq
    pubu-6-seq
    pubugn-6-seq
    purd-6-seq
    purples-6-seq
    rdpu-6-seq
    reds-6-seq
    ylgn-6-seq
    ylgnbu-6-seq
    ylorbr-6-seq
    ylorrd-6-seq
    
    # diverging
    brbg-6-div
    piyg-6-div
    prgn-6-div
    puor-6-div
    rdbu-6-div
    rdgy-6-div
    rdylbu-6-div
    rdylgn-6-div
    spectral-6-div
    
    # qualitative
    accent-6-qual
    dark2-6-qual
    paired-6-qual
    pastel1-6-qual
    pastel2-6-qual
    set1-6-qual
    set2-6-qual
    set3-6-qual
    

Each has a `-rev` (reversed) counterpart (e.g. `spectral-6-div` and
`spectral-6-div-rev`).

These lists are automatically imported from `etc/colors.brewer.lists.conf` via
`etc/colors.brewer.conf`. Thus, if you import the Brewer colors (done by
default), you are automatically including all Brewer lists.

### HSV color lists

Brewer palettes provide sets of perceptually uniform colors and should be used
whenever possible (i.e., _always_).

Additionally, color sets of pure HSV colors (s = 1, v = 1) are defined in
`colors.hsv.conf`. Two kind of HSVG color lists are defined.

Lists of colors by hue step are named hue-sH, for a set of colors that vary by
a change in hue of H. For example, `hue-s45` includes the colors `hue000`,
`hue045`, `hue090`, `hue135`, `hue180`, `hue225`, `hue270`, `hue315`. Lists
for steps 2, 3, 4, 5, 6, 8, 9, 10, 12, 15, 18, 20, 24, 30, 36, 40, 45, 60, 72,
90, 120, 180 and 360 are defined.

The other set of lists are named hue-N, for a set of N uniformly spaced
colors. For example, `hue-7` includes the colors `hue000`, `hue051`, `hue103`,
`hue154`, `hue206`, `hue257`, and `hue309`. Lists for 3 to 30 colors are
defined.

### color list cache

Generating the color lists can take several seconds. For this reason, Circos
employs a caching mechanism to store color lists definitions. By default, the
cache file is `/tmp/circos.colorlist.dat`. If the cache is older than the
configuration file, or color definitions, it is recomputed. The length of time
required is a function of the total number of colors (color definitions
multiplied by automatic transparency levels) and the number of lists. If you
are trying to optimize image generation speed, and do not wish to count on
caching, remove any list definitions you are not using and reduce the number
of automatic transparency levels.

### chromosome color scheme

A set of colors named after chromosomes is also defined and corresponds to the
chromosome color scheme used by [UCSC Genome Browser](https://genome.ucsc.edu)
and other online resources. This is a standardized palette.

    
    
    chr1 = 153,102,0
    chr2 = 102,102,0
    chr3 = 153,153,30
    ...
    chrX = 153,153,153
    chrY = 204,204,204
    

Another set of colors is named after cytogenetic band colors, typically
reported in karyotype files. These colors define the G-staining shades seen in
ideograms.

    
    
    gpos100 = 0,0,0
    gpos    = 0,0,0
    gpos75  = 130,130,130
    gpos66  = 160,160,160
    gpos50  = 200,200,200
    gpos33  = 210,210,210
    gpos25  = 200,200,200
    gvar    = 220,220,220
    gneg    = 255,255,255
    acen    = 217,47,39
    stalk   = 100,127,164
    

### creating your own colors

I strongly suggest that you place new color definitions in a separate file.
Modularity will make maintenance easier. And given that you'll likely want
access to your custom colors for all images, include them globally rather than
on an image-by-image basis.

For example, if you create your own blue

    
    
    # in mycolors.conf
    niceblue = 17,111,227
    

you can include this file like this

    
    
    # all default color definitions
    <<include colors_fonts_patterns.conf>>
    
    # this will append your definitions to the <colors> block
    <colors>
    <<include mycolors.conf>>
    </colors>
    

You can quickly add colors directly

    
    
    # all default color definitions
    <<include colors_fonts_patterns.conf>>
    
    # this will append your definitions to the <colors> block
    <colors>
    <<include mycolors.conf>>
    niceblue2 = 37,101,179
    </colors>
    

## fonts

Circos uses CMU Modern fonts. These are found in `fonts/` in the distribution
and are associated with unique definitions (e.g. light, bold, italic) used in
configuration files.

    
    
    light          = fonts/modern/cmunbmr.otf # CMUBright-Roman
    normal         = fonts/modern/cmunbmr.otf # CMUBright-Roman
    default        = fonts/modern/cmunbmr.otf # CMUBright-Roman
    semibold       = fonts/modern/cmunbsr.otf # CMUBright-Semibold
    bold           = fonts/modern/cmunbbx.otf # CMUBright-Bold
    italic         = fonts/modern/cmunbmo.otf # CMUBright-Oblique
    bolditalic     = fonts/modern/cmunbxo.otf # CMUBright-BoldOblique
    italicbold     = fonts/modern/cmunbxo.otf # CMUBright-BoldOblique
    

To use a specific font for an element, specify its label (e.g. normal, bold)
in the configuration file. The default fonts are [shown here](images).

To add your own fonts, copy the TTF file to `fonts/` and add a new label to
the font in the `fonts.conf` configuration.

To render very small labels, you should consider using bitmapped fonts. These
fonts are designed to be used at a specific size and without anti-aliasing.
One such family is the Mini Font set from
[minifonts.com](https://www.minifonts.com).

Other legible fonts, commonly used in terminals and text editors are

  * andale mono 
  * anonymous 
  * aurulent sans mono 
  * vera sans mono 
  * courier 
  * dejavu sans mono 
  * droid sans mono 
  * inconsolata 
  * liberation mono 
  * lucida console 
  * lucida typewriter 
  * monofur 
  * pragmata 
  * profont 
  * proggy 
  * saxmono 
  * the sans mono 

These fonts are shown in the [image](images) section of this tutorial.

## gddiag

If you suspect there may be a problem with drawing images, please run

    
    
    > bin/gddiag
    

and look at the output `gddiag.png`. It should look like the [image in this
tutorial](images).

### units

Many quantities defined in the configuration files require units, which are
one of

  * b (bases) - used to indicate distance along the ideogram 
  * p (pixels) - used for quantities defined in absolute pixel size, such as track radius, label size, glyph size, and others. 
  * r (relative) - quantifies a parameter relative to another value, which is sometimes more intuitive than using absolute pixel values. For example, label radial padding is relative to label width and label angular padding is relative to label height 
  * u (chromosome units) - special relative unit which expresses distance long ideogram in terms of the chromosomes_unit value 
  * n (no unit) - explicit suffix for unitless values 

Unit designations are suffixed to the value and may be mixed

    
    
    # 1 pixel padding
    padding = 1p 
    # relative padding (e.g. relative to label width)
    padding = -0.25r
    
    # radius of track (relative to inner ideogram radius)
    r0 = 0.5r
    # combination of relative and pixel values
    r1 = 0.5r+200p
    

The reason why Circos insists on units is to reduce the strain of interpreting
the configuration file parameters - a large number of custom values can
quickly make the file opaque to quick inspection.

