---
author: DoubleCat
date: 2025-04-11
layout: post
category: 2d_tracks
title: Text—Stacking
---

## Text—Stacking
### lesson
In the previous example, I had drawn just a few labels. If labels are dense,
they will be automatically stacked to avoid overlap. In other words, if a
label's position results in overlap with another label, the label is drawn at
the same angular position but is radially shifted out.

However, if snuggling is turned on `label_snuggle=yes`, the label's radial
position may be slightly adjusted to reduce the number of layers of text.

Snuggling is heuristic—it is not based on any kind of global optimization.

```    
    <plot>
    
    ...
    label_snuggle             = yes
    
    # shift label up to 2x its height in pixels in the angular direction
    max_snuggle_distance            = 2r
    
    # sample possible label positions every 2 pixels
    snuggle_sampling                = 2
    
    snuggle_tolerance               = 0.25r
    
    snuggle_link_overlap_test      = yes 
    snuggle_link_overlap_tolerance = 2p
    
    snuggle_refine                 = yes
    
    </plot>
```
#### snuggling parameters
To help arrange the labels so that they occupy less space, use label
snuggling. The `max_snuggle_distance` controls how far the label may be
shifted, in the angular direction, to fit better. The distance limit is
expressed in pixels or relative to the label's size along the tangential
direction.

The label is tested at a new angular position every `snuggle_sampling` pixels,
within the `max_snuggle_distance` of its original position. By increasing the
`snuggle_sampling` value, the layout process runs faster, but is less precise.

