---
author: DoubleCat
date: 2025-04-11
layout: post
category: ideograms
title: Labels
---

### lesson
Each ideogram has a label field in the karyotype file

```    
    #
    # A name of chromosome used in coordinate files
    # B label of chromosome and derived ideograms
    #
    #     A    B
    chr - hs12 12 0 132349534 green
```
This label field defines the text that is shown in the figure. This text is
optional and can be positioned and formatted flexibly.

#### ideograms vs chromosomes
Keep the difference between chromosomes and ideograms in mind. The
_chromosome_ is the structure on which you define position of data. The
_ideogram_ is the visual representation of the chromosome or a region of a
chromosome.

Most of the time, each chromosome will have one ideogram. However, if you use
axis breaks and suppress the display of a region of a chromosome, a chromosome
will have more than one ideogram.

When chromosomes are broken up into multple ideograms, each ideogram is
identified by a tag (e.g. `a b c`). You can have this tag added to the label
using `label_with_tag` as described below.

#### fonts
Circos supports True Type and Open Type fonts. These fonts are defined in the
<font> block. In all of the tutorials this definition is included via the
`colors_fonts_patterns.conf` file, which defines <fonts>, <colors> and
<patterns> blocks.

```    
    # circos.conf
    <<include colors_fonts_patterns.conf>>
    ...
```
The <font> block is used to associate a font file (.TTF or .OTF) with a unique
name, such as "normal", "bold", or "condensed". For example,

```    
    light          = fonts/modern/cmunbmr.otf
    normal         = fonts/modern/cmunbmr.otf
    default        = fonts/modern/cmunbmr.otf
    semibold       = fonts/modern/cmunbsr.otf
    bold           = fonts/modern/cmunbbx.otf
    italic         = fonts/modern/cmunbmo.otf
    bolditalic     = fonts/modern/cmunbxo.otf
    italicbold     = fonts/modern/cmunbxo.otf
```
To use the font, specify it by using its definition (e.g. light), _not_ the
font file name (e.g. `fonts/modern/cmunbmbr.otf`). If you specify a font
definition that has not been defined, `default` is used. It's a good idea to
always have a `default` definition.

#### ideogram labels
Ideogram labels are controlled by these parameters within the <ideogram>
block.

```    
    <ideogram>
    show_label     = yes
    label_with_tag = yes
    label_font     = light
    label_radius   = dims(ideogram,radius_outer) + 0.05r
    label_center   = yes
    label_size     = 48p
    label_color    = grey
    label_parallel = yes
    label_case     = upper 
    label_format   = eval(sprintf("chr%s",var(label)))
    ...
    </ideogram>
```
#### label tags
The `label_with_tag` parameter controls whether a tag associated with the
ideogram region is included with the label. Tags are used to identify
ideograms from the same chromosome

