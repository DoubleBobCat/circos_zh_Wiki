---
author: DoubleCat
date: 2025-04-11
layout: post
category: scaling
title: Global Scale Adjustment
---

## Global Scale Adjustment
### lesson
This series of tutorials focuses on adjusting ideogram scale, both globally
and locally. By scale I mean the quantity

```    
    scale = size/degree
```
which defines the magnification factor of each ideogram on the image.

By default, if you draw all (or some) of the ideograms using

```    
    chromosomes_display_default = yes
```
all ideograms will have the same magnification. This means that the angles
they subtend are proportional to the length of the ideogram. Unless you change
the scale locally, this proportionality factor is constant across the entire
image.

The first image in this example shows the entire human genome—about 3Gb— fit
in 360 degrees. This gives a scale of about 8 Mb/degree. The circumference of
the ideogram circle for an 800 x 800 pixel image (the resolution of the images
in this example) is about 2000 pixels. When expressed in terms of pixels, the
scale is 1.5 Mb/pixel at the radius of the ideograms.

The output resolution of a figure (screen or print) limits how finely you
should sample your data. Please read my [Limits of Human Visual Acuity and
Consequences on Sequence
Visualization](https://mk.bcgsc.ca/vizbi/2012/resolution/resolution.pdf</p>)
for useful guidelines.

#### increasing image size
The simplest way to make _everything_ larger is to increase the size of the
output image. The best way to do this is to override the `radius` parameter in
the <image> block.

```    
    <image>
    <<include etc/image.conf>>
    radius* = 3000p
    </image>
```
The default value is `radius = 1500p`, which creates images 3,000 x 3,000
pixels in size. This is generally sufficient (>300 dpi) for images printed at
10 inches or less.

#### global scale control
Within an image you can adjust the magnification factor of individual
ideograms, or groups of ideograms. This is useful to do because genomes tend
to be interesting in spots.

You can adjust the length scale for each ideogram using the
`chromosomes_scale` parameter. The parameter associates a magnification with
each ideogram. For example,

```    
    chromosomes_scale = hs1:0.2;hs2:0.2;hs3:0.2;hs8:5;hs9:5;hs10:5
```
would result in chromosomes 1, 2, and 3 drawn at 0.2x their size and
chromosomes 8, 9, and 10 drawn at 5x. All other ideograms are scaled
appropriately so that all elements fit within the circle.

#### adjusting scale for multiple ideograms
You can individually enumerate the ideograms for which scale should be
adjusted, as shown above, or use a regular expression to select more than one
ideogram.

For example, to shrink all ideograms matching the regular expression `/rn/`,

```    
    chromosomes_scale = /rn/:0.5
```
You can combine regular expressions with lists. This will apply a scale of 2x
to `rn5`, with all other `rn` ideograms shown at 0.5x.

```    
    chromosomes_scale = /rn/:0.5;rn5:2
```
#### scale-driven display of ticks and tick labels
By defining the `tick_separation` and `label_separation` parameters in the
<ticks> block, you can supress the display of ticks and their labels in areas
where they appear densely. This is useful to help avoid micro-managing tick
and label over-crowding.

Another parameter that helps manage tick labels is
`min_label_distance_to_edge`, which controls the display of labels which are
too close to the edge of an ideogram. This parameter is useful if ideograms
are closely spaced and their edge tick labels start to overlap. You can also
use this parameter to effectively hide the first tick label (typically 0).

```    
    <ticks>
    tick_separation = 3p
    label_separation = 10p
    min_label_distance_to_edge = 10p
    ...
    </ticks>
```
#### toggling ticks by ideogram
When changing the scale of ideograms, you may need to toggle the display of
ticks for specific ideograms to keep the image clean. One use case is to show
ticks only for the first ideogram, to establish the scale for the image, and
then only for subsequent ideograms for which scale changes.

To hide ticks for specific ideograms (e.g. chr9), use `chromosomes` parameter
in the <tick> block

```    
    <tick>
    chromosomes = -hs9
    spacing     = 0.5u
    ...
    </tick>
```
To display ticks on specific ideograms (e.g. chr9),

```    
    <tick>
    chromosomes_display_default = no
    chromosomes = hs9
    spacing     = 0.5u
    ...
    </tick>
```### images
![Circos tutorial image - Global Scale
Adjustment](/documentation/tutorials/scaling/global_scale/img/01.png) ![Circos
tutorial image - Global Scale
Adjustment](/documentation/tutorials/scaling/global_scale/img/02.png) ![Circos
tutorial image - Global Scale
Adjustment](/documentation/tutorials/scaling/global_scale/img/03.png)
### configuration
#### circos.conf
```    
    <<include etc/colors_fonts_patterns.conf>>
    
    <<include ideogram.conf>>
    <<include ticks.conf>>
    
    karyotype = data/karyotype/karyotype.human.txt
    
    <image>
    <<include etc/image.conf>>
    </image>
    
    chromosomes_units           = 1000000
    chromosomes_display_default = yes
    
    chromosomes_scale = hs1:0.2;hs2:0.2;hs3:0.2;hs8:5;hs9:5;hs10:5
    
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
    default = 0.005r
    break   = 0.5r
    
    <<include breaks.conf>>
    
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
    label_size       = 36
    label_parallel   = yes
    label_case       = lower
    label_format     = eval(sprintf("chr%s",var(label)))
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
    label_separation = 10p
    radius           = dims(ideogram,radius_outer)
    multiplier       = 1e-6
    color            = black
    thickness        = 2p
    label_offset     = 5p
    format           = %d
    
    <tick>
    #chromosomes_display_default = no
    chromosomes    = -hs9
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
    spacing        = 100u
    show_label     = yes
    label_size     = 24p
    size           = 22p
    </tick>
    
    </ticks>
```
  

* * *
