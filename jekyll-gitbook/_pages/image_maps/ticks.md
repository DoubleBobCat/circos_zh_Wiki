---
author: DoubleCat
date: 2025-04-11
layout: post
category: image_maps
title: Clickable Tick Marks
---

### lesson
To create links that access regions of an ideogram, define a `url` parameter
within a <tick> mark block.

```    
    <tick>
    spacing  = 25u
    size     = 10p
    ...
    url      = script?type=tick&start=[start]&end=[end]
    </tick>
```
With this setting, the area in the image map associated with the tick will be
a slice that extends from the base of the tick (usually outer ideogram
radius), to the end of the tick (defined by the tick size). Since this may be
too small, you can use the `map_size` parameter to extend the area to any
value.

```    
    <tick>
    spacing  = 25u
    size     = 10p
    ...
    url      = script?type=tick&start=[start]&end=[end]
    map_size = 100p
    </tick>
```
The first image in this tutorial shows the image map with a `map_size=100p`.
This value may take on a negative value, in which case the link area will be
extended inward from the base of the tick. This is shown in the second example
image.

You can precisely control the radial extent of the tick mark link area by
using `map_radius_inner` and `map_radius_outer`.

```    
    <tick>
    spacing  = 25u
    size     = 10p
    ...
    url      = script?type=tick&start=[start]&end=[end]
    map_radius_inner = 0.5r
    map_radius_outer = 1.2r
    </tick>
```
#### multiple tick maps
You can define any number of tick map layers. The fourth image in this example
shows two tick mark layers: one layer of absolute ticks spaced every 25Mb and
one layer of relative ticks spaced every 1/4 of an ideogram. Each layer is at
a different radius and has its own set of links.

If you have multiple tick definitions at the same radius (e.g. one tick
definition for 25Mb ticks, one for 5Mb ticks and one for 1Mb ticks, for
example), I suggest that you attach a url parameter to only one of them.
Although you can create overlapping image map elements for each tick spacing,
this is likely to confuse the user.
### images
![Circos tutorial image - Clickable Tick
Marks](/documentation/tutorials/image_maps/ticks/img/01.png) ![Circos tutorial
image - Clickable Tick
Marks](/documentation/tutorials/image_maps/ticks/img/02.png) ![Circos tutorial
image - Clickable Tick
Marks](/documentation/tutorials/image_maps/ticks/img/03.png) ![Circos tutorial
image - Clickable Tick
Marks](/documentation/tutorials/image_maps/ticks/img/04.png)
### configuration
#### circos.conf
```    
    <<include colors_fonts_patterns.conf>>
    
    <<include ideogram.conf>>
    
    <ideogram>
    band_url* = undef
    </ideogram>
    
    <<include ticks.conf>>
    
    karyotype   = data/karyotype/karyotype.human.txt
    
    <image>
    <<include etc/image.conf>>
    
    ################################################################
    # Here are the new image map parameters
    
    image_map_use      = yes
    
    image_map_missing_parameter = removeurl
    
    #image_map_name     = circos
    #image_map_file     = circos-tutorial.html
    #image_map_protocol = http
    #image_map_xshift = 0
    #image_map_yshift = 0
    
    # original image is 3000 x 3000, resized for web at 800 x 800
    
    image_map_xfactor = 0.266667
    image_map_yfactor = 0.266667
    image_map_overlay                  = yes
    #image_map_overlay_fill_color      = lred_a5
    image_map_overlay_stroke_color     = red
    image_map_overlay_stroke_thickness = 2
    
    </image>
    
    chromosomes_units           = 1000000
    #chromosomes                 = hs1:0-50
    chromosomes_display_default = yes
    
    <<include etc/housekeeping.conf>>
```
  

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
    </spacing>
    
    <<include ideogram.position.conf>>
    <<include ideogram.label.conf>>
    <<include bands.conf>>
    
    #ideogram_url = https://www.google.com
    #ideogram_url = https://www.google.com/search?q=[chr]
    #ideogram_url = script?type=ideogram&start=[start]&end=[end]&length=[chrlength]&chr=[chr]&tag=[tag]&label=[label]&idx=[idx]&display_idx=[display_idx]&scale=[scale]
    #ideogram_url = script?chr=[chr]
    band_url = script?start=[start]&end=[end]&label=[label]
    
    </ideogram>
``````
  

* * *

#### ideogram.label.conf
```    
    show_label       = yes
    label_font       = default
    label_radius     = dims(image,radius) - 70p
    label_size       = 48
    label_parallel   = yes
    label_case       = upper
```
  

* * *

#### ideogram.position.conf
```    
    radius           = 0.85r
    thickness        = 100p
    fill             = yes
    fill_color       = black
    stroke_thickness = 2
    stroke_color     = black
```
  

* * *

#### ticks.conf
```    
    show_ticks       = yes
    show_tick_labels = yes
    
    show_grid  = no
    
    <ticks>
    
    radius         = dims(ideogram,radius_outer)
    label_offset   = 10p
    multiplier     = 1e-6
    color          = black
    
    <tick>
    
    spacing        = 25u
    size           = 10p
    thickness      = 3p
    color          = black
    show_label     = yes
    label_size     = 30p
    label_offset   = 0p
    format         = %d
    grid           = yes
    grid_color     = grey
    grid_thickness = 2p
    
    url              = script?type=tick&chr=chr[label]&start=[start]&end=[end]
    map_size         = 100p
    
    #map_radius_inner = 0.5r
    #map_radius_outer = 1.2r
    
    </tick>
    
    <tick>
    
    show = no
    
    spacing        = 5u
    spacing_type   = relative
    rspacing       = 0.25
    size           = 10p
    radius         = 0.9r
    thickness      = 3p
    color          = black
    show_label     = yes
    label_size     = 30p
    label_relative = yes
    label_offset   = 0p
    format         = %.0f
    rmultiplier    = 100
    suffix         = %
    grid           = yes
    grid_color     = grey
    grid_thickness = 2p
    
    url              = script?type=tick&chr=chr[label]&start=[start]&end=[end]
    map_size         = -100p
    
    #map_radius_inner = 0.5r
    #map_radius_outer = 1.2r
    
    </tick>
    
    </ticks>
```
  

* * *
