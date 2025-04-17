---
author: DoubleCat
date: 2025-04-11
layout: post
category: scaling
title: Drawing Data with Scale Adjustment
---

### lesson
In this example, I use local scale adjustment to draw attention to regions of
chromosomes 1 and 2 in an image that contains sparse data.

The benefit of using scale adjustments is that the data domain is not cropped
and therefore all data points are plotted.
### images
![Circos tutorial image - Drawing Data with Scale
Adjustment](/documentation/tutorials/scaling/data_example/img/01.png) ![Circos
tutorial image - Drawing Data with Scale
Adjustment](/documentation/tutorials/scaling/data_example/img/02.png)
### configuration
#### circos.conf
```    
    <<include etc/colors_fonts_patterns.conf>>
    
    <ideogram>
    radius* = 0.8r
    </ideogram>
    
    <<include ideogram.conf>>
    <<include ticks.conf>>
    
    karyotype = data/karyotype/karyotype.human.txt
    
    <image>
    <<include etc/image.conf>>
    </image>
    
    chromosomes_units           = 1000000
    chromosomes_display_default = no
    
    chromosomes                 = hs1;hs2
    #chromosomes                = hs1[a]:0-0.8;hs1[b]:16.6-17.2;hs1[c]:141.5-148;hs1[d]:220.6-222.4;hs2[e]:90.8-95.2;hs2[f]:132.3-132.8;hs2[g]:242.5-)
    #chromosomes_breaks = -hs1:142.3-143.9;-hs1:144.2-144.7;-hs1:145-146;-hs1:220.8-222;-hs2:91.8-94.6
    
    <zooms>
    smooth_distance = 1r
    smooth_steps    = 40
    <zoom>
    chr = hs1
    start = 0u
    end = 0.5u
    scale = 120
    </zoom>
    <zoom>
    chr = hs1
    start = 16.7u
    end = 17u
    scale = 200
    </zoom>
    <zoom>
    chr = hs1
    start = 20u
    end = 100u
    scale = 0.1
    </zoom>
    <zoom>
    chr = hs1
    start = 144u
    end = 145u
    scale = 20
    </zoom>
    <zoom>
    chr = hs1
    start = 160u
    end = 195u
    scale = 0.1
    </zoom>
    <zoom>
    chr = hs2
    start = 10u
    end = 80u
    scale = 0.1
    </zoom>
    <zoom>
    chr = hs2
    start = 89.5u
    end = 110u
    scale = 10
    </zoom>
    <zoom>
    chr = hs2
    start = 87.2u
    end = 87.8u
    scale = 40
    </zoom>
    <zoom>
    chr = hs2
    start = 90.5u
    end = 92u
    scale = 40
    </zoom>
    <zoom>
    chr = hs2
    start = 93u
    end = 103u
    scale = 0.02
    </zoom>
    <zoom>
    chr = hs2
    start = 109.5u
    end = 112.5u
    scale = 20
    </zoom>
    <zoom> 
    chr = hs2
    start = 115u
    end =  240u
    scale = 0.1
    </zoom>
    </zooms>
    
    <links>
    
    radius = 0.99r
    crest  = 1
    color  = grey
    bezier_radius        = 0r
    bezier_radius_purity = 0.5
    
    <link>
    file         = data/5/segdup.txt
    ribbon       = yes
    thickness    = 2
    stroke_color = vdgrey
    stroke_thickness = 2
    
    <rules>
    
    flow = continue
    
    <rule>
    condition  = var(intrachr)
    condition  = abs(var(pos1) - var(pos2)) < 10Mb
    show       = no
    </rule>
    
    <rule>
    condition  = max(var(size1),var(size2)) < 5000
    show       = no
    </rule>
    
    <rule>
    condition  = 1
    z          = eval(int(max(var(size1),var(size2))/5000))
    </rule>
    
    <rule>
    condition    = var(intrachr) 
    condition    = (var(chr1) eq "hs1" && var(start1) < 1Mb) || (var(chr2) eq "hs1" && var(start2) < 1Mb)
    color        = orange
    stroke_color = dorange
    </rule>
    
    <rule>
    condition    = var(intrachr) 
    condition    = (var(chr1) eq "hs1" && var(start1) > 16Mb && var(start1) < 17Mb) || (var(chr2) eq "hs1" && var(start2) > 16Mb && var(start2) < 17Mb)
    color        = lblue
    stroke_color = dblue
    </rule>
    
    </rules>
    
    </link>
    
    </links>
    
    <plots>
    <plot>
    type  = heatmap
    file  = data/7/heatmap.zoom-06.txt
    r1    = 1.16r
    r0    = 1.12r
    color = spectral-9-div
    stroke_thickness = 0
    scale_log_base   = 0.5
    </plot>
    </plots>
    
    <<include etc/housekeeping.conf>>
    data_out_of_range* = trim
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
    label_separation = 10p
    tick_separation  = 3p
    radius           = dims(ideogram,radius_outer)
    multiplier       = 1e-6
    label_offset     = 0p
    color            = black
    
    <tick>
    spacing        = 0.02u
    size           = 5p
    thickness      = 2p
    show_label     = no
    label_size     = 12p
    format         = %.1f
    </tick>
    
    <tick>
    spacing        = 0.1u
    size           = 8p
    thickness      = 2p
    show_label     = yes
    label_size     = 12p
    format         = %.1f
    </tick>
    
    <tick>
    spacing        = 0.5u
    size           = 10p
    thickness      = 2p
    show_label     = yes
    label_size     = 12p
    format         = %.1f
    </tick>
    
    <tick>
    spacing        = 1u
    size           = 12p
    thickness      = 2p
    show_label     = yes
    label_size     = 12p
    format         = %d
    </tick>
    
    <tick>
    spacing        = 5u
    size           = 14p
    thickness      = 2p
    show_label     = yes
    label_size     = 16p
    format         = %d
    </tick>
    
    <tick>
    spacing        = 10u
    size           = 18p
    thickness      = 2p
    show_label     = yes
    label_size     = 20p
    label_offset   = 5p
    format         = %d
    </tick>
    
    </ticks>
```
  

* * *