You can also short-circuit precise placement by setting `snuggle_tolerance`
(absolute or relative to label's tangential size). The larger this value, the
less precise the placement.

If the labels have a link line, you choose to test whether link lines overlap
with previous labels using `snuggle_link_overlap_test`. The extent of
acceptable overlap is set using `snuggle_link_overlap_tolerance`.

The `snuggle_refine` parameter toggles an additional check for crossing of
links of labels that are placed at similar radial positions. Label pairs whose
link lines cross are swapped. This refine parameter is functionaly only if
`show_links=yes`.

#### label padding
You can increase the `max_snuggle_distance` to make the label layout more
compact. When snuggling, it can also be helpful to adjust padding, both
angular (via `padding`) and radial (via `rpadding`) directions around the
label. Both can be absolute or relative.

```    
    <plot>
    ...
    padding  = 2p
    rpadding = 0.1r
    
    </plot>
```
By making padding negative, labels are more tightly spaced. When expressed in
relative units (e.g. `0.1r`), radial padding is relative to label width and
angular padding is relative to label height.

Experiment with the `max_snuggle_distance` and padding parameters to find a
good combination for your data. If you have a large number of labels
(hundreds) then the track may take a while to optimize (several minutes).

#### uniformly placed text
If you want text to be placed uniformly don't use snuggling, which will move
labels around.

For example, snuggling works best when label density varies. But if you're
showing text that is defined at specific intervals (e.g. sequence), don't
snuggle. You'll probably want to turn links off (this is the default) and use
a monospaced font

```    
    label_font = mono
```
All font definitions are in `etc/fonts.conf` in the Circos distribution.

```    
    # etc/fonts.conf
    
    ...
    mono           = fonts/modern/cmuntt.ttf  # CMUTypewriter-Regular
    mono_light     = fonts/modern/cmunbtl.otf # CMUTypewriter-Light
    
    # same as mono and mono_light
    fixed          = fonts/modern/cmuntt.ttf  # CMUTypewriter-Regular
    fixed_light    = fonts/modern/cmunbtl.otf # CMUTypewriter-Light
    ...
```
#### debugging text placement
Text placement can take while, especially if snuggling is turned on and you
have many labels. Run Circos with `-debug_group text` to convince yourself
that something is happening.

```    
    > circos ... -debug_group text
    ...
    debuggroup text 6.45s label layer 2 snuggle seek - STX12 8.0 d 26 label_min_height 42 global_min_height 28
    debuggroup text 6.45s label layer 2 snuggle seek + PPP1R8 0.0 d 14 label_min_height 42 global_min_height 28
    debuggroup text 6.45s label layer 2 snuggle seek - PPP1R8 0.0 d 14 label_min_height 42 global_min_height 28
    ...
```
Text that does not fit into the track boundaries won't be placed. Run Circos
with `-debug_group textplace` to monitor which labels are not placed.

```    
    > circos ... -debug_group textplace
    ...
    debuggroup textplace 23.02s placed hs1 40858938 40903911 RIMS3
    debuggroup textplace 23.02s placed hs1 29346951 29380948 SFRS4
    debuggroup textplace 23.03s not_placed hs1 1466916 1500125 SSU72
    debuggroup textplace 23.03s placed hs1 27972280 28023550 STX12
    debuggroup textplace 23.03s placed hs1 40079314 40121764 TRIT1
    ...
``````### images
![Circos tutorial image -
Text—Stacking](/documentation/tutorials/2d_tracks/text_2/img/01.png) ![Circos
tutorial image -
Text—Stacking](/documentation/tutorials/2d_tracks/text_2/img/02.png) ![Circos
tutorial image -
Text—Stacking](/documentation/tutorials/2d_tracks/text_2/img/03.png) ![Circos
tutorial image -
Text—Stacking](/documentation/tutorials/2d_tracks/text_2/img/04.png) ![Circos
tutorial image -
Text—Stacking](/documentation/tutorials/2d_tracks/text_2/img/05.png)
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
    
    chromosomes_units           = 1000000
    chromosomes                 = hs1:0-50
    chromosomes_display_default = no
    
    <plots>
    
    type       = text
    color      = black
    label_font = condensed
    
    <plot>
    
    file = data/6/text.genes.txt
    r1   = 0.2r+300p
    r0   = 0.2r
    
    label_size = 8p
    
    show_links     = yes
    link_dims      = 1p,1p,2p,1p,1p
    link_thickness = 1p
    link_color     = red
    
    padding        = 2p
    rpadding       = 2p
    
    label_snuggle         = yes
    max_snuggle_distance  = 1r
    snuggle_tolerance     = 0.25r
    snuggle_sampling      = 2
    
    <rules>
    <rule>
    condition  = var(value) =~ /5/i
    color      = red
    </rule>
    </rules>
    
    </plot>
    
    <plot>
    
    file = data/6/text.genes.txt
    r1   = 0.975r
    r0   = 0.5r
    
    label_size = 12p
    
    show_links     = yes
    link_dims      = 2p,2p,4p,2p,2p
    link_thickness = 2p
    link_color     = red
    
    label_snuggle         = yes
    max_snuggle_distance  = 1r
    snuggle_tolerance     = 0.25r
    snuggle_sampling      = 2
    
    <rules>
    <rule>
    condition  = var(value) =~ /ZNF/i
    label_font = condensedbold
    </rule>
    </rules>
    
    </plot>
    
    <plot>
    
    file = data/6/text.genes.txt
    r1   = 1r+200p
    r0   = 1r
    
    label_size = 24p
    
    show_links     = yes
    link_dims      = 0p,0p,100p,0p,0p
    link_thickness = 2p
    link_color     = blue
    
    <rules>
    <rule>
    condition = var(value) =~ /znf/i
    color     = red
    </rule>
    <rule>
    condition = var(value) =~ /ifi/i
    color     = green
    </rule>
    <rule>
    condition  = var(value) =~ /orf/;
    color      = grey
    link_color = grey
    label_size = 16p
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
    format           = %d
    
    <tick>
    spacing        = 1u
    show_label     = no
    size           = 10p
    </tick>
    
    <tick>
    spacing        = 5u
    show_label     = yes
    label_size     = 20p
    size           = 15p
    </tick>
    
    <tick>
    spacing        = 10u
    show_label     = yes
    label_size     = 24p
    </tick>
    
    </ticks>
```
  

* * *
