---
author: DoubleCat
date: 2025-04-11
layout: post
category: 2d_tracks
title: Text—Rules
---

## Text—Rules
### lesson
This tutorial shows you how to use rules with the text track. All tracks allow
for rules and using rules works the same way for each track. The [previous
tutorial](/documentation/tutorials/2d_tracks/text_2) used rules to color text.

We'll draw some sequence on the image and color the base pairs. We'll use a
monospaced font using

```    
    label_font = mono
```
There are two data files used in this example, `data/6/sequence.txt` (20,000
entries)

```    
    # sequence.txt
    ...
    hs1 2 2 C
    hs1 3 3 A
    hs1 4 4 A
    ...
```
and `data/6/sequence.long.txt` (100,000 entries).

```    
    # sequence.long.txt
    ...
    hs1 1 1 A
    hs1 1 1 C
    hs1 1 1 A
    hs1 1 1 G
    hs1 2 2 T
    hs1 2 2 A
    hs1 2 2 C
    hs1 2 2 T
    ...
```
The ideogram in the image is `hs1:0-20kb`, but it's a good idea to start with
a smaller interval to see how things work, e.g. `hs1:0-1`. A track with
100,000 bases can take a very long time to draw—the code that determines the
character layout has not been optimized.

#### applying text rules
A good way to include rules is using the <<include ... >> directive to read
them from another file. This keeps the configuration file tidy and allows you
to reuse the same rules for other tracks.

```    
    <plots>
    
    # default values for all <plot> blocks
    type       = text
    color      = black
    label_font = mono
    label_size = 32
    # radial padding
    rpadding   = 0.2r
    
    <plot>
    
    file       = data/6/sequence.txt
    r1         = 0.9r
    r0         = 0.3r
    label_size = 16
    # angular padding
    padding    = -0.25r 
    
    <rules>
    <<include rule.textcolor.conf>>
    </rules>
    
    </plot>
    
    </plots>
``````
The `rule.textcolor.conf` file is

```    
    <rule>
    condition = var(value) eq "A"
    color     = red
    </rule>
    <rule>
    
    condition = var(value) eq "T"
    color     = blue
    </rule>
    <rule>
    
    condition = var(value) eq "C"
    color     = green
    </rule>
```
The text label is referenced using `var(value)` and the conditions check
whether the text is `A`, `T` or `C`. The default track coloring assumes the
label is `G`, so we don't have to check for this condition.

#### adjusting text size
With rules, you can adjust any attribute of the text characters. For example,
you can adjust the size of the letters in the label by setting `label_size`.
This is done in the tracks immediately inside and outside the circle.

```    
    <rule>
    # If the text is not A, then hide it. When this rule triggers,
    # other rules are not evaluated.
    condition  = var(value) ne "A"
    show       = no
    </rule>
    
    # This rule is applied to any text that didn't pass the previous
    # rule (i.e. only A). The label is set to a random value between
    # 12 and 48. The rand() function returns a uniformly sampled
    # random value in the interval [0,1).
    
    <rule>
    condition  = 1
    label_size = eval(12+32*rand())
    </rule>
```### images
![Circos tutorial image -
Text—Rules](/documentation/tutorials/2d_tracks/text_3/img/01.png) ![Circos
tutorial image -
Text—Rules](/documentation/tutorials/2d_tracks/text_3/img/02.png) ![Circos
tutorial image -
Text—Rules](/documentation/tutorials/2d_tracks/text_3/img/03.png) ![Circos
tutorial image -
Text—Rules](/documentation/tutorials/2d_tracks/text_3/img/04.png) ![Circos
tutorial image -
Text—Rules](/documentation/tutorials/2d_tracks/text_3/img/05.png) ![Circos
tutorial image -
Text—Rules](/documentation/tutorials/2d_tracks/text_3/img/06.png)
### configuration
#### circos.conf
```    
    <<include colors_fonts_patterns.conf>>
    
    <<include ideogram.conf>>
    <<include ticks.conf>>
    
    karyotype = data/karyotype/karyotype.human.txt
    
    <image>
    <<include etc/image.conf>>
    </image>
    
    chromosomes_units = 1000
    chromosomes       = hs1:0-1
    chromosomes_display_default = no
    
    <plots>
    
    type       = text
    color      = black
    label_font = mono
    label_size = 32
    show_links = no
    rpadding   = 0.2r
    
    <plot>
    file       = data/6/sequence.txt
    r1         = 0.9r
    r0         = 0.3r
    label_size = 16
    padding    = -0.25r
    
    <rules>
    <<include rule.textcolor.conf>>
    </rules>
    
    </plot>
    
    <plot>
    file       = data/6/sequence.txt
    r1         = 0.9r
    r0         = 0.4r
    rpadding   = 0.25r
    
    <rules>
    <<include rule.textcolor.conf>>
    </rules>
    
    </plot>
    
    <plot>
    file       = data/6/sequence.long.txt
    r1         = 0.9r
    r0         = 0.7r
    
    label_rotate = no
    
    <rules>
    <<include rule.textcolor.conf>>
    </rules>
    
    </plot>
    
    <plot>
    file  = data/6/sequence.txt
    r0    = 1r+80p
    r1    = 1r+250p
    
    label_parallel = yes
    
    <rules>
    
    <rule>
    condition  = var(value) ne "A"
    show       = no
    </rule>
    
    <rule>
    condition  = 1
    label_size = eval(12+32*rand())
    </rule>
    
    </rules>
    
    </plot>
    
    </plots>
    
    <<include etc/housekeeping.conf>>
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
    
    radius*       = 0.825r
    
    </ideogram>
``````
  

* * *

#### ideogram.label.conf
```    
    show_label       = yes
    label_font       = default
    label_radius     = dims(image,radius)-30p
    label_size       = 24
    label_parallel   = yes
    label_case       = lower
    label_format     = eval(sprintf("chr%s",var(label)))
``````
  

* * *

#### ideogram.position.conf
```    
    radius           = 0.775r
    thickness        = 30p
    fill             = yes
    fill_color       = black
    stroke_thickness = 2
    stroke_color     = black
```
  

* * *

#### rule.textcolor.conf
```    
    <rule>
    condition = var(value) eq "A"
    color     = red
    </rule>
    <rule>
    condition = var(value) eq "T"
    color     = blue
    </rule>
    <rule>
    condition = var(value) eq "C"
    color     = green
    </rule>
```
  

* * *

#### ticks.conf
```    
    show_ticks       = yes
    show_tick_labels = yes
    show_grid        = no
    grid_start       = dims(ideogram,radius_inner)-0.5r
    grid_end         = dims(ideogram,radius_inner)
    
    <ticks>
    radius           = dims(ideogram,radius_outer)
    label_offset     = 5p
    label_size       = 20p
    multiplier       = 1
    color            = black
    format           = %d
    size             = 10p
    thickness        = 2p
    
    <tick>
    spacing        = 0.002u
    show_label     = no
    </tick>
    <tick>
    spacing        = .02u
    show_label     = yes
    </tick>
    <tick>
    spacing        = .1u
    show_label     = yes
    label_size     = 24p
    </tick>
    
    </ticks>
```
  

* * *
