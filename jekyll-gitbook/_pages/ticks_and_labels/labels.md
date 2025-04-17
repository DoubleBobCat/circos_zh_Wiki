---
author: DoubleCat
date: 2025-04-11
layout: post
category: ticks_and_labels
title: Tick Marks - Label Margins
---

### lesson
If your tick marks are densely spaced, their labels may overlap and lose their
legibility. Like the tick mark margin parameter, tick label margins help you
suppress labels that might overlap.

A tick label will not be drawn if its tick mark is not drawn. Thus, a natural
way to suppress labels is to suppress the tick marks. This is done using
tick_separation and is described in the previous tutorial.

Label separation is controlled independently using label_separation. Like
tick_separation, the label_separation parameter defines a minimum allowed
distance between labels. Labels closer than this distance to another label
will not be drawn. Also, as with tick marks themselves, label overlap is
checked within a tick mark group (i.e. 1u and 5u labels are compared for
overlap).

```    
    <ticks>
    
      tick_separation  = 2p
      label_separation = 5p
      ...
    
      <tick>
      tick_separation  = 5p
      label_separation = 10p
        ...
      </tick>
    
      ...
    
    </ticks>
```
The mechanics behind label margins work exactly the same way as tick mark
margins. For example, you can define label_separation globally or within
individual <tick> blocks.

Overlap is calculated in the angular direction only. Any tick label offset
does not change the way overlap is calculated, a process in which the radial
position of the label is disregarded. By introducing label offsets (shifting
labels of tick mark sets radially) you can effectively eliminate overlap
without supressing ticks. This is covered in the next section.

If you want to turn off label overlap check for a given tick mark group, set
label_separation=0p.

#### minimum label distance to ideogram edge
To suppress tick labels near the edge of the ideogram, use
min_label_distance_to_edge. This parameter can be used globally in the <ticks>
block to affect all ticks, or locally with a <tick> block to affect an
individual tick group.

```    
    <ticks>
    min_label_distance_to_edge = 10p
    ...
    <tick>
    min_label_distance_to_edge = 5p
    ...
    </tick>
    ...
    </ticks>
```
The corresponding parameter to suppress ticks near an ideogram edge is
min_distance_to_edge. If the tick mark is suppressed with this parmaeter then
no label is shown.

#### suppressing first or last label of a group
You can suppress the label of the first tick, or last tick, in a group using
skip_first_label and skip_last_label.

```    
    <ticks>
    skip_first_label = yes
    skip_last_label  = yes
    ...
    <tick>
    # will overwrite the skip_first_label for this tick group
    skip_first_label = no
    ...
    </tick>
    ...
    </ticks>
```
The purpose of this parameter is to reduce label clutter near the edges of the
ideogram. The effect is similar to using min_label_distance_to_edge, which was
described above, but skip_*_label affects at most one label.

The mechanics of the first/last label suppression is applied on a group-by-
group basis. Thus, if skip_last_label is set for all tick groups, the last
label for _each group_ will be suppressed, and not the last label on the
ideogram.
### images
![Circos tutorial image - Tick Marks - Label
Margins](/documentation/tutorials/ticks_and_labels/labels/img/01.png)
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
    
    chromosomes_units  = 1000000
    chromosomes        = hs1;hs2;hs3:0-100;hs4:100-150
    chromosomes_scale  = hs1:0.5;hs2:1;hs3:4;hs4:8
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
    radius               = dims(ideogram,radius_outer)
    multiplier           = 1e-6
    
    label_offset = 5p
    thickness = 3p
    size      = 20p
    
    # ticks must be separated by 2 pixels in order
    # to be displayed
    tick_separation      = 2p
    # Density of labels is independently controlled.
    # While all tick sets have labels, only labels
    # no closer than 5 pixels to nearest label will be drawn
    label_separation     = 5p
    
    <tick>
    spacing        = 0.5u
    color          = red
    show_label     = yes
    label_size     = 14p
    label_offset   = 0p
    format         = %.1f
    </tick>
    
    <tick>
    spacing        = 1u
    color          = blue
    show_label     = yes
    label_size     = 16p
    label_offset   = 0p
    format         = %d
    </tick>
    
    <tick>
    spacing        = 5u
    color          = green
    show_label     = yes
    label_size     = 20p
    label_offset   = 0p
    format         = %d
    </tick>
    
    <tick>
    spacing        = 10u
    color          = black
    show_label     = yes
    label_size     = 24p
    label_offset   = 5p
    format         = %d
    </tick>
    
    </ticks>
```
  

* * *
