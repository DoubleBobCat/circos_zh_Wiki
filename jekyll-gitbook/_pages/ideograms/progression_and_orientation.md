---
author: DoubleCat
date: 2025-04-11
layout: post
category: ideograms
title: Progression and Orientation
---

### lesson
#### angle offset
The angle offset determines the angular position of the first ideogram.

```    
          -90
           |
     180 --+-- 0
           |
           90
```
The default value is 0, which makes the first ideogram appear at 3 o'clock. I
like to use -90 to make the first ideogram appear at the top of the circle.

```    
    <image>
    angle_offset = -90
    ...
    </image>
```
#### ideogram progression
The progression of ideograms around the circle is controlled by the
angle_orientation parameter in the <image> block, which can be either
`clockwise` (this is the default) or `counterclockwise`.

```    
    <image>
    angle_orientation = counterclockwise
    ...
    </image>
```
Don't forget that if you've included your image parameters from another file,
you can override the any of those parameters using the `*` suffix.

```    
    <image>
    <<include etc/image.conf>>
    angle_orientation* = counterclockwise
    ...
    </image>
```
The direction of the scale of each ideogram will, by default, be the same as
the orientation. For example, if `angle_orientation=counterclockwise` the
direction of the scale of each ideogram will counterclockwise.

#### ideogram orientation
The orientation of ideograms is globally controlled by `angle_orientation`. To
adjust the orientation of the scale for individual ideograms, use

```    
    chromosomes_reverse = hs1,hs2,...
```
This setting reverses the ideogram orientation relative to the default
orientation, which is controlled by the ideogram progression set by
angle_orientation.

Why would you want to reverse individual ideograms? If you are using ribbon
links to show alignments, you can have control whether the ribbon twists or
not by adjusting the ideogram orientation. Or, if you are only showing two
ideograms (e.g. a sample and a reference), it may be more instructive to show
the ideograms with their start, and end, points near each other, respectively.
This would be achieved by

```    
    chromosomes = hs1;hs2
    chromosomes_reverse = hs2
```### images
![Circos tutorial image - Progression and
Orientation](/documentation/tutorials/ideograms/progression_and_orientation/img/01.png)
![Circos tutorial image - Progression and
Orientation](/documentation/tutorials/ideograms/progression_and_orientation/img/02.png)
![Circos tutorial image - Progression and
Orientation](/documentation/tutorials/ideograms/progression_and_orientation/img/03.png)
![Circos tutorial image - Progression and
Orientation](/documentation/tutorials/ideograms/progression_and_orientation/img/04.png)
### configuration
#### circos.conf
```    
    <<include etc/colors_fonts_patterns.conf>>
    
    <<include ideogram.conf>>
    <<include ticks.conf>>
    
    <image>
    <<include etc/image.conf>>
    # The * suffix is used to overwrite any value of angle_orientation
    # in the etc/image.conf file included in this block.
    angle_orientation* = counterclockwise
    </image>
    
    karyotype   = data/karyotype/karyotype.human.txt
    
    chromosomes_units           = 1000000
    chromosomes_display_default = no
    
    # to explicitly define what is drawn
    chromosomes                 = hs1;hs2;hs3;hs4;hs5
    
    # reverse direction of individual ideograms 
    chromosomes_reverse = hs2;hs3
    
    <highlights>
    <highlight>
    file = data/3/chr.highlights.txt
    r0 = 0.9r
    r1 = 0.95r
    </highlight>
    </highlights>
    
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
    label_radius     = dims(ideogram,radius) - 0.25r
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
