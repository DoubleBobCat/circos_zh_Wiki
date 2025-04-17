---
author: DoubleCat
date: 2025-04-11
layout: post
category: 2d_tracks
title: Tiles
---

### lesson
Tile tracks are used to show spans such as genomic regions (genes, exons,
duplications) or coverage elements (clones, sequence reads). Tiles will stack
within their track to avoid overlap. The stacking process is controlled by
several parameters, which are the topic of this example.

The image for this example has 5 different tile tracks. From outside in, these
are: assembly clones (black/red), gene regions (green), copy-number
polymorphism regions (blue), segmental duplications (orange) and conservation
regions (purple). Each track is formatted slightly differently to illustrate
various formatting options.

#### how tiles stack
Tiles are stacked in layers, which are annuli within the tile track. The
parameters that define the tile track position, layers and direction of
stacking are (in the case of the assembly track for this example)

```    
    r1 = 0.98r
    r0 = 0.86r
    
    layers      = 15
    margin      = 0.02u
    orientation = out
    
    thickness   = 15
    padding     = 8
```
This track is placed within the radial extent defined by `[0.86r,0.98r]`
(these are radial values relative to the inner ideogram radius). The `r0/r1`
values define the baseline from which the tiles are stacked.

When `orientation=out`, tiles stack from `r0` out towards `r1`. When
`orientation=in`, tiles stack from `r1` in towards `r0`. When
`orientation=center`, tiles stack from the midpoint between `r0/r1` in an
alternating fashion towards `r0` and `r1`.

Each tile element has a radial width of 15 pixels with 8 pixels of padding
between elements.

Tiles will stack in layers to avoid overlap and each tile is given a margin to
control the distance of neighbouring tiles within the same layer.

The full extent of tile elements is defined by the layers parameter. In this
case, there are 15 layers that are allowed. The value of `layers_overflow`
controls what happens when additional layers are needed to accomodate tiles.
It's important to realize that it is the layers parameter that controls the
radial extent of the track, and not the `r0/r1` values. The radius `r0/r1`
values are used to define the baselines of the track whereas the combination
of `layers/thickness/padding` controls how far in the image the tiles stack.

The illustrations associated with this example explain the tile stacking
process.

#### handling overflow
When tiles cannot fit into the number of layers you have specified using
`layers`, Circos looks to `layers_overflow` to determine how to handle the
overflow tiles.

When `layers_overflow=hide`, overflow tiles are not drawn. Use this setting
for the overflow option with caution, since Circos will not alert you to the
fact that not all of your tiles are drawn.

When `layers_overflow=collapse`, overflow tiles are drawn on the first layer.
The position of the first layer depends on the track orientation.

When `layers_overflow=grow`, new layers are added as required. There is no
limit to how many layers may be added.

To help inform you that overflow actions have been taken, you may set the fill
color of overflow tiles to a specific color using `layers_overflow_color`. If
you set this value to be different than the tiles' default color, overflow
tiles will be obvious.

Several images in this example show how overflow can be handled.

#### applying rules
Rules apply to tiles just like for other data points. For example, you may
format tile color by its size.

```    
    <rules>
    <rule>
    condition  = var(size) > 100kb
    color      = red
    </rule>
    
    <rule>
    condition  = var(size) > 50kb
    color      = orange
    </rule>
    
    <rule>
    condition  = var(size) > 20kb
    color      = yellow
    </rule>
```### images
![Circos tutorial image -
Tiles](/documentation/tutorials/2d_tracks/tiles/img/01.png) ![Circos tutorial
image - Tiles](/documentation/tutorials/2d_tracks/tiles/img/02.png) ![Circos
tutorial image - Tiles](/documentation/tutorials/2d_tracks/tiles/img/03.png)
![Circos tutorial image -
Tiles](/documentation/tutorials/2d_tracks/tiles/img/04.png) ![Circos tutorial
image - Tiles](/documentation/tutorials/2d_tracks/tiles/img/05.png) ![Circos
tutorial image - Tiles](/documentation/tutorials/2d_tracks/tiles/img/06.png)
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
    chromosomes                 = hs9[a]:40-45;hs1[b]:40-45;hs9[c]:65-70;hs1[d]:50-55
    chromosomes_display_default = no
    
    <plots>
    
    type            = tile
    layers_overflow = hide
    
    <plot>
    file        = data/6/assembly.txt
    r1          = 0.98r
    r0          = 0.86r
    orientation = out
    
    layers      = 15
    margin      = 0.02u
    thickness   = 15
    padding     = 8
    
    stroke_thickness = 1
    stroke_color     = grey
    </plot>
    
    <plot>
    file        = data/6/genes.txt
    r1          = 0.84r
    r0          = 0.71r
    orientation = center
    
    layers      = 11
    margin      = 0.02u
    thickness   = 8
    padding     = 4
    
    layers_overflow       = collapse
    layers_overflow_color = red
    
    stroke_thickness = 1
    stroke_color     = dgreen
    color            = green
    
    <backgrounds>
    <background>
    color = vvlgrey
    </background>
    </backgrounds>
    
    </plot>
    
    <plot>
    
    file        = data/6/variation.txt
    r1          = 0.69r
    r0          = 0.5r
    orientation = in
    
    layers      = 15
    margin      = 0.02u
    thickness   = 10
    padding     = 5
    
    stroke_thickness = 1
    stroke_color     = dblue
    color            = blue
    
    </plot>
    
    <plot>
    
    file            = data/6/segdup.txt
    r1              = 0.525r
    r0              = 0.2r
    orientation     = in
    
    layers          = 15
    margin          = 0.02u
    thickness       = 8
    padding         = 5
    
    layers_overflow = hide
    color           = orange
    
    <backgrounds>
    color = vlgrey_a5
    <background>
    y1    = 0.25r
    </background>
    <background>
    y1    = 0.5r
    </background>
    <background>
    y1    = 0.75r
    </background>
    <background>
    y1    = 1r
    </background>
    </backgrounds>
    
    <rules>
    <rule>
    condition = var(size) < 150kb
    color     = eval((qw(lgrey grey dgrey vdgrey black))[remap_round(var(size),10000,150000,0,4)])
    </rule>
    
    </rules>
    
    </plot>
    
    <plot>
    file        = data/6/conservation.txt
    r0          = 0.2r
    r1          = 0.525r
    orientation = out
    
    layers      = 5
    margin      = 0.02u
    thickness   = 8
    padding     = 5
    
    layers_overflow       = grow
    layers_overflow_color = red
    
    color       = lpurple
    
    <rules>
    <rule>
    condition        = ! on(hs1)
    color            = blue
    stroke_thickness = 1
    stroke_color     = dblue
    </rule>
    </rules>
    
    </plot>
    
    </plots>
    
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
    spacing        = .1u
    show_label     = no
    </tick>
    
    <tick>
    spacing        = .5u
    show_label     = yes
    label_size     = 20p
    format         = %d
    </tick>
    
    <tick>
    spacing        = 1u
    show_label     = yes
    label_size     = 24p
    format         = %d
    </tick>
    
    </ticks>
```
  

* * *
