---
author: DoubleCat
date: 2025-04-11
layout: post
category: recipes
title: Cell Cycle—Part 2
---

## Cell Cycle—Part 2
### lesson
This tutorial will show you how to use Circos to create a diagram of a
[typical cell cycle](https://en.wikipedia.org/wiki/Cell_cycle) (G1, S, G2, M)
and annotate it with links and text.

This is the second part of the tutorial, continuing from [Cell Cycle — Part
1](/documentation/tutorials/recipes/cell_cycle_part_1).

This tutorial shows a more advanced way to define the phase axes. Depending on
how you wish to define your coordinate system (e.g. relative to cycle, not
phase), the approach taken by this tutorial may be more helpful.

In general, this tutorial should be of interest to anyone who wishes to use
Circos for display of data that is not based on sequence coordinates.

#### cycle segment
There are four phases in the cell cycle: gap 1 (G1), synthesis (S), gap 2 (G2)
and mitosis (M). There's also a senescence phase (gap 0, G0), into which the
cell can pass to/from G1. I'll ignore G0 in this example.

Instead of defining one axis per phase, like in [Cell Cycle — Part
1](/documentation/tutorials/recipes/cell_cycle_part_1), I will create an axis
segment for the whole cycle.

```    
    # cycle.txt
    chr - cycle cycle 0 100 greys-6-seq-5
```
#### phases as cycle segment ideograms — using cropping
Each phase will be defined as a cropped region of the cycle axis.

```    
    karyotype   = cycle.txt
    chromosomes = cycle[g1]:0-45;cycle[s]:45-80;cycle[g2]:80-95;cycle[m]:95-100
```
The spacing between the cropped regions is defined by the `break` parameter in
<spacing> block

```    
    <ideogram>
    <spacing>
    default = 0.005r
    break   = 1r
    </spacing>
    </ideogram>
```
#### segment colors
Colors are defined in the same way as [Cell Cycle — Part
1](/documentation/tutorials/recipes/cell_cycle_part_1), except now the
arguments to `chromosomes_color` are the ideogram tags, not axis names.

```    
    palette  = greys-6-seq
    <phases>
    g1 = 3
    s  = 4
    g2 = 5
    m  = 6
    </phases>
    # g1, s, g2, m are tags defined in 'chromosomes' above
    chromosomes_color = g1=conf(palette)-conf(phases,g1),
                        s=conf(palette)-conf(phases,s),
                        g2=conf(palette)-conf(phases,g2),
                        m=conf(palette)-conf(phases,m)
```
#### tick marks
There are two options in this tutorial for tick marks.

The `ticks.absolute.conf` file defines them across the full cycle (e.g. first
tick on G2 is 80%). Nothing special needs to be done in this case, because
ticks are automatically generated relative to the original axis segment, and
not to any cropped regions. The tick labels will run from the start of the
segment (position 0 on `cycle` axis) to the end (position 100 on `cycle`
axis).

The `ticks.relative.conf` defines them relative to each ideogram (e.g. first
tick on G2 is 0%). The definition is almost identical to that of [Cell Cycle —
Part 1](/documentation/tutorials/recipes/cell_cycle_part_1) except for the
`rdivisor = ideogram` parameter, which tells Circos to label the ticks
relative to their position on the cropped ideogram and not on the underlying
axis segment.
### images
![Circos tutorial image - Cell Cycle—Part
2](/documentation/tutorials/recipes/cell_cycle_part_2/img/01.png) ![Circos
tutorial image - Cell Cycle—Part
2](/documentation/tutorials/recipes/cell_cycle_part_2/img/02.png)
### configuration
#### circos.conf
```    
    <<include etc/colors_fonts_patterns.conf>>
    
    <<include ideogram.conf>>
    # choose one
    <<include ticks.absolute.conf>>
    #<<include ticks.relative.conf>>
    
    <image>
    <<include etc/image.conf>>
    </image>
    
    chromosomes_units           = 1
    chromosomes_display_default = yes
    
    karyotype                   = cycle.txt
    
    #chromosomes                 = cycle[g1]:0-45;cycle[s]:45-80;cycle[g2]:80-95;cycle[m]:95-100
    #chromosomes                 = cycle[g1]:0-20;cycle[s]:20-80;cycle[g2]:80-95;cycle[m]:95-100
    #chromosomes                 = cycle[g1]:0-20;cycle[s]:20-40;cycle[g2]:40-95;cycle[m]:95-100
    chromosomes                 = cycle[g1]:0-20;cycle[s]:20-40;cycle[g2]:40-70;cycle[m]:70-100
    
    palette = greys-6-seq
    
    <phases>
    g1 = 3
    s  = 4
    g2 = 5
    m  = 6
    </phases>
    
    # g1, s, g2, m are tags defined in 'chromosomes' above
    chromosomes_color = g1=conf(palette)-conf(phases,g1),s=conf(palette)-conf(phases,s),g2=conf(palette)-conf(phases,g2),m=conf(palette)-conf(phases,m)
    
    <links>
    
    # connections between genes
    <link>
    file          = links.txt
    
    radius        = 0.95r
    bezier_radius = 0r
    
    # shorter links will be drawn closer
    # to the edge of the circle
    bezier_radius_purity = 0.1
    crest                = 1
    thickness            = 3
    
    <rules>
    
    <rule>
    condition = var(type) == 1
    color     = red
    </rule>
    <rule>
    condition = var(type) == 2
    color     = blue
    </rule>
    </rules>
    
    </link>
    </links>
    
    <plots>
    
    <plot>
    # gene labels
    
    type = text
    file = genes.txt
    
    r0   = 0.95r
    r1   = 1.5r
    
    label_size     = 36
    label_font     = bold
    
    show_links     = yes
    link_dims      = 0p,200p,20p,10p,20p
    link_thickness = 3
    link_color     = black
    
    <rules>
    <rule>
    condition = 1
    value     = eval(var(name))
    </rule>
    </rules>
    
    </plot>
    
    <plot>
    # circular glyph at start of gene label
    
    type = scatter
    file = genes.txt
    
    r0   = 0.95r
    r1   = 0.95r
    
    glyph = circle
    
    glyph_size       = 36
    color            = white
    stroke_color     = black
    stroke_thickness = 2
    
    <rules>
    <rule>
    condition = var(type) == 1
    color     = blues-5-seq-4
    </rule>
    <rule>
    condition = var(type) == 2
    color     = reds-5-seq-4
    </rule>
    </rules>
     
    </plot>
    
    </plots>
    
    <<include etc/housekeeping.conf>>
    restrict_parameter_names* = no
```
  

* * *

#### break.conf
```    
    axis_break_at_edge = yes
    axis_break         = yes
    axis_break_style   = 2
    
    <break_style 1>
    stroke_color     = black
    fill_color       = blue
    thickness        = 0.25r
    stroke_thickness = 2p
    </break_style>
    
    <break_style 2>
    stroke_color     = black
    stroke_thickness = 5p
    thickness        = 2r
    </break_style>
```
  

* * *

#### ideogram.conf
```    
    <ideogram>
    
    <spacing>
    
    default = 0.005r
    break   = 1r
    
    </spacing>
    
    <<include ideogram.position.conf>>
    <<include ideogram.label.conf>>
    </ideogram>
``````
  

* * *

#### ideogram.label.conf
```    
    show_label       = yes
    label_font       = bold
    label_radius     = (dims(ideogram,radius_inner)+dims(ideogram,radius_outer)-conf(ideogram,label_size))/2
    label_with_tag   = yes
    label_size       = 72
    label_color      = white
    label_parallel   = yes
    label_case       = upper
    
    # you can format the label by using properties
    # of the ideogram, accessible with var(PROPERTY):
    #
    # chr, chr_with_tag, chrlength, display_idx, end, idx, 
    # label, length, reverse, scale, size, start, tag
    
    label_format     = eval(sprintf("%s",var(tag)))
```
  

* * *

#### ideogram.position.conf
```    
    radius           = 0.90r
    thickness        = 100p
    fill             = yes
    fill_color       = black
    stroke_thickness = 2
    stroke_color     = dgrey
```
  

* * *

#### ticks.absolute.conf
```    
    show_ticks          = yes
    show_tick_labels    = yes
    show_grid           = yes
    
    <ticks>
    
    radius         = dims(ideogram,radius_outer)
    multiplier     = 1
    color          = dgrey
    thickness      = 2p
    size           = 15p
    
    grid           = yes
    grid_start     = dims(ideogram,radius_outer)
    grid_end       = dims(ideogram,radius_inner)
    grid_color     = white
    
    format         = %d
    suffix         = %
    
    label_size     = 26p
    label_offset   = 5p
    
    <tick>
    spacing        = 1u
    grid_thickness = 1p
    </tick>
    
    <tick>
    spacing        = 5u
    grid_thickness = 1p
    show_label     = yes
    </tick>
    
    <tick>
    spacing        = 10u
    show_label     = yes
    grid_thickness = 2p
    </tick>
    
    </ticks>
    
    offsets* = 0,1
```
  

* * *

#### ticks.relative.conf
```    
    show_ticks          = yes
    show_tick_labels    = yes
    show_grid           = yes
    
    <ticks>
    radius         = dims(ideogram,radius_outer)
    multiplier     = 0.1
    color          = dgrey
    thickness      = 2p
    size           = 15p
    
    grid           = yes
    grid_start     = dims(ideogram,radius_outer)
    grid_end       = dims(ideogram,radius_inner)
    grid_color     = white
    
    spacing_type   = relative
    label_relative = yes
    format         = %d
    rmultiplier    = 100
    rdivisor       = ideogram
    suffix         = %
    
    label_size     = 26p
    label_offset   = 5p
    
    <tick>
    rspacing       = 0.05
    grid_thickness = 1p
    </tick>
    
    <tick>
    rspacing       = 0.10
    show_label     = yes
    grid_thickness = 2p
    </tick>
    
    </ticks>
```
  

* * *
