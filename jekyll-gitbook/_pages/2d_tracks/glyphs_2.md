---
author: DoubleCat
date: 2025-04-11
layout: post
category: 2d_tracks
title: Glyphs—Part II
---

### lesson
Modifying labels into symbols is ideal for making a general glyph tracks. For
example, consider a list of genes (`data/6/genes.glyph.txt`).

```    
    ...
    hs12 56428271 56432431 CDK4_cancer
    hs12 64504506 64595566 HMGA2_cancer
    hs12 64504506 64638901 P52926_cancer
    ...
    hs10 108323411 108914282 SORCS1_omim
    hs10 111614513 111673192 XPNPEP1_omim
    hs10 111755715 111885310 ADD3_omim
    ...
    hs7 139864688 139948811 DENND2A_other
    hs7 140019421 140041377 ADCK2_other
    hs7 140042949 140052913 NDUFB2_other
    ...
```
I've added _cancer to those genes that are in the Cancer Census, _omim to any
others that are in the OMIM list (disease-related), and _other to the
remaining. Using the rules below, genes become glyphs colored by their names.

```    
    <rules>
    
    flow = continue
    
    <rule>
    condition  = var(value) =~ /cancer/
    color      = red
    </rule>
    
    <rule>
    condition  = var(value) =~ /omim/
    color      = green
    </rule>
    
    <rule>
    condition  = var(value) =~ /other/
    color      = blue
    </rule>
    
    <rule>
    condition  = 1
    value      = N
    </rule>
    
    </rules>
```
Individual gene groups (cancer, omim, other) can be split into multiple tracks
by setting a rule to hide all genes except one. For example, this track shows
only the cancer genes outside the circle

```    
    <plot>
    
    r0 = 1r+10p
    r1 = 1r+200p
    color = red
    ...
    
    <rules>
    
    <rule>
    condition  = var(value) !~ /cancer/
    # hide anything that doesn't match "cancer"
    show = no
    </rule>
    
    <rule>
    condition  = 1
    # circle
    value = N
    </rule>
    
    </rules>
    
    </plot>
```
#### using glyphs to plot density
Finally, let's look at an example where the size of the glyph encodes density
of data points. While Circos won't calculate the density for you, you can pre-
process your data and encode the density as the label size.

In the `data/6/gene.density.txt` file, the number of gene entries for each of
cancer, omim and other groups (per Mb) is reported as the `label_size`.

```    
    ...
    hs1 3000000 3000000 cancer label_size=1
    hs1 6000000 6000000 cancer label_size=2
    ...
    hs1 1000000 1000000 omim label_size=9
    hs1 2000000 2000000 omim label_size=14
    ...
    hs1 1000000 1000000 other label_size=26
    hs1 2000000 2000000 other label_size=10
    ...
```
Using a rule, you can remap the label_size to another value. The original
label_size values range from 1p to 42p.

```    
    # linear remap to [6,50]
    label_size = eval(remap_int(var(label_size),1,42,6,50))
    
    # ... with shallower increase
    label_size = eval(remap_int(sqrt(var(label_size)),1,sqrt(42),6,50))
    
    # ... with steeper increase
    label_size = eval(remap_int(var(label_size)**2,1,42**2,6,50))
```### images
![Circos tutorial image - Glyphs—Part
II](/documentation/tutorials/2d_tracks/glyphs_2/img/01.png) ![Circos tutorial
image - Glyphs—Part
II](/documentation/tutorials/2d_tracks/glyphs_2/img/02.png) ![Circos tutorial
image - Glyphs—Part
II](/documentation/tutorials/2d_tracks/glyphs_2/img/03.png) ![Circos tutorial
image - Glyphs—Part
II](/documentation/tutorials/2d_tracks/glyphs_2/img/04.png)
### configuration
#### circos.conf
```    
    <<include colors_fonts_patterns.conf>>
    
    <<include ideogram.conf>>
    <<include ticks.conf>>
    
    <image>
    <<include etc/image.conf>>
    </image>
    
    karyotype = data/karyotype/karyotype.human.txt
    
    chromosomes_units           = 1000000
    chromosomes_display_default = yes
    chromosomes                 = -/hs/;/hs[1-9]$/
    
    <plots>
    
    # glyph character mappings
    #
    # small
    # | medium
    # | | large
    # | | |
    # a b c   square
    # d e f   rhombus
    # g h i   triangle up
    # j k l   triangle down
    # m n o   circle
    #
    # lower case - hollow
    # upper case - solid
    
    type       = text
    label_font = glyph
    label_size = 20
    padding    = -0.2r
    rpadding   = -0.2r
    
    <plot>
    file       = data/6/genes.glyph.txt
    r0         = 0.4r
    r1         = 0.99r
    
    <rules>
    
    flow = continue
    
    <rule>
    condition  = var(value) =~ /cancer/
    color      = red
    </rule>
    
    <rule>
    condition  = var(value) =~ /omim/
    color      = green
    </rule>
    
    <rule>
    condition  = var(value) =~ /other/
    color      = blue
    </rule>
    
    <rule>
    condition  = 1
    value      = N
    </rule>
    
    </rules>
    
    </plot>
    
    </plots>
    
    <<include etc/housekeeping.conf>>
```
  

