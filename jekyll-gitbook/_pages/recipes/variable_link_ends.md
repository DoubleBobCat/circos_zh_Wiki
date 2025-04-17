---
author: DoubleCat
date: 2025-04-11
layout: post
category: recipes
title: Variable Radius Link Ends
---

### lesson
Using entries in the link data file, or rules, you can independently
manipulate the radial position of each end of a link. One application of this
is to move link ends out of the way of another data track.

This is done by setting `radius1` and `radius2` values, which are the radial
positions of the link ends associated with the first and second data point,
respectively.

The first way to achieve this is to associate a radius value with one or both
of the ends.

```    
    hs1 486 76975 hs15 100263879 100338121 radius1=0.5r
    hs1 342608 393885 hs15 100218755 100268630 radius2=0.5r
    hs1 576306 626811 hs15 100218755 100268630 radius=0.75r
```
Link ends for which radius is not defined will use the `radius` value defined
in the <link> or <links> blcok.

The second way to adjust radius values is to use a rule and set `radius1` and
`radius2` variables.

```    
    <rules>
    
    # if a rule is triggered, continue testing with other rules
    flow       = continue
    
    # remap the color of the link to the first chromosome
    <rule>
    condition  = 1
    color      = eval(sprintf("%s_a4",var(chr1)))
    </rule>
    
    # Alter radial position of one or both ends of a link, depending
    # on its position. The function on(RX) tests whether a link
    # is on a chromosome matching the regular expression RX.
    
    # to/from hs1
    <rule>
    # the trailing $ (end of string anchor) is required so that 
    # chromosome names like hs10, hs11, hs12, etc don't match
    condition  = on(hs1$)
    radius     = 0.85r
    </rule>
    
    # to hs10, hs11 or hs12
    <rule>
    condition  = to(hs1[012])
    radius2    = 0.75r
    </rule>
    
    # from hs10, hs11, hs12
    <rule>
    condition  = from(hs1[012])
    radius1    = 0.75r
    </rule>
    
    # from hs14 and has start beyond 100mb
    <rule>
    condition  = from(hs14) && var(start1) > 100mb
    radius1    = 1r+50p
    z          = 5
    thickness  = 3
    color      = blue
    </rule>
    
    # to hs5 and has end within 50mb of position 100mb
    <rule>
    condition  = to(hs5) && abs(var(start2) - 100mb) < 50mb
    radius2    = 1r+50p
    z          = 5
    thickness  = 3
    color      = red
    </rule>
    
    </rules>
```### images
![Circos tutorial image - Variable Radius Link
Ends](/documentation/tutorials/recipes/variable_link_ends/img/01.png)
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
    #chromosomes       = hs1;hs2;hs3;hs4;hs5;hs6;hs7;hs8
    chromosomes_display_default = yes
    
    <links>
    
    <link>
    
    file          = data/5/segdup.bundle4.txt
    radius        = 0.95r
    bezier_radius = 0r
    color         = vvdgrey
    thickness     = 2
    record_limit  = 2500
    
    <rules>
    
    # if a rule is triggered, continue testing with other rules
    flow       = continue
    
    # remap the color of the link to the first chromosome
    <rule>
    condition  = 1
    color      = eval(sprintf("%s_a4",var(chr1)))
    </rule>
    
    # Alter radial position of one or both ends of a link, depending
    # on its position. The function on(RX) tests whether a link
    # is on a chromosome matching the regular expression RX.
    
    <rule>
    # to/from hs1
    condition  = on(hs1$)
    radius     = 0.85r
    </rule>
    
    <rule>
    # to hs10, hs11 or hs12
    condition  = to(hs1[012])
    radius2    = 0.75r
    </rule>
    
    <rule>
    # from hs10, hs11, hs12
    condition  = from(hs1[012])
    radius1    = 0.75r
    </rule>
    
    <rule>
    # from hs14 and has start beyond 100mb
    condition  = from(hs14) && var(start1) > 100mb
    radius1    = 1r+50p
    z          = 5
    thickness  = 3
    color      = blue
    </rule>
    
    <rule>
    # to hs5 and has end within 50mb of position 100mb
    condition  = to(hs5) && abs(var(start2) - 100mb) < 50mb
    radius2    = 1r+50p
    z          = 5
    thickness  = 3
    color      = red
    </rule>
    
    </rules>
    
    </link>
    
    </links>
    
    <<include etc/housekeeping.conf>>
    data_out_of_range* = trim
``````
  

* * *

#### bands.conf
```    
    show_bands            = yes
    fill_bands            = yes
    band_stroke_thickness = 2
    band_stroke_color     = white
    band_transparency     = 3
```
  

* * *

#### ideogram.conf
```    
    <ideogram>
    
    <spacing>
    default = 0.005r
    break   = 0.5r
    
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
    stroke_thickness = 2
    thickness        = 1.5r
    </break>
    
    </spacing>
    
    <<include ideogram.position.conf>>
    <<include ideogram.label.conf>>
    <<include bands.conf>>
    
    </ideogram>
``````
  

* * *

#### ideogram.label.conf
```    
    show_label       = yes
    label_font       = default
    label_radius     = dims(image,radius) - 50p
    label_size       = 36
    label_parallel   = yes
    label_case       = lower
    label_format     = eval(sprintf("chr%s",var(label)))
``````
  

* * *

#### ideogram.position.conf
```    
    radius           = 0.85r
    thickness        = 30p
    fill             = yes
    fill_color       = black
    stroke_thickness = 2
    stroke_color     = black
```
  

* * *

#### ticks.conf
```    
    show_ticks          = yes
    show_tick_labels    = yes
    
    <ticks>
    tick_separation      = 3p
    label_separation     = 5p
    radius               = dims(ideogram,radius_outer)+50p
    multiplier           = 1e-6
    color          = black
    size           = 20p
    thickness      = 4p
    label_offset   = 5p
    format         = %d
    
    <tick>
    spacing        = 1u
    show_label     = yes
    label_size     = 16p
    </tick>
    
    <tick>
    spacing        = 5u
    show_label     = yes
    label_size     = 18p
    </tick>
    
    <tick>
    spacing        = 10u
    show_label     = yes
    label_size     = 20p
    </tick>
    
    <tick>
    spacing        = 20u
    show_label     = yes
    label_size     = 24p
    </tick>
    
    </ticks>
```
  

* * *
