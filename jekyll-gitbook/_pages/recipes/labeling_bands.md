---
author: DoubleCat
date: 2025-04-11
layout: post
category: recipes
title: Labeling Karyotype Bands
---

### lesson
This tutorial show syou how to add a narrow band of text labels to your
figure. We'll label the cytogenetic bands on the ideograms for the example.

First, we'll extract the position and names of the bands from the human
karyotype file that is included with Circos
(`data/karyotype/karyotype.human.txt`).

```    
    > cat data/karyotype.human.txt | grep band | awk '{print $2,$5,$6,$3}'
    hs1 0 2300000 p36.33
    hs1 2300000 5300000 p36.32
    hs1 5300000 7100000 p36.31
    ...
```
This data file to populate a text track. In this example, I've placed the band
labels immediately outside the ideogram circle, which required that I shift
the ticks outward.

```    
    <plot>
    
    type  = text
    color = red
    file  = data/8/text.bands.txt
    
    r0 = 1r
    r1 = 1r+300p
    
    label_size = 12
    label_font = condensed
    
    show_links     = yes
    link_dims      = 0p,2p,6p,2p,5p
    link_thickness = 2p
    link_color     = black
    
    label_snuggle        = yes
    max_snuggle_distance = 1r
    snuggle_tolerance    = 0.25r
    snuggle_sampling     = 2
    snuggle_refine       = yes
    
    </plot>
``````
#### adjusting text color
One way to adjust the color of the text is to use rules. For example, the
three rules below adjust the color of the text based on chromosome, position
and text label, respectively.

```    
    <rules>
    <rule>
    condition  = on(hs1)
    color      = blue
    flow       = continue
    </rule>
    
    <rule>
    condition  = var(start) > 50mb && var(end) < 100mb
    color      = green
    flow       = continue
    </rule>
    
    <rule>
    condition  = var(value) =~ /[.]\d\d/
    color      = grey
    </rule>
    
    </rules>
```
You can also adjust the color of the label (or any other format parameter) by
including the corresponding variable/value pairs directly in the data file.

```    
    hs10 111800000 114900000 q25.2 color=orange
    hs10 114900000 119100000 q25.3 color=orange
    hs10 119100000 121700000 q26.11 color=purple
    hs10 121700000 123100000 q26.12 color=purple
    hs10 123100000 127400000 q26.13 label_size=24p
    hs10 127400000 130500000 q26.2 label_size=18p
    hs10 130500000 135374737 q26.3 label_size=14p
```
Remember that rules will override these settings, unless `overwrite=no` is set
in a rule.
### images
![Circos tutorial image - Labeling Karyotype
Bands](/documentation/tutorials/recipes/labeling_bands/img/01.png) ![Circos
tutorial image - Labeling Karyotype
Bands](/documentation/tutorials/recipes/labeling_bands/img/02.png) ![Circos
tutorial image - Labeling Karyotype
Bands](/documentation/tutorials/recipes/labeling_bands/img/03.png) ![Circos
tutorial image - Labeling Karyotype
Bands](/documentation/tutorials/recipes/labeling_bands/img/04.png)
### configuration
#### circos.conf
```    
    <<include etc/colors_fonts_patterns.conf>>
    
    <<include ideogram.conf>>
    <<include ticks.conf>>
    
    karyotype = data/karyotype/karyotype.human.txt
    
    <image>
    <<include etc/image.conf>>
    </image>
    
    chromosomes_units = 1000000
    chromosomes       = /hs([1-9]|10)$/
    chromosomes_display_default = no
    
    <plots>
    
    <plot>
    type  = text
    color = red
    file  = data/8/text.bands.txt
    
    r0    = 1r
    r1    = 1r+300p
    
    label_size = 12
    label_font = condensed
    
    show_links     = yes
    link_dims      = 0p,2p,6p,2p,5p
    link_thickness = 2p
    link_color     = black
    
    label_snuggle        = yes
    max_snuggle_distance = 1r
    snuggle_tolerance    = 0.25r
    snuggle_sampling     = 2
    snuggle_refine       = yes
    
    <rules>
    <rule>
    condition  = on(hs1)
    color      = blue
    flow       = continue
    </rule>
    
    <rule>
    condition  = var(start) > 50mb && var(end) < 100mb
    color      = green
    flow       = continue
    </rule>
    
    <rule>
    condition  = var(value) =~ /[.]\d\d/
    color      = grey
    </rule>
    </rules>
    
    </plot>
    
    </plots>
    
    <<include etc/housekeeping.conf>>
```
  

* * *

#### ideogram.conf
```    
    <ideogram>
    
    <spacing>
    
    default = 5u
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
    thickness        = 30p
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
    label_font     = default
    label_radius   = dims(ideogram,radius) + 175p
    label_size     = 30p
    label_parallel = yes
    label_case     = upper
    
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
    
    <ticks>
    
    radius               = dims(ideogram,radius_outer)+120p
    multiplier           = 1e-6
    
    <tick>
    spacing        = 0.5u
    size           = 3p
    thickness      = 1p
    color          = black
    show_label     = no
    label_size     = 16p
    label_offset   = 0p
    format         = %d
    </tick>
    
    <tick>
    spacing        = 5u
    size           = 5p
    thickness      = 2p
    color          = black
    show_label     = no
    label_size     = 16p
    label_offset   = 0p
    format         = %d
    </tick>
    <tick>
    spacing        = 10u
    size           = 8p
    thickness      = 2p
    color          = black
    show_label     = yes
    label_size     = 12p
    label_offset   = 5p
    format         = %d
    </tick>
    
    </ticks>
```
  

* * *
