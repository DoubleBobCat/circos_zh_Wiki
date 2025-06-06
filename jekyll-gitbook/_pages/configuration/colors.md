---
author: DoubleCat
date: 2025-04-11
layout: post
category: configuration
title: Colors
---

### lesson
[Lesson](/documentation/tutorials/configuration/colors/lesson)
[Images](/documentation/tutorials/configuration/colors/images)

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

### color definitions
#### RGB and HSV
Colors are defined using RGB or HSV values.

```    
    red = 255,0,0    # RGB definition
    red = hsv(0,1,1) # HSV definition
```
The range of RGB components is `[0..255]`. HSV values range is `H=[0,360]`
(integer), `S=[0,1]` (float) and `V=[0,1]` (float).

#### transparent RGB values
RGB values can have an optional 4th field to indicate transparency. The
transparency can be specified in the range [0,1] or [0,127]. Both map onto the
same result. The minimum value (0) indicates full opacity while the maximum (1
or 127) indicates full transparency.

```    
    # 0 < alpha < 1 
    # 0 opaque
    # 1 transparent
    red_faint = 255,0,0,0.8
    
    # or 
    #
    # 0 < alpha < 127
    # 0   opaque
    # 127 transparent
    red_also_faint = 255,0,0,102
```
Please see [Transparent
Link](/documentation/tutorials/recipes/transparent_links/) tutorial for
discussion about automating definition of these colors.

##### full transparency
To create a fully transparent color (e.g. for an image with transparent
background), you'll need to define a color named `transparent`. A transparent
color still requires an RGB value (a strange artefact in gd implementation).
Choose an RGB value that you aren't using elsewhere. Typically something like
`1,0,0` will be suitable.

```    
    # in color.conf
    transparent = 1,0,0
```
The transparent color will be available using the name `transparent`. A
synonym `clear` is also provided. To use the transparent color (e.g. for
background),

```    
    <image>
    ...
    background = transparent # 'clear' also works here 
    ...
    </image>
```
The names `transparent` and `clear` are reserved. Do not use these two color
names for other colors.

#### synonyms
You can include synonyms for colors, by defining one color using the name of
another color, instead of RGB or RGBA values.

```    
    green  = 51,204,94
    orange = 255,136,0
    ...
    favourite        = green
    almost_favourite = orange
```
Be careful not to create infinite lookup loops — these produce an error.

```    
    # don't do this
    favourite = green
    green     = favourite
```
### <color> block
The <colors> block contains all the color definitions.

Circos comes with a large number of default color definitions (pure colors and
hues, Brewer palettes, UCSC chromosome color schemes, luminance-normalized
colors, etc). You should always include these in your configuration, unless
you have a good reason not to.

The best way to do this is to import the `etc/colors_fonts_patterns.conf` in
your `circos.conf`. Importing this file will define colors, fonts and
patterns, using the appropriate block structure.

```    
    # circos.conf
    <<include etc/colors_fonts_patterns.conf>>
```
For example, `etc/colors_fonts_patterns.conf` contains the following

```    
    <colors>
    <<include etc/colors.conf>>
    </colors>
```
In turn, `etc/colors.conf` has the following definitions

```    
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
```
### using colors
Colors are referenced using their RGB values or their names (see below).

```    
    # using RGB values
    color = 107,174,241
    
    # using name
    color = blue
```
When passing a color as an option in data files, the RGB values need to be
delimited by `(...)`. For example, if you want to add a color to a link

```    
    # using a color name
    chr1 100 200 chr2 200 250 color=blue,thickness=2
    
    # using RGB value
    chr1 100 200 chr2 200 250 color=(107,174,241),thickness=2
```
### predefined colors
#### named colors with tone prefix
For each of the named colors `red`, `orange`, `yellow`, `green`, `blue`, and
`purple`, the following are defined

```    
    vvl{name} - very very light version of color
    vl{name}  - very light
    l{name}   - light
    {name}    - default tone
    d{name}   - dark
    vd{name}  - very dark
    vvd{name} - very very dark
```
The tone ladder is based on Brewer palette colors (see below).

