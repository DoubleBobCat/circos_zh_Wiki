---
author: DoubleCat
date: 2025-04-11
layout: post
category: quick_start
title: Ideogram Selection, Scale, Color & Orientation
---

## Ideogram Selection, Scale, Color & Orientation
### lesson
In this section, we will adjust which chromosomes are drawn and change their
scale, color and orientation.

Getting the ideogram layout right is important. For example, making all
chromosomes appear to be the same size can emphasize the comparison between
relative positions in patterns.

#### ideogram selection
The default behaviour is to display all chromosomes defined in the karyotype
file, in order of appearance.

To select a subset of chromosomes, set `chromosomes_display_default=no`

```    
    chromosomes_display_default = no
```
and then use the `chromosomes` parameter to provide either a list

```    
    chromosomes                 = hs1;hs2;hs3;h4
```
or regular expression in

```    
    chromosomes                 = /hs[1-4]$/
```
to specify which chromosomes to show. You can combine these methods

```    
    chromosomes                 = /hs[1-4]$/;hs10;hs11
```
and use `-` prefix to specify that you don't want a chromosome to be drawn

```    
    chromosomes                 = /hs[1-4]$/;-hs3
```
Note that the list uses `;` as the delimiter. The reason why `,` is not used
is because the chromosome entry can include a list of chromosome regions to
draw, such as

```    
    chromosomes                 = hs1:(-100,120-);hs2;hs3;h4
```
The regular expression can match a partial string, so don't forget to include
a trailing `$` anchor if you don't mean to match hs10,hs11,...

#### ideogram scale
The size of the ideogram on the figure can be adjusted using an absolute or
relative magnification.

Absolute scale applies a fixed magnification to an ideogram

```    
    # hs1 0.25x zoom
    # hs2 2.00x zoom
    chromosomes_scale   = hs1=0.25,hs2=2.0
```
Relative scale defines the size of the ideogram relative to image
circumference

```    
    # hs1 25% of figure
    # hs2 50% of figure
    chromosomes_scale   = hs1=0.25r,hs2=0.50r
```
Normalized relative scale distributes several ideograms evenly within a
fraction of the figure.

```    
    # hs1,hs2 distributed evenly within 50% of figure (each is 25%)
    chromosomes_scale   = /hs[12]/=0.5rn
```
A useful idiom is to select all ideograms and distribute them across entire
figure.

```    
    # all ideograms distributed evenly within entire figure
    chromosomes_scale   = /./=1rn
```
#### scale progression
By default, the scale progression is clockwise. You can set the global angle
progression using `angle_orientation` in the `<image>` block

```    
    <image>
    # The * suffix is used to overwrite a parameter. In this case, the 
    # angle_orientation imported from etc/image is assigned a different value.
    angle_orientation* = counterclockwise
    <<include etc/image>>
    </image>
```
To reverse it for one or several ideograms, use `chromosomes-reverse`

```    
    chromosomes_reverse = /hs[234]/
```
In this case the regular expression did not require a trailing `$` because it
applies only to those chromosomes that are displayed. Thus, even though
`/hs[234]/` does match `hs20`, it does not matter because this chromosome is
not shown.

#### ideogram color
The color of each ideogram is taken from the karyotype file. To change it, use
`chromosomes_color`

```    
    chromosomes_color   = hs1=red,hs2=orange,hs3=green,hs4=blue
```
#### ideogram radial position
By default, all ideograms are placed at the same radial position, as defined
by the `radius` parameter in the `<ideogram>` block. You can selectively move
one or more of the ideograms radially by definining a new radial position
using `chromosomes_radius`.

Probably the most convenient way to do this is to use relative coordinates
(`r` suffix), which are interpreted relative to the default ideogram radius.
For example,

```    
    chromosomes_radius  = hs4:0.9r
```
would place chromosome 4 at `0.9x` the radius of all other chromosomes.
### images
![Circos tutorial image - Ideogram Selection, Scale, Color &
Orientation](/documentation/tutorials/quick_start/selection_and_scale/img/01.png)
### configuration
#### circos.conf
```    
    # 1.3 IDEOGRAM SELECTION, SCALE, COLOR AND ORIENTATION
    #
    # This tutorial shows you how to select which chromosomes to draw and
    # flexibly arrange them in the image by applying custom scaling and
    # colors.
    
    karyotype = data/karyotype/karyotype.human.txt
    chromosomes_units = 1000000
    
    # The default behaviour is to display all chromosomes defined in the
    # karyotype file. In this example, I select only a subset.
    #
    # The 'chromosomes' parameter has several uses, and selecting which
    # chromosomes to show is one of them. You can list them
    #
    # hs1;hs2;hs3;hs4
    #
    # or provide a regular expression that selects them based on a successful match
    #
    # /hs[1-4]$/
    #
    # The $ anchor is necessary, otherwise chromosomes like hs10, hs11 and
    # hs20 are also matched.
    
    chromosomes_display_default = no
    chromosomes                 = /hs[1-4]$/
    
    # The size of the ideogram on the figure can be adjusted using an
    # absolute or relative magnification. Absolute scaling,
    #
    # hs1=0.5
    #
    # shrinks or expands the ideogram by a fixed factor. When the "r"
    # suffix is used, the magnification becomes relative to the
    # circumference of the figure. Thus, 
    #
    # hs1=0.5r 
    #
    # makes hs1 to occupy 50% of the figure. To uniformly distribute
    # several ideogram within a fraction of the figure, use a regular
    # expression that selects the ideograms and the "rn" suffix (relative
    # normalized).
    #
    # /hs[234]/=0.5rn
    #
    # Will match hs2, hs3, hs4 and divide them evenly into 50% of the figure. Each ideogram will be about 16% of the figure.
    
    chromosomes_scale   = hs1=0.5r,/hs[234]/=0.5rn
    
    # By default, the scale progression is clockwise. You can set the
    # global angle progression using 'angle_orientation' in the <image>
    # block (clockwise or counterclockwise). To reverse it for one or
    # several ideograms, use 'chromosomes-reverse'
    
    chromosomes_reverse = /hs[234]/
    
    # The color of each ideogram is taken from the karyotype file. To
    # change it, use 'chromosomes_color'.
    
    chromosomes_color   = hs1=red,hs2=orange,hs3=green,hs4=blue
    
    # The default radial position for all ideograms is set by 'radius' in
    # the <ideogram> block (see ideogram.conf). To change the value for
    # specific ideograms, use chromosomes_radius.
    
    chromosomes_radius  = hs4:0.9r
    
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
    label_radius     = 1.075r  # if ideogram radius is constant, and you'd like labels close to image edge, 
                               # use the dims() function to access the size of the image
                               # label_radius  = dims(image,radius) - 60p
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
