---
author: DoubleCat
date: 2025-04-11
layout: post
category: scaling
title: Smoothing Scale
---

## Smoothing Scale
### lesson
In the last example, I created a series of regions with gradually
increasing/decreasing scale in order to avoid large changes in scale over
short distances.

To automate scale smoothing, each zoom block supports a smooth_distance and
smooth_steps parameters. When using the smoothing feature, you define the zoom
setting for your region of interest and then the number of smoothing steps and
distance over which the scale smoothing is applied. Flanks around your zoomed
region will have their scale progressively grow/shrink from the scale of your
zoomed region to 1.

```    
    <zoom>
    chr    = hs1
    start  = 120u
    end    = 125u
    scale  = 10
    smooth_distance = 2r
    smooth_steps    = 10
    </zoom>
```
In this block, I define a 5Mb region on chromosome 1 that is expanded to 10x
scale. The smoothing distance is 2r = 10Mb (here the "r" is relative to the
size of the zoomed region) and smoothing is applied over 10 steps. Each
smoothing step is 10Mb/10 = 1Mb and the scale decreases linearly across the
smoothing regions.

You can define the smooth_distance parameter in relative units (r), chromosome
units (u) or bases (b).
### images
![Circos tutorial image - Smoothing
Scale](/documentation/tutorials/scaling/scale_smoothing/img/01.png) ![Circos
tutorial image - Smoothing
Scale](/documentation/tutorials/scaling/scale_smoothing/img/02.png) ![Circos
tutorial image - Smoothing
Scale](/documentation/tutorials/scaling/scale_smoothing/img/03.png)
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
    start  = 120u
    end    = 125u
    scale  = 10
    
    smooth_distance = 2r
    smooth_steps    = 10
    
    </zoom>
    
    <zoom>
    
    smooth_distance = 10r
    smooth_steps    = 5
    
    chr    = hs2
    start  = 120u
    end    = 125u
    scale  = 0.1
    </zoom>
    
    </zooms>
    
    chromosomes_units = 1000000
    chromosomes = hs1;hs2
    chromosomes_display_default = no
    
    <plots>
    <plot>
    type  = heatmap
    file  = data/7/heatmap.zoom-04.txt
    r1    = 0.95r
    r0    = 0.90r
    color = spectral-9-div
    stroke_color     = black
    stroke_thickness = 1
    scale_log_base   = 0.5
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
