---
author: DoubleCat
date: 2025-04-11
layout: post
category: recipes
title: Automating Heatmaps
---

## Automating Heatmaps
### lesson
Before reading this tutorial, make sure that you understand how dynamic
configuration parameters work (see [Configuration Files
Tutorial](/documentation/tutorials/configuration/configuration_files/)) and
have read through the [Automating Tracks
Tutorial](/documentation/tutorials/recipes/automating_tracks/).

For this tutorial, I have created an image with 100 heat map tracks. The data
for these tracks are gene densities computed across differently sized windows
(0.5-50 Mb). The higest resolution file is `data/8/17/genes.0.txt` which
samples density every 500kb. The lowest resolution file is
`data/8/17/genes.99.txt` which samples density every 50,000kb (1/100th
resolution of `genes.0.txt`).

The gene densities were designed so that each heat map interval occupies the
same number of pixels along the map's circumference.

#### changing heat map color
The color of the heat map is specified using a list of colors

```    
    color = red,green,blue
```
or a color list

```    
    color = spectral-11-div
```
For more about color lists, see the [Configuration Files
Tutorial](/documentation/tutorials/configuration/configuration_files/).

The track counter can be used to dynamically change the color scheme. For
example, as the track counter increases from 0 to 99, the definition

```    
    color = eval(sprintf("spectral-%d-div",remap_round(counter(plot),0,99,11,3)))
```
will assign a list to a track based on the counter. The assignment will range
from `spectral-11-div` for the outer-most track, progressing through
`spectral-10-div`, ..., and end at `spectral-3-div` for the inner-most track.

You can combine multiple color maps. Here, an orange sequential color list is
added to a reversed blue sequential one.

```    
    color = eval(sprintf("blues-%d-seq-rev,oranges-%d-seq-rev",
                         remap_round(counter(plot),0,99,9,3),
                         remap_round(counter(plot),0,99,9,3)))
```
Given the reduced resolution of the inner-most track, reducing the number of
colors in its heat map can make the figure more legible.

#### adjusting log scaling
The `scale_log_base` parameter controls how heat map values are mapped onto
colors. The default value of this parameter is `scale_log_base = 1`, which
corresponds to a linear mapping. For more details about this parameter, see
the [Heat Map Tutorial](/documentation/tutorials/2d_tracks/heat_maps/).

Keeping the color list constant, but varying the `scale_log_base`, you can
increase the dynamic range of color sampling for small values (if
`log_scale_base < 1`) or large values (if `log_scale_base > 1`).

```    
    color          = spectral-11-div
    # 0.05, 0.10, 0.15, ..., 5.00
    scale_log_base = eval(0.05*(1+counter(plot)))
```### images
![Circos tutorial image - Automating
Tracks](/documentation/tutorials/recipes/automating_heatmaps/img/image-01.png)
![Circos tutorial image - Automating
Tracks](/documentation/tutorials/recipes/automating_heatmaps/img/image-02.png)
![Circos tutorial image - Automating
Tracks](/documentation/tutorials/recipes/automating_heatmaps/img/image-03.png)
![Circos tutorial image - Automating
Tracks](/documentation/tutorials/recipes/automating_heatmaps/img/image-04.png)
![Circos tutorial image - Automating
Tracks](/documentation/tutorials/recipes/automating_heatmaps/img/image-05.png)
![Circos tutorial image - Automating
Tracks](/documentation/tutorials/recipes/automating_heatmaps/img/image-06.png)
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
    chromosomes_display_default = no
    
    chromosomes = hs1;hs2;hs3
    
    track_width   = 0.007
    track_start   = 0.991
    track_step    = 0.01
    
    <plots>
    
    type = heatmap
    min  = 0
    max  = 1
    
    <<include 10plot.conf>>
    <<include 10plot.conf>>
    <<include 10plot.conf>>
    <<include 10plot.conf>>
    <<include 10plot.conf>>
    
    <<include 10plot.conf>>
    <<include 10plot.conf>>
    <<include 10plot.conf>>
    <<include 10plot.conf>>
    <<include 10plot.conf>>
    
    </plots>
    
    <<include etc/housekeeping.conf>>
