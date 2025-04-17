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

# 9 — Recipes

## 23\. Naming Names

[Lesson](/documentation/tutorials/recipes/naming_names/lesson)
[Images](/documentation/tutorials/recipes/naming_names/images)
[Configuration](/documentation/tutorials/recipes/naming_names/configuration)

### circos.conf

    
    
    <<include etc/colors_fonts_patterns.conf>>
    
    <colors>
    rep = 211,121,111
    dem = 85,143,190
    </colors>
    
    <<include ideogram.conf>>
    <<include ticks.conf>>
    
    <image>
    <<include etc/image.conf>>
    </image>
    
    chromosomes_units           = 1
    chromosomes_display_default = yes
    
    karyotype = karyotype.txt
    
    <links>
    <link>
    file      = links.txt
    radius    = dims(ideogram,radius_inner)
    bezier_radius = 0r
    thickness = 5
    color     = rep # make it republican, by default
    <rules>
    <rule>
    # set dem color if start is on a democrat
    condition = var(chr1) =~ /obama|richardson|clinton/
    color     = dem
    </rule>
    </rules>
    </link>
    
    </links>
    
    <plots>
    
    <plot>
    file  = slices.txt
    type  = highlight
    r0    = dims(ideogram,radius_inner)
    r1    = dims(ideogram,radius_outer)
    fill_color       = undef
    stroke_color     = white
    stroke_thickness = 5
    </plot>
    
    <plot>
    z    = 10
    type = highlight
    file = axis.txt
    r0   = dims(ideogram,radius_outer) - 2p
    r1   = dims(ideogram,radius_outer) + 3p
    fill_color = black
    </plot>
    </plots>
    
    <<include etc/housekeeping.conf>>
    track_defaults* = undef
    

  

* * *

### ideogram.conf

    
    
    <ideogram>
    
    <spacing>
    
    default = 0.01r
    
    </spacing>
    
    <<include ideogram.position.conf>>
    <<include ideogram.label.conf>>
    
    </ideogram>
    
    

  

* * *

### ideogram.label.conf

    
    
    show_label       = yes
    label_font       = default
    label_radius     = dims(image,radius)-70p
    label_with_tag   = yes
    label_size       = 40
    label_parallel   = yes
    label_case       = upper
    

  

* * *

### ideogram.position.conf

    
    
    radius           = 0.90r
    thickness        = 150p
    fill             = yes
    

  

* * *

### ticks.conf

    
    
    show_ticks          = yes
    show_tick_labels    = yes
    
    <ticks>
    radius           = dims(ideogram,radius_outer)
    multiplier       = 1
    color            = black
    thickness        = 4p
    size             = 20p
    
    <tick>
    spacing        = 100u
    </tick>
    
    </ticks>
    

  

* * *

