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

## 6\. Label Formats

[Lesson](/documentation/tutorials/ticks_and_labels/label_format/lesson)
[Images](/documentation/tutorials/ticks_and_labels/label_format/images)
[Configuration](/documentation/tutorials/ticks_and_labels/label_format/configuration)

### circos.conf

    
    
    <<include colors_fonts_patterns.conf>>
    
    <<include ideogram.conf>>
    <<include ticks.conf>>
    
    <image>
    <<include etc/image.conf>>
    </image>
    
    karyotype   = data/karyotype/karyotype.human.txt
    
    chromosomes_units           = 1000000
    chromosomes_display_default = no
    chromosomes                 = hs1:0-100
    
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
    show_label* = no
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
    
    radius       = dims(ideogram,radius_outer)
    multiplier   = 1/1u
    label_offset = 0.4r
    thickness    = 4p
    size         = 20p
    show_label   = yes
    
    <tick>
    spacing        = 0.25u
    color          = red
    label_size     = 16p
    label_color    = red
    format         = %df
    mod            = 1u
    suffix         = kb
    multiplier     = 1000/1u
    prefix         = +
    </tick>
    
    <tick>
    spacing        = 1u
    color          = green
    label_color    = green
    label_size     = 18p
    label_offset   = 30p
    format         = %.1f
    mod            = 5u
    suffix         = " Mb"
    prefix         = +
    </tick>
    
    <tick>
    spacing       = 5u
    color         = blue
    label_color   = blue
    label_size    = 20p
    label_offset  = 30p
    format        = %d
    mod           = 100u
    suffix        = Mb
    </tick>
    
    <tick>
    spacing        = 20u
    label_size     = 24p
    format         = %d
    suffix         = " Mb"
    label_offset   = 30p
    </tick>
    
    </ticks>
    

  

* * *

