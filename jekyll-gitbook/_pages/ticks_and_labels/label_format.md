---
author: DoubleCat
date: 2025-04-11
layout: post
category: ticks_and_labels
title: Label Formats
---

## Label Formats
### lesson
In previous tutorials, tick marks have been formatted by a combination of the
multiplier and format parameters. The multiplier served to derive a value for
the tick label (value = position * multiplier) and the format string
controlled how the value was shown.

For example, if multiplier = 1/1u (it can be expressed in units of
chromosomes_units; e.g., 1/1u = 1e-6 if chromosomes_units = 1000000) and
format %d, then the tick mark at 10,000,000 will be labeled 10. If format is
%.2f, then the label will be 10.00.

#### multiplier
The multiplier is useful to avoid the presence of large number of non-
significant zeroes in the labels. You can change the format for each <tick>
block. For example, with a multiplier of 1/1u, the ticks spaced every 1 Mb
should have a format of %d, whereas ticks spaced every 0.1 Mb should receive a
format of %.1f. Note that there is no relation between the "multiplier" and
"chromosomes_unit" parameters.

```    
    <ticks>
    multiplier   = 1/1u
    ...
    
    <tick>
     format = %d
     ...
    </tick>
    
    <tick>
     format = %.1f
     ...
    </tick>
    ...
    </ticks>
```
You can adjust the multipler for each tick level. For example, the second tick
level in the configuration below uses a 1000/1u multiplier instead of 1/1u.
This would result in a label "100000" (or "100,000" if thousands_sep=yes)
instead of "100".

```    
    <ticks>
    multiplier   = 1/1u
    ...
    
    <tick>
     ...
    </tick>
    
    <tick>
     multiplier    = 1000/1u
     thousands_sep = yes
     ...
    </tick>
    ...
    </ticks>
```
#### modulo ticks
If defined, the value of "mod" is used to adjust the label by performing
modulo arithmetic on the tick mark value based on the formula.

```    
    given
    
      mod = M
    
    then
    
      tick_label = mod(tick_value,M) * multiplier
```
The "mod" parameter is expected to be defined locally within each <tick>
block. Its purpose is to further reduce the complexity of the tick labels for
finer ticks. For example, if you have ticks every 1u and every 0.1u (e.g., u =
1,000,000) and set

```    
    multiplier = 1/1u
    
    <tick>
    spacing = 0.1u
    mod = 1u
    </tick>
``````
Then the label at tick mark 10,100,000 would be

```    
    mod(10,100,000 , 1,000,000) * 1e-6 = 100,000 * 1e-6 = 0.1
```
rather than 10.1. If you redefine the multiplier for this tick block to 10/1u,
then your ticks would progress as follows

```    
    0 1 2 ... 8 9 10 1 2 ... 8 9 20 1 2 ... 8 9 30 1 2 ...
```
#### note on units of tick spacing
You should always define your tick mark parameters in units of "u" (the value
of the chromosomes_units parameter). Doing so will give the context of your
configuration file the same length scale as your ideograms (e.g. mammalian
genome images might use 1u=1000000 whereas smaller genomes might use 1u=1000).

#### prefix and suffix
You can additionally alter the tick mark label with a suffix and prefix by
defining a "suffix" and "prefix" parameters.

```    
    ...
    <tick>
    suffix = kb
    prefix = +
    ...
    </tick>
```
You can also add a prefix or suffix by adjusting the format of the tick.

```    
    <tick>
    format = position %.1f kb
    ...
    </tick>
```````````````````````````### images
![Circos tutorial image - Label
Formats](/documentation/tutorials/ticks_and_labels/label_format/img/01.png)
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
    show_label* = no
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
    
    radius       = dims(ideogram,radius_outer)
    multiplier   = 1/1u
    label_offset = 0.4r
    thickness    = 4p
    size         = 20p
    show_label   = yes
    
    <tick>
    spacing        = 0.25u
    color          = red
    label_size     = 16p
    label_color    = red
    format         = %df
    mod            = 1u
    suffix         = kb
    multiplier     = 1000/1u
    prefix         = +
    </tick>
    
    <tick>
    spacing        = 1u
    color          = green
    label_color    = green
    label_size     = 18p
    label_offset   = 30p
    format         = %.1f
    mod            = 5u
    suffix         = " Mb"
    prefix         = +
    </tick>
    
    <tick>
    spacing       = 5u
    color         = blue
    label_color   = blue
    label_size    = 20p
    label_offset  = 30p
    format        = %d
    mod           = 100u
    suffix        = Mb
    </tick>
    
    <tick>
    spacing        = 20u
    label_size     = 24p
    format         = %d
    suffix         = " Mb"
    label_offset   = 30p
    </tick>
    
    </ticks>
```
  

* * *
