---
author: DoubleCat
date: 2025-04-11
layout: post
category: 2d_tracks
title: Glyphs—Part I
---

### lesson
Rules can be used to adjust the text of the label. This is done by setting the
`value` parameter in the rule. The rule below sets all labels to `X`,
regardless of their original text.

```    
    <rule>
    condition  = 1
    value      = X
    </rule>
```
You can combine this with other rules. For example, if the text is sequence,
you can set the color of the character based on its identity and then change
it to another value. The color rules must have `flow=continue` to allow the
downstream label-changing rule to also be evaluated (recall that without this
`flow=continue statement`, triggered rules terminate the rule chain).

```    
    # first change color
    <rule>
    condition  = var(value) eq "A"
    color      = red
    flow       = continue
    </rule>
    
    <rule>
    condition  = var(value) eq "T"
    color      = blue
    flow       = continue
    </rule>
    
    <rule>
    condition  = var(value) eq "C"
    color      = green
    flow       = continue
    </rule>
    
    # change label text, for all data points
    <rule>
    condition  = 1
    value      = X
    </rule>
```
You can turn a text track into a glyph track by changing the font and
adjusting the text label to the desired glyph. For example, using the symbol
font (fonts/symbols/symbols.ttf, defined under the font name `glyph` in
`etc/fonts.conf`), you can obtain square glyphs like so

```    
    <plot>
    label_font = glyph
    
    <rules>
    ...
    <rule>
    condition = 1
    value     = m
    </rule>
    ...
    </rules>
```
The symbols font defines the following characters

```    
     small
     | medium
     | | large
     | | |
     a b c   square
     d e f   rhombus
     g h i   triangle up
     j k l   triangle down
     m n o   circle
    
    upper case - solid
    lower case - hollow
```
By adjusting the padding more tightly, you can pack the square glyphs to
touch. By adjusting the color and glyph shape, you can create attractive
tracks.
### images
![Circos tutorial image - Glyphs—Part
I](/documentation/tutorials/2d_tracks/glyphs_1/img/01.png) ![Circos tutorial
image - Glyphs—Part I](/documentation/tutorials/2d_tracks/glyphs_1/img/02.png)
![Circos tutorial image - Glyphs—Part
I](/documentation/tutorials/2d_tracks/glyphs_1/img/03.png)
### configuration
#### circos.2.conf
```    
    <<include colors_fonts_patterns.conf>>
    
    <<include ideogram.conf>>
    <<include ticks.conf>>
    
    <image>
    <<include etc/image.conf>>
    file* = circos.2.png
    </image>
    
    karyotype = data/karyotype/karyotype.human.txt
    
    chromosomes_units           = 1000
    chromosomes                 = hs1:0-10
    chromosomes_display_default = no
    
    <plots>
    
    <plot>
    
    type       = text
    label_font = glyph
    file       = data/6/sequence.txt
    padding    = -0.1r
    rpadding   = 0p
    r1         = 0.975r
    r0         = 0.975r-250p
    color      = black
    label_size = 36p
    
    <rules>
    
    <rule>
    condition   = var(value) eq "A"
    color       = red
    flow        = continue
    </rule>
    
    <rule>
    condition   = var(value) eq "C" || var(value) eq "T"
    # or use a regular expression
    # condition = var(value) =~ /[CT]/
    color       = white
    flow        = continue
    </rule>
    
    <rule>
    condition   = 1
    # small
    # | medium
    # | | large
    # | | |
    # a b c   square
    # d e f   rhombus
    # g h i   triangle up
    # j k l   triangle down
    # m n o   circle
    value       = n
    </rule>
    
    </rules>
    
    </plot>
    
    </plots>
    
    <<include etc/housekeeping.conf>>
```
  

* * *

