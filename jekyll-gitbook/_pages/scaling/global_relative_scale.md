---
author: DoubleCat
date: 2025-04-11
layout: post
category: scaling
title: Global Relative Scale Adjustment
---

### lesson
In the previous tutorial, I showed how to adjust the magnification of
ideograms. There, you learned how to make an ideogram twice as large (or twice
as small), as others.

However, sometimes it is useful to change the size of an ideogram in an image
so that it fills a given fraction of the image. The first example image shows
the full human and mouse genome, and the second image limits the display to
human chromosomes 1, 2, 3 and mouse chromosomes 14-19. In this image human
chromosome occupies about 20% of the image.

#### scaling ideograms relative to image
Now suppose you want to change the scale of human chromosome so that it fills
exactly a quarter of the image (25%). You could compute the required
magnification by requiring that

```    
    scale(hs1) * size(hs1) / size(all displayed ideograms) = 0.25
```
But there is a simpler way,

```    
    chromosomes_scale = hs1:0.25r
```
By using the `r` suffix on scale, you indicate that the scale is relative to
the circumference of the ideogram circle.

#### scaling multiple ideograms individually relative to image
By using a regular expression you can adjust the scale of multiple ideograms.
When this is combined with relative scale, you can make each ideogram have the
same size on the image, regardless of its physical size.

For example, this will make each of the 6 mouse chromosomes on the image each
occupy 10% of the image.

```    
    chromosomes_scale = /mm/:0.1r
```
You can mix relative and absolute scales, but be careful that your relative
scales don't add up to more than 1.0. For example,

```    
    chromosomes_scale = hs1:0.75r;hs2:0.75r
```
will have a strange effect because you've asked that two ideograms each occupy
3/4 of the image. Circos doesn't check the sanity of your scale expressions.

#### scaling multiple ideograms as a group relative to image
Now suppose you wanted all the mouse chromosomes to occupy 50% of the image,
as a group. You could to this by calculating the required relative scale for
each (e.g. 0.5/6 = 0.0833)

```    
    chromosomes_scale           = /mm/:0.0833r
```
But there's a better way. By using the `n` suffix, you indicate that the
fraction of the image should be divided evenly by the number of ideograms that
match the regular expression. Thus,

```    
    chromosomes_scale           = /mm/:0.5rn
```
scales all ideograms matching `/mm/` to occupy, as a group, 50% of the image.

Note that in this method each ideogram has the same size in the image.

#### application to multiple genomes
Consider the image in which three genomes are shown (human, mouse, rat). The
following limits the rat and mouse chromosomes to 1/4 of the image, regardless
how many ideograms from these genomes are shown.

```    
    chromosomes_color = /hs/:green;/mm/:red;/rn/:blue
    chromosomes_scale = /mm/:0.25rn;/rn/:0.25rn
```
Note that in this method each rat and mouse ideogram has the same size in the
image.

The calculation behind these settings is iterative and sometimes has a hard
time correctly adjusting for ideogram spacing. You may need to adjust the
fractions to accomodate this inaccuracy. It's a shortcoming of the code.
### images
![Circos tutorial image - Global Relative Scale
Adjustment](/documentation/tutorials/scaling/global_relative_scale/img/01.png)
![Circos tutorial image - Global Relative Scale
Adjustment](/documentation/tutorials/scaling/global_relative_scale/img/02.png)
![Circos tutorial image - Global Relative Scale
Adjustment](/documentation/tutorials/scaling/global_relative_scale/img/03.png)
![Circos tutorial image - Global Relative Scale
Adjustment](/documentation/tutorials/scaling/global_relative_scale/img/04.png)
![Circos tutorial image - Global Relative Scale
Adjustment](/documentation/tutorials/scaling/global_relative_scale/img/05.png)
![Circos tutorial image - Global Relative Scale
Adjustment](/documentation/tutorials/scaling/global_relative_scale/img/06.png)
### configuration
#### circos.conf
```    
    <<include etc/colors_fonts_patterns.conf>>
    
    <<include ideogram.conf>>
    <<include ticks.conf>>
    
    karyotype = data/karyotype/karyotype.human.txt,data/karyotype/karyotype.mouse.txt,data/karyotype/karyotype.rat.txt
    
    <image>
    <<include etc/image.conf>>
    </image>
    
    chromosomes_units           = 1000000
    
    chromosomes_display_default = no
    chromosomes                 = hs1;hs2;hs3;/mm1[4-9]/
    #chromosomes_scale          = /hs/:0.25r
    #chromosomes_scale          = /mm/:0.0833r # if 6 mouse ideograms are drawn, these two
    chromosomes_scale           = /mm/:0.5rn   # are equivalent
    
    #chromosomes_display_default = yes
    #chromosomes_scale           = /hs/:0.25r
    #chromosomes_scale           = /mm/:0.0833r # if 6 mouse ideograms are drawn, these two
    #chromosomes_scale           = /mm/:0.5rn   # are equivalent
    #chromosomes_color           = /hs/:green;/mm/:red;/rn/:blue
    #chromosomes_scale           = /mm/:0.175rn;/rn/:0.2rn
    
    <<include etc/housekeeping.conf>>
```
  

* * *

#### bands.conf
```    
    show_bands            = no
    fill_bands            = yes
    band_stroke_thickness = 2
    band_stroke_color     = white
    band_transparency     = 3
```
  

* * *

#### breaks.conf
```    
    axis_break_at_edge = yes
    axis_break         = yes
    axis_break_style   = 2
    
    <break_style 1>
    stroke_color     = black
    fill_color       = blue
    thickness        = 0.25r
    stroke_thickness = 2
    </break_style>
    
    <break_style 2>
    stroke_color     = black
    stroke_thickness = 2
    thickness        = 2r
    </break_style>
``````
  

* * *

#### ideogram.conf
```    
    <ideogram>
    
    <spacing>
    default = 0.0025r
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
    label_radius     = dims(image,radius) - 50p
    label_size       = 18
    label_parallel   = yes
    label_case       = lower
    label_format     = eval(var(chr))
``````
  

* * *

#### ideogram.position.conf
```    
    radius           = 0.90r
    thickness        = 50p
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
    tick_separation  = 3p
    label_separation = 5p
    radius           = dims(ideogram,radius_outer)
    multiplier       = 1e-6
    color            = black
    thickness        = 2p
    label_offset     = 5p
    format           = %d
    
    <tick>
    spacing        = 0.5u
    show_label     = no
    size           = 6p
    </tick>
    
    <tick>
    spacing        = 1u
    show_label     = yes
    label_size     = 16p
    size           = 10p
    </tick>
    
    <tick>
    spacing        = 5u
    show_label     = yes
    label_size     = 18p
    size           = 14p
    </tick>
    
    <tick>
    spacing        = 10u
    show_label     = yes
    label_size     = 20p
    size           = 18p
    </tick>
    
    <tick>
    spacing        = 20u
    show_label     = yes
    label_size     = 24p
    size           = 22p
    </tick>
    
    <tick>
    spacing        = 50u
    show_label     = yes
    label_size     = 24p
    size           = 22p
    </tick>
    
    </ticks>
```
  

* * *