```    
    # tags "a" and "b"
    chromosomes = hs1[a]:50-75,hs1[b]:100-125
```
#### label font
The `label_font` specifies the name of the font (using its label, as defined
in the <fonts> block.

#### label position
The `label_radius` controls the radial position of the ideogram label. Here,
it is best to put the label relative to the ideogram outer (or inner) radius.
If you would like the label to be centered at this radius, use `label_center =
yes`. A few examples are

```    
    # 50 pixels outside the outer ideogram radius
    label_radius = dims(ideogram,radius_outer) + 50p
    
    # 5% of inner radius outside outer ideogram radius
    label_radius = dims(ideogram,radius_outer) + 0.05r
    
    # inside ideogram
    label_radius = (dims(ideogram,radius_outer)+dims(ideogram,radius_inner))/2
    
    # 100 pixels inside the ideogram radius
    label_radius = dims(ideogram,radius_inner) - 100p
    
    # 50 pixels inside the image radius
    label_radius = dims(image,radius) - 50p
```
#### label orientation
You can make the baseline of the ideogram labels to be parallel to the circle
by using the `label_parallel` parameter within the ideogram block.

#### label case
To override the way the label is displayed, you can force upper or lower case
with `label_case`, which can be set to `upper` or `lower`.

```    
    # ideogram labels will be uppercase
    label_case = upper
```
#### label format
You can define the format of the label flexibly by using `sprintf`. Here, the
label of the chromosome (e.g. 1) is prefixed with the string "chr".

```    
    label_format = eval(sprintf("chr%s",var(label)))
```
Here are a few other examples of the use of `label_format`. In all cases
`var()` refers to a property of the ideogram, such as `chr` (e.g. `hs10`) or
`label` (e.g. `10`).

```    
    # show labels only for chromosomes 1-5
    label_format     = eval( var(chr) =~ /hs[1-5]$/ ? var(label) : "")
    
    # hide label for chromosome hs10
    label_format     = eval( var(chr) eq "hs10" ? "" : var(label))
```
In some cases, you may want to simplify the ideogram label. For example, if
all your labels contain the string `ctg.` (e.g. `ctg.123`) and you want to
trim it, use the helper function `replace(str,rx,replace_str)`.

```    
    # replace the string ctg. in the label with empty string (i.e. remove the string)
    label_format     = eval( replace(var(label),"ctg.","") )
    
    # use the chromosome name as the label, but replace "hs" with "human "
    label_format     = eval( replace(var(chr),"hs","human ") )
```
You can use other properties of the ideogram in the label

```    
    # include length in the label (divided by 1,000,000 and suffixed with "Mb")
    label_format     = eval( sprintf("%s %dMb",var(label),var(size)/1e6) )
```
#### help with `var()`
For a full list of parameter names that are available for the `var()`
function, use `var(?)`. When Circos parses this it will return (and quit) a
list of parameters with their values.

```    
    # e.g. using
    label_format     = eval( sprintf("%s %dMb",var(label),**var(?)** /1e6) )
    
    # will return
    You asked for help in the expression [eval( sprintf("%s %dMb",1,var(?)/1e6) )].
    In this expression the arguments marked with * are available for the var() function.
                   break   HASH
                     chr * hs1
            chr_with_tag * 1
               chrlength * 249250622
                  covers   ARRAY
             display_idx * 0
                     end * 249250621
                     idx * 0
                   label * 1
                  length   HASH
                    next   HASH
                   param   HASH
                    prev   HASH
                  radius * 1350
            radius_inner * 1275
           radius_middle * 1312.5
            radius_outer * 1350
                 reverse * 0
                   scale * 1
                     set   Set::IntSpan
                    size * 249250622
                   start * 0
                     tag * hs1
               thickness * 75
```
For now, the parameters listed as `HASH`, `ARRAY`, or an object (e.g.
`Set::IntSpan`) cannot be polled by `var()`.
### images
![Circos tutorial image -
Labels](/documentation/tutorials/ideograms/labels/img/01.png) ![Circos
tutorial image - Labels](/documentation/tutorials/ideograms/labels/img/02.png)
### configuration
#### circos.conf
```    
    <<include etc/colors_fonts_patterns.conf>>
    
    <<include ideogram.conf>>
    <<include ticks.conf>>
    
    show_ticks* = no
    
    <image>
    <<include etc/image.conf>>
    </image>
    
    karyotype = data/karyotype/karyotype.human.txt
    
    chromosomes_units           = 1000000
    chromosomes_display_default = yes
    
    <<include etc/housekeeping.conf>>
```
  

* * *

#### bands.conf
```    
    show_bands            = no
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
    
    default = 10u
    break   = 5u
    
    axis_break_at_edge = yes
    axis_break         = yes
    axis_break_style   = 2
    
    <break_style 1>
    stroke_color = black
    fill_color   = blue
    thickness    = 0.25r
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
    
    # 50 pixels outside the outer ideogram radius
    label_radius = dims(ideogram,radius_outer) + 50p
    
    # 5% of inner radius outside outer ideogram radius
    # label_radius = dims(ideogram,radius_outer) + 0.05r
    
    # inside ideogram
    # label_radius = (dims(ideogram,radius_inner)+dims(ideogram,radius_outer))/2-24
    
    # 100 pixels inside the ideogram radius
    # label_radius = dims(ideogram,radius_inner) - 100p
    
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
