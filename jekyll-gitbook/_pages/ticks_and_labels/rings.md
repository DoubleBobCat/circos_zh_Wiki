---
author: DoubleCat
date: 2025-04-11
layout: post
category: ticks_and_labels
title: Tick Rings
---

## Tick Rings
### lesson
A tick set can be automatically drawn at multiple radial positions if you
define more than one radius for the set.

```    
    <tick>
    # drawn at one radius
    radius = dims(ideogram,radius_outer)
    ...
    </tick>
    
    <tick>
    # drawn at two radii
    radius = dims(ideogram,radius_outer)
    radius = 0.8r
    ...
    </tick>
    
    <tick>
    # drawn at three radii
    radius = dims(ideogram,radius_outer)
    radius = 0.8r
    radius = 0.6r
    ...
    </tick>
```
Tick rings are useful when your image has many tracks and you'd like to have
multiple instances of tick marks.
### images
![Circos tutorial image - Tick
Rings](/documentation/tutorials/ticks_and_labels/rings/img/01.png)
### configuration
#### circos.conf
```    
    <<include colors_fonts_patterns.conf>>
    
    <<include ideogram.conf>>
    <<include ticks.conf>>
    
    <image>
    <<include etc/image.conf>>
    </image>
    
    karyotype   = data/karyotype/karyotype.human.txt
    
    chromosomes_units           = 1000000
    #chromosomes                 = hs1[a]:0-75;hs1[b]:100-150;hs1[c]:200-)
    chromosomes = hs1
    chromosomes_display_default = no
    
    <<include etc/housekeeping.conf>>
```
  

* * *

#### bands.conf
```    
    show_bands            = no
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
    break   = 2u
    </spacing>
    
    <<include ideogram.position.conf>>
    <<include ideogram.label.conf>>
    <<include bands.conf>>
    
    </ideogram>
``````
  

* * *

#### ideogram.label.conf
```    
    show_label     = yes
    label_font     = default
    label_radius   = (dims(ideogram,radius_inner) + dims(ideogram,radius_outer))/2
    label_center   = yes
    label_size     = 72
    label_with_tag = yes
    label_parallel = yes
    label_case     = upper
```
  

* * *

#### ideogram.position.conf
```    
    radius           = 0.90r
    thickness        = 100p
    fill             = no
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
    label_separation = 5p
    radius         = dims(ideogram,radius_outer)
    multiplier     = 1/1u
    color          = black
    thickness      = 4p
    show_label     = yes
    label_offset   = 5p
    format         = %d
    size = 20p
    
    <tick>
    spacing        = 1u
    radius         = dims(ideogram,radius_outer)
    label_size     = 18p
    format         = %d
    color          = purple
    </tick>
    
    <tick>
    spacing        = 2.5u
    radius         = 0.8r
    label_size     = 36p
    format         = %.1f
    color          = green
    </tick>
    
    <tick>
    spacing        = 5u
    radius         = dims(ideogram,radius_outer)
    radius         = 0.8r
    radius         = 0.4r
    label_size     = 36p
    </tick>
    
    <tick>
    spacing        = 10u
    radius         = dims(ideogram,radius_outer)
    radius         = 0.8r
    radius         = 0.4r
    radius         = 0.25r
    show           = yes
    label_size     = 36p
    color          = red
    </tick>
    
    <tick>
    spacing        = 50u
    radius         = dims(ideogram,radius_outer)
    radius         = 0.8r
    radius         = 0.4r
    radius         = 0.25r
    radius         = 0.1r
    label_size     = 36p
    color          = blue
    </tick>
    
    </ticks>
```
  

* * *
