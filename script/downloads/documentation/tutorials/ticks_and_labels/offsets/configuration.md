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

## 4\. Tick Marks - Offsets

[Lesson](/documentation/tutorials/ticks_and_labels/offsets/lesson)
[Images](/documentation/tutorials/ticks_and_labels/offsets/images)
[Configuration](/documentation/tutorials/ticks_and_labels/offsets/configuration)

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
    # global offset for ticks (remember that labels are automatically offset)
    offset               = 0p
    radius               = dims(ideogram,radius_outer)
    multiplier           = 1e-6
    
    thickness      = 4p
    
    # if set to yes, all ticks at all spacings will be drawn, regardless of whether
    # there is another tick at this position (e.g. at 100Mb the ticks for 10u, 5u and 1u
    # will be drawn. force_display=yes is useful only when offset is used to make each
    # tick set drawn at a different radial position)
    force_display        = no
    
    # global label offset - useful if set to relative size
    # (will be relative to ticks size)
    # local label offsets add to this value
    # label_offset = 0.5r
    
    <tick>
    spacing        = 0.5u
    offset         = 0p
    size           = 15p
    color          = red
    show_label     = yes
    label_size     = 20p
    label_offset   = dims(tick,max_tick_length) - 15p
    format         = %.1f
    </tick>
    
    <tick>
    spacing        = 1u
    offset         = 0p
    size           = 20p
    color          = blue
    show_label     = yes
    label_size     = 20p
    label_offset   = dims(tick,max_tick_length) - 20p
    format         = %d
    </tick>
    
    <tick>
    spacing        = 5u
    offset         = 0p
    size           = 25p
    color          = green
    show_label     = yes
    label_size     = 20p
    label_offset   = dims(tick,max_tick_length) - 25p
    format         = %d
    </tick>
    
    <tick>
    spacing        = 10u
    offset         = 0p
    size           = 30p
    color          = black
    show_label     = yes
    label_size     = 24p
    label_offset   = dims(tick,max_tick_length) - 30p
    format         = %d
    </tick>
    
    </ticks>
    

  

* * *

