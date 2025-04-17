---
author: DoubleCat
date: 2025-04-11
layout: post
category: highlights
title: Drawing on Top of Data
---

## Drawing on Top of Data
### lesson
Highlights defined in <highlight> blocks are always drawn behind links, data,
and grids.

In order to draw highlights on top of links, you need to use the <plot>.

```    
    <plots>
    <plot>
    type = highlight
    file = data/3/chr.highlights.txt
    r0   = 0.7r
    r1   = 0.75r
    z    = 10
    </plot>
    </plots>
```
The plot type must be set to `type=highlight`, with the rest of the syntax
being the same as for the highlight block.

The `z` parameter in the <plot> block will define the layer, relative to other
plots, on which the highlights will be drawn. Tracks with larger `z` are drawn
on top of those with smaller `z`.

If you want to place the highlight within the ideogram, set the inner and
outer track radii to

```    
    r0 = dims(ideogram,radius_inner)
    r1 = dims(ideogram,radius_outer)
```
Plot blocks are discussed in detail in the [2D Data
Tutorial](/documentation/tutorials/2d_tracks/). Briefly, these blocks are used
to define and format 2D data plots such as scatter plots, histograms, and
heatmaps.
### images
![Circos tutorial image - Drawing on Top of
Data](/documentation/tutorials/highlights/on_data/img/01.png)
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
    
    karyotype   = data/karyotype.human.colorbychr.txt
    
    <image>
    dir = /tmp
    file  = circos-tutorial.png
    png   = yes
    svg   = yes
    24bit = yes
    # radius of inscribed circle in image
    radius         = 1500p
    background     = white
    #angle_orientation = counterclockwise
    # by default angle=0 is at 3 o'clock position
    angle_offset   = -90
    
    auto_alpha_steps = 5
    auto_alpha_colors = yes
    </image>
    
    chromosomes_units           = 1000000
    
    # to explicitly define what is drawn
    chromosomes                 = hs1;hs2
    chromosomes_reverse = hs2
    
    chromosomes_display_default = no
    
    <highlights>
    <highlight>
    file = data/3/chr.highlights.txt
    r0 = 0.9r
    r1 = 0.95r
    </highlight>
    </highlights>
    
    <plots>
    <plot>
    type = highlight
    file = data/3/chr.highlights.txt
    r0   = 0.8r
    r1   = 0.85r
    z    = 10
    </plot>
    
    <plot>
    type = highlight
    file = data/3/chr.highlights.txt
    r0   = 0.7r
    r1   = 0.75r
    z    = 10
    <rules>
    <rule>
    importance = 100
    condition  = 1
    fill_color = eval(_fill_color_."_a1")
    </rule>
    </rules>
    </plot>
    
    <plot>
    type = highlight
    file = data/3/chr.highlights.txt
    r0   = 0.6r
    r1   = 0.65r
    z    = 10
    <rules>
    <rule>
    importance = 100
    condition  = 1
    fill_color = eval(_fill_color_."_a2")
    </rule>
    </rules>
    </plot>
    
    <plot>
    type = highlight
    file = data/3/chr.highlights.txt
    r0   = 0.5r
    r1   = 0.55r
    z    = 10
    <rules>
    <rule>
    importance = 100
    condition  = 1
    fill_color = eval(_fill_color_."_a3")
    </rule>
    </rules>
    </plot>
    
    <plot>
    type = highlight
    file = data/3/chr.highlights.txt
    r0   = 0.4r
    r1   = 0.45r
    z    = 10
    <rules>
    <rule>
    importance = 100
    condition  = 1
    fill_color = eval(_fill_color_."_a4")
    </rule>
    </rules>
    </plot>
    
    <plot>
    type = highlight
    file = data/3/chr.highlights.txt
    r0   = 0.3r
    r1   = 0.35r
    z    = 10
    <rules>
    <rule>
    importance = 100
    condition  = 1
    fill_color = eval(_fill_color_."_a5")
    </rule>
    </rules>
    </plot>
    
    </plots>
    
    <links>
    <link 1>
    ribbon = yes
    flat   = yes
    file   = data/5/ribbon.txt
    bezier_radius = 0r
    radius = 0.95r
    color  = grey
    stroke_color = black
    stroke_thickness = 2
    </link>
    </links>
    
    anglestep       = 0.5
    minslicestep    = 10
    beziersamples   = 40
    debug           = no
    #debug_group = ticks
    warnings        = no
    imagemap        = no
    
    units_ok = bupr
    units_nounit = n
    svg_font_scale = 1.3
``````
  

* * *

#### ideogram.conf
```    
    <ideogram>
    
    <spacing>
    
    default = 10u
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
    label_font     = default
    label_radius   = dims(ideogram,radius) + 0.125r
    label_size     = 72
    
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
    
    grid_start         = dims(ideogram,radius_inner)-0.5r
    grid_end           = dims(ideogram,radius_outer)+100
    
    <ticks>
    radius               = dims(ideogram,radius_outer)
    tick_separation      = 1p
    min_label_distance_to_edge = 0p
    label_separation = 1p
    label_offset     = 2p
    label_size = 48p
    multiplier = 1e-6
    color = black
    
    <tick>
    spacing        = 5u
    size           = 5p
    thickness      = 2p
    color          = black
    show_label     = no
    label_size     = 10p
    label_offset   = 0p
    format         = %d
    grid           = yes
    grid_color     = grey
    grid_thickness = 1p
    </tick>
    
    <tick>
    spacing        = 20u
    size           = 8p
    thickness      = 2p
    color          = black
    show_label     = yes
    label_offset   = 0p
    format         = %d
    grid           = yes
    grid_color     = dgrey
    grid_thickness = 1p
    </tick>
    </ticks>
```
  

* * *
