---
author: DoubleCat
date: 2025-04-11
layout: post
category: links
title: Ribbon Twists
---

## Ribbon Twists
### lesson
A ribbon is drawn as a filled path. The corner vertices of the path are the
start and end positions of the spans defined by the link.

```    
    linkID chr1 start1 end1
    linkID chr2 start2 end2
```
The ribbon path is drawn in this direction

```    
     >>  start1 >> end1 >> end2 >> start2 >>
     |                                     |
     <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
```
Notice that the start positions of the link spans are connected by a path, and
so are the end positions.

Therefore, depending on the orientation of the ideograms associated with the
link, and the orientation of start/end coordinates, the ribbon _may twist_.
The first example image in this tutorial shows how this twist happens.

#### controling twist by ideogram orientation
One way to control the twisting of ribbons is to adjust the orientation of
ideograms. This is particularly effective when you have links between ideogram
pairs, shown in the second example image in this tutorial.

If your links are oriented in the same direction on both ideograms (i.e.
start1>end1 and start2>end2), then ribbons will twist if orientation of
ideograms is the same. This twisted visual representation, however, may be
inappropriate because it suggests that there is an inversion. One way to
untwist the ribbon is to adjust the orientation of the second ideogram

```    
    chromosomes_reverse = hs2
```
#### removing twist with "flat" parameter
If you want all your ribbons untwisted, regardless of ideogram orientation or
their relative start/end positions, set the flat flag in the <link> block

```    
    <link>
    ribbon = yes
    flat   = yes
    ...
    </link>
```
With the flat flag set, any adjustment to ideogram progression and orientation
will have no effect on the layout of the ribbons, which will always be drawn
untwisted.

You can add the flat parameter individually to a link.

```    
    linkID chr1 start1 end1 flat=yes
    linkID chr2 start2 end2 flat=yes
```
#### forcing twist with "twist" parameter
If you want all your ribbons twisted, regardless of ideogram orientation or
their relative start/end positions, set the twist flag in the <link> block

```    
    <link>
    ribbon = yes
    twist  = yes
    ...
    </link>
```
Like for "flat", the "twist" flag renders any adjustment to ideogram
progression and orientation independent of the twist appearance of ribbons,
which will always be drawn twisted.

You can individually force a link to be drawn as a twisted ribbon by adding
"twist" to the data file,

```    
    linkID chr1 start1 end1 twist=yes
    linkID chr2 start2 end2 twist=yes
```
#### adding twist with inverted coordinates
The "flat" and "twist" flags specify the twist state for a ribbon. These
parameters are useful when you want a particular twist state, regardless of
the layout of the ideograms and their orientation.

Another way to incorporate twist is to define the link coordinates to be
inverted. Thus, instead of

```    
    linkID chr1 start1 end1 
    linkID chr2 start2 end2 
```
you would define

```    
    linkID chr1 end1 start1
    linkID chr2 start2 end2
```
For example, instead of

```    
    link1 hs1 10 20
    link1 hs2 10 20
```
use

```    
    link1 hs1 20 10
    link1 hs2 10 20
```
Alternatively, if you want to keep your start coordinate always smaller than
the end, you can use inverted=1, like this

```    
    link1 hs1 10 20 inverted=1 # this inverts role of start/end for this span (now start=20 end=10)
    link1 hs2 10 20
```
With the link coordinates implicitly defining the orientation of the link, the
correct twist state will be drawn.
### images
![Circos tutorial image - Ribbon
Twists](/documentation/tutorials/links/twists/img/01.png) ![Circos tutorial
image - Ribbon Twists](/documentation/tutorials/links/twists/img/02.png)
![Circos tutorial image - Ribbon
Twists](/documentation/tutorials/links/twists/img/03.png) ![Circos tutorial
image - Ribbon Twists](/documentation/tutorials/links/twists/img/04.png)
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
    
    # to explicitly define what is drawn
    chromosomes         = hs1;hs2
    chromosomes_reverse = hs2
    
    chromosomes_display_default = no
    
    <highlights>
    <highlight>
    file = data/3/chr.highlights.txt
    r0 = 0.95r
    r1 = 0.975r
    </highlight>
    </highlights>
    
    <links>
    
    <link>
    
    #flat   = yes
    #twist  = yes
    ribbon = yes
    file   = data/5/ribbon.twist.txt
    
    radius        = 0.95r
    bezier_radius = 0r
    
    color            = grey
    stroke_color     = black
    stroke_thickness = 2
    
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
