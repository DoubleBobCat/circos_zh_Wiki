---
author: DoubleCat
date: 2025-04-11
layout: post
category: quick_start
title: Ticks & Labels
---

## Ticks & Labels
### lesson
In this tutorial, I will add labels to the ideograms as well as ticks and tick
labels.

To do this, the `<ideogram>` block needs to be expanded to include label
parameters. Tick labels are defined in a different block, `<ticks>`.

#### ideogram labels
Labels for ideograms can be placed at any radial position and formatted
flexibly. The minimum label definition is shown below.

```    
    <ideogram>
    
    <spacing>
    default = 0.005r
    </spacing>
    
    # Ideogram position, fill and outline
    
    radius           = 0.90r
    thickness        = 20p
    fill             = yes
    stroke_color     = dgrey
    stroke_thickness = 2p
    
    # Minimum definition for ideogram labels.
    
    show_label       = yes
    # see etc/fonts.conf for list of font names
    label_font       = default 
    label_radius     = 1r + 75p
    label_size       = 30
    label_parallel   = yes
    
    </ideogram>
``````
The radial position of the labels can be adjusted using `label_radius`.

```    
    # relative to outer ideogram radius 
    label_radius = 1.1r
    label_radius = 0.8r
    # absolute position
    label_radius = 500p
    # relative position with absolute offset
    label_radius = 1r + 100p
    # using image dimensions
    label_radius = dims(image,radius) - 50p
    # using ideogram position
    label_radius = dims(ideogram,radius_outer) + 50p
    label_radius = dims(ideogram,radius_inner) - 50p
``````
In other parts of Circos configuration, positional parameters (e.g.
inner/outer radius of data tracks) support compound expressions that combine
absolute and relative values (e.g. `1r+50p`).

The quantity used as the reference for relative units depends on which
parameter is defined. It is usually defined as the "parent container" of the
element. For example, when definition ideogram position, the reference is
image radius. When using track position, the reference is ideogram radius. As
a result, when the parent element is moved (e.g. ideogram), all other elements
move with it (e.g. data tracks).

#### tick marks and labels
Ticks are defined by group. You can have absolute or relatively spaced ticks,
as well as ticks at specific positions. An [entire tutorial is dedicated to
ticks](//documentation/tutorials/ticks_and_labels). Here, I show a minimum
definition.

```    
    show_ticks          = yes
    show_tick_labels    = yes
    
    <ticks>
    
    radius           = 1r
    color            = black
    thickness        = 2p
    
    # the tick label is derived by multiplying the tick position
    # by 'multiplier' and casting it in 'format':
    #
    # sprintf(format,position*multiplier)
    
    multiplier       = 1e-6
    
    # %d   - integer
    # %f   - float
    # %.1f - float with one decimal
    # %.2f - float with two decimals
    #
    # for other formats, see <https://perldoc.perl.org/functions/sprintf.html>
    
    format           = %d
    
    <tick>
    spacing        = 5u
    size           = 10p
    </tick>
    
    <tick>
    spacing        = 25u
    size           = 15p
    show_label     = yes
    label_size     = 20p
    label_offset   = 10p
    format         = %d
    </tick>
    
    </ticks>
```
The primary parameter in each `<tick>` block is `spacing`. This defines the
distance between adjacent ticks in this group. Typically, this value is
defined in terms of `chromosomes_units` parameter — the suffix `u` is used for
this — to keep the number legible.

If a tick belongs to multiple groups, the group with largest spacing is
prefered. Thus, the tick at 50 Mb will take its formatting from the
`spacing=25u` group, not the `spacing=5u` group.
### images
![Circos tutorial image - Ticks &
Labels](/documentation/tutorials/quick_start/ticks_and_labels/img/01.png)
### configuration
#### circos.conf
```    
    # 1.2 IDEOGRAM LABELS, TICKS, AND MODULARIZING CONFIGURATION
    #
    # In this tutorial, I will add tick marks, tick labels and ideogram
    # labels to the previous image. This will require the use of a <ticks>
    # block and expanding the <ideogram> block. 
    #
    # To make the configuration more modular, the tick and ideogram
    # parameters will be stored in different files and imported using the
    # <<include>> directive.
    
    karyotype = data/karyotype/karyotype.human.txt
    
    # The chromosomes_unit value is used as a unit (suffix "u") to shorten
    # values in other parts of the configuration file. Some parameters,
    # such as ideogram and tick spacing, accept "u" suffixes, so instead of
    #
    # spacing = 10000000
    #
    # you can write
    #
    # spacing = 10u
    #
    # See ticks.conf for examples.
    
    chromosomes_units = 1000000
    
    <<include ideogram.conf>>
    
    <<include ticks.conf>>
    
    <image>
    <<include etc/image.conf>>                
    </image>
    
    <<include etc/colors_fonts_patterns.conf>> 
    
    <<include etc/housekeeping.conf>> 
```
  

* * *

#### ideogram.conf
```    
    <ideogram>
    
    <spacing>
    default = 0.005r
    </spacing>
    
    # Ideogram position, fill and outline
    radius           = 0.90r
    thickness        = 20p
    fill             = yes
    stroke_color     = dgrey
    stroke_thickness = 2p
    
    # Minimum definition for ideogram labels.
    
    show_label       = yes
    # see etc/fonts.conf for list of font names
    label_font       = default 
    label_radius     = dims(image,radius) - 60p
    label_size       = 30
    label_parallel   = yes
    
    </ideogram>
``````
  

* * *

#### ticks.conf
```    
    show_ticks          = yes
    show_tick_labels    = yes
    
    <ticks>
    radius           = 1r
    color            = black
    thickness        = 2p
    
    # the tick label is derived by multiplying the tick position
    # by 'multiplier' and casting it in 'format':
    #
    # sprintf(format,position*multiplier)
    #
    
    multiplier       = 1e-6
    
    # %d   - integer
    # %f   - float
    # %.1f - float with one decimal
    # %.2f - float with two decimals
    #
    # for other formats, see https://perldoc.perl.org/functions/sprintf.html
    
    format           = %d
    
    <tick>
    spacing        = 5u
    size           = 10p
    </tick>
    
    <tick>
    spacing        = 25u
    size           = 15p
    show_label     = yes
    label_size     = 20p
    label_offset   = 10p
    format         = %d
    </tick>
    
    </ticks>
```
  

* * *
