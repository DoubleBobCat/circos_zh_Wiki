---
author: DoubleCat
date: 2025-04-11
layout: post
category: highlights
title: Recipe 1 - Ideogram Highlights
---

### lesson
Ideogram highlights are particularly suitable for data that draws attention to
some parts of the ideograms, leaving most of the ideogram uncovered. Remember
that ideogram highlights obscure the cytogenetic bands, if any, that you've
drawn. Thus, as you increase highlight coverage, you are actually obscuring
one data set (cytogenetic bands) in favour of display another (the highlights
themselves).

In this example, I've created highlights from two gene lists. One gene list is
the set of genes in the OMIM database, which lists genes associated with any
kind of disease. The other list is a set of genes that have been implicated in
cancers. The latter list is much smaller than the former.

I've defined two ideogram highlight tracks, the OMIM genes drawn in orange and
the cancer genes in blue. Since the cancer genes are a proper subset of the
OMIM genes, I've drawn the cancer genes on top by assigning them a higher
z-depth.

```    
    <highlights>
    
    ideogram   = yes
    z          = 5
    
     <highlight>
     file       = data/3/genes.omim.txt
     fill_color = orange
     </highlight>
    
     <highlight>
     file       = data/3/genes.cancer.txt
     z          = 10
     fill_color = blue
     </highlight>
    
    </highlights>
```
Since both higlight data sets are of the ideogram type, I've put the ideogram
parameter in the outer <highlights> block. This applies the parameter value to
all inner <highlight;> blocks.

I've set the default z-depth to be 5, and gave the cancer gene highlights a
higher z-depth, 10. It's good to space your z-depths by steps of 5 or 10,
because this allows you to insert highlight data sets at any relative position
to existing higlights without changing existing z-depth values. It's also a
good idea not to start z-depth at 0, because you can then insert a data set
behind all others, without using a negative z-depth, which is acceptable but
simply less aesthetically pleasing than all-positive z-depths.

One of the two fill_color parameters could have been global to both
<highlight> blocks. It's up to you how to manage parameter values in a way
that's reasonable for your application. Depending on your use, one of the two
statements below may be more intuitive

  * all genes are orange, but cancer genes are blue 
  * all genes are blue, but disease genes are orange 
  * disease genes are orange and cancer genes are blue 
### images
![Circos tutorial image - Recipe 1 - Ideogram
Highlights](/documentation/tutorials/highlights/recipe1/img/01.png)
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
    
    chromosomes        = hs1;hs2;hs3
    chromosomes_display_default = no
    
    <highlights>
    
    z          = 5
    ideogram   = yes
    fill_color = orange
    
    <highlight>
    file       = data/3/genes.omim.txt
    </highlight>
    
    <highlight>
    file       = data/3/genes.cancer.txt
    z          = 10
    fill_color = blue
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
