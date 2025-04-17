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

# 7 — 2D Data Tracks

## 10\. Glyphs — Part II

[Lesson](/documentation/tutorials/2d_tracks/glyphs_2/lesson)
[Images](/documentation/tutorials/2d_tracks/glyphs_2/images)
[Configuration](/documentation/tutorials/2d_tracks/glyphs_2/configuration)

### circos.conf

    
    
    <<include colors_fonts_patterns.conf>>
    
    <<include ideogram.conf>>
    <<include ticks.conf>>
    
    <image>
    <<include etc/image.conf>>
    </image>
    
    karyotype = data/karyotype/karyotype.human.txt
    
    chromosomes_units           = 1000000
    chromosomes_display_default = yes
    chromosomes                 = -/hs/;/hs[1-9]$/
    
    <plots>
    
    # glyph character mappings
    #
    # small
    # | medium
    # | | large
    # | | |
    # a b c   square
    # d e f   rhombus
    # g h i   triangle up
    # j k l   triangle down
    # m n o   circle
    #
    # lower case - hollow
    # upper case - solid
    
    type       = text
    label_font = glyph
    label_size = 20
    padding    = -0.2r
    rpadding   = -0.2r
    
    <plot>
    file       = data/6/genes.glyph.txt
    r0         = 0.4r
    r1         = 0.99r
    
    <rules>
    
    flow = continue
    
    <rule>
    condition  = var(value) =~ /cancer/
    color      = red
    </rule>
    
    <rule>
    condition  = var(value) =~ /omim/
    color      = green
    </rule>
    
    <rule>
    condition  = var(value) =~ /other/
    color      = blue
    </rule>
    
    <rule>
    condition  = 1
    value      = N
    </rule>
    
    </rules>
    
    </plot>
    
    </plots>
    
    <<include etc/housekeeping.conf>>
    

  

* * *

### bands.conf

    
    
    show_bands            = yes
    fill_bands            = yes
    band_stroke_thickness = 2
    band_stroke_color     = white
    band_transparency     = 0
    

  

* * *

### ideogram.conf

    
    
    <ideogram>
    
    <spacing>
    default = 0.01r
    break   = 0.5r
    </spacing>
    
    <<include ideogram.position.conf>>
    <<include ideogram.label.conf>>
    <<include bands.conf>>
    
    radius*       = 0.825r
    
    </ideogram>
    
    

  

* * *

### ideogram.label.conf

    
    
    show_label       = yes
    label_font       = default
    label_radius     = dims(image,radius)-30p
    label_size       = 24
    label_parallel   = yes
    label_case       = lower
    label_format     = eval(sprintf("chr%s",var(label)))
    
    

  

* * *

### ideogram.position.conf

    
    
    radius           = 0.775r
    thickness        = 30p
    fill             = yes
    fill_color       = black
    stroke_thickness = 2
    stroke_color     = black
    

  

* * *

### ticks.conf

    
    
    show_ticks          = no
    show_tick_labels    = no
    
    show_grid = no
    grid_start         = dims(ideogram,radius_inner)-0.5r
    grid_end           = dims(ideogram,radius_inner)
    
    <ticks>
    skip_first_label     = no
    skip_last_label      = no
    radius               = dims(ideogram,radius_outer)
    tick_separation      = 2p
    min_label_distance_to_edge = 0p
    label_separation = 5p
    label_offset     = 2p
    label_size = 8p
    multiplier = 1e-6
    color = black
    
    #<tick>
    #hide = yes
    #spacing        = 0.01u
    #size           = 3p
    #thickness      = 2p
    #color          = black
    #show_label     = no
    #label_size     = 12p
    #label_offset   = 0p
    #format         = %.2f
    #grid           = no
    #grid_color     = lblue
    #grid_thickness = 1p
    #</tick>
    #<tick>
    #spacing        = 0.1u
    #size           = 5p
    #thickness      = 2p
    #color          = black
    #show_label     = yes
    #label_size     = 12p
    #label_offset   = 0p
    #format         = %.1f
    #grid           = yes
    #grid_color     = lgrey
    #grid_thickness = 1p
    #</tick>
    <tick>
    spacing        = 1u
    size           = 8p
    thickness      = 2p
    color          = black
    show_label     = no
    label_size     = 16p
    label_offset   = 0p
    format         = %.1f
    grid           = yes
    grid_color     = grey
    grid_thickness = 1p
    </tick>
    <tick>
    spacing        = 5u
    size           = 10p
    thickness      = 2p
    color          = black
    show_label     = yes
    label_size     = 24p
    label_offset   = 0p
    format         = %d
    grid           = yes
    grid_color     = grey
    grid_thickness = 1p
    </tick>
    </ticks>
    

  

* * *

