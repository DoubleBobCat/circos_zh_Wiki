---
author: DoubleCat
date: 2025-04-11
layout: post
category: highlights
title: Ideogram Highlights
---

### lesson
Ideogram highlights are placed on top of the ideograms in the figure. You do
not need to specify the radial position of these highlights, because these
parameters are fixed by the size and position of the ideograms.

In this section, I have used the same data file to draw to highlight tracks.
One is an ideogram track and one is a wedge-style track, with radial positions
specified.

```    
    <highlights>
     <highlight>
     file       = data/3/random.highlights.z_by_size.txt
     ideogram   = yes
     </highlight>
    
     <highlight>
     file       = data/3/random.highlights.z_by_size.txt
     r0 = 0.5r
     r1 = 0.6r
     </highlight>
    </highlights>
```
In the example above, the highlights cover each ideogram completely, obscuring
the cytogenetic bands. In this kind of situation, it's best to use wedge-style
highlights.

Ideogram highlights are very effective when they are used to highlight
specific positions on the genome.

When the radial position of individual ideograms is set with
chromosome_radius, the position of highlights is automatically adjusted.
Relative highlight radial position is computed relative to the new ideogram
position. Highlights drawn on the ideogram (ideogram=yes) are drawn at the new
ideogram position.

#### adding transparency to ideogram highlights
It is possible to make ideogram highlights transparent. This is done in the
same way as for wedge highlights, and any other elements that require
transparency.

Note that if you have colored ideograms, cytogenetic bands with transparency
and transparent ideogram highlights these three colors will blend.

To make ideogram highlights transparent, add _aN to their fill_color. Below is
the part of circos.conf that achieves this.

```    
    <highlights>
    
    # transparent wedge highlights at radial position 0.85-0.95
    <highlight>
    file        = highlight.txt
    fill_color  = blue_a5
    r0 = 0.85r
    r1 = 0.95r
    </highlight>
    
    # transparent ideogram highlights, using the same data file as for wedge highlights
    <highlight>
    file        = highlight.txt
    fill_color  = blue_a2
    ideogram = yes
    </highlight>
    
    </highlights> 
```### images
![Circos tutorial image - Ideogram
Highlights](/documentation/tutorials/highlights/ideogram_highlights/img/01.png)
![Circos tutorial image - Ideogram
Highlights](/documentation/tutorials/highlights/ideogram_highlights/img/02.png)
![Circos tutorial image - Ideogram
Highlights](/documentation/tutorials/highlights/ideogram_highlights/img/03.png)
### configuration
#### circos.2.conf
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
    
    chromosomes        = hs1;hs2;hs3
    
    chromosomes_radius = hs2:0.9r;hs3:0.8r
    #chromosomes_breaks = -hs1:120-145;-hs1:180-200
    
    chromosomes_display_default = no
    
    <highlights>
    
    z = 0
    fill_color = green
    
    <highlight>
    file       = data/3/random.highlights.3chrs.txt
    ideogram   = yes
    </highlight>
    
    <highlight>
    file       = data/3/random.highlights.3chrs.txt
    r0 = 0.5r
    r1 = 0.5r+100p
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
    
    chromosomes = hs1;hs2:0-50
    #chromosomes        = hs1;hs2;hs3
    chromosomes_breaks = -hs1:120-145;-hs1:180-200
    
    chromosomes_display_default = no
    
    <highlights>
    
    z = 0
    fill_color = green
    
    <highlight>
    file       = data/3/random.highlights.z_by_size.txt
    ideogram   = yes
    </highlight>
    
    <highlight>
    file       = data/3/random.highlights.z_by_size.txt
    r0 = 0.5r
    r1 = 0.6r
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
    label_radius   = dims(ideogram,radius) + 0.075r
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
    grid_end           = 0.999r
    
    <ticks>
    skip_first_label     = no
    skip_last_label      = no
    radius               = dims(ideogram,radius_outer)
    #tick_separation      = 2p
    min_label_distance_to_edge = 10p
    #label_separation = 5p
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
