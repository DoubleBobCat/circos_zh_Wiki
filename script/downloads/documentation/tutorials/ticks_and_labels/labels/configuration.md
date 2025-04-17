Use the [latest version of Circos](/software/download/circos/) and read
[Circos best
practices](/documentation/tutorials/reference/best_practices/)—these list
recent important changes and identify sources of common problems.

If you are having trouble, post your issue to the [Circos Google
Group](https://groups.google.com/group/circos-data-visualization) and [include
all files and detailed error logs](/support/support/). Please do not email me
directly unless it is urgent—you are much more likely to receive a timely
reply from the group.

Don't know what question to ask? Read [Points of View: Visualizing Biological
Data](https://www.nature.com/nmeth/journal/v9/n12/full/nmeth.2258.html) by
Bang Wong, myself and invited authors from the [Points of View
series](https://mk.bcgsc.ca/pointsofview).

# 5 — Tick Marks, Grids and Labels

## 3\. Tick Marks - Label Margins

[Lesson](/documentation/tutorials/ticks_and_labels/labels/lesson)
[Images](/documentation/tutorials/ticks_and_labels/labels/images)
[Configuration](/documentation/tutorials/ticks_and_labels/labels/configuration)

### circos.conf

    
    
    <<include colors_fonts_patterns.conf>>
    
    <<include ideogram.conf>>
    <<include ticks.conf>>
    
    <image>
    <<include etc/image.conf>>
    </image>
    
    karyotype   = data/karyotype/karyotype.human.txt
    
    chromosomes_units  = 1000000
    chromosomes        = hs1;hs2;hs3:0-100;hs4:100-150
    chromosomes_scale  = hs1:0.5;hs2:1;hs3:4;hs4:8
    chromosomes_display_default = no
    
    <<include etc/housekeeping.conf>>
    

  

* * *

### bands.conf

    
    
    show_bands            = no
    fill_bands            = yes
    band_stroke_thickness = 2
    band_stroke_color     = white
    band_transparency     = 0
    

  

* * *

### ideogram.conf

    
    
    <ideogram>
    
    <spacing>
    default = 0.01r
    break   = 2u
    </spacing>
    
    <<include ideogram.position.conf>>
    <<include ideogram.label.conf>>
    <<include bands.conf>>
    
    </ideogram>
    
    

  

* * *

### ideogram.label.conf

    
    
    show_label     = yes
    label_font     = default
    label_radius   = (dims(ideogram,radius_inner) + dims(ideogram,radius_outer))/2
    label_center   = yes
    label_size     = 72
    label_with_tag = yes
    label_parallel = yes
    label_case     = upper
    

  

* * *

### ideogram.position.conf

    
    
    radius           = 0.90r
    thickness        = 100p
    fill             = no
    fill_color       = black
    stroke_thickness = 2
    stroke_color     = black
    

  

* * *

### ticks.conf

    
    
    show_ticks          = yes
    show_tick_labels    = yes
    
    <ticks>
    radius               = dims(ideogram,radius_outer)
    multiplier           = 1e-6
    
    label_offset = 5p
    thickness = 3p
    size      = 20p
    
    # ticks must be separated by 2 pixels in order
    # to be displayed
    tick_separation      = 2p
    # Density of labels is independently controlled.
    # While all tick sets have labels, only labels
    # no closer than 5 pixels to nearest label will be drawn
    label_separation     = 5p
    
    <tick>
    spacing        = 0.5u
    color          = red
    show_label     = yes
    label_size     = 14p
    label_offset   = 0p
    format         = %.1f
    </tick>
    
    <tick>
    spacing        = 1u
    color          = blue
    show_label     = yes
    label_size     = 16p
    label_offset   = 0p
    format         = %d
    </tick>
    
    <tick>
    spacing        = 5u
    color          = green
    show_label     = yes
    label_size     = 20p
    label_offset   = 0p
    format         = %d
    </tick>
    
    <tick>
    spacing        = 10u
    color          = black
    show_label     = yes
    label_size     = 24p
    label_offset   = 5p
    format         = %d
    </tick>
    
    </ticks>
    

  

* * *

