---
author: DoubleCat
date: 2025-04-11
layout: post
category: ideograms
title: Cropping
---

### lesson
If you do not wish to have the entire ideogram drawn, you can choose to create
an axis break and remove a region from the display. This can be achieved in
two ways: specify what to draw, or specify what not to draw.

You should never use the [karyotype
file](https://mk.bcgsc.ca/circos/tutorials/lessons/ideograms/karyotypes) to
crop the ideograms. In other words, in the karyotype file the chromosome
start/end positions should reflect the physical chromosome size, not the
regions you wish to draw.

#### specifying chromosome ranges
To specify what regions of an ideogram to draw, use the following syntax

```    
    chromosomes = ...;ID:START-END;...
```
For example,

```    
    chromosomes_units = 1000000
    chromosomes       = hs1:0-100;hs2:50-150;hs3:50-100;hs4;hs5;hs6;hs7;hs8
```
Will draw all 8 chromosomes, but only 0-100 Mb of hs1, 50-150Mb of hs2 and
50-100 Mb of hs3. The start and end ranges are given in units of
chromosomes_units.

#### chromosomes_units
This parameter defines a multiplier which can be applied to many other
variable values within the configuration files. Some values have this
multiplier automatically applied (e.g. the display ranges in the chromosomes
parameter, like shown above). Other values require the use of the "u" suffix.
For example,

```    
    spacing = 5u
``````
In this case, this tick's spacing is 5u. If chromosomes_units=1000000, then
the tick spacing is 5Mb.

The chromosome units value can be defined in absolute terms, such as 1000000
(1Mb), or in relative terms, such as 0.005r. The relative definition is
calculated relative to the total size of all ideograms in the image. For
example, you show the entire human genome (3Gb) in the image, and use
chromosome_units=0.001r, then this is equivalent to a chromosome_units value
of 3Mb (0.001 * 3Gb).

The reason why the relative value is useful is to maintain relatively constant
(and sane!) spacing between elements that use the chromosomes_unit value (such
as ticks) when the number and size of ideograms changes in the image.

Let's look at a quick example. Suppose that you show the entire human genome
and you set chromosomes_units=0.001r. The unit multiplier is 0.001=1/1000 and
you are effectively dividing the image into 1000 slices (every 1Mb). If your
major ticks are spaced every 10u, then you will have a major tick every 10Mb
and there will be about 300 major ticks around your image. Now consider what
happens when you change the ideogram set to display, and let's say that you're
now showing only one ideogram whose size is 100Mb. If chromosomes_unit was
constant (1Mb) , then the tick mark spacing would still be 10Mb and you would
only have 10 major ticks. This may be too coarse a scale. However, if your
chromosomes_units value is relative (e.g. 0.001r), then your major tick marks
will be spaced every 10u = 10*(100*0.001) = 1Mb and you will have 100 major
ticks. Thus, even though you radically changed the extent of the data domain,
spacing of elements in the image relative to the image dimensions is
maintained.

#### axis breaks
Axis breaks are defined in the <ideogram> block and will be covered in another
tutorial section. For now, take a look at the ideogram.conf file associated
with this section for a preview of how breaks are defined.

#### supressing ranges
Instead of specifying what to draw, you can supress a range by using
chromosomes_breaks

```    
    chromosomes = hs1;hs2;hs3;hs4;hs5;hs6;hs7;hs8
    chromosomes_breaks = -hs1:100-200;-hs2:0-50;-hs2:150-);-hs3:0-50
```
Each of the entries in chromosomes_breaks must be preceeded by a "-" and
specifies a range to exclude from the final image. You can specify multiple
ranges for a chromosome. Use ")" to indicate the end of the chromosome (e.g.,
-hs2:150-) supresses drawing from 150 Mb to the end of the chromosome).

#### combining region declarations
You can combine region declarations in "chromosomes" and "chromosomes_breaks"
fields. For example,

```    
    chromosomes = hs1:0-100;hs2:0-100;hs3:0-100;hs4:0-100;hs5;hs6;hs7;hs8
    chromosomes_breaks = -hs1:25-75;-hs2:25-75;-hs3:25-75;-hs4:25-75;-hs5:75-);-hs6:75-);-hs7:75-);-hs8:75-)
```### images
![Circos tutorial image -
Cropping](/documentation/tutorials/ideograms/cropping/img/01.png)
### configuration
#### circos.conf
```    
    <<include etc/colors_fonts_patterns.conf>>
    
    <<include ideogram.conf>>
    <<include ticks.conf>>
    
    <image>
    <<include etc/image.conf>>
    </image>
    
    karyotype   = data/karyotype/karyotype.human.txt
    chromosomes_units           = 1000000
    chromosomes_display_default = no
    
    # to explicitly define what is drawn
    #chromosomes                  = hs1:0-100;hs2:50-150;hs3:50-100;hs4;hs5;hs6;hs7;hs8
    
    # use chromosomes_breaks to indicate which regions you want to supress
    #chromosomes        = hs1;hs2;hs3;hs4;hs5;hs6;hs7;hs8
    #chromosomes_breaks = -hs1:100-200;-hs2:0-50;-hs2:150-);-hs3:0-50
    
    # combine region declarations and breaks
    chromosomes = hs1:0-100;hs2:0-100;hs3:0-100;hs4:0-100;hs5;hs6;hs7;hs8
    chromosomes_breaks = -hs1:25-75;-hs2:25-75;-hs3:25-75;-hs4:25-75;-hs5:75-);-hs6:0-10,75-);-hs7:75-);-hs8:75-)
    
    <<include etc/housekeeping.conf>>
```
  

* * *

#### bands.conf
```    
    show_bands            = yes
    fill_bands            = yes
    band_stroke_thickness = 2
    band_stroke_color     = white
    band_transparency     = 4
```
  

* * *

#### ideogram.conf
```    
    <ideogram>
    
    <spacing>
    
    default = 0.005r
    break   = 0.5r
    
    axis_break_at_edge = yes
    axis_break         = yes
    axis_break_style   = 2
    
    <break_style 1>
    stroke_color     = black
    fill_color       = blue
    thickness        = 0.25r
    stroke_thickness = 2p
    </break>
    
    <break_style 2>
    stroke_color     = black
    stroke_thickness = 5p
    thickness        = 2r
    </break>
    
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
    label_font       = bold
    # labels outside circle
    #label_radius     = dims(ideogram,radius) + 0.05r
    #labels inside circle
    label_radius     = dims(ideogram,radius) - 0.15r
    label_with_tag   = yes
    label_size       = 48
    label_parallel   = yes
    label_case       = upper
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
    skip_first_label = no
    skip_last_label  = no
    radius           = dims(ideogram,radius_outer)
    tick_separation  = 3p
    label_separation = 1p
    multiplier       = 1e-6
    color            = black
    thickness        = 4p
    size             = 20p
    
    <tick>
    spacing        = 1u
    show_label     = no
    thickness      = 2p
    color          = dgrey
    </tick>
    
    <tick>
    spacing        = 5u
    show_label     = no
    thickness      = 3p
    color          = vdgrey
    </tick>
    
    <tick>
    spacing        = 10u
    show_label     = yes
    label_size     = 20p
    label_offset   = 10p
    format         = %d
    grid           = yes
    grid_color     = dgrey
    grid_thickness = 1p
    grid_start     = 0.5r
    grid_end       = 0.999r
    </tick>
    
    </ticks>
```
  

* * *
