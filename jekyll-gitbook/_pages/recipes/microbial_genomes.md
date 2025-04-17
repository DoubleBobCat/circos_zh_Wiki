---
author: DoubleCat
date: 2025-04-11
layout: post
category: recipes
title: Microbial Genome
---

## Microbial Genome
### lesson
Circos is suitable for creating images of genomes that only have one
chromosome, such as circular bacterial genomes. This example mentions a few
tips in creating such images.

#### structures crossing origin
First, and perhaps ironically, Circos doesn't actually understand the concept
of a circular chromosome. In other words, a chromosome, which is represented
by one or more ideograms, must have a beginning and an end which are
explicitly defined.

This means that on circular chromosomes, structures (e.g. clone, gene) that
cross the origin must be defined by two entries. For example, if you have a 1
Mb genome, and wish to have a highlight from `950,000` to `50,000` you must
define two highlights: `950,000-1,000,000` and then another `1-50,000`.

#### ideogram breaks
To achieve an image with an ideogram that appears circular, set the ideogram
spacing values to `0`. This is done in the <ideogram><spacing> found in the
`ideogram.conf` file (which is linked to the main `circos.conf` file via the
`<<include ideogram.conf>>` directive.

```    
    <ideogram>
     <spacing>
      default = 0u
      break   = 0u
     </ideogram>
    </spacing>
```
If you would like to decompose the chromosome into multiple ideograms, you
still need to maintain a zero-separation between the ideograms containing the
end and beginning of the chromosome. One of the images in this example shows
how to introduce three axis breaks into the image in this manner, using the
<pairwise> block.
### images
![Circos tutorial image - Microbial
Genome](/documentation/tutorials/recipes/microbial_genomes/img/01.png)
![Circos tutorial image - Microbial
Genome](/documentation/tutorials/recipes/microbial_genomes/img/02.png)
![Circos tutorial image - Microbial
Genome](/documentation/tutorials/recipes/microbial_genomes/img/03.png)
### configuration
#### circos.conf
```    
    <<include etc/colors_fonts_patterns.conf>>
    
    <<include ideogram.conf>>
    <<include ticks.conf>>
    
    karyotype = data/8/karyotype.microbe.txt
    
    <image>
    <<include etc/image.conf>>
    </image>
    
    chromosomes_units           = 1000
    chromosomes_display_default = yes
    
    <<include highlights.conf>>
    
    <plots>
    
    <plot>
    type  = text
    file  = data/8/microbe.labels.txt
    color = black
    r1    = 0.95r
    r0    = 0.85r
    
    label_size = 16
    label_font = light
    padding    = 5p
    rpadding   = 5p
    show_links     = yes
    link_dims      = 5p,4p,8p,4p,0p
    link_thickness = 1p
    link_color     = dgrey
    label_snuggle        = yes
    max_snuggle_distance = 2r
    snuggle_sampling     = 1
    snuggle_tolerance    = 0.25r
    snuggle_link_overlap_test      = yes 
    snuggle_link_overlap_tolerance = 2p
    snuggle_refine                 = yes
    </plot>
    
    <plot>
    type  = text
    file  = data/8/microbe.labels.2.txt
    color = black
    r1    = 0.4r
    r0    = 0.2r
    label_size = 10p
    label_font = default
    padding    = 1p
    rpadding   = 1p
    show_links     = yes
    link_dims      = 1p,2p,3p,2p,1p
    link_thickness = 1p
    link_color     = red
    label_snuggle        = yes
    max_snuggle_distance = 2r
    snuggle_sampling     = 1
    snuggle_tolerance    = 0.25r
    snuggle_link_overlap_test      = yes 
    snuggle_link_overlap_tolerance = 2p
    snuggle_refine                 = yes
    </plot>
    
    <plot>
    type      = tile
    file      = data/8/microbe.tile.txt
    r1        = 0.78r
    r0        = 0.72r
    layers    = 5
    margin    = 0.2u
    thickness = 12
    padding   = 6
    layers_overflow  = hide
    orientation      = out
    stroke_thickness = 1
    stroke_color     = grey
    color            = orange
    <rules>
    <rule>
    condition = var(size) < 5kb
    color     = lgrey
    </rule>
    </rules>
    </plot>
    
    <plot>
    type        = histogram
    file        = data/8/microbe.plot.1.txt
    r1          = 0.68r
    r0          = 0.65r
    min         = 0
    max         = 1
    extend_bin  = no
    fill_color  = lblue
    color       = blue
    thickness   = 0
    orientation = out
    </plot>
    
    <plot>
    type        = histogram
    file        = data/8/microbe.plot.2.txt
    r1          = 0.65r
    r0          = 0.63r
    max         = 1
    min         = 0
    extend_bin  = no
    fill_color  = orange
    orientation = in
    
    <rules>
    <rule>
    condition = var(start) % 2000
    show      = no
    </rule>
    </rules>
    </plot>
    
    <plot>
    type        = histogram
    file        = data/8/microbe.plot.3.txt
    color       = black
    thickness   = 2
    r1          = 0.62r
    r0          = 0.57r
    max         = 1
    min         = 0
    orientation = out
    <rules>
    <rule>
    condition = var(value) > 0.9
    color     = red
    </rule>
    <rule>
    condition = var(value) < 0.1
    color     = green
    </rule>
    </rules>
    </plot>
    
    </plots>
    
    <<include etc/housekeeping.conf>>
```
  

* * *

#### highlights.conf
```    
    <highlights>
    
    <highlight>
    init_counter = highlight:1
    file = data/8/microbe.highlights.counter(highlight).txt
    r1   = conf(.,r0)+0.03r
    r0   = 0.95r
    </highlight>
    <highlight>
    file = data/8/microbe.highlights.counter(highlight).txt
    r1   = conf(.,r0)+0.03r
    r0   = 0.82r
    </highlight>
    <highlight>
    file = data/8/microbe.highlights.counter(highlight).txt
    r1   = conf(.,r0)+0.01r
    r0   = 0.53r
    </highlight>
    <highlight>
    file = data/8/microbe.highlights.counter(highlight).txt
    r1   = conf(.,r0)+0.01r
    r0   = 0.51r
    </highlight>
    <highlight>
    file = data/8/microbe.highlights.counter(highlight).txt
    r1   = conf(.,r0)+0.01r
    r0   = 0.46r
    </highlight>
    <highlight>
    file = data/8/microbe.highlights.counter(highlight).txt
    r1   = conf(.,r0)+0.01r
    r0   = 0.48r
    </highlight>
    <highlight>
    file = data/8/microbe.highlights.counter(highlight).txt
    r1   = conf(.,r0)+0.01r
    r0   = 0.41r
    </highlight>
    <highlight>
    file = data/8/microbe.highlights.counter(highlight).txt
    r1   = conf(.,r0)+0.01r
    r0   = 0.43r
    </highlight>
    <highlight>
    file = data/8/microbe.highlights.counter(highlight).txt
    r1   = conf(.,r0)+0.01r
    r0   = 0.19r
    </highlight>
    <highlight>
    file = data/8/microbe.highlights.counter(highlight).txt
    r1   = conf(.,r0)+0.01r
    r0   = 0.17r
    </highlight>
    <highlight>
    file = data/8/microbe.highlights.counter(highlight).txt
    r1   = conf(.,r0)+0.01r
    r0   = 0.15r
    </highlight>
    
    <highlight>
    file = data/8/microbe.separator.txt
    r1   = conf(.,r0)+0.005r
    r0   = 0.80r
    fill_color = vvlgrey
    </highlight>
    <highlight>
    file = data/8/microbe.separator.txt
    r1   = conf(.,r0)+0.005r
    r0   = 0.70r
    fill_color = vvlgrey
    </highlight>
    <highlight>
    file = data/8/microbe.separator.txt
    r1   = conf(.,r0)+0.005r
    r0   = 0.55r
    fill_color = vvlgrey
    </highlight>
    <highlight>
    file = data/8/microbe.separator.txt
    r1   = conf(.,r0)+0.005r
    r0   = 0.50r
    fill_color = vvlgrey
    </highlight>
    <highlight>
    file = data/8/microbe.separator.txt
    r1   = conf(.,r0)+0.005r
    r0   = 0.45r
    fill_color = vvlgrey
    </highlight>
    <highlight>
    file = data/8/microbe.separator.txt
    r1   = conf(.,r0)+0.005r
    r0   = 0.40r
    fill_color = vvlgrey
    </highlight>
    
    </highlights>
```
  

* * *

#### ideogram.conf
```    
    <ideogram>
    
    <spacing>
    
    default = 0u
    break   = 0u
    
    </spacing>
    
    # thickness (px) of chromosome ideogram
    thickness        = 20p
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
    label_font     = default
    label_radius   = dims(ideogram,radius) + 0.05r
    label_size     = 36
    label_parallel = yes
    label_case     = upper
    
    # cytogenetic bands
    band_stroke_thickness = 2
    
    # show_bands determines whether the outline of cytogenetic bands
    # will be seen
    show_bands            = yes
    # in order to fill the bands with the color defined in the karyotype
    # file you must set fill_bands
    fill_bands            = yes
    
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
    skip_first_label     = yes
    skip_last_label      = no
    radius               = dims(ideogram,radius_outer)
    tick_separation      = 2p
    min_label_distance_to_edge = 0p
    label_separation = 5p
    label_offset     = 5p
    label_size = 8p
    multiplier = 0.001
    color = black
    
    thickness = 3p
    size      = 20p
    
    <tick>
    size           = 10p
    spacing        = 1u
    color          = black
    show_label     = no
    label_size     = 12p
    format         = %.2f
    grid           = no
    grid_color     = lblue
    grid_thickness = 1p
    </tick>
    <tick>
    size           = 15p
    spacing        = 5u
    color          = black
    show_label     = yes
    label_size     = 16p
    format         = %s
    grid           = yes
    grid_color     = lgrey
    grid_thickness = 1p
    
    </tick>
    <tick>
    size           = 18p
    spacing        = 10u
    color          = black
    show_label     = yes
    label_size     = 16p
    format         = %s
    grid           = yes
    grid_color     = grey
    grid_thickness = 1p
    </tick> 
    <tick>
    spacing        = 100u
    color          = black
    show_label     = yes
    suffix = " kb"
    label_size     = 36p
    format         = %s
    grid           = yes
    grid_color     = dgrey
    grid_thickness = 1p
    </tick>
    </ticks>
```
  

* * *
