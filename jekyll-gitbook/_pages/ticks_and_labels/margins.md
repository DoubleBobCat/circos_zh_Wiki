---
author: DoubleCat
date: 2025-04-11
layout: post
category: ticks_and_labels
title: Tick Marks - Margins
---

## Tick Marks - Margins
### lesson
If your ticks are densely spaced, they may overlap and form dreaded tick
blobs. Likewise, tick labels can start to overlap and lose their legibility.
To mitigate this problem, you can insist that adjacent ticks (or labels) are
separated by a minimum distance.

Here I show how to manage spacing between tick marks. The next tutorial
discusses label spacing.

#### minimum tick mark separation
The tick_separation parameter controls the minimum distance between two ticks
marks. Note that this parameter applies to tick marks only, not to labels.
Labels have their own minimum distance parameter, covered in the next session.
Of course, if a tick mark is not drawn, neither will its label.

```    
    <ticks>
      # define minimum separation for all ticks
      tick_separation = 3p
      ...
    
      <tick>
      # define minimum separation for a specific tick group
      tick_separation = 2p
        ...
      </tick>
    
      ...
    
    </ticks>
```
The primary purpose of the tick_separation parameter is to allow automatic
supression of ticks if you shrink the image size, change the ideogram position
radius, change the ideogram scale or, in general, perform any adjustment to
the image that changes the base/pixel resolution.

Since Circos supports local scale adjustments (at the level of ideogram, or
region of ideogram), the the tick separation parameter is used to dynamically
show/hide ticks across the image. You should keep this value at 2-3 pixels at
all times, so that your tick marks do not run into each other.

Tick marks are suppressed on a group-by-group basis. In other words, tick
separation is checked separately for each <tick> block. For example, if you
define 1u, 5u and 10u ticks, these will be checked for overlap independently
(Circos does not check if the 10u tick overlaps with a tick from another
group, such as the 1u tick).

This approach is slightly different than the method that was initially
implemented, which compared inter-tick distances across tick groups.

The tick mark thickness plays no role in determining the distance between
ticks. The tick-to-tick distance is calculated based on the positions of the
ticks.

In the first example image in this tutorial, three ideograms are drawn, each
at a different scale. Depending on the magnification, ticks are suppressed for
some ideograms because they are closer than the tick_separation parameter. For
example, 0.25u and 0.5u ticks do not appear on hs1 and 0.25u ticks do not
appear on hs2.

In the second example image, only one chromosome is shown but its scale is
smoothly expanded. Region 100-110 Mb is magnified at 10x and with the scale in
the neighbourhood decreasing smoothly from 10x to 1x. All tick marks are shown
within the magnified area and away from it, as the scale returns to 1x, some
ticks disappear.

#### minimum tick distance to ideogram edge
To suppress ticks near the edge of the ideogram, use min_distance_to_edge.
This parameter can be used globally in the <ticks> block to affect all ticks,
or locally with a <tick> block to affect an individual tick group.

```    
    <ticks>
    min_distance_to_edge = 10p
    ...
    <tick>
    min_distance_to_edge = 5p
    ...
    </tick>
    ...
    </ticks>
```
The corresponding parameter to suppress labels near an ideogram edge is
min_label_distance_to_edge.
### images
![Circos tutorial image - Tick Marks -
Margins](/documentation/tutorials/ticks_and_labels/margins/img/01.png)
![Circos tutorial image - Tick Marks -
Margins](/documentation/tutorials/ticks_and_labels/margins/img/02.png)
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
    
    chromosomes_units   = 1000000
    chromosomes_display_default = no
    #chromosomes        = hs1;hs2;hs3:0-100
    chromosomes         = hs1
    #chromosomes_scale  = hs1:0.5;hs2:1;hs3:6.5
    
    <zooms>
    <zoom>
    chr   = hs1
    start = 100u
    end   = 110u
    scale = 10
    smooth_steps = 10
    smooth_distance = 5r
    </zoom>
    </zooms>
    
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
    
    label_offset   = 5p
    thickness      = 4p
    size           = 20p
    # ticks must be separated by 10 pixels in order to be displayed
    tick_separation      = 15p
    
    <tick>
    spacing        = 0.25u
    color          = red
    show_label     = no
    label_size     = 12p
    format         = %.2f
    </tick>
    
    <tick>
    spacing        = 0.5u
    color          = blue
    show_label     = no
    label_size     = 12p
    format         = %.2f
    </tick>
    
    <tick>
    spacing        = 1u
    color          = green
    show_label     = no
    label_size     = 12p
    format         = %.2f
    </tick>
    
    <tick>
    spacing        = 5u
    color          = black
    show_label     = yes
    label_size     = 20p
    format         = %d
    </tick>
    
    <tick>
    spacing        = 10u
    color          = black
    show_label     = yes
    label_size     = 24p
    format         = %d
    </tick>
    
    </ticks>
```
  

* * *
