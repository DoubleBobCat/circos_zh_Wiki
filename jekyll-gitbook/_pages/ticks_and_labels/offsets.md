---
author: DoubleCat
date: 2025-04-11
layout: post
category: ticks_and_labels
title: Tick Marks - Offsets
---

### lesson
The radial position of ticks and labels can be adjusted by the offset
parameter.

#### tick mark offset
The tick mark offset can be specified in the <ticks> and/or <tick> blocks. The
offset can be in pixels, or specified relatively (in which case it is relative
to ideogram thickness) and controls the degree of radial shift applied to both
the tick mark and its label (it would not be wise to shift the tick mark
without applying the same offset to the label). Both the tick mark and the
label are shifted by the same amount (independent offset can be applied to the
label - read below).

```    
    <ticks>
    ...
    offset = 2p
    ...
      <tick>
      offset = 1p
      ...
      </tick>
    </ticks>
```
#### tick label offset
The label offset is an additional offset that can be applied to the label,
without further disturbing the radial position of the tick mark.

Both global and local label offsets are allowed, and they are cumulative.

A label offset expressed in relative form (label_offset=0.5r) is relative to
the size of the corresponding tick.

```    
    <ticks>
    ...
    # all labels offset by 0.4x their tick size
    label_offset = 0.4r
    ...
      <tick>
      # this label has an additional 2 pixel offset
      label_offset = 2p
      ...
      </tick>
    </ticks>
```### images
![Circos tutorial image - Tick Marks -
Offsets](/documentation/tutorials/ticks_and_labels/offsets/img/01.png)
![Circos tutorial image - Tick Marks -
Offsets](/documentation/tutorials/ticks_and_labels/offsets/img/02.png)
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
    chromosomes_display_default = no
    chromosomes                 = hs1:0-100
    
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
    # global offset for ticks (remember that labels are automatically offset)
    offset               = 0p
    radius               = dims(ideogram,radius_outer)
    multiplier           = 1e-6
    
    thickness      = 4p
    
    # if set to yes, all ticks at all spacings will be drawn, regardless of whether
    # there is another tick at this position (e.g. at 100Mb the ticks for 10u, 5u and 1u
    # will be drawn. force_display=yes is useful only when offset is used to make each
    # tick set drawn at a different radial position)
    force_display        = no
    
    # global label offset - useful if set to relative size
    # (will be relative to ticks size)
    # local label offsets add to this value
    # label_offset = 0.5r
    
    <tick>
    spacing        = 0.5u
    offset         = 0p
    size           = 15p
    color          = red
    show_label     = yes
    label_size     = 20p
    label_offset   = dims(tick,max_tick_length) - 15p
    format         = %.1f
    </tick>
    
    <tick>
    spacing        = 1u
    offset         = 0p
    size           = 20p
    color          = blue
    show_label     = yes
    label_size     = 20p
    label_offset   = dims(tick,max_tick_length) - 20p
    format         = %d
    </tick>
    
    <tick>
    spacing        = 5u
    offset         = 0p
    size           = 25p
    color          = green
    show_label     = yes
    label_size     = 20p
    label_offset   = dims(tick,max_tick_length) - 25p
    format         = %d
    </tick>
    
    <tick>
    spacing        = 10u
    offset         = 0p
    size           = 30p
    color          = black
    show_label     = yes
    label_size     = 24p
    label_offset   = dims(tick,max_tick_length) - 30p
    format         = %d
    </tick>
    
    </ticks>
```
  

* * *
