---
author: DoubleCat
date: 2025-04-11
layout: post
category: scaling
title: Overlapping Zoomed Regions
---

### lesson
When overlapping zoom regions are defined, the zoom level at an ideogram
position is taken to be the highest (in absolute terms) zoom of any
overlapping regions.

For example, if you define the following regions

```    
    100-200Mb - 2x
    150-180Mb - 3x
    160-170Mb - 5x
```
then the net effect will be as if you defined

```    
    100-150Mb - 2x
    150-160Mb - 3x
    160-170Mb - 5x
    170-180Mb - 3x
    180-200Mb - 2x
```
The zoom precedence is defined by the absolute zoom level, which is taken to
be max(scale,1/scale) For example, a scale of 0.1 (absolute zoom = 1/0.1 =
10x) overrides any zoom setting with an absolute zoom level smaller than 10x.
### images
![Circos tutorial image - Overlapping Zoomed
Regions](/documentation/tutorials/scaling/overlaping_zooms/img/01.png)
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
    
    <zooms>
    <zoom>
    chr    = hs1
    start  = 100u
    end    = 200u
    scale  = 2
    </zoom>
    <zoom>
    chr    = hs1
    start  = 130u
    end    = 170u
    scale  = 3
    </zoom>
    <zoom>
    chr    = hs1
    start  = 140u
    end    = 160u
    scale  = 5
    </zoom>
    <zoom>
    chr    = hs1
    start  = 148u
    end    = 152u
    scale  = 10
    </zoom>
    
    <zoom>
    chr    = hs2
    start  = 100u
    end    = 200u
    scale  = 0.5
    </zoom>
    <zoom>
    chr    = hs2
    start  = 130u
    end    = 170u
    scale  = 0.33
    </zoom>
    <zoom>
    chr    = hs2
    start  = 140u
    end    = 160u
    scale  = 0.2
    </zoom>
    <zoom>
    chr    = hs2
    start  = 148u
    end    = 152u
    scale  = 0.1
    </zoom>
    
    </zooms>
    
    chromosomes_units = 1000000
    chromosomes = hs1;hs2
    chromosomes_display_default = no
    
    <plots>
    <plot>
    type  = heatmap
    file  = data/7/heatmap.zoom-02.txt
    r1    = 0.95r
    r0    = 0.90r
    color = spectral-9-div
    stroke_color     = black
    stroke_thickness = 1
    scale_log_base   = 0.33
    </plot>
    </plots>
    
    <<include etc/housekeeping.conf>>
```
  

* * *

#### bands.conf
```    
    show_bands            = no
    fill_bands            = yes
    band_stroke_thickness = 2
    band_stroke_color     = white
    band_transparency     = 3
```
  

* * *

#### breaks.conf
```    
    axis_break_at_edge = yes
    axis_break         = yes
    axis_break_style   = 2
    
    <break_style 1>
    stroke_color     = black
    fill_color       = blue
    thickness        = 0.25r
    stroke_thickness = 2
    </break_style>
    
    <break_style 2>
    stroke_color     = black
    stroke_thickness = 2
    thickness        = 2r
    </break_style>
``````
  

* * *

#### ideogram.conf
```    
    <ideogram>
    
    <spacing>
    default = 0.005r
    break   = 0.5r
    
    <<include breaks.conf>>
    
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
    radius           = 0.90r
    thickness        = 50p
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
    tick_separation  = 3p
    label_separation = 10p
    radius           = dims(ideogram,radius_outer)
    multiplier       = 1e-6
    color            = black
    thickness        = 2p
    label_offset     = 5p
    format           = %d
    
    <tick>
    #chromosomes_display_default = no
    chromosomes    = -hs9
    spacing        = 0.5u
    show_label     = no
    size           = 6p
    </tick>
    
    <tick>
    spacing        = 1u
    show_label     = yes
    label_size     = 16p
    size           = 10p
    </tick>
    
    <tick>
    spacing        = 5u
    show_label     = yes
    label_size     = 18p
    size           = 14p
    </tick>
    
    <tick>
    spacing        = 10u
    show_label     = yes
    label_size     = 20p
    size           = 18p
    </tick>
    
    <tick>
    spacing        = 20u
    show_label     = yes
    label_size     = 24p
    size           = 22p
    </tick>
    
    <tick>
    spacing        = 100u
    show_label     = yes
    label_size     = 24p
    size           = 22p
    </tick>
    
    </ticks>
```
  

* * *
