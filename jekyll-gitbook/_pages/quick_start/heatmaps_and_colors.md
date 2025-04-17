---
author: DoubleCat
date: 2025-04-11
layout: post
category: quick_start
title: Heat Maps & Colors
---

### lesson
Heat maps are used for data types which associate a value with a genomic
position, or region. As such, this track uses the same data format as
histograms.

The track linearly maps a range of values `[min,max]` onto a list of colors
`c[n], i=0..N`.

```    
    f = (value - min) / ( max - min )
    n = 0      if f < 0 
        N      if f > 1 
        N * f  otherwise
```
The track shares many of the same format parameters with a histogram. As
usual, you need to define the `type`, `file` and `r0/r1` parameters.

```    
    <plot>
    type  = heatmap
    file  = data/5/segdup.hs1234.heatmap.txt
    r1    = 0.89r
    r0    = 0.88r
    </plot>
```
#### linear vs power scaling
If scale_log_base is used, the mapping is not linear, but a power law

```    
    n = N * f**(1/scale_log_base)
```
When scale_log_base > 1 the dynamic range for values close to min is expanded.
When scale_log_base < 1 the dynamic range for values close to max is expanded.

```    
    scale_log_base = 5
```
#### colors
Heat map colors are defined by a combination of CSV or color lists.

In this tutorial, the heat map color range is made up of 5 levels of
transparency of chromosome colors, plus a fully opaque version of the color.

