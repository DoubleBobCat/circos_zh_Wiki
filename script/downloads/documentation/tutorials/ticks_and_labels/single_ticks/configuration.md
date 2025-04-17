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

## 8\. Ticks at Specific Positions

[Lesson](/documentation/tutorials/ticks_and_labels/single_ticks/lesson)
[Images](/documentation/tutorials/ticks_and_labels/single_ticks/images)
[Configuration](/documentation/tutorials/ticks_and_labels/single_ticks/configuration)

### circos.conf

    
    
    <<include colors_fonts_patterns.conf>>
    
    <<include ideogram.conf>>
    <<include ticks.conf>>
    
    <image>
    <<include etc/image.conf>>
    </image>
    
    karyotype   = data/karyotype/karyotype.human.txt
    
    chromosomes_units           = 1000000
    #chromosomes                 = hs1[a]:0-75;hs1[b]:100-150;hs1[c]:200-)
    chromosomes = hs1
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
    
    radius         = dims(ideogram,radius_outer)
    multiplier     = 1/1u
    color          = black
    force_display  = yes
    thickness      = 4p
    size           = 20p
    show_label     = yes
    label_size     = 36p
    label_offset   = 10p
    format         = %d
    
    <tick>
    show           = yes
    position       = 25u
    </tick>
    
    <tick>
    show           = yes
    position       = 30u,32u,34u,40u
    color          = red
    </tick>
    
    <tick>
    show           = yes
    rposition      = 0.05,0.15,0.2
    spacing_type   = relative
    color          = blue
    format         = %d
    </tick>
    
    <tick>
    show           = yes
    rposition      = 0.55,0.7,0.9
    spacing_type   = relative
    label_relative = yes
    color          = green
    format         = %.2f
    </tick>
    
    <tick>
    show           = yes
    position       = start
    label          = 3'
    color          = purple
    format         = %s
    </tick>
    
    <tick>
    show           = yes
    position       = end
    label          = 5'
    color          = purple
    format         = %s
    </tick>
    
    </ticks>
    

  

* * *

