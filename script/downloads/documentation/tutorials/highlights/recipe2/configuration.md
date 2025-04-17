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

# 4 — Highlights

## 7\. Recipe 2 - Focusing on a Genome Region

[Lesson](/documentation/tutorials/highlights/recipe2/lesson)
[Images](/documentation/tutorials/highlights/recipe2/images)
[Configuration](/documentation/tutorials/highlights/recipe2/configuration)

### circos.conf

    
    
    <colors>
    <<include etc/colors.conf>>
    </colors>
    
    <fonts>
    <<include etc/fonts.conf>>
    </fonts>
    
    <<include ideogram.conf>>
    <<include ticks.conf>>
    
    karyotype   = data/karyotype.human.txt
    
    <image>
    dir = /tmp
    file  = circos-tutorial.png
    # radius of inscribed circle in image
    radius         = 1500p
    background     = white
    # by default angle=0 is at 3 o'clock position
    angle_offset   = -90
    </image>
    
    chromosomes_units           = 1000000
    
    # first image
    #chromosomes                 = hs1;hs2;hs3
    #chromosomes_breaks          = -hs1:120-145;-hs1:180-200
    #chromosomes_display_default = no
    
    # second image
    chromosomes = hs1;hs2;hs3;hs13;hs14;hs15
    
    <highlights>
    
    z          = 5
    
    # For the first image, the same highlight set is
    # drawn both inside and outside the ideogram
    # circle. Another highlight set is layered
    # on top of the outer highlight set.
    
    #<highlight>
    #file       = data/3/chr.highlights.txt
    #r0 = 0.5r
    #r1 = 1r
    #</highlight>
    
    #<highlight>
    #file       = data/3/chr.highlights.txt
    #stroke_thickness = 2
    #stroke_color = black
    #r0 = 1.1r
    #r1 = 1.15r
    #</highlight>
    
    #<highlight>
    #file       = data/3/chr.hetero.highlights.txt
    #stroke_thickness = 2
    #stroke_color = black
    #fill_color = white
    #r0 = 1.1r
    #r1 = 1.15r
    #z = 10
    #</highlight>
    
    # In the second image, selected regions of the
    # genome are singled out using several highlights.
    # Note that highlights do not radially cross the
    # ideograms. Highlights with r0 < 1 < r1 are not
    # supported (Circos will not always behave well in
    # these cases).
    
    <highlight>
    file       = data/3/highlights.few.txt
    r0 = 0.5r
    r1 = 1r
    fill_color = lgrey
    </highlight>
    
    <highlight>
    file       = data/3/highlights.few.txt
    r0 = 1r
    r1 = 1.10r
    fill_color = lyellow
    </highlight>
    
    <highlight>
    file       = data/3/highlights.few.txt
    r0 = 1.10r
    r1 = 1.15r
    fill_color = lgrey
    </highlight>
    
    </highlights>
    
    anglestep       = 0.025
    minslicestep    = 5
    beziersamples   = 40
    debug           = no
    warnings        = no
    imagemap        = no
    
    units_ok = bupr
    units_nounit = n
    

  

* * *

### ideogram.conf

    
    
    <ideogram>
    
    <spacing>
    
    default = 3u
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
    thickness        = 100p
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
    label_font     = condensedbold
    label_radius   = dims(ideogram,radius) + 0.05r
    label_size     = 48
    
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
    
    show_grid          = yes
    grid_start         = 0.5r
    grid_end           = 1.0r
    
    <ticks>
    skip_first_label     = no
    skip_last_label      = no
    radius               = dims(ideogram,radius_outer)
    tick_separation      = 2p
    min_label_distance_to_edge = 10p
    label_separation = 5p
    label_offset     = 2p
    label_size = 8p
    multiplier = 1e-6
    color = black
    
    <tick>
    spacing        = 1u
    size           = 6p
    thickness      = 1p
    color          = black
    show_label     = no
    label_size     = 16p
    label_offset   = 0p
    format         = %.2f
    grid           = no
    grid_color     = grey
    grid_thickness = 1p
    </tick>
    <tick>
    spacing        = 5u
    size           = 10p
    thickness      = 1p
    color          = black
    show_label     = yes
    label_size     = 16p
    label_offset   = 0p
    format         = %d
    grid           = yes
    grid_color     = grey
    grid_thickness = 2p
    </tick>
    <tick>
    spacing        = 10u
    size           = 16p
    thickness      = 2p
    color          = black
    show_label     = yes
    label_size     = 16p
    label_offset   = 0p
    format         = %d
    grid           = yes
    grid_color     = vdgrey
    grid_thickness = 2p
    </tick>
    </ticks>
    

  

* * *

