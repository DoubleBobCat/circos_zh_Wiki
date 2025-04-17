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

## 15\. Pattern Fills

[Lesson](/documentation/tutorials/recipes/pattern_fills/lesson)
[Images](/documentation/tutorials/recipes/pattern_fills/images)
[Configuration](/documentation/tutorials/recipes/pattern_fills/configuration)

### circos.conf

    
    
    <colors>
    <<include etc/colors.conf>>
    </colors>
    
    <fonts>
    <<include etc/fonts.conf>>
    </fonts>
    
    <patterns>
    <<include etc/pattern.conf>>
    </patterns>
    
    <<include ideogram.conf>>
    <<include ticks.conf>>
    
    karyotype = data/karyotype/karyotype.human.hg18.txt
    
    <image>
    <<include etc/image.conf>>
    </image>
    
    chromosomes_units           = 1000000
    chromosomes_display_default = yes
    
    <highlights>
    <highlight>
    file        = data/3/chr.highlights.txt
    r0 = 0.99r
    r1 = 0.995r
    </highlight>
    </highlights>
    
    <links>
    <link linkexample>
    
    file   = data/8/15/tmp.1
    ribbon = yes
    flat   = yes
    radius        = 0.95r
    bezier_radius = 0r
    crest         = 0.2
    
    color      = black
    
    <rules>
    <rule>
    importance = 100
    condition  = rand() < 0.5
    pattern    = eval((qw(hline vline checker dot))[rand(4)])
    color      = eval((qw(red orange yellow green blue purple))[rand(6)])
    z          = 10
    </rule>
    </rules>
    </link>
    
    </links>
    
    <<include etc/housekeeping.conf>>
    
    

  

* * *

### ideogram.conf

    
    
    <ideogram>
    
    <spacing>
    
    default = 10u
    
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
    show_label     = yes
    label_font     = condensedbold
    label_radius   = dims(ideogram,radius) + 0.05r
    label_size     = 36
    label_parallel = no
    
    # cytogenetic bands
    band_stroke_thickness = 2
    
    # show_bands determines whether the outline of cytogenetic bands
    # will be seen
    show_bands            = yes
    # in order to fill the bands with the color defined in the karyotype
    # file you must set fill_bands
    fill_bands            = yes
    
    band_transparency     = 0
    
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
    tick_separation      = 2p
    min_label_distance_to_edge = 0p
    label_separation = 5p
    label_offset     = 2p
    label_size = 8p
    multiplier = 1e-6
    color = black
    
    <tick>
    spacing        = 5u
    size           = 5p
    thickness      = 2p
    color          = black
    show_label     = no
    label_size     = 8p
    label_offset   = 0p
    format         = %d
    grid           = yes
    grid_color     = grey
    grid_thickness = 1p
    </tick>
    <tick>
    spacing        = 10u
    size           = 8p
    thickness      = 2p
    color          = black
    show_label     = yes
    label_size     = 12p
    label_offset   = 0p
    format         = %d
    grid           = yes
    grid_color     = dgrey
    grid_thickness = 1p
    </tick>
    </ticks>
    

  

* * *

