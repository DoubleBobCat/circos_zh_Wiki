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

# 2 — Quick Start

## 7\. Heat maps

[Lesson](/documentation/tutorials/quick_start/heatmaps_and_colors/lesson)
[Images](/documentation/tutorials/quick_start/heatmaps_and_colors/images)
[Configuration](/documentation/tutorials/quick_start/heatmaps_and_colors/configuration)

Heat maps are used for data types which associate a value with a genomic
position, or region. As such, this track uses the same data format as
histograms.

The track linearly maps a range of values `[min,max]` onto a list of colors
`c[n], i=0..N`.

    
    
    f = (value - min) / ( max - min )
    n = 0      if f < 0 
        N      if f > 1 
        N * f  otherwise
    

The track shares many of the same format parameters with a histogram. As
usual, you need to define the `type`, `file` and `r0/r1` parameters.

    
    
    <plot>
    type  = heatmap
    file  = data/5/segdup.hs1234.heatmap.txt
    r1    = 0.89r
    r0    = 0.88r
    </plot>
    

### linear vs power scaling

If scale_log_base is used, the mapping is not linear, but a power law

    
    
    n = N * f**(1/scale_log_base)
    

When scale_log_base > 1 the dynamic range for values close to min is expanded.
When scale_log_base < 1 the dynamic range for values close to max is expanded.

    
    
    scale_log_base = 5
    

### colors

Heat map colors are defined by a combination of CSV or color lists.

In this tutorial, the heat map color range is made up of 5 levels of
transparency of chromosome colors, plus a fully opaque version of the color.

    
    
    color = hs1_a5,hs1_a4,hs1_a3,hs1_a2,hs1_a1,hs1
    

A large number of colors and color lists are defined by default (see
`etc/colors.conf` in the Circos distribution.

#### common colors

Common colors (red, green, blue, purple, orange, yellow, grey) are defined in
7 tones. Where possible, these are taken from [Brewer
palletes](https://www.colorbrewer.org).

    
    
    vvlHUE very very light HUE (e.g. vvlred)
     vlHUE      very light     
      lHUE           light
       HUE
      dHUE           dark
     vdHUE      very dark
    vvdHUE very very dark
    

Colors `white` and `black` are also defined, as is `transparent`.

#### cytogenetic band colors

Colors for conventional cytogenetic band patterns are defined

    
    
    gposNNN # NNN = 25, 33, 50, 66, 75, 100
    gpos
    gvar
    gneg
    acen
    stalk
    

#### human chromosome color scheme

The UCSC browser uses a conventional color scheme for human chromosomes. These
colors are defined as

    
    
    chr1
    chr2
    ...
    chr22
    chrx
    chry
    chrm
    chrun
    

Synonyms with `hs` prefix are also defined (e.g. `chr1` and `hs1`).

Luminance corrected chromosome palettes are defined for L= 70, 80 and 90

    
    
    lumLchr* # L=70,80,90   e.g. lum70chr1 lum90chr11
    

#### brewer palettes

All [Brewer pallete](https://www.colorbrewer.org) colors are available through
the syntax

    
    
    PALETTE-N-TYPE-M
    

for color M (M=1..N) in the N-color brewer palette `PALETTE` of type `TYPE`
(`TYPE=seq|div|qual`). For each `PALETTE`, there are several versions for
different values of `N=I..J`.

    
    
            I J
    
    TYPE=seq
    blues   3 9 
    bugn    3 9 # blue-green
    bupu    3 9 # blue-purple
    gnbu    3 9 # green-blue
    greens  3 9 
    greys   3 9
    oranges 3 9
    orrd    3 9 # orange-red
    pubu    3 9 # purple-blue
    pubugn  3 9 # purple-blue-green
    purd    3 9 # purple-red
    purples 3 9
    rdpu    3 9 # red-purple
    reds    3 9 
    ylgn    3 9 # yellow-green
    ylgnbu  3 9 # yellow-green-blue
    ylorbr  3 9 # yellow-orange-brown
    ylorrd  3 9 # yellow-orange-red
    
      e.g. blues-9-seq-3 (3rd color in 9 color blues palette)
           rdpu-3-seq-1 (1st color in 3 color red-purple sequential palette)
    
    TYPE=div
    brbg     3 11 # brown-blue-green
    piyg     3 11 # pink-yellow-green
    prgn     3 11 # purple-green
    puor     3 11 # purple-orange
    rdbu     3 11 # red-blue
    rdgy     3 11 # red-green
    rdylbu   3 11 # red-yellow-blue
    rdylgn   3 11 # red-yellow-green
    spectral 3 11 # rainbow: red-orange-yellow-green-blue
    
      e.g. piyg-11-div-2 (2rd color in 11 color pink-yellow-green diverging palette)
    
    TYPE=qual
    accent   3 8
    dark2    3 8
    paired   3 12
    pastel1  3 9
    pastel2  3 8
    set1     3 9
    set2     3 8
    set3     3 12
    
      e.g. set1-5-qual-1 (1st color in 5 color set1 qualitative palette)
    

#### pure hues

For each pure hue H in HSV space, the color hueHHH is defined

    
    
    hue000
    hue001
    hue002
    ...
    hue359
    hue360
    

#### Color lists

Color lists are named sets of colors used for parameters which accept a list
(e.g. heat map `color` parameter).

Lists exist for all Brewer palettes, of the format `PALETTE-N-TYPE`. For
example, `reds-5-seq`, `spectral-7-div` and `set3-5-qual` are all lists.

Pure hue lists are available, `hue-sN`, for each hue step of N (e.g. `hue-s2`,
`hue-s5`, ...). For example, `hue-s5` list is made up of the colors `hue000`,
`hue005`, `hue010`, `hue015`, and so on.

N-color hue lists are available as `hue-N` (e.g. `hue-3`, `hue-10`, ...). For
example, `hue-10` is made up of the 10 colors `hue000`, `hue036`, `hue072`,
... `hue324`. It is the same list as `hue-s32`.

#### transparency

Color transparency is specified using the suffix `_aN` for transparency level
`N`. The number of allowable levels is controled by the `auto_alpha_steps`
parameter in `etc/image.generic.conf`. By default this is set to 5 which
allows for 5 levels of transparency

    
    
    green    fully opaque
    green_a1 16% transparent
    green_a2 33% transparent
    green_a3 50% transparent
    green_a4 66% transparent
    green_a5 83% transparent
    

