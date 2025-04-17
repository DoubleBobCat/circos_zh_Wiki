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

## 14\. Directed Links

[Lesson](/documentation/tutorials/recipes/directed_links/lesson)
[Images](/documentation/tutorials/recipes/directed_links/images)
[Configuration](/documentation/tutorials/recipes/directed_links/configuration)

### circos.conf

    
    
    <colors>
    <<include etc/colors.conf>>
    </colors>
    
    <fonts>
    <<include etc/fonts.conf>>
    </fonts>
    
    <<include ideogram.conf>>
    <<include ticks.conf>>
    
    karyotype = karyotype.human.hg18.txt
    
    <image>
    dir   = .
    file  = links-directed.png
    24bit = yes
    radius         = 1500p
    background     = white
    angle_offset   = -90
    auto_alpha_colors = yes
    auto_alpha_steps  = 5
    </image>
    
    chromosomes_units           = 1e6
    chromosomes_display_default = yes
    chromosomes = hs3:101-121
    chromosomes_scale = hs3:50
    
    <plots>
    <plot>
    type = scatter
    glyph = triangle
    glyph_size = 24p
    file = linkends.txt
    min = 0
    max = 1
    r0 = 0.99r
    r1 = 0.99r
    fill_color=black
    <rules>
    <rule>
    importance = 100
    condition  = 1
    fill_color = eval("chr".substr(_CHR_,2))
    </rule>
    </rules>
    </plot>
    </plots>
    
    <links>
    <link testlinks>
    file          = links.txt
    thickness     = 2
    bezier_radius = 0r
    radius        = 0.995r
    crest         = 0.25
    color         = black_a2
    </link>
    </links>
    
    anglestep       = 0.5
    minslicestep    = 10
    beziersamples   = 120
    debug           = no
    warnings        = no
    imagemap        = no
    
    units_ok = bupr
    units_nounit = n
    
    #debug_group = ticks
    

  

* * *

### ideogram.conf

    
    
    <ideogram>
    
    <spacing>
    
    default = 5u
    
    </spacing>
    
    # thickness (px) of chromosome ideogram
    thickness        = 20p
    stroke_thickness = 2
    # ideogram border color
    stroke_color     = black
    fill             = yes
    # the default chromosome color is set here and any value
    # defined in the karyotype file overrides it
    fill_color       = black
    
    # fractional radius position of chromosome ideogram within image
    radius         = 0.85r
    show_label     = no
    label_font     = condensedbold
    label_radius   = dims(ideogram,radius) + 0.10r
    label_size     = 36
    label_parallel = no
    
    # cytogenetic bands
    band_stroke_thickness = 2
    
    # show_bands determines whether the outline of cytogenetic bands
    # will be seen
    show_bands            = no
    # in order to fill the bands with the color defined in the karyotype
    # file you must set fill_bands
    fill_bands            = no
    
    band_transparency     = 1
    
    </ideogram>
    
    

  

* * *

### ticks.conf

    
    
    show_ticks          = yes
    show_tick_labels    = yes
    
    grid_start         = dims(ideogram,radius_inner)-0.5r
    grid_end           = dims(ideogram,radius_outer)+100
    
    <ticks>
    skip_first_label     = no
    skip_last_label      = no
    radius               = dims(ideogram,radius_outer)
    tick_separation      = 5p
    min_label_distance_to_edge = 0p
    label_separation = 5p
    label_offset     = 5p
    label_size = 8p
    multiplier = 1e-6
    color = black
    
    <tick>
    spacing        = 5u
    size           = 8p
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
    <tick>
    #chromosomes_display_default=no
    #chromosomes    = hs3
    spacing        = 1u
    size           = 8p
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
    <tick>
    spacing        = 25u
    size           = 12p
    thickness      = 2p
    color          = black
    show_label     = yes
    label_size     = 24p
    label_offset   = 0p
    format         = %d
    grid           = yes
    grid_color     = dgrey
    grid_thickness = 1p
    </tick>
    </ticks>
    

  

* * *

