---
author: DoubleCat
date: 2025-04-11
layout: post
category: ticks_and_labels
title: Grids
---

## Grids
### lesson
You can add a radial grid to any set of tick marks. Grids are drawn on top of
highlights, but behind all other data.

The radial start and end position of the grid lines can be controlled globally
within the <ticks> block, or locally, within each <tick> block.

```    
    show_grid  = yes
    
    <ticks>
    
     grid_start     = 0.5r
     grid_end       = 0.975r
     grid_color     = black
     grid_thickness = 2p
     ...
     <tick>
      spacing = 1u
      ...
      grid           = yes
      grid_color     = grey
      grid_thickness = 1
      grid_start     = 0.55r
      grid_end       = 0.95r
     </tick>
     <tick>
      spacing = 5u
      ...
      grid           = yes
      grid_color     = dgrey
      grid_thickness = 2
      grid_start     = 0.6r
      grid_end       = 0.925r
     </tick>
     <tick>
      spacing = 10u
      ...
      grid           = yes
      grid_color     = black
      grid_thickness = 2
     </tick>
    </ticks>
```### images
![Circos tutorial image -
Grids](/documentation/tutorials/ticks_and_labels/grids/img/01.png)
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
    chromosomes = hs1;hs2;hs3
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
    show_ticks       = yes
    show_tick_labels = yes
    show_grid        = yes
    
    <ticks>
    
    radius               = dims(ideogram,radius_outer)
    multiplier           = 1e-6
    
    thickness      = 4p
    size           = 20p
    
    grid_start     = 0.5r
    grid_end       = 0.975r
    grid_color     = black
    grid_thickness = 2p
    
    <tick>
    spacing        = 0.5u
    thickness      = 2p
    color          = red
    grid           = yes
    grid_color     = red
    grid_thickness = 1p
    grid_start     = 0.90r
    grid_end       = 0.999r
    </tick>
    
    <tick>
    spacing        = 1u
    color          = blue
    grid           = yes
    grid_color     = blue
    grid_thickness = 1p
    grid_start     = 0.55r
    grid_end       = 0.95r
    </tick>
    
    <tick>
    spacing        = 5u
    color          = green
    show_label     = yes
    label_size     = 20p
    label_offset   = 5p
    format         = %d
    grid           = yes
    grid_color     = green
    grid_start     = 0.5r
    grid_end       = 0.925r
    </tick>
    
    <tick>
    spacing        = 10u
    color          = black
    show_label     = yes
    label_size     = 24p
    label_offset   = 5p
    format         = %d
    grid           = yes
    </tick>
    
    </ticks>
```
  

* * *
