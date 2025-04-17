---
author: DoubleCat
date: 2025-04-11
layout: post
category: highlights
title: Highlight Parameters - Part I - Embedded in Data File
---

## Highlight Parameters - Part I - Embedded in Data File
### lesson
In this tutorial, I'll cover how to embed highlight parameters in your
highlight data file. This is a convenient way of formatting highlights because
generation of the parameters can be incorporated into your data analysis and
reporting pipeline.

#### formatting a gene list
Using the genes.txt file used in the previous section, I added a random fill
color (red, green, blue, purple, yellow, orange, grey) to each entry. For
entries that received a red color, I adjusted the radial start/end positions
to be closer to the center of the circle than other colors. For entries that
received a green color, I similiarly adjusted r0,r1 to format these entries to
fall outside of the circle.

Here is an excerpt of the data file, with the additional formatting option
fields.

```    
    hs1 1298972 1300443 fill_color=blue
    hs1 1311738 1324571 fill_color=red,r0=0.6r,r1=0.6r+50p
    hs1 1397026 1421444 fill_color=green,r0=1.1r,r1=1.15r
    hs1 1437417 1459927 fill_color=green,r0=1.1r,r1=1.15r
    hs1 1540746 1555847 fill_color=yellow
    hs1 1560962 1645635 fill_color=purple
    hs1 1624179 1645623 fill_color=grey
```
The configuration block for this highlight set defines a default r0,r1 value,
which applies to any entries in the data file that don't have overriding r0,r1
values. Thus, most of the highlights fall between r0,r1 = 0.7r,0.7r+200p, with
the red and green entries shifted inward and outward in the circle,
respectively.

All of the other highlight parameters may be specified in a similar manner in
the data file.
### images
![Circos tutorial image - Highlight Parameters - Part I - Embedded in Data
File](/documentation/tutorials/highlights/parameters/img/01.png)
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
    
    chromosomes        = hs1
    chromosomes_breaks = -hs1:120-145;-hs1:180-200
    
    chromosomes_display_default = no
    
    <highlights>
    
    z = 0
    fill_color = green
    
    <highlight>
    file       = data/3/genes.formatted.txt
    r0         = 0.7r
    r1         = 0.7r + 200p
    </highlight>
    
    </highlights>
    
    anglestep       = 0.5
    minslicestep    = 10
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
    grid           = yes
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
