---
author: DoubleCat
date: 2025-04-11
layout: post
category: links
title: Link Rules - Part III
---

### lesson
Rules can affect the geometry of a link. This example expands on the previous
one and modifies the position of intrachromosomal links to face outward.

The new rules sample intrachromosomal links. The first of these rules, hides
any whose ends are within 1 Mb of each other. Here the `var(pos1)` and
`var(pos2)` are used to sample the middle of the start and end of the link.

The second rule applies to intrachromosomal links whose ends are within 50 Mb.
These are colored blue and made to face outward by setting their
`bezier_radius` larger than 1. The next performs a similar function but for
any links left within 100 Mb.

The last rule suppresses the display of any other intrachromosomal links (i.e.
those whose ends are more than 100 Mb apart).

```    
    <rule>
    condition  = var(intrachr)
    condition  = abs(var(pos1) - var(pos2)) < 1Mb
    show       = no
    </rule>
    
    <rule>
    condition  = var(intrachr)
    condition  = abs(var(pos1) - var(pos2)) < 50Mb
    color         = dblue_a2
    bezier_radius = 1.1r
    bezier_radius_purity = 0.25
    </rule>
    
    <rule>
    condition  = var(intrachr)
    condition  = abs(var(pos1) - var(pos2)) < 100Mb
    color         = dgreen_a2
    crest         = 2
    bezier_radius = 0.75r
    bezier_radius_purity = 0.25
    </rule>
    
    <rule>
    condition  = var(intrachr)
    show       = no
    </rule>
```### images
![Circos tutorial image - Link Rules - Part
III](/documentation/tutorials/links/rules3/img/01.png)
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
    
    chromosomes_units = 1000000
    chromosomes_display_default = no
    chromosomes       = hs1;hs2;hs3;hs4
    
    <links>
    
    z      = 0
    radius = 0.90r
    crest  = 1
    color  = vvlgrey
    bezier_radius        = 0r
    bezier_radius_purity = 0.50
    thickness    = 2
    
    <link>
    
    file         = data/5/segdup.txt
    
    <rules>
    
    <rule>
    condition     = var(intrachr)
    condition     = abs(var(pos1) - var(pos2)) < 1Mb
    show          = no
    </rule>
    
    <rule>
    condition     = var(intrachr)
    condition     = abs(var(pos1) - var(pos2)) < 50Mb
    bezier_radius = 1.1r
    bezier_radius_purity = 0.25
    color         = dblue_a2
    </rule>
    
    <rule>
    condition     = var(intrachr)
    condition     = abs(var(pos1) - var(pos2)) < 100Mb
    bezier_radius = 0.75r
    crest         = 2
    bezier_radius_purity = 0.25
    color         = dgreen_a2
    </rule>
    
    <rule>
    condition  = var(intrachr)
    show       = no
    </rule>
    
    <rule>
    condition  = var(interchr)
    condition  = on(hs2,65Mb,75Mb)
    z          = 60
    color      = red_a1
    thickness  = 5
    radius     = 1r
    </rule>
    
    <rule>
    condition  = max(var(size1),var(size2)) > 40kb
    z          = 50
    color      = black
    thickness  = 5
    </rule>
    
    <rule>
    condition  = max(var(size1),var(size2)) > 10kb
    z          = 45
    color      = dgrey
    thickness  = 4
    </rule>
    
    <rule>
    condition  = max(var(size1),var(size2)) > 5kb
    z          = 40
    color      = grey
    thickness  = 3
    </rule>
    
    <rule>
    condition  = max(var(size1),var(size2)) > 1kb
    z          = 35
    color      = lgrey
    thickness  = 2
    </rule>
    
    </rules>
    
    </link>
    
    </links>
    
    <<include etc/housekeeping.conf>>
    data_out_of_range* = trim
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
    
    </ideogram>
``````
  

* * *

#### ideogram.label.conf
```    
    show_label       = yes
    label_font       = default
    label_radius     = dims(ideogram,radius) + 0.075r
    label_with_tag   = yes
    label_size       = 36
    label_parallel   = yes
    label_case       = lower
    label_format     = eval(sprintf("chr%s",var(label)))
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
    
    radius           = dims(ideogram,radius_outer)
    orientation      = out
    label_multiplier = 1e-6
    color            = black
    size             = 20p
    thickness        = 3p
    label_offset     = 5p
    
    <tick>
    spacing        = 1u
    show_label     = no
    </tick>
    
    <tick>
    spacing        = 5u
    show_label     = yes
    label_size     = 20p
    format         = %d
    </tick>
    
    <tick>
    spacing        = 10u
    show_label     = yes
    label_size     = 24p
    format         = %d
    </tick>
    
    </ticks>
```
  

* * *
