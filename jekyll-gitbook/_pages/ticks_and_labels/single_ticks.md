---
author: DoubleCat
date: 2025-04-11
layout: post
category: ticks_and_labels
title: Ticks at Specific Positions
---

## Ticks at Specific Positions
### lesson
Up to now, each tick block defined a tick series, with the positions of ticks
in a series defined by the spacing (absolute or relative). In this tutorial,
you'll see how to define ticks at specific positions.

#### Ticks at specific absolute positions
To define a tick at a given absolute position, use `position` instead of
`spacing`.

```    
    <ticks>
    
    ...
    
    <tick>
    # define position 
    position     = 25u
    # no spacing definition necessary
    ...
    </tick>
    
    <tick>
    # define multiple positions
    position     = 30u,32u,34u,40u
    ...
    </tick>
    
    ...
    
    </ticks>
```
Do not define `spacing` when `position` is used.

#### Ticks at specific relative positions
To place at specific relative positions, use `rposition` and set
`spacing_type=relative`.

```    
    <tick>
    # define multiple positions
    rposition      = 0.5,0.7,0.9
    spacing_type   = relative
    color          = blue
    label_relative = yes
    format         = %.2f
    </tick>
```
Note the difference between `position` (for absolute positions) and
`rposition` (for relative positions).

Do not define `rspacing` when `rposition` is used.

#### Ticks at start and end of ideogram
Two special positions are defined. These are `start` and `end`. Using these
strings you can place a tick at the start or end of the ideogram. This tick
can have a label. In addition, you can define the label to be any string by
using the `label` parameter. This parameter is supported for all ticks, but is
particularly useful for start/end ideogram ticks.

```    
    <tick>
    position = start
    label    = 3'
    ...
    </tick>
    
    <tick>
    position = end
    label    = 5'
    ...
    </tick>
```### images
![Circos tutorial image - Ticks at Specific
Positions](/documentation/tutorials/ticks_and_labels/single_ticks/img/01.png)
![Circos tutorial image - Ticks at Specific
Positions](/documentation/tutorials/ticks_and_labels/single_ticks/img/02.png)
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
    
    radius         = dims(ideogram,radius_outer)
    multiplier     = 1/1u
    color          = black
    force_display  = yes
    thickness      = 4p
    size           = 20p
    show_label     = yes
    label_size     = 36p
    label_offset   = 10p
    format         = %d
    
    <tick>
    show           = yes
    position       = 25u
    </tick>
    
    <tick>
    show           = yes
    position       = 30u,32u,34u,40u
    color          = red
    </tick>
    
    <tick>
    show           = yes
    rposition      = 0.05,0.15,0.2
    spacing_type   = relative
    color          = blue
    format         = %d
    </tick>
    
    <tick>
    show           = yes
    rposition      = 0.55,0.7,0.9
    spacing_type   = relative
    label_relative = yes
    color          = green
    format         = %.2f
    </tick>
    
    <tick>
    show           = yes
    position       = start
    label          = 3'
    color          = purple
    format         = %s
    </tick>
    
    <tick>
    show           = yes
    position       = end
    label          = 5'
    color          = purple
    format         = %s
    </tick>
    
    </ticks>
```
  

* * *