```
  

* * *

#### 10plot.conf
```    
    <<include plot.conf>>
    <<include plot.conf>>
    <<include plot.conf>>
    <<include plot.conf>>
    <<include plot.conf>>
    <<include plot.conf>>
    <<include plot.conf>>
    <<include plot.conf>>
    <<include plot.conf>>
    <<include plot.conf>>
```
  

* * *

#### color.conf
```    
    # The track counter will run 0-99, and we want to map this into range 3..11 
    # to smoothly vary the spectral color map
    #color = spectral-11-div
    color = eval(sprintf("spectral-%d-div",remap_round(counter(plot),0,99,11,3)))
    
    # The track counter will run 0-99, and we want to map this into range 3..9
    # to smoothly vary the red color map
    # color = eval(sprintf("reds-%d-seq",remap_round(counter(plot),0,99,9,3)))
    
    # Combine two color maps
    #color = eval(sprintf("blues-%d-seq-rev,oranges-%d-seq-rev",remap_round(counter(plot),0,99,9,3),remap_round(counter(plot),0,99,9,3)))
```
  

* * *

#### file.conf
```    
    file    = data/8/17/genes.counter(plot).txt
```
  

* * *

#### ideogram.conf
```    
    <ideogram>
    
    show = no
    
    <spacing>
    
    default = 0u
    
    </spacing>
    
    # thickness (px) of chromosome ideogram
    thickness        = 20p
    stroke_thickness = 2
    # ideogram border color
    stroke_color     = black
    fill             = yes
    # the default chromosome color is set here and any value
    # defined in the karyotype file overrides it
    fill_color       = black
    
    # fractional radius position of chromosome ideogram within image
    radius         = 1r
    show_label     = no
    label_with_tag = yes
    label_font     = default
    label_radius   = dims(ideogram,radius) + 0.075r
    label_size     = 60p
    
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

#### plot.conf
```    
    <plot>
    <<include file.conf>>
    <<include r0r1.conf>>
    <<include color.conf>>
    <<include rules.conf>>
    scale_log_base = eval(0.05*(100-counter(plot)))
    </plot>
```
  

* * *

#### r0r1.conf
```    
    r0      = eval(sprintf("%fr",conf(track_start)-counter(plot)*conf(track_step)))
    r1      = eval(sprintf("%fr",conf(track_start)+conf(track_width)-counter(plot)*conf(track_step)))
    orientation = eval( counter(plot) % 2 ? "in" : "out" )
```
  

* * *

#### rules.conf
```    
    <rules>
    
    # If you wish, you can generate the random
    # values using this rule. Don't forget to set
    # flow=continue so that rule testing
    # doesn't short-circuit.
    #<rule>
    #condition  = 1
    #value      = eval(rand())
    #flow       = continue
    #</rule>
    
    <rule>
    importance = 100
    condition  = var(value) < 0.005
    #fill_color = white
    show = no
    </rule>
    </rules>
```
  

* * *

#### ticks.conf
```    
    show_ticks          = yes
    show_tick_labels    = yes
    
    <ticks>
    radius               = dims(ideogram,radius_outer)
    multiplier           = 1e-6
    
    <tick>
    spacing        = 5u
    size           = 10p
    thickness      = 3p
    color          = black
    show_label     = yes
    label_size     = 24pp
    label_offset   = 5p
    format         = %d
    </tick>
    
    <tick>
    spacing        = 20u
    size           = 16p
    thickness      = 3p
    color          = black
    show_label     = yes
    label_size     = 30p
    label_offset   = 5p
    format         = %d
    </tick>
    
    </ticks>
```
  

* * *
