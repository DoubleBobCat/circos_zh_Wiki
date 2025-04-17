---
author: DoubleCat
date: 2025-04-11
layout: post
category: highlights
title: Recipe 2 - Focusing on a Genome Region
---

### lesson
In many of the examples in this series of tutorials, the highlights were used
to draw data sets, such as gene position. Highlights are very useful for
drawing data because you have a high degree of control in formatting each
highlight wedge.

In other cases, highlights are useful to help the eye focus on a part, or
parts, of your diagram.

All other data types, as well as tick mark grids, are placed on top of the
highlights.

#### continuing with the chromosome color scheme
For the first image in this section, I've prepared two highlight files. The
first file, recapitulates the chromosome size and uses the chromosome color
scheme.

```    
    hs1 0 247249719 fill_color=chr1
    hs2 0 242951149 fill_color=chr2
    hs3 0 199501827 fill_color=chr3
    hs4 0 191273063 fill_color=chr4
    hs5 0 180857866 fill_color=chr5
    hs6 0 170899992 fill_color=chr6
    hs7 0 158821424 fill_color=chr7
    hs8 0 146274826 fill_color=chr8
    hs9 0 140273252 fill_color=chr9
    hs10 0 135374737 fill_color=chr10
    hs11 0 134452384 fill_color=chr11
    hs12 0 132349534 fill_color=chr12
    hs13 0 114142980 fill_color=chr13
    hs14 0 106368585 fill_color=chr14
    hs15 0 100338915 fill_color=chr15
    hs16 0 88827254 fill_color=chr16
    hs17 0 78774742 fill_color=chr17
    hs18 0 76117153 fill_color=chr18
    hs19 0 63811651 fill_color=chr19
    hs20 0 62435964 fill_color=chr20
    hs21 0 46944323 fill_color=chr21
    hs22 0 49691432 fill_color=chr22
    hsX 0 154913754 fill_color=chrX
    hsY 0 57772954 fill_color=chrY
```
Using this file, I can recreate the ideogram size in chromosome-specific color
anywhere in the image. I've drawn two highlight tracks using this file.

The first track is drawn in side the circle from 0.5 to 1.0 times the inner
ideogram radius.

```    
    <highlight>
    file       = data/3/chr.highlights.txt
    r0 = 0.5r
    r1 = 1r
    </highlight>
```
The second track is drawn outside the circle, and includes a black stroke.

```    
    <highlight>
    file       = data/3/chr.highlights.txt
    stroke_thickness = 2
    stroke_color = black
    r0 = 1.1r
    r1 = 1.15r
    </highlight>
```
The second file stores the position of cytogenetic bands classified as
centromeres and stalks in the karyotype. This is a union of all coordinates
whose bands were labeled as acen or stalk.

```    
    hs1 121100000 128000000
    hs10 38800000 42100000
    hs11 51400000 56400000
    hs12 33200000 36500000
    hs13 3800000 8300000
    hs13 13500000 18400000
    hs14 3100000 6700000
    hs14 13600000 19100000
    hs15 3500000 7900000
    hs15 14100000 18400000
    hs16 34400000 40700000
    hs17 22100000 23200000
    hs18 15400000 17300000
    hs19 26700000 30200000
    hs2 91000000 95700000
    hs20 25700000 28400000
    hs21 2900000 6300000
    hs21 10000000 13200000
    hs22 3000000 6600000
    hs22 9600000 16300000
    hs3 89400000 93200000
    hs4 48700000 52400000
    hs5 45800000 50500000
    hs6 58400000 63400000
    hs7 57400000 61100000
    hs8 43200000 48100000
    hs9 46700000 60300000
    hsX 56600000 65000000
    hsY 11200000 12500000
```
This set of highlights is drawn on top of the previous, outer track and filled
white, effectively splitting the highlights along centromeres and stalks.

```    
    <highlight>
    file       = data/3/chr.hetero.highlights.txt
    stroke_thickness = 2
    stroke_color = black
    fill_color = white
    r0 = 1.1r
    r1 = 1.15r
    z = 10
    </highlight>
```
#### focus on genomic regions
If you have a figure in which certain genomic areas are of interest,
highlights are the best way to guide your audience's eyes.

For this example, I've created a data file with just a few highlights.

```    
    hs1 15000000 50000000
    hs2 100000000 150000000
    hs3 50000000 60000000
    hs3 80000000 90000000
    hs3 100000000 105000000
    hs14 0 106368585
```
Using this data set, I've drawn three sets of highlights that isolate these
regions. These are shown in the second image in this section. The first set of
highlights is light grey and spans 0.5r-1.0r radial region. These second falls
outside of the ideogram circle and is light yellow from 1.0r to 1.1r. The last
is light grey again from 1.1r to 1.15r.

