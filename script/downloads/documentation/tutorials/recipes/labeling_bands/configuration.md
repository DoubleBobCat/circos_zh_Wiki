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

## 3\. Labeling Karyotype Bands

[Lesson](/documentation/tutorials/recipes/labeling_bands/lesson)
[Images](/documentation/tutorials/recipes/labeling_bands/images)
[Configuration](/documentation/tutorials/recipes/labeling_bands/configuration)

### circos.conf

    
    
    <<include etc/colors_fonts_patterns.conf>>
    
    <<include ideogram.conf>>
    <<include ticks.conf>>
    
    karyotype = data/karyotype/karyotype.human.txt
    
    <image>
    <<include etc/image.conf>>
    </image>
    
    chromosomes_units = 1000000
    chromosomes       = /hs([1-9]|10)$/
    chromosomes_display_default = no
    
    <plots>
    
    <plot>
    type  = text
    color = red
    file  = data/8/text.bands.txt
    
    r0    = 1r
    r1    = 1r+300p
    
    label_size = 12
    label_font = condensed
    
    show_links     = yes
    link_dims      = 0p,2p,6p,2p,5p
    link_thickness = 2p
    link_color     = black
    
    label_snuggle        = yes
    max_snuggle_distance = 1r
    snuggle_tolerance    = 0.25r
    snuggle_sampling     = 2
    snuggle_refine       = yes
    
    <rules>
    <rule>
    condition  = on(hs1)
    color      = blue
    flow       = continue
    </rule>
    
    <rule>
    condition  = var(start) > 50mb && var(end) < 100mb
    color      = green
    flow       = continue
    </rule>
    
    <rule>
    condition  = var(value) =~ /[.]\d\d/
    color      = grey
    </rule>
    </rules>
    
    </plot>
    
    </plots>
    
    <<include etc/housekeeping.conf>>
    

  

* * *

### ideogram.conf

    
    
    <ideogram>
    
    <spacing>
    
    default = 5u
    break   = 1u
    
    axis_break_at_edge = yes
    axis_break         = yes
    axis_break_style   = 2
    
    <break_style 1>
    stroke_color = black
    fill_color   = blue
    thickness    = 0.25r
    stroke_thickness = 2
    </break>
    
    <break_style 2>
    stroke_color     = black
    stroke_thickness = 3
    thickness        = 1.5r
    </break>
    
    </spacing>
    
    # thickness (px) of chromosome ideogram
    thickness        = 30p
    stroke_thickness = 2
    # ideogram border color
    stroke_color     = black
    fill             = yes
    # the default chromosome color is set here and any value
    # defined in the karyotype file overrides it
    fill_color       = black
    
    # fractional radius position of chromosome ideogram within image
    radius         = 0.85r
    show_label     = yes
    label_with_tag = yes
    label_font     = default
    label_radius   = dims(ideogram,radius) + 175p
    label_size     = 30p
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
    
    

  

* * *

### ticks.conf

    
    
    show_ticks          = yes
    show_tick_labels    = yes
    
    <ticks>
    
    radius               = dims(ideogram,radius_outer)+120p
    multiplier           = 1e-6
    
    <tick>
    spacing        = 0.5u
    size           = 3p
    thickness      = 1p
    color          = black
    show_label     = no
    label_size     = 16p
    label_offset   = 0p
    format         = %d
    </tick>
    
    <tick>
    spacing        = 5u
    size           = 5p
    thickness      = 2p
    color          = black
    show_label     = no
    label_size     = 16p
    label_offset   = 0p
    format         = %d
    </tick>
    <tick>
    spacing        = 10u
    size           = 8p
    thickness      = 2p
    color          = black
    show_label     = yes
    label_size     = 12p
    label_offset   = 5p
    format         = %d
    </tick>
    
    </ticks>
    

  

* * *

