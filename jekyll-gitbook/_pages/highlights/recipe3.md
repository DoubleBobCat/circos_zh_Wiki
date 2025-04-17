---
author: DoubleCat
date: 2025-04-11
layout: post
category: highlights
title: Recipe 3 - Plot Axis Range Highlights
---

### lesson
In this section, I'll look ahead and show how you can use highlights to
annotate 2D data plots (e.g. scatter plots).

By defining highlights to span the entire data domain (e.g. entire genome),
you can draw multiple instances of the highlight using different colors and
radial positions, in effect setting up a set of concentric circles that
provide radial axis highlights.

By drawing a scatter plot, for example, and synchronizing the radial extent of
the scatter plot with the position of the highlights, you can draw attention
to outlying data in your scatter plot.

```    
    <highlight>
    file       = data/3/chr.highlights.colourless.txt
    r0 = 0.715r
    r1 = 0.725r
    fill_color = lred
    </highlight>
    
    <highlight>
    file       = data/3/chr.highlights.colourless.txt
    r0 = 0.725r
    r1 = 0.75r
    fill_color = lorange
    </highlight>
    
    <highlight>
    file       = data/3/chr.highlights.colourless.txt
    r0 = 0.75r
    r1 = 0.80r
    fill_color = lyellow
    </highlight>
    
    <highlight>
    file       = data/3/chr.highlights.colourless.txt
    r0 = 0.8r
    r1 = 0.9r
    fill_color = lgrey
    </highlight>
    
    <highlight>
    file       = data/3/chr.highlights.colourless.txt
    r0 = 0.9r
    r1 = 0.95r
    fill_color = lyellow
    </highlight>
    
    <highlight>
    file       = data/3/chr.highlights.colourless.txt
    r0 = 0.95r
    r1 = 0.975r
    fill_color = lorange
    </highlight>
    
    <highlight>
    file       = data/3/chr.highlights.colourless.txt
    r0 = 0.975r
    r1 = 0.985r
    fill_color = lred
    </highlight>
```### images
![Circos tutorial image - Recipe 3 - Plot Axis Range
Highlights](/documentation/tutorials/highlights/recipe3/img/01.png)
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
    chromosomes_display_default = yes
    
    # same highlight set drawn at different radial positions
    # and in different colors to highlight
    # radial axis data range
    
    <highlights>
    
    <highlight>
    file       = data/3/chr.highlights.colourless.txt
    r0 = 0.715r
    r1 = 0.725r
    fill_color = lred
    </highlight>
    
    <highlight>
    file       = data/3/chr.highlights.colourless.txt
    r0 = 0.725r
    r1 = 0.75r
    fill_color = lorange
    </highlight>
    
    <highlight>
    file       = data/3/chr.highlights.colourless.txt
    r0 = 0.75r
    r1 = 0.80r
    fill_color = lyellow
    </highlight>
    
    <highlight>
    file       = data/3/chr.highlights.colourless.txt
    r0 = 0.8r
    r1 = 0.9r
    fill_color = lgrey
    </highlight>
    
    <highlight>
    file       = data/3/chr.highlights.colourless.txt
    r0 = 0.9r
    r1 = 0.95r
    fill_color = lyellow
    </highlight>
    
    <highlight>
    file       = data/3/chr.highlights.colourless.txt
    r0 = 0.95r
    r1 = 0.975r
    fill_color = lorange
    </highlight>
    
    <highlight>
    file       = data/3/chr.highlights.colourless.txt
    r0 = 0.975r
    r1 = 0.985r
    fill_color = lred
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
