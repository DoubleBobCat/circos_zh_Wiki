---
author: DoubleCat
date: 2025-04-11
layout: post
category: ideograms
title: Filtering
---

## Filtering
### lesson
To remove ideograms from the image, the "chromosomes" and
"chromosomes_display_default" configuration parameters are used.

#### chromosomes_display_default
If this is set, then any ideograms not explicitly excluded will be drawn.
Setting this flag is useful if you want to exclude a few ideograms, but draw
the majority of others.

#### chromosomes
This field is used identify which ideograms to draw and/or exclude. When
referring to ideograms, always use the ID of the ideogram as defined in the
karyotype file (not the ideogram's text label).

For example,

```    
    chromosomes = hs1;hs2;hs3
```
will draw only the ideograms listed. To exclude an ideogram, preceed the ID
with "-". Thus, to draw all ideograms but exclude those drawn above

```    
    chromosomes = -hs1;-hs2;-hs3
    chromosomes_display_default = yes
```
The order in which the ideogram IDs appear in the "chromosomes" parameter does
not influence the order in which they are drawn. To apply a different order,
use chromosomes_order, discussed in another tutorial. Without specifying the
order, the ideograms are drawn in the order of appearance in the karyotype
file.
### images
![Circos tutorial image -
Filtering](/documentation/tutorials/ideograms/filtering/img/01.png)
### configuration
#### circos.conf
```    
    <<include etc/colors_fonts_patterns.conf>>
    
    <<include ideogram.conf>>
    <<include ticks.conf>>
    
    <image>
    <<include etc/image.conf>>
    </image>
    
    karyotype   = data/karyotype/karyotype.human.txt
    
    chromosomes_units           = 1000000
    
    # to explicitly define what is drawn
    
    chromosomes_display_default = no
    chromosomes                 = hs1;hs2;hs3;hs10;hs11;hsX
    
    # to explicity define what is not drawn
    
    #chromosomes_display_default = yes
    #chromosomes                 = -hs1;-hs2;-hs3;-hs10;-hs11;-hsX
    
    <<include etc/housekeeping.conf>>
```
  

* * *

#### bands.conf
```    
    show_bands            = yes
    fill_bands            = yes
    band_stroke_thickness = 2
    band_stroke_color     = white
    band_transparency     = 4
```
  

* * *

#### ideogram.conf
```    
    <ideogram>
    
    <spacing>
    
    default = 0.0025r
    break   = 0.5r
    
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
    label_font       = bold
    # labels outside circle
    #label_radius     = dims(ideogram,radius) + 0.05r
    #labels inside circle
    label_radius     = dims(ideogram,radius) - 0.15r
    label_with_tag   = yes
    label_size       = 48
    label_parallel   = yes
    label_case       = upper
```
  

* * *

#### ideogram.position.conf
```    
    radius           = 0.90r
    thickness        = 100p
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
    skip_first_label = no
    skip_last_label  = no
    radius           = dims(ideogram,radius_outer)
    tick_separation  = 3p
    label_separation = 1p
    multiplier       = 1e-6
    color            = black
    thickness        = 4p
    size             = 20p
    
    <tick>
    spacing        = 1u
    show_label     = no
    thickness      = 2p
    color          = dgrey
    </tick>
    
    <tick>
    spacing        = 5u
    show_label     = no
    thickness      = 3p
    color          = vdgrey
    </tick>
    
    <tick>
    spacing        = 10u
    show_label     = yes
    label_size     = 20p
    label_offset   = 10p
    format         = %d
    grid           = yes
    grid_color     = dgrey
    grid_thickness = 1p
    grid_start     = 0.5r
    grid_end       = 0.999r
    </tick>
    
    </ticks>
```
  

* * *
