---
author: DoubleCat
date: 2025-04-11
layout: post
category: links
title: Link Formatting
---

### lesson
In this example, the image will be created using multiple data sources for
links. I'm also going to subvert the record_limit setting, and in combination
with z depth, to sample different links from the same data file.

In general, if you have multiple data files, each is associated with its own
<link> block.

```    
    <links>
    
     # global parameters here
     ...
    
     <link>
      file = /path/to/file
      # local parameters for this data set
      ...
     </link>
    
     <link>
      file = /path/to/file
      # local parameters for this data set
      ...
     </link>
    
     ...
    
    </links>
```
When combining multiple link data sets in one image, there are a few things to
keep in mind.

First, set the z depth for each data set accordingly. Data sets with a higher
the z depth value are drawn on top of data sets with a lower value. In this
example, I draw the first 10,000 records from segdup.txt in very light grey
(z=5), then the first 2,500 records in light grey (z=10, thus on top of any
z<10 data), then the first 1,000 records in grey (z=15, thus on top of any
z<15 data), and so on.

Second, you can adjust link geometry for each data set. In this example, I've
modified the crest and bezier radius purity for links drawn from the three
`segdup.bundle*.txt` files.

Finally, thickness and color can be effectively used to help layer the data. I
typically draw links with a lower z value in a light shade of a color and with
thin lines.
### images
![Circos tutorial image - Link
Formatting](/documentation/tutorials/links/formatting/img/01.png)
### configuration
#### circos.conf
```    
    <<include colors_fonts_patterns.conf>>
    
    <<include ideogram.conf>>
    <<include ticks.conf>>
    
    <image>
    <<include etc/image.conf>>
    </image>
    
    karyotype   = data/karyotype/karyotype.human.txt
    
    chromosomes_units = 1000000
    chromosomes_display_default = no
    chromosomes       = hs1;hs2;hs3
    
    <links>
    
    z      = 0
    radius = 0.975r
    crest  = 0.5
    bezier_radius        = 0.5r
    bezier_radius_purity = 0.75
    
    <link>
    z            = 50
    color        = green_a2
    thickness    = 4
    file         = data/5/segdup.bundle3.txt
    bezier_radius_purity = 0.2
    crest = 1
    </link>
    
    <link>
    z            = 40
    color        = orange_a2
    thickness    = 4
    file         = data/5/segdup.bundle2.txt
    bezier_radius_purity = 0.2
    crest = 1
    </link>
    
    <link>
    z            = 30
    color        = blue_a2
    thickness    = 4
    file         = data/5/segdup.bundle1.txt
    bezier_radius_purity = 0.2
    crest        = 1
    </link>
    
    <link>
    z            = 20
    color        = dgrey_a2
    thickness    = 3
    file         = data/5/segdup.txt
    record_limit = 500
    </link>
    
    <link>
    z            = 15
    color        = grey_a2
    thickness    = 3
    file         = data/5/segdup.txt
    record_limit = 1000
    </link>
    
    <link>
    z            = 10
    color        = lgrey_a2
    thickness    = 2
    file         = data/5/segdup.txt
    record_limit = 2500
    </link>
    
    <link>
    z            = 5
    color        = vlgrey_a2
    thickness    = 1
    file         = data/5/segdup.txt
    record_limit = 10000
    </link>
    
    </links>
    
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
    
    </ideogram>
``````
  

* * *

#### ideogram.label.conf
```    
    show_label       = yes
    label_font       = default
    label_radius     = dims(ideogram,radius) + 0.075r
    label_with_tag   = yes
    label_size       = 36
    label_parallel   = yes
    label_case       = lower
    label_format     = eval(sprintf("chr%s",var(label)))
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
    
    radius           = dims(ideogram,radius_outer)
    orientation      = out
    label_multiplier = 1e-6
    color            = black
    size             = 20p
    thickness        = 3p
    label_offset     = 5p
    
    <tick>
    spacing        = 1u
    show_label     = no
    </tick>
    
    <tick>
    spacing        = 5u
    show_label     = yes
    label_size     = 20p
    format         = %d
    </tick>
    
    <tick>
    spacing        = 10u
    show_label     = yes
    label_size     = 24p
    format         = %d
    </tick>
    
    </ticks>
```
  

* * *
