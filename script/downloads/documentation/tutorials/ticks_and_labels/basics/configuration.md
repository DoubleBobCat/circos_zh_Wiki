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

## 1\. Tick Marks - Basics

[Lesson](/documentation/tutorials/ticks_and_labels/basics/lesson)
[Images](/documentation/tutorials/ticks_and_labels/basics/images)
[Configuration](/documentation/tutorials/ticks_and_labels/basics/configuration)

### circos.conf

    
    
    <<include etc/colors_fonts_patterns.conf>>
    
    <<include ideogram.conf>>
    <<include ticks.conf>>
    
    <image>
    <<include etc/image.conf>>
    </image>
    
    karyotype   = data/karyotype/karyotype.human.txt
    
    chromosomes_units           = 1000000
    chromosomes_display_default = no
    chromosomes                 = hs1;hs2;hs3;hs4;hs5
    
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
    
    #chromosomes_display_default = yes
    chromosomes_display_default = no
    
    # no ticks on chromosomes hs1 and hs2
    # use with chromosomes_display_default = yes
    # chromosomes = -hs1;-hs2:0-100;-hs3:100-)
    
    chromosomes          = hs1;hs2:0-100;hs3:100-)
    
    radius               = dims(ideogram,radius_outer)
    label_offset         = 5p
    orientation          = out
    label_multiplier     = 1e-6
    color                = black
    
    <tick>
    #chromosomes    = -hs2
    spacing        = 1u
    size           = 8p
    thickness      = 2p
    color          = dgrey
    show_label     = no
    </tick>
    
    <tick>
    chromosomes    = hs4
    spacing        = 5u
    size           = 12p
    color          = dred
    thickness      = 2p
    show_label     = yes
    label_size     = 20p
    label_color    = dred
    label_offset   = 3p
    format         = %d
    </tick>
    
    <tick>
    chromosomes    = -hs2;hs5
    spacing        = 10u
    size           = 14p
    thickness      = 2p
    show_label     = yes
    label_size     = 24p
    label_offset   = 5p
    format         = %d
    </tick>
    
    </ticks>
    

  

* * *

