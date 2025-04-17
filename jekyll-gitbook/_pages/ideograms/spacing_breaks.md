---
author: DoubleCat
date: 2025-04-11
layout: post
category: ideograms
title: Spacing and Axis Breaks
---

### lesson
#### ideogram spacing
Spacing between ideograms derived from different chromosomes is controlled by
the `default` parameter in <ideogram><spacing> block.

##### absolute spacing
This parameter may be set relative to chromosome units (suffixed with `u`).
For example, if `chromosomes_units=1000000` and the spacing value is `10u`,
then the actual spacing in the image will be 10Mb.

```    
    <ideogram>
     <spacing>
      default = 10u
     </spacing>
    </ideogram>
```
##### relative spacing
You can also set the parameter to be relative to the total size of ideograms
in the image (suffix with `r`). This is useful if you would like to maintain a
fixed spacing between ideograms as you add/remove ideograms from the image.

```    
    <ideogram>
     <spacing>
      default = 0.01r
     </spacing>
    </ideogram>
```
In this example, the spacing will be 1% of the size of all ideograms. This
will be close to 1% of the circumference of the image.

Use the absolute value format (e.g. `10u`), when you have created your
ideogram layout and want to adjust the spacing value to be visually compatible
with adjacent tick marks. For example, if you have major ticks every 5Mb, you
may want to set the spacing value to this.

Use the relative value format (e.g. `0.01r`), when you anticipate that you
will be adding/removing/cropping ideograms from the image but do not want the
spacing value to fluctuate.

#### changing spacing between specific ideograms
Spacing between specific ideograms can be adjusted in <pairwise> block.

```    
    <ideogram>
     <spacing>
      default = 10u
    
      <pairwise hs1>
       spacing = 5u
      </pairwise>
    
      <pairwise hs3 hs4>
       spacing = 0.25r
      </pairwise>
    
     </spacing>
    </ideogram>
```
When you specify the name of one ideogram, spacing on either side of it will
be affected. The first pairwise block creates `5u` spacing around `hs1`.

When you specify the names of two ideograms, the spacing between them is
affected. If you use relative spacing, it is interpreted to be relative to the
default spacing. Thus, `spacing=0.25r` between `hs3` and `hs4` will be 2.5u
(i.e. 25% of `10u`).

##### making room for a legend
To make room for a track legend, use the <pairwise> block to adjust spacing
between the ideograms at the top of the image and then `angle_offset` to
rotate the image to center the spacing along the vertical line.

```    
    # ideogram.conf
    <ideogram>
     <spacing> 
      # spacing between ideograms is 0.1% of image
      default = 0.001r 
    
      <pairwise hsY hs1>
       # spacing between hsY and hs1 is 50x 0.1% of image
       spacing = 50r 
      </pairwise>
    
     </spacing>
    </ideogram>
    
    # circos.conf
    <image>
     # override angle_offset defined in etc/image.conf 
     angle_offset* = -82
     <<include etc/image.conf>>
    </image>
```
This example assumes that `hsY` and `hs1` are the last and first ideograms in
your image, flanking the 12 o'clock position.

By default, `angle_offset=-90`, which makes ideograms start at 12 o'clock
position. The image is rotated slightly clockwise by reducing this offset.
You'll need to determine this offset yourself—start at `-85` and then vary the
value up/down as required.

#### axis breaks
When only a subregion of a chromosome is drawn, you have the option to place
axis breaks on the ideogram to indicate that the chromosome extent is larger
than shown in the figure.

There are two axis break styles, with style properties defined in
`break_style` blocks. The size of the axis break is controlled by the break
parameter and can be defined in absolute units (`u`) or relative to the
default spacing (`r`).

```    
    <ideogram>
      block(spacing>
    
      default = 10u
      break   = 2u
    
      axis_break         = yes
      axis_break_style   = 2
      axis_break_at_edge = yes
    
      <break_style 1>
        stroke_color = black
        fill_color   = blue
        thickness    = 0.25r
        stroke_thickness = 2
      </break_style>
    
      <break_style 2>
        stroke_color     = black
        stroke_thickness = 3
        thickness        = 1.5r
      </break_style>
    
      </spacing>
    </ideogram>
```
If an ideogram does not begin at its chromosome start or end, you can choose
to place an axis break at the edge with `axis_break_at_edge=yes`.

The thickness parameter defines the radial extent of the break and can be
expressed relative to the thickness of the ideogram (e.g. `0.25r`) or in in
absolute pixel size (e.g. `100p`). Typically, break style 1 should have a
thickness <`1r` and style 2 should have a thickness >`1r`.

The axis break defined by style 1 uses a rectangle to join the ideogram across
the break. Style 2 uses two radial lines to indicate a break. The size of the
break is independent of spacing between two ideograms. Thus, if two
neighbouring ideograms have breaks at neighbouring ends, then the total space
between them is the sum of break sizes and ideogram spacing.
### images
![Circos tutorial image - Spacing and Axis
Breaks](/documentation/tutorials/ideograms/spacing_breaks/img/01.png) ![Circos
tutorial image - Spacing and Axis
Breaks](/documentation/tutorials/ideograms/spacing_breaks/img/02.png) ![Circos
tutorial image - Spacing and Axis
Breaks](/documentation/tutorials/ideograms/spacing_breaks/img/03.png)
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
    
    # explicitly define what is drawn
    chromosomes        = hs1:0-200;hs2;hs3;hs4
    chromosomes_breaks = -hs1:50-150;-hs2:0-50;-hs2:150-);-hs3:0-100;-hs4:50-150
    
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
    
    default = 20u
    break   = 5u
    
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
    
    # control over spacing between individual ideogram
    # pairs (e.g., hs1;hs2) or around a given ideogram
    # (e.g., hs3)
    
    <pairwise hs1,hs2>
    spacing = 0.25r
    </pairwise>
    
    <pairwise hs3>
    spacing = 10u
    </pairwise>
    
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