#### circos.3.conf
```    
    <<include colors_fonts_patterns.conf>>
    
    <<include ideogram.conf>>
    <<include ticks.conf>>
    
    <image>
    <<include etc/image.conf>>
    file* = circos.3.png
    </image>
    
    karyotype = data/karyotype/karyotype.human.txt
    
    chromosomes_units           = 1000
    chromosomes                 = hs1:0-10
    chromosomes_display_default = no
    
    <plots>
    
    <plot>
    
    type       = text
    label_font = glyph
    file       = data/6/sequence.txt
    padding    = -0.1r
    rpadding   = 0p
    r1         = 0.975r
    r0         = 0.975r-250p
    color      = black
    label_size = 36p
    
    <rules>
    
    # glyph character mappings
    #
    # small
    # | medium
    # | | large
    # | | |
    # a b c   square
    # d e f   rhombus
    # g h i   triangle up
    # j k l   triangle down
    # m n o   circle
    #
    # lower case - hollow
    # upper case - solid
    
    <rule>
    condition   = var(value) eq "A"
    color       = red
    value       = b
    </rule>
    
    <rule>
    condition   = var(value) eq "T"
    color       = red
    value       = B
    </rule>
    
    <rule>
    condition   = var(value) eq "C"
    color       = black
    value       = n
    </rule>
    
    <rule>
    condition   = var(value) eq "G"
    color       = black
    value       = N
    </rule>
    
    </rules>
    
    </plot>
    
    </plots>
    
    <<include etc/housekeeping.conf>>
```
  

* * *

#### circos.conf
```    
    <<include colors_fonts_patterns.conf>>
    
    <<include ideogram.conf>>
    <<include ticks.conf>>
    
    <image>
    <<include etc/image.conf>>
    </image>
    
    karyotype = data/karyotype/karyotype.human.txt
    
    chromosomes_units           = 1000
    chromosomes                 = hs1:0-10
    chromosomes_display_default = no
    
    <plots>
    
    type       = text
    label_font = glyph
    
    <plot>
    file       = data/6/sequence.txt
    padding    = -0.1r
    rpadding   = 0p
    r1         = 0.975r
    r0         = 0.975r-250p
    color      = black
    label_size = 36
    
    <rules>
    
    flow        = continue
    
    <rule>
    condition   = var(value) eq "A"
    color       = red
    </rule>
    
    <rule>
    condition   = var(value) eq "C"
    color       = green
    </rule>
    
    <rule>
    condition   = var(value) eq "T"
    color       = blue
    </rule>
    
    <rule>
    condition   = 1
    value       = b
    </rule>
    
    </rules>
    
    </plot>
    
    </plots>
    
    <<include etc/housekeeping.conf>>
```
  

* * *

#### ideogram.conf
```    
    <ideogram>
    
    <spacing>
    
    default = 0.05u
    
    </spacing>
    
    # thickness (px) of chromosome ideogram
    thickness        = 0p
    stroke_thickness = 2
    # ideogram border color
    stroke_color     = black
    fill             = yes
    # the default chromosome color is set here and any value
    # defined in the karyotype file overrides it
    fill_color       = black
    
    # fractional radius position of chromosome ideogram within image
    radius         = 0.85r
    show_label     = no
    label_font     = condensedbold
    label_radius   = dims(ideogram,radius) + 0.05r
    label_size     = 36
    
    # cytogenetic bands
    band_stroke_thickness = 2
    
    # show_bands determines whether the outline of cytogenetic bands
    # will be seen
    show_bands            = no
    # in order to fill the bands with the color defined in the karyotype
    # file you must set fill_bands
    fill_bands            = no
    
    </ideogram>
``````
  

* * *

#### ticks.conf
```    
    show_ticks          = yes
    show_tick_labels    = yes
    
    show_grid          = no
    grid_start         = dims(ideogram,radius_inner)-0.5r
    grid_end           = dims(ideogram,radius_inner)
    
    <ticks>
    skip_first_label     = no
    skip_last_label      = no
    radius               = dims(ideogram,radius_outer)
    tick_separation      = 2p
    min_label_distance_to_edge = 0p
    label_separation = 5p
    label_offset     = 5p
    label_size       = 24p
    multiplier       = 1e-3
    color            = black
    size = 20p
    format         = %.1f
    thickness = 4p
    
    <tick>
    spacing        = 0.02u
    show_label     = no
    </tick>
    
    <tick>
    spacing        = 0.1u
    show_label     = yes
    </tick>
    
    <tick>
    spacing        = 1u
    show_label     = yes
    </tick>
    
    <tick>
    spacing        = 5u
    show_label     = yes
    label_font     = bold
    </tick>
    </ticks>
```
  

* * *
