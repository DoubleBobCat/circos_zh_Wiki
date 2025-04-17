---
author: DoubleCat
date: 2025-04-11
layout: post
category: ticks_and_labels
title: Relative Ticks
---

### lesson
Ticks can be spaced and/or labeled in relative units, with respect to the
length of the ideogram to which they belong. Up to now, you've seen how to
label and space ticks in absolute distances (e.g. every 10 Mb), and this
tutorial shows you how to space your ticks in relative distances (e.g. every
1% along ideogram).

There are two independent relative tick settings: relative spacing and
relative labels. Relative spacing is used to set the tick period to be
relative to the ideogram (e.g. every 1%). Relative labels are used to format
the label of the tick to be relative to the length of the ideogram. These two
settings are independent. You can have ticks spaced relatively, but labeled by
their absolute position, and vice versa.

#### Relative Spacing
To space ticks relatively, use the rspacing and spacing_type parameter in the
block. For example, to place ticks every 1% along the ideogram,

```    
    <ticks>
    <tick>
    spacing_type = relative
    rspacing     = 0.01
    ...
    </tick>
    ...
    </ticks>
```
Note that relative spacing parameters do not collide with absolute spacing,
which is defined by the "spacing" parameter. This means that you can have both
"spacing" and "rspacing" defined, and then toggle between relative and
absolute spacing by defining the value of spacing_type.

```    
    <ticks>
    # this tick is relatively spaced
    <tick>
    spacing      = 10u
    rspacing     = 0.01
    spacing_type = relative
    ...
    </tick>
    
    # this tick is absolutely spaced
    <tick>
    spacing      = 10u
    rspacing     = 0.01
    spacing_type = absolute
    ...
    </tick>
    ...
    </ticks>
```
Since each tick definition is independent, you can mix relatively spaced ticks
with absolutely spaced ticks. For example, you can have ticks every 10Mb and
every 10% if you like.

```    
    <ticks>
    # these ticks are every 1Mb (assumes chromosome_units=1000000)
    <tick>
    spacing      = 1u
    spacing_type = absolute
    ...
    </tick>
    
    # these ticks are every 1% of ideogram 
    <tick>
    rspacing     = 0.01
    spacing_type = relative
    ...
    </tick>
    ...
    </ticks>
```
In the first example image, there are three layers of ticks: absolute spacing
every 1Mb, relative spacing every 0.01 and relative spacing every 0.1. Notice
that the labels for each tick layer are absolute. This works well for
absolutely spaced ticks, but looks awkward for relatively spaced ticks (e.g.
first tick in relative layer 0.1 is "24").

#### Relative Labels
When ticks are relatively spaced (e.g. every 1%), it makes more sense that
their labels are relative too (e.g. appear as 1% rather than the corresponding
absolute amount, such as 24.72 for chr1). To set the tick label to be
relative, use the label_relative and rmultiplier settings.

```    
    <tick>
    spacing_type   = relative
    rspacing       = 0.01
    label_relative = yes
    format         = %.2f
    ...
    </tick>
```
You can define a relative multiplier for the label so that relative labels
like "0.07" can be displayed as "7".

```    
    <tick>
    spacing_type   = relative
    rspacing       = 0.01
    label_relative = yes
    format         = %.2f # labels will be 0.01 0.02 0.03 ...
    ...
    </tick>
```
With these settings, the tick labels will read 0.01, 0.02, ... 0.99. The
"rmultiplier" works just like "multiplier", but is reserved for labels of
relatively spaced ticks. If rmultiplier was set to 100, the tick labels would
be 1.00, 2.00, ... 99.00. For example, to have ticks every 1% labeled 1%, 2%,
... 99%, use

```    
    <tick>
    spacing_type   = relative
    rspacing       = 0.01
    label_relative = yes
    rmultiplier    = 100 # labels will be 1 2 3 4 ... 
    format         = %d
    </tick>
```
By adding a suffix, you can construct labels such as "6%" or "2/10".

```    
    <tick>
    spacing_type   = relative
    rspacing       = 0.01
    label_relative = yes
    rmultiplier    = 100 
    format         = %d
    suffix         = %  # labels will be 1% 2% 3% ... 
    </tick>
    
    <tick>
    spacing_type   = relative
    rspacing       = 0.1
    label_relative = yes
    rmultiplier    = 10 
    format         = %d
    suffix         = "/10" # labels will be 1/10 2/10 3/10 ...
    </tick>
```
#### relative ticks - relative to chromsomes or ideograms
If a chromosome is represented by a single ideogram in its entirety, then the
default relative tick settings, which are relative to chromosome size, are
appropriate.

However, if you are displaying a fraction of a chromosome, or are splitting it
up into multiple ideograms, you may wish to make tick marks relative to the
ideogram and not the chromosome. To do this, set the rdivisor.

```    
    <tick>
    spacing_type   = relative
    rspacing       = 0.1
    rdivisor       = ideogram
    </tick>
```
With this block, ticks will be spaced every 1/10th of the ideogram they belong
to.
### images
![Circos tutorial image - Relative
Ticks](/documentation/tutorials/ticks_and_labels/relative_ticks/img/01.png)
![Circos tutorial image - Relative
Ticks](/documentation/tutorials/ticks_and_labels/relative_ticks/img/02.png)
![Circos tutorial image - Relative
Ticks](/documentation/tutorials/ticks_and_labels/relative_ticks/img/03.png)
![Circos tutorial image - Relative
Ticks](/documentation/tutorials/ticks_and_labels/relative_ticks/img/04.png)
![Circos tutorial image - Relative
Ticks](/documentation/tutorials/ticks_and_labels/relative_ticks/img/05.png)
![Circos tutorial image - Relative
Ticks](/documentation/tutorials/ticks_and_labels/relative_ticks/img/06.png)
![Circos tutorial image - Relative
Ticks](/documentation/tutorials/ticks_and_labels/relative_ticks/img/07.png)
![Circos tutorial image - Relative
Ticks](/documentation/tutorials/ticks_and_labels/relative_ticks/img/08.png)
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
    # use this to see how relative ticks can be drawn relative to
    # the ideograms (use rdivisor=ideogram in the tick blocks)
    #chromosomes                 = hs1[a]:0-75;hs1[b]:100-150;hs1[c]:200-)
    chromosomes = hs1
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
    
    radius*     = 0.75r
    
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
    
    radius         = dims(ideogram,radius_outer)
    multiplier     = 1/1u
    color          = black
    force_display  = yes
    thickness      = 2p
    show_label     = yes
    format         = %d
    
    size           = 20p
    thicknes       = 4p
    label_offset   = 5p
    
    <tick>
    show           = yes
    spacing        = 1u
    rspacing       = 0.02
    # this is the default spacing type
    spacing_type   = absolute
    label_size     = 24p
    </tick>
    
    <tick>
    # when spacing_type is relative, define
    # rspacing to be the increment
    show           = yes
    rspacing       = 0.01
    spacing_type   = relative
    color          = red
    label_size     = 30p
    offset         = 85p
    label_relative = yes
    rmultiplier    = 100
    suffix         = %
    # This will make ticks spaced relatively by ideogram,
    # and not chromosome. This setting is useful when
    # the chromosome is displayed as multiple ideograms
    # rdivisor        = ideogram
    </tick>
    
    <tick>
    show           = yes
    rspacing       = 0.1
    spacing_type   = relative
    thickness      = 3p
    color          = blue
    label_size     = 36p
    offset         = 215p
    label_relative = yes
    rmultiplier    = 10
    suffix         = /10
    #rdivisor       = ideogram
    </tick>
    
    </ticks>
```
  

* * *
