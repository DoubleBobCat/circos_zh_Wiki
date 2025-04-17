---
author: DoubleCat
date: 2025-04-11
layout: post
category: recipes
title: Nature Cover Encode Diagram
---

## Nature Cover Encode Diagram
### lesson
[Nature's special
issue](https://www.nature.com/nature/journal/v489/n7414/index.html) dedicated
to the [Encode Project](https://www.genome.gov/10005107) uses the Circos motif
on its
[cover](https://www.nature.com/nature/journal/v489/n7414/index.html#about-the-
cover) as well as the interactive [Encode
Explorer](https://www.nature.com/encode/), which is available as an [app at
iTunes](https://itunes.apple.com/app/id553487333).

In this tutorial, I'll show you how to automatically generate the image that
appears on the cover. The original was created for Nature by [Carl
DeTorres](https://www.carldetorres.com/).

#### image elements
The figure contains 23 segments — these are human chromosomes 1–22 and
chromosome X. The proportions in the figure aren't exactly the same as the
lengths of the assembled chromosomes in the hg19 human assembly. Here, we'll
use the assembled lengths.

The color scheme used is is a pleasant range of pastel hues that cycle through
orange, green, blue and purple. We'll redefine the default chromosome colors
to make use of this color scheme.

The data in the figure is shown in six concentric tracks, whose spacing
decreases slightly towards the inside of the circle. Each track appears to
highlight fixed-width regions, colored after the chromosome color scheme. I
don't know how the data tracks were populated, whether the data are randomly
placed, designed for visual effect, or drawn from an actual Encode data set.
In this example, we'll create the tracks using a random scheme.

#### color scheme
I sampled the RGB colors from the cover image and obtained the following
values, which I've placed in a <colors> block. The `*` suffix overrides
existing color definitions.

```    
    # circos.conf
    <<include etc/colors_fonts_patterns.conf>>
    <colors>
    chr1*  = 163,132,130
    chr2*  = 188,162,118
    chr3*  = 216,196,96
    chr4*  = 233,212,56
    chr5*  = 229,229,50
    chr6*  = 212,222,56
    chr7*  = 195,215,57
    chr8*  = 177,209,58
    chr9*  = 160,204,61
    chr10* = 139,198,61
    chr11* = 128,193,95
    chr12* = 115,186,126
    chr13* = 102,183,152
    chr14* = 91,178,176
    chr15* = 61,174,199
    chr16* = 36,170,224
    chr17* = 75,129,194
    chr18* = 85,111,180
    chr19* = 92,92,168
    chr20* = 98,70,156
    chr21* = 101,45,145
    chr22* = 121,74,141
    chrx*  = 140,104,137
    </colors>
```
The background of the image is set in the <image> block. The `*` suffix is
used to overwrite values of parameters set elsewhere in the block (e.g., here
defined in the included file `etc/image.conf`).

```    
    <image>
    <<include etc/image.conf>>
    background* = black
    </image>
```
#### track positions
Each track has the same data source but has a different appearance because of
dynamic rules that alter the data randomly.

The definition of each track is actually the same, but includes dynamically
changing fields called counters that change the position of each track. The
figure with 7 tracks is created like this

```    
    # variables used in each plot.conf block
    
    plot_width   = 80 
    plot_padding = 25 
    num_plots    = 6  
    
    <plots>
    type             = highlight
    file             = bins.txt
    stroke_thickness = 0
    <<include plot.conf>>
    <<include plot.conf>>
    <<include plot.conf>>
    <<include plot.conf>>
    <<include plot.conf>>
    <<include plot.conf>>
    <<include plot.conf>>
    </plots>
```
where the `plot.conf` file is

```    
    <plot>
    r1   = dims(ideogram,radius_inner)
             - conf(plot_padding)*eval(remap(counter(plot),0,conf(num_plots),1,0.9))
             - eval((conf(plot_width)+conf(plot_padding))*counter(plot)*eval(remap(counter(plot),0,conf(num_plots),1,0.9)))
    r0   = conf(.,r1)
             - conf(plot_width)*eval(remap(counter(plot),0,conf(num_plots),1,0.9))
    post_increment_counter = plot:1
    <<include rules.conf>>
    </plot>
```
The inner and outer radii of the the track (`r0` and `r1`) are computed using
the value of the `plot_padding` and `plot_width` parameters. Each time a plot
is drawn, the value of the variable `counter(plot`) is incremented by 1.

The `dims(ideogram,radius_inner`) variable refers to the position of the inner
radius of the ideograms. The function `remap(VAR,MIN,MAX,TARGETMIN,TARGETMAX`)
is used to remap the variable `VAR` from the range `[MIN,MAX]` to
`[TARGETMIN,TARGETMAX]`. The expressions are designed so that the spacing
between the tracks decreases slightly towards the center of the circle, to
match the appearance of the original image in Nature.

#### track data
Each track uses the same data file, `bins.txt`. How is it that the tracks look
different, then?

The data file defines 7.5 Mb bins across the genome

```    
    hs1 0 7499999
    hs1 7500000 14999999
    hs1 15000000 22499999
    hs1 22500000 29999999
    ...
```
and the color associated with each bin is dynamically altered by rules that
are included in each <plot> block, from the file `rules.conf`.

```    
    # rules.conf
    <rules>
    
    <rule>
    
    # Rules with multiple condition 
    
    # The first condition tests that bins are further than 5 Mb from the
    # start and end of each ideogram.  This ensures that the color
    # for the first/last bin will be the same as the ideogram.
    
    condition  = var(start) >= 5e6 && var(end) < chrlen(var(chr))-5e6
    
    # The probability that the second condition is true is proportional to
    # the track counter. Bins in inner tracks are more likely to trigger
    # this rule.  Here, rand() is a uniformly distributed random number in
    # the range [0,1).
    
    condition  = rand() < remap(counter(plot),0,conf(num_plots)-1,1/conf(num_plots),1) 
    
    # If this rule is true, the color of the bin is changed to that of a
    # random ideogram.
    
    fill_color = eval("chr" . (sort {rand() <=> rand()} (1..22,"x"))[0])
    
    </rule>
    
    # If the above rule is not true, the color of the bin is assigned to
    # that of its ideogram.
    
    <rule>
    condition  = 1
    fill_color = eval("chr" . lc substr(var(chr),2))
    </rule>
    </rules>
```
This is an advanced technique—one meant for designing illustrations more than
for the display of data. However, next time you're in the need of random
circular heatmaps, give it a try.
### images
![Circos tutorial image - Nature Cover Encode
Diagram](/documentation/tutorials/recipes/nature_cover_encode/img/00.png)
![Circos tutorial image - Nature Cover Encode
Diagram](/documentation/tutorials/recipes/nature_cover_encode/img/01.png)
![Circos tutorial image - Nature Cover Encode
Diagram](/documentation/tutorials/recipes/nature_cover_encode/img/02.png)
![Circos tutorial image - Nature Cover Encode
Diagram](/documentation/tutorials/recipes/nature_cover_encode/img/03.png)
### configuration
#### circos.conf
```    
    <<include etc/colors_fonts_patterns.conf>>
    
    <colors>
    chr1*  = 163,132,130
    chr2*  = 188,162,118
    chr3*  = 216,196,96
    chr4*  = 233,212,56
    chr5*  = 229,229,50
    chr6*  = 212,222,56
    chr7*  = 195,215,57
    chr8*  = 177,209,58
    chr9*  = 160,204,61
    chr10* = 139,198,61
    chr11* = 128,193,95
    chr12* = 115,186,126
    chr13* = 102,183,152
    chr14* = 91,178,176
    chr15* = 61,174,199
    chr16* = 36,170,224
    chr17* = 75,129,194
    chr18* = 85,111,180
    chr19* = 92,92,168
    chr20* = 98,70,156
    chr21* = 101,45,145
    chr22* = 121,74,141
    chrx*  = 140,104,137
    </colors>
    
    <<include ideogram.conf>>
    #<<include ticks.conf>>
    
    <image>
    <<include etc/image.conf>>
    background* = black
    </image>
    
    chromosomes_units           = 1000000
    chromosomes_display_default = yes
    chromosomes                 = -hsY
    
    karyotype = data/karyotype/karyotype.human.txt
    
    plot_width   = 80 # 35 if drawing 20 plots
    plot_padding = 25 # 20 if drawing 20 plots
    num_plots    = 6  # 20 if drawing 20 plots
    
    <plots>
    
    type             = highlight
    file             = bins.txt
    stroke_thickness = 0
    
    <<include plot.conf>>
    <<include plot.conf>>
    <<include plot.conf>>
    <<include plot.conf>>
    <<include plot.conf>>
    <<include plot.conf>>
    
    # To draw 20 plots, comment the <<include plot.conf>> lines above and use these:
    
    #<<include plot.10.conf>>
    #<<include plot.10.conf>>
    
    </plots>
    
    <<include etc/housekeeping.conf>>
```
  

* * *

#### ideogram.conf
```    
    <ideogram>
    
    <spacing>
    
    default = 0.0030r
    
    </spacing>
    
    <<include ideogram.position.conf>>
    
    </ideogram>
``````
  

* * *

#### ideogram.label.conf
```    
    show_label       = no
    label_font       = default
    label_radius     = 0.95r
    label_with_tag   = yes
    label_size       = 36
    label_parallel   = yes
    label_case       = lower
    
    # you can format the label by using properties
    # of the ideogram, accessible with var(PROPERTY):
    #
    # chr, chr_with_tag, chrlength, display_idx, end, idx, 
    # label, length, reverse, scale, size, start, tag
    
    label_format     = eval(sprintf("chr%s",var(label)))
```
  

* * *

#### ideogram.position.conf
```    
    radius           = dims(image,radius)-35p
    thickness        = 80p
    fill             = yes
    fill_color       = black
    stroke_thickness = 0
    stroke_color     = black
```
  

* * *

#### plot.10.conf
```    
    <<include plot.conf>>
    <<include plot.conf>>
    <<include plot.conf>>
    <<include plot.conf>>
    <<include plot.conf>>
    <<include plot.conf>>
    <<include plot.conf>>
    <<include plot.conf>>
    <<include plot.conf>>
    <<include plot.conf>>
```
  

* * *

#### plot.conf
```    
    <plot>
    r1   = dims(ideogram,radius_inner)-conf(plot_padding)*eval(remap(counter(plot),0,conf(num_plots),1,0.9))-eval((conf(plot_width)+conf(plot_padding))*counter(plot)*eval(remap(counter(plot),0,conf(num_plots),1,0.9)))
    r0   = conf(.,r1)-conf(plot_width)*eval(remap(counter(plot),0,conf(num_plots),1,0.9))
    post_increment_counter = plot:1
    <<include rules.conf>>
    </plot>
```
  

* * *

#### rules.conf
```    
    <rules>
    <rule>
    
    # Multiple conditions are evaluated using AND. That is, they all
    # have to be true for the rule to trigger.
    
    # The first condition tests that bins are further than 5 Mb from the
    # start and end of each ideogram.  This ensures that the color
    # for the first/last bin will be the same as the ideogram.
    
    condition  = var(start) >= 5e6 && var(end) < chrlen(var(chr))-5e6 
    
    # The probability that the second condition is true is proportional to
    # the track counter. Bins in inner tracks are more likely to trigger
    # this rule.  Here, rand() is a uniformly distributed random number in
    # the range [0,1).
    
    condition  = rand() < remap(counter(plot),0,conf(num_plots)-1,1/conf(num_plots),1)
    
    # If this rule is true, the color of the bin is changed to that of a
    # random ideogram.
    
    fill_color = eval("chr" . (sort {rand() <=> rand()} (1..22,"x"))[0])
    </rule>
    
    # If the above rule is not true, the color of the bin is assigned to
    # that of its ideogram.
    
    <rule>
    condition  = 1
    fill_color = eval("chr" . lc substr(var(chr),2))
    </rule>
    </rules>
```
  

* * *

#### ticks.conf
```    
    show_ticks          = no
    show_tick_labels    = no
    
    <ticks>
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