* * *

#### bands.conf
```    
    show_bands            = yes
    fill_bands            = yes
    band_stroke_thickness = 2
    band_stroke_color     = white
    band_transparency     = 0
```
  

* * *

#### ideogram.conf
```    
    <ideogram>
    
    <spacing>
    default = 0.01r
    break   = 0.5r
    </spacing>
    
    <<include ideogram.position.conf>>
    <<include ideogram.label.conf>>
    <<include bands.conf>>
    
    radius*       = 0.825r
    
    </ideogram>
``````
  

* * *

#### ideogram.label.conf
```    
    show_label       = yes
    label_font       = default
    label_radius     = dims(image,radius)-30p
    label_size       = 24
    label_parallel   = yes
    label_case       = lower
    label_format     = eval(sprintf("chr%s",var(label)))
``````
  

* * *

#### ideogram.position.conf
```    
    radius           = 0.775r
    thickness        = 30p
    fill             = yes
    fill_color       = black
    stroke_thickness = 2
    stroke_color     = black
```
  

* * *

#### ticks.conf
```    
    show_ticks          = no
    show_tick_labels    = no
    
    show_grid = no
    grid_start         = dims(ideogram,radius_inner)-0.5r
    grid_end           = dims(ideogram,radius_inner)
    
    <ticks>
    skip_first_label     = no
    skip_last_label      = no
    radius               = dims(ideogram,radius_outer)
    tick_separation      = 2p
    min_label_distance_to_edge = 0p
    label_separation = 5p
    label_offset     = 2p
    label_size = 8p
    multiplier = 1e-6
    color = black
    
    #<tick>
    #hide = yes
    #spacing        = 0.01u
    #size           = 3p
    #thickness      = 2p
    #color          = black
    #show_label     = no
    #label_size     = 12p
    #label_offset   = 0p
    #format         = %.2f
    #grid           = no
    #grid_color     = lblue
    #grid_thickness = 1p
    #</tick>
    #<tick>
    #spacing        = 0.1u
    #size           = 5p
    #thickness      = 2p
    #color          = black
    #show_label     = yes
    #label_size     = 12p
    #label_offset   = 0p
    #format         = %.1f
    #grid           = yes
    #grid_color     = lgrey
    #grid_thickness = 1p
    #</tick>
    <tick>
    spacing        = 1u
    size           = 8p
    thickness      = 2p
    color          = black
    show_label     = no
    label_size     = 16p
    label_offset   = 0p
    format         = %.1f
    grid           = yes
    grid_color     = grey
    grid_thickness = 1p
    </tick>
    <tick>
    spacing        = 5u
    size           = 10p
    thickness      = 2p
    color          = black
    show_label     = yes
    label_size     = 24p
    label_offset   = 0p
    format         = %d
    grid           = yes
    grid_color     = grey
    grid_thickness = 1p
    </tick>
    </ticks>
```
  

* * *