Note that unless you are using ideogram highlights, Circos does not support
highlights that cross the circle of ideograms. I strongly advise against
setting r0<1 and r1>1 for a set of highlights :)
### images
![Circos tutorial image - Recipe 2 - Focusing on a Genome
Region](/documentation/tutorials/highlights/recipe2/img/01.png)
### configuration
#### circos.conf
```    
    <colors>
    <<include etc/colors.conf>>
    </colors>
    
    <fonts>
    <<include etc/fonts.conf>>
    </fonts>
    
    <<include ideogram.conf>>
    <<include ticks.conf>>
    
    karyotype   = data/karyotype.human.txt
    
    <image>
    dir = /tmp
    file  = circos-tutorial.png
    # radius of inscribed circle in image
    radius         = 1500p
    background     = white
    # by default angle=0 is at 3 o'clock position
    angle_offset   = -90
    </image>
    
    chromosomes_units           = 1000000
    
    # first image
    #chromosomes                 = hs1;hs2;hs3
    #chromosomes_breaks          = -hs1:120-145;-hs1:180-200
    #chromosomes_display_default = no
    
    # second image
    chromosomes = hs1;hs2;hs3;hs13;hs14;hs15
    
    <highlights>
    
    z          = 5
    
    # For the first image, the same highlight set is
    # drawn both inside and outside the ideogram
    # circle. Another highlight set is layered
    # on top of the outer highlight set.
    
    #<highlight>
    #file       = data/3/chr.highlights.txt
    #r0 = 0.5r
    #r1 = 1r
    #</highlight>
    
    #<highlight>
    #file       = data/3/chr.highlights.txt
    #stroke_thickness = 2
    #stroke_color = black
    #r0 = 1.1r
    #r1 = 1.15r
    #</highlight>
    
    #<highlight>
    #file       = data/3/chr.hetero.highlights.txt
    #stroke_thickness = 2
    #stroke_color = black
    #fill_color = white
    #r0 = 1.1r
    #r1 = 1.15r
    #z = 10
    #</highlight>
    
    # In the second image, selected regions of the
    # genome are singled out using several highlights.
    # Note that highlights do not radially cross the
    # ideograms. Highlights with r0 < 1 < r1 are not
    # supported (Circos will not always behave well in
    # these cases).
    
    <highlight>
    file       = data/3/highlights.few.txt
    r0 = 0.5r
    r1 = 1r
    fill_color = lgrey
    </highlight>
    
    <highlight>
    file       = data/3/highlights.few.txt
    r0 = 1r
    r1 = 1.10r
    fill_color = lyellow
    </highlight>
    
    <highlight>
    file       = data/3/highlights.few.txt
    r0 = 1.10r
    r1 = 1.15r
    fill_color = lgrey
    </highlight>
    
    </highlights>
    
    anglestep       = 0.025
    minslicestep    = 5
    beziersamples   = 40
    debug           = no
    warnings        = no
    imagemap        = no
    
    units_ok = bupr
    units_nounit = n
```
  

* * *

#### ideogram.conf
```    
    <ideogram>
    
    <spacing>
    
    default = 3u
    break   = 1u
    
    axis_break_at_edge = yes
    axis_break         = yes
    axis_break_style   = 2
    
    <break_style 1>
    stroke_color = black
    fill_color   = blue
    thickness    = 0.25r
    stroke_thickness = 2
    </break>
    
    <break_style 2>
    stroke_color     = black
    stroke_thickness = 3
    thickness        = 1.5r
    </break>
    
    </spacing>
    
    # thickness (px) of chromosome ideogram
    thickness        = 100p
    stroke_thickness = 2
    # ideogram border color
    stroke_color     = black
    fill             = yes
    # the default chromosome color is set here and any value
    # defined in the karyotype file overrides it
    fill_color       = black
    
    # fractional radius position of chromosome ideogram within image
    radius         = 0.85r
    show_label     = yes
    label_with_tag = yes
    label_font     = condensedbold
    label_radius   = dims(ideogram,radius) + 0.05r
    label_size     = 48
    
    # cytogenetic bands
    band_stroke_thickness = 2
    
    # show_bands determines whether the outline of cytogenetic bands
    # will be seen
    show_bands            = yes
    # in order to fill the bands with the color defined in the karyotype
    # file you must set fill_bands
    fill_bands            = yes
    
    </ideogram>
``````
  

* * *

#### ticks.conf
```    
    show_ticks          = yes
    show_tick_labels    = yes
    
    show_grid          = yes
    grid_start         = 0.5r
    grid_end           = 1.0r
    
    <ticks>
    skip_first_label     = no
    skip_last_label      = no
    radius               = dims(ideogram,radius_outer)
    tick_separation      = 2p
    min_label_distance_to_edge = 10p
    label_separation = 5p
    label_offset     = 2p
    label_size = 8p
    multiplier = 1e-6
    color = black
    
    <tick>
    spacing        = 1u
    size           = 6p
    thickness      = 1p
    color          = black
    show_label     = no
    label_size     = 16p
    label_offset   = 0p
    format         = %.2f
    grid           = no
    grid_color     = grey
    grid_thickness = 1p
    </tick>
    <tick>
    spacing        = 5u
    size           = 10p
    thickness      = 1p
    color          = black
    show_label     = yes
    label_size     = 16p
    label_offset   = 0p
    format         = %d
    grid           = yes
    grid_color     = grey
    grid_thickness = 2p
    </tick>
    <tick>
    spacing        = 10u
    size           = 16p
    thickness      = 2p
    color          = black
    show_label     = yes
    label_size     = 16p
    label_offset   = 0p
    format         = %d
    grid           = yes
    grid_color     = vdgrey
    grid_thickness = 2p
    </tick>
    </ticks>
```
  

* * *