```    
    color = hs1_a5,hs1_a4,hs1_a3,hs1_a2,hs1_a1,hs1
```
A large number of colors and color lists are defined by default (see
`etc/colors.conf` in the Circos distribution.

##### common colors
Common colors (red, green, blue, purple, orange, yellow, grey) are defined in
7 tones. Where possible, these are taken from [Brewer
palletes](https://www.colorbrewer.org).

```    
    vvlHUE very very light HUE (e.g. vvlred)
     vlHUE      very light     
      lHUE           light
       HUE
      dHUE           dark
     vdHUE      very dark
    vvdHUE very very dark
```
Colors `white` and `black` are also defined, as is `transparent`.

##### cytogenetic band colors
Colors for conventional cytogenetic band patterns are defined

```    
    gposNNN # NNN = 25, 33, 50, 66, 75, 100
    gpos
    gvar
    gneg
    acen
    stalk
```
##### human chromosome color scheme
The UCSC browser uses a conventional color scheme for human chromosomes. These
colors are defined as

```    
    chr1
    chr2
    ...
    chr22
    chrx
    chry
    chrm
    chrun
```
Synonyms with `hs` prefix are also defined (e.g. `chr1` and `hs1`).

Luminance corrected chromosome palettes are defined for L= 70, 80 and 90

```    
    lumLchr* # L=70,80,90   e.g. lum70chr1 lum90chr11
```
##### brewer palettes
All [Brewer pallete](https://www.colorbrewer.org) colors are available through
the syntax

```    
    PALETTE-N-TYPE-M
```
for color M (M=1..N) in the N-color brewer palette `PALETTE` of type `TYPE`
(`TYPE=seq|div|qual`). For each `PALETTE`, there are several versions for
different values of `N=I..J`.

```    
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
```
##### pure hues
For each pure hue H in HSV space, the color hueHHH is defined

```    
    hue000
    hue001
    hue002
    ...
    hue359
    hue360
```
##### Color lists
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

##### transparency
Color transparency is specified using the suffix `_aN` for transparency level
`N`. The number of allowable levels is controled by the `auto_alpha_steps`
parameter in `etc/image.generic.conf`. By default this is set to 5 which
allows for 5 levels of transparency

```    
    green    fully opaque
    green_a1 16% transparent
    green_a2 33% transparent
    green_a3 50% transparent
    green_a4 66% transparent
    green_a5 83% transparent
```### images
![Circos tutorial image - Heat Maps &
Colors](/documentation/tutorials/quick_start/heatmaps_and_colors/img/01.png)
### configuration
#### circos.conf
```    
    # 1.7 HEAT MAPS
    
    karyotype = data/karyotype/karyotype.human.txt
    chromosomes_units = 1000000
    
    chromosomes_display_default = no
    chromosomes                 = /hs[1234]$/
    chromosomes_radius          = hs4:0.9r
    
    <colors>
    chr1* = red
    chr2* = orange
    chr3* = green
    chr4* = blue
    </colors>
    
    chromosomes_reverse = /hs[234]/
    chromosomes_scale   = hs1=0.5r,/hs[234]/=0.5rn
    
    <plots>
    
    # Heat maps are used for data types which associate a value with a
    # genomic position, or region. As such, this track uses the same data
    # format as histograms.
    #
    # The track linearly maps a range of values [min,max] onto a list of colors c[n], i=0..N.
    #
    # f = (value - min) / ( max - min )
    # n = N * f
    
    <plot>
    type  = heatmap
    file  = data/5/segdup.hs1234.heatmap.txt
    r1    = 0.89r
    r0    = 0.88r
    
    # Colors are defined by a combination of lists or CSV. Color lists
    # exist for all Brewer palletes (see etc/colors.brewer.lists.conf) as
    # well as for N-step hue (hue-sN, e.g. hue-s5 =
    # hue000,hue005,hue010,...) and N-color hue (hue-sN, e.g. hue-3 =
    # hue000,hue120,hue140).
    
    color = hs1_a5,hs1_a4,hs1_a3,hs1_a2,hs1_a1,hs1
    
    # If scale_log_base is used, the mapping is not linear, but a power law 
    #
    # n = N * f**(1/scale_log_base)
    #
    # When scale_log_base > 1 the dynamic range for values close to min is expanded. 
    # When scale_log_base < 1 the dynamic range for values close to max is expanded. 
    
    scale_log_base = 0.25
    
    <rules>
    <<include rule.exclude.hs1.conf>>
    </rules>
    
    </plot>
    
    # The other three heatmap tracks are the same as the one above, except
    # that each uses a different color list and var(id) condition to show
    # the number of links to/from hs2, hs3 and hs4.
    
    <plot>
    type  = heatmap
    file  = data/5/segdup.hs1234.heatmap.txt
    r1    = 0.90r
    r0    = 0.89r
    color = hs2_a5,hs2_a4,hs2_a3,hs2_a2,hs2_a1,hs2
    scale_log_base = 0.25
    
    <rules>
    <<include rule.exclude.hs1.conf>>
    
    # Show only data points that have id=hs2
    <rule>
    condition = var(id) ne "hs2"
    show      = no
    </rule>
    
    </rules>
    
    </plot>
    
    <plot>
    type  = heatmap
    file  = data/5/segdup.hs1234.heatmap.txt
    r1    = 0.91r
    r0    = 0.90r
    color = hs3_a5,hs3_a4,hs3_a3,hs3_a2,hs3_a1,hs3
    scale_log_base = 0.25
    
    <rules>
    <<include rule.exclude.hs1.conf>>
    
    # Show only data points that have id=hs3 
    <rule>
    condition = var(id) ne "hs3"
    show      = no
    </rule>
    
    </rules>
    
    </plot>
    
    <plot>
    type  = heatmap
    file  = data/5/segdup.hs1234.heatmap.txt
    r1    = 0.92r
    r0    = 0.91r
    color = hs4_a5,hs4_a4,hs4_a3,hs4_a2,hs4_a1,hs4
    scale_log_base = 0.25
    
    <rules>
    <<include rule.exclude.hs1.conf>>
    
    # Show only data points that have id=hs4
    <rule>
    condition = var(id) ne "hs4"
    show      = no
    </rule>
    
    </rules>
    
    </plot>
    
    <plot>
    type = histogram
    file = data/5/segdup.hs1234.hist.txt
    r1   = 0.88r
    r0   = 0.81r
    
    fill_color = vdgrey
    extend_bin = no
    
    <rules>
    <<include rule.exclude.hs1.conf>>
    </rules>
    
    <<include backgrounds.conf>>
    
    </plot>
    
    <plot>
    type = histogram
    file = data/5/segdup.hs1234.stacked.txt
    r1   = 0.99r
    r0   = 0.92r
    fill_color  = hs1,hs2,hs3,hs4
    orientation = in
    extend_bin  = no
    
    <rules>
    <<include rule.exclude.hs1.conf>>
    </rules>
    
    <<include axes.conf>>
    
    </plot>
    
    </plots>
    
    <links>
    
    <link>
    file          = data/5/segdup.txt
    radius        = 0.8r
    bezier_radius = 0r
    color         = black_a4
    thickness     = 2
    
    <rules>
    <<include rules.link.conf>>
    </rules>
    
    </link>
    
    </links>
    
    <<include ideogram.conf>>
    <<include ticks.conf>>
    
    <image>
    <<include etc/image.conf>>                
    </image>
    
    <<include etc/colors_fonts_patterns.conf>> 
    <<include etc/housekeeping.conf>> 
    data_out_of_range* = trim
```
  

* * *

#### axes.conf
```    
    <axes>
    # Show axes only on ideograms that have data for this track
    show = data
    
    thickness = 1
    color     = lgrey
    <axis>
    spacing   = 0.1r
    </axis>
    <axis>
    spacing   = 0.2r
    color     = grey
    </axis>
    <axis>
    position  = 0.5r
    color     = red
    </axis>
    <axis>
    position  = 0.85r
    color     = green
    thickness = 2
    </axis>
    
    </axes>
```
  

* * *

#### backgrounds.conf
```    
    <backgrounds>
    # Show the backgrounds only for ideograms that have data
    show  = data
    <background>
    color = vvlgrey
    </background>
    <background>
    color = vlgrey
    y0    = 0.2r
    y1    = 0.5r
    </background>
    <background>
    color = lgrey
    y0    = 0.5r
    y1    = 0.8r
    </background>
    <background>
    color = grey
    y0    = 0.8r
    </background>
    
    </backgrounds>
```
  

* * *

#### ideogram.conf
```    
    <ideogram>
    
    <spacing>
    default = 0.005r
    </spacing>
    
    # Ideogram position, fill and outline
    radius           = 0.90r
    thickness        = 20p
    fill             = yes
    stroke_color     = dgrey
    stroke_thickness = 2p
    
    # Minimum definition for ideogram labels.
    
    show_label       = yes
    # see etc/fonts.conf for list of font names
    label_font       = default 
    label_radius     = 1.075r  # if ideogram radius is constant, and you'd like labels close to image edge, 
                               # use the dims() function to access the size of the image
                               # label_radius  = dims(image,radius) - 60p
    label_size       = 30
    label_parallel   = yes
    
    </ideogram>
``````
  

* * *

#### rule.exclude.hs1.conf
```    
    <rule>
    condition = on(hs1)
    show      = no
    </rule>
```
  

* * *

#### rules.link.conf
```    
    <rule>
    condition     = var(intrachr)
    show          = no
    </rule>
    <rule>
    condition     = 1
    color         = eval(var(chr2))
    flow          = continue
    </rule>
    <rule>
    condition     = from(hs1)
    radius1       = 0.99r
    </rule>
    <rule>
    condition     = to(hs1)
    radius2       = 0.99r
    </rule>
```
  

* * *

#### ticks.conf
```    
    show_ticks          = yes
    show_tick_labels    = yes
    
    <ticks>
    radius           = 1r
    color            = black
    thickness        = 2p
    
    # the tick label is derived by multiplying the tick position
    # by 'multiplier' and casting it in 'format':
    #
    # sprintf(format,position*multiplier)
    #
    
    multiplier       = 1e-6
    
    # %d   - integer
    # %f   - float
    # %.1f - float with one decimal
    # %.2f - float with two decimals
    #
    # for other formats, see https://perldoc.perl.org/functions/sprintf.html
    
    format           = %d
    
    <tick>
    spacing        = 5u
    size           = 10p
    </tick>
    
    <tick>
    spacing        = 25u
    size           = 15p
    show_label     = yes
    label_size     = 20p
    label_offset   = 10p
    format         = %d
    </tick>
    
    </ticks>
```
  

* * *
