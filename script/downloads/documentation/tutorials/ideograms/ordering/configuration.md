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

# 3 — Drawing Ideograms

## 4\. Ordering

[Lesson](/documentation/tutorials/ideograms/ordering/lesson)
[Images](/documentation/tutorials/ideograms/ordering/images)
[Configuration](/documentation/tutorials/ideograms/ordering/configuration)

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
    
    # to explicitly define what is drawn
    chromosomes                 = hs1;hs2;hs3;hs4;hs5;hs6;hs7;hs8
    
    # absolute order - specify the order for all ideograms
    chromosomes_order           = hs2,hs3,hs1,hs5,hs4,hs8,hs7,hs6
    
    # relative order - 1 2 3 6 5 4 7 8
    # why does hs6 appear before hs5? The order requires that hs4 
    # come after hs5. In turn, the position of hs5 is its original position 
    # (i.e. 5th ideogram). Since the position of hs4 has been reserved
    # to come after hs5, the next unordered ideogram (hs6) is placed before
    # hs5 to make hs5 the 5th ideogram.
    #chromosomes_order = hs5,hs4
    
    # relative order - 1 2 3 5 4 6 8 7
    #chromosomes_order = hs3,hs5,hs4,hs6,hs8
    
    # relative order 4 2 3 5 6 7 8 1
    # chromosomes_order = ^,hs4,|,hs1,$
    
    # relative order 4 2 6 7 5 3 8 1
    #chromosomes_order = ^,hs4,|,hs5,hs3,|,hs1,$
    
    # line below will give an error because there are more entries (9)
    # in this ordered list than ideograms (8)
    # chromosomes_order = ^,-,hs5,hs2,|,hs4,-,-,-,hs3,|,hs7,$
    
    <<include etc/housekeeping.conf>>
    

  

* * *

### bands.conf

    
    
    show_bands            = yes
    fill_bands            = yes
    band_stroke_thickness = 2
    band_stroke_color     = white
    band_transparency     = 4
    

  

* * *

### ideogram.conf

    
    
    <ideogram>
    
    <spacing>
    
    default = 0.0025r
    break   = 0.5r
    
    </spacing>
    
    <<include ideogram.position.conf>>
    <<include ideogram.label.conf>>
    <<include bands.conf>>
    
    </ideogram>
    
    

  

* * *

### ideogram.label.conf

    
    
    show_label       = yes
    label_font       = bold
    # labels outside circle
    #label_radius     = dims(ideogram,radius) + 0.05r
    #labels inside circle
    label_radius     = dims(ideogram,radius) - 0.15r
    label_with_tag   = yes
    label_size       = 48
    label_parallel   = yes
    label_case       = upper
    

  

* * *

### ideogram.position.conf

    
    
    radius           = 0.90r
    thickness        = 100p
    fill             = yes
    fill_color       = black
    stroke_thickness = 2
    stroke_color     = black
    

  

* * *

### ticks.conf

    
    
    show_ticks          = yes
    show_tick_labels    = yes
    
    <ticks>
    skip_first_label = no
    skip_last_label  = no
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
    

  

* * *