```    
    # points to Brewer color...
    orange = oranges-7-seq-4
    
    # ...which is defined in colors.brewer.conf as
    oranges-7-seq-4 = 253,141,60
```
For example, for `red` we have `vvlred`, `vlred`, `lred`, `red`, `dred`,
`vdred` and `vvdred`.

```    
    vvlred = reds-7-seq-1
    vlred  = reds-7-seq-2
    lred   = reds-7-seq-3
    red    = reds-7-seq-4
    dred   = reds-7-seq-5
    vdred  = reds-7-seq-6
    vvdred = reds-7-seq-7
```
In the case of grey, additional `vvvlgrey` and `vvvdgrey` are available.

Also defined are `white` and `black`.

#### named pure colors with tone prefix
For pure color versions of the above definitions (i.e. not based on Brewer
palettes), use the `p` (pure) prefix to the color name.

```    
    vvlp{name} - very very light version of color
    vlp{name}  - very light
    lp{name}   - light
    p{name}    - default tone
    dp{name}   - dark
    vdp{name}  - very dark
    vvdp{name} - very very dark
```
For example, for `red` we have `vvlpred`, `vlpred`, `lpred`, `pred`, `dpred`,
`vdpred` and `vvdpred`.

```    
    # pure orange
    porange  = 255,127,0
    
    # dark pure orange
    dporange = 234,110,0
```
#### Brewer colors
Brewer colors compose [Brewer palettes](https://www.colorbrewer.org) which
have been manually defined by Cynthia Brewer for their perceptual properties.

Brewer colors are categorized into one of three palette types: sequential,
diverging and qualitative. For a given palette type (e.g. sequential), there
are a variety of palettes (e.g. reds, greens, blues). Each palette is
available for various number of colors (e.g. 3, 4, 5, ...).

The syntax for a Brewer color name is `palettename-ncolors-palettetype-index`.
The palette names, for each type, are

```    
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
```
For example, purple-orange diverging 9-color palette colors are
`puor-9-div-1`, `puor-9-div-2`, ..., `puor-9-div-9`.

I suggest that you try using the Brewer colors (e.g. `orange` vs `porange`),
because they are perceptually uniform. However, they will appear less punchy
and saturated than their pure equivalents. In particular, the Brewer reds may
appear pinkish and light when used on their own.

Experiment, but be aware of the perceptual aspects of color, which will
influence how your figure is perceived (see my [Color Palettes
Matter](https://mk.bcgsc.ca/brewer/talks/color-palettes-brewer.pdf)
presentation).

#### HSV colors
You can use the HSV color space to define colors. To do so, specify the HSV
values as hsv(h,s,v). For example,

```    
    red = hsv(0,1,1)
```
All pure HSV colors (s = 1, v = 1) are defined in `colors.hsv.conf`.

```    
    hue000 = hsv(0,1,1)
    hue001 = hsv(1,1,1)
    ...
    hue359 = hsv(359,1,1)
    hue360 = hsv(360,1,1) # same as hue000
```
#### chromosome color scheme
A set of colors named after chromosomes is also defined and corresponds to the
chromosome color scheme used by [UCSC Genome Browser](https://genome.ucsc.edu)
and other online resources. This is a standardized palette.

```    
    chr1 = 153,102,0
    chr2 = 102,102,0
    chr3 = 153,153,30
    ...
    chrX = 153,153,153
    chrY = 204,204,204
```
Another set of colors is named after cytogenetic band colors, typically
reported in karyotype files. These colors define the G-staining shades seen in
ideograms.

```    
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
```
Because the original UCSC color palette is not uniform in brightness (e.g.
chr10 is a very bright yellow, whereas chr1 is a dark brown), I make
luminance-normalized (70, 80 and 90%) versions of these colors available.

```    
    # 70% luminance
    lum70chr1
    ...
    lum70chrY
    
    # 80% luminance
    lum80chr1
    ...
    lum80chrY
    
    # 90% luminance
    lum90chr1
    ...
    lum90chrY
```
Given that Circos uses species prefix for chromosome names (e.g. human
chromosomes are named `hsN` rather than `chrN`, I also provide synonyms for
all the UCSC colors using the `chr` -> `hs` name.

```    
    hs1 = chr1
    hs2 = chr2
    ...
    lum70hs1 = lum70chr1
    lum90hs1 = lum80chr1
    lum90hs1 = lum90chr1
    ...
```
#### unix colors
The file `etc/colors.unixnames.txt` defines a large number (700+) of named
colors, taken from UNIX's [rgb.txt
file](https://www.uize.com/examples/sortable-color-table.html). This file is
_not_ included by default.

Many definitions in this file duplicate definitions in `colors.conf` (e.g.
`colors.unixnames.txt` defines blue as 0,0,255 but in `colors.conf` it is
blues-7-seq-4, which is 107,174,214). Including `colors.unixnames.txt`
together with (colors.conf) will result in an error.

### color lists
A color list can be defined by specifying a comma-delimited list of existing
colors

```    
    red_list = dred,red,lred,vlred
```
or, more conveniently, a regular expression. The results will be sorted by the
value of any capture buffers. The order will be reasonable (numerically or
alphanumerically depending on the value of the capture buffer). If you want to
sort the matches in reverse, wrap the regular expression in `rev(`).

For example, to create a list of the 9-color spectral Brewer palette,

```    
    spectral9 = spectral-9-div-(\d+)
```
and to create a reversed list

```    
    spectral9r = rev(spectral-9-div-(\d+))
```
Color lists are used with [heat
maps](/documentation/tutorials/lessons/2d_tracks/heat_maps/).

#### Brewer palette Lists
Lists for all [Brewer palettes](https://www.colorbrewer.org) are predefined
(see `etc/brewer.lists.conf`). For a given color set `name-ncolors-type-
index`, two lists are available

  * `name-ncolors-type` Brewer palette color list (e.g. `reds-8-seq = reds-8-seq-1,reds-8-seq-2,...`) 
  * `name-ncolors-type-rev` corresponding palette, with colors in reverse order (e.g. `reds-8-seq-rev = reds-8-seq-8,reds-8-seq-7,...`) 

For example, the 6-color Brewer palette lists that are defined are

```    
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
```
Each has a `-rev` (reversed) counterpart (e.g. `spectral-6-div` and
`spectral-6-div-rev`).

These lists are automatically imported from `etc/colors.brewer.lists.conf` via
`etc/colors.brewer.conf`. Thus, if you import the Brewer colors (done by
default), you are automatically including all Brewer lists.

##### HSV color lists
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

##### color list cache
Generating the color lists can take several seconds. For this reason, Circos
employs a caching mechanism to store color lists definitions. By default, the
cache file is `/tmp/circos.colorlist.dat`. If the cache is older than the
configuration file, or color definitions, it is recomputed. The length of time
required is a function of the total number of colors (color definitions
multiplied by automatic transparency levels) and the number of lists. If you
are trying to optimize image generation speed, and do not wish to count on
caching, remove any list definitions you are not using and reduce the number
of automatic transparency levels.

### creating your own colors
I strongly suggest that you place new color definitions in a separate file.
Modularity will make maintenance easier. And given that you'll likely want
access to your custom colors for all images, include them globally rather than
on an image-by-image basis.

For example, if you create your own blue

```    
    # in mycolors.conf
    niceblue = 17,111,227
```
you can include this file like this

```    
    # all default color definitions
    <<include colors_fonts_patterns.conf>>
    
    # this will append your definitions to the <colors> block
    <colors>
    <<include mycolors.conf>>
    </colors>
```
You can quickly add colors directly

```    
    # all default color definitions
    <<include colors_fonts_patterns.conf>>
    
    # this will append your definitions to the <colors> block
    <colors>
    <<include mycolors.conf>>
    niceblue2 = 37,101,179
    </colors>
```### images
[Lesson](/documentation/tutorials/configuration/colors/lesson)
[Images](/documentation/tutorials/configuration/colors/images)

![Circos tutorial image -
Colors](/documentation/tutorials/configuration/colors/img/image-01.png)
![Circos tutorial image -
Colors](/documentation/tutorials/configuration/colors/img/image-02.png)
![Circos tutorial image -
Colors](/documentation/tutorials/configuration/colors/img/image-03.png)
### configuration
[Lesson](/documentation/tutorials/configuration/colors/lesson)
[Images](/documentation/tutorials/configuration/colors/images)
