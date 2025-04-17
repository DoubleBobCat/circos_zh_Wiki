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

## 7\. Relative Ticks

[Lesson](/documentation/tutorials/ticks_and_labels/relative_ticks/lesson)
[Images](/documentation/tutorials/ticks_and_labels/relative_ticks/images)
[Configuration](/documentation/tutorials/ticks_and_labels/relative_ticks/configuration)

### circos.conf

    
    
    <<include colors_fonts_patterns.conf>>
    
    <<include ideogram.conf>>
    <<include ticks.conf>>
    
    <image>
    <<include etc/image.conf>>
    </image>
    
    karyotype   = data/karyotype/karyotype.human.txt
    
    chromosomes_units           = 1000000
    # use this to see how relative ticks can be drawn relative to
    # the ideograms (use rdivisor=ideogram in the tick blocks)
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
    
    radius*     = 0.75r
    
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
    thickness      = 2p
    show_label     = yes
    format         = %d
    
    size           = 20p
    thicknes       = 4p
    label_offset   = 5p
    
    <tick>
    show           = yes
    spacing        = 1u
    rspacing       = 0.02
    # this is the default spacing type
    spacing_type   = absolute
    label_size     = 24p
    </tick>
    
    <tick>
    # when spacing_type is relative, define
    # rspacing to be the increment
    show           = yes
    rspacing       = 0.01
    spacing_type   = relative
    color          = red
    label_size     = 30p
    offset         = 85p
    label_relative = yes
    rmultiplier    = 100
    suffix         = %
    # This will make ticks spaced relatively by ideogram,
    # and not chromosome. This setting is useful when
    # the chromosome is displayed as multiple ideograms
    # rdivisor        = ideogram
    </tick>
    
    <tick>
    show           = yes
    rspacing       = 0.1
    spacing_type   = relative
    thickness      = 3p
    color          = blue
    label_size     = 36p
    offset         = 215p
    label_relative = yes
    rmultiplier    = 10
    suffix         = /10
    #rdivisor       = ideogram
    </tick>
    
    </ticks>
    

  

* * *

