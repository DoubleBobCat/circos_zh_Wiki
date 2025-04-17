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

## 5\. Image Transparency and Background

[Lesson](/documentation/tutorials/recipes/transparency_background/lesson)
[Images](/documentation/tutorials/recipes/transparency_background/images)
[Configuration](/documentation/tutorials/recipes/transparency_background/configuration)

### circos.conf

    
    
    <colors>
    <<include etc/colors.conf>>
    </colors>
    
    <fonts>
    <<include etc/fonts.conf>>
    </fonts>
    
    <<include ideogram.conf>>
    <<include ticks.conf>>
    
    karyotype = data/8/karyotype.microbe.txt
    
    <image>
    dir = /tmp
    file  = circos-tutorial.png
    # radius of inscribed circle in image
    radius         = 1500p
    # specify a color or image
    # to make the background transparent, use "transparent"
    background     = data/8/background.png
    # by default angle=0 is at 3 o'clock position
    angle_offset   = -90
    </image>
    
    chromosomes_units = 1000
    chromosomes_display_default = yes
    
    <highlights>
    
    <highlight>
    file = data/8/microbe.highlights.1.txt
    r0 = 0.95r
    r1 = 0.98r
    </highlight>
    
    <highlight>
    file = data/8/microbe.highlights.13.txt
    r0 = 0.91r
    r1 = 0.94r
    </highlight>
    
    <highlight>
    file = data/8/microbe.highlights.14.txt
    r0 = 0.86r
    r1 = 0.90r
    </highlight>
    
    <highlight>
    file = data/8/microbe.highlights.2.txt
    r0 = 0.82r
    r1 = 0.85r
    </highlight>
    
    <highlight>
    file = data/8/microbe.highlights.4.txt
    r0 = 0.53r
    r1 = 0.54r
    </highlight>
    <highlight>
    file = data/8/microbe.highlights.5.txt
    r0 = 0.51r
    r1 = 0.52r
    </highlight>
    
    <highlight>
    file = data/8/microbe.highlights.6.txt
    r0 = 0.46r
    r1 = 0.47r
    </highlight>
    <highlight>
    file = data/8/microbe.highlights.7.txt
    r0 = 0.48r
    r1 = 0.49r
    </highlight>
    
    <highlight>
    file = data/8/microbe.highlights.8.txt
    r0 = 0.41r
    r1 = 0.42r
    </highlight>
    <highlight>
    file = data/8/microbe.highlights.9.txt
    r0 = 0.43r
    r1 = 0.44r
    </highlight>
    <highlight>
    file = data/8/microbe.highlights.10.txt
    r0 = 0.19r
    r1 = 0.20r
    </highlight>
    <highlight>
    file = data/8/microbe.highlights.19.txt
    r0 = 0.21r
    r1 = 0.22r
    </highlight>
    <highlight>
    file = data/8/microbe.highlights.20.txt
    r0 = 0.23r
    r1 = 0.24r
    </highlight>
    <highlight>
    file = data/8/microbe.highlights.21.txt
    r0 = 0.25r
    r1 = 0.265r
    </highlight>
    <highlight>
    file = data/8/microbe.highlights.22.txt
    r0 = 0.275r
    r1 = 0.29r
    </highlight>
    <highlight>
    file = data/8/microbe.highlights.23.txt
    r0 = 0.30r
    r1 = 0.32r
    </highlight>
    <highlight>
    file = data/8/microbe.highlights.24.txt
    r0 = 0.33r
    r1 = 0.355r
    </highlight>
    <highlight>
    file = data/8/microbe.highlights.25.txt
    r0 = 0.365r
    r1 = 0.395r
    </highlight>
    <highlight>
    file = data/8/microbe.highlights.11.txt
    r0 = 0.17r
    r1 = 0.18r
    </highlight>
    <highlight>
    file = data/8/microbe.highlights.12.txt
    r0 = 0.15r
    r1 = 0.16r
    </highlight>
    
    <highlight>
    file = data/8/microbe.highlights.15.txt
    r0 = 0.72r
    r1 = 0.78r
    </highlight>
    
    <highlight>
    file = data/8/microbe.highlights.16.txt
    r0 = 0.56r
    r1 = 0.60r
    </highlight>
    
    <highlight>
    file = data/8/microbe.highlights.17.txt
    r0 = 0.615r
    r1 = 0.635r
    </highlight>
    
    <highlight>
    file = data/8/microbe.highlights.18.txt
    r0 = 0.65r
    r1 = 0.69r
    </highlight>
    <highlight>
    file = data/8/microbe.highlights.26.txt
    r0 = 0.65r
    r1 = 0.69r
    </highlight>
    
    <highlight>
    file = data/8/microbe.separator.txt
    r0 = 0.80r
    r1 = 0.805r
    fill_color = vvlgrey
    </highlight>
    <highlight>
    file = data/8/microbe.separator.txt
    r0 = 0.70r
    r1 = 0.705r
    fill_color = vvlgrey
    </highlight>
    <highlight>
    file = data/8/microbe.separator.txt
    r0 = 0.55r
    r1 = 0.555r
    fill_color = vvlgrey
    </highlight>
    <highlight>
    file = data/8/microbe.separator.txt
    r0 = 0.50r
    r1 = 0.505r
    fill_color = vvlgrey
    </highlight>
    <highlight>
    file = data/8/microbe.separator.txt
    r0 = 0.45r
    r1 = 0.455r
    fill_color = vvlgrey
    </highlight>
    <highlight>
    file = data/8/microbe.separator.txt
    r0 = 0.40r
    r1 = 0.405r
    fill_color = vvlgrey
    </highlight>
    </highlights>
    
    anglestep       = 0.5
    minslicestep    = 10
    beziersamples   = 40
    debug           = no
    warnings        = no
    imagemap        = no
    
    # don't touch!
    units_ok        = bupr
    units_nounit    = n
    
    

  

* * *

### ideogram.conf

    
    
    <ideogram>
    
    <spacing>
    
    default = 0u
    break   = 0u
    
    #<pairwise a;b>
    #spacing = 5u
    #</pairwise>
    
    #<pairwise b;c>
    #spacing = 10u
    #</pairwise>
    
    #<pairwise c;d>
    #spacing = 20u
    #</pairwise>
    
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
    label_radius   = dims(ideogram,radius) + 0.05r
    label_size     = 36
    
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
    
    show_grid = no
    grid_start         = dims(ideogram,radius_inner)-0.5r
    grid_end           = dims(ideogram,radius_inner)
    
    <ticks>
    skip_first_label     = yes
    skip_last_label      = no
    radius               = dims(ideogram,radius_outer)
    tick_separation      = 2p
    min_label_distance_to_edge = 0p
    label_separation = 5p
    label_offset     = 2p
    label_size = 8p
    multiplier = 0.001
    color = black
    
    <tick>
    spacing        = 1u
    size           = 3p
    thickness      = 2p
    color          = black
    show_label     = no
    label_size     = 12p
    label_offset   = 0p
    format         = %.2f
    grid           = no
    grid_color     = lblue
    grid_thickness = 1p
    </tick>
    <tick>
    spacing        = 5u
    size           = 5p
    thickness      = 1p
    color          = black
    show_label     = yes
    label_size     = 16p
    label_offset   = 0p
    format         = %s
    grid           = yes
    grid_color     = lgrey
    grid_thickness = 1p
    </tick>
    <tick>
    spacing        = 10u
    size           = 8p
    thickness      = 2p
    color          = black
    show_label     = yes
    label_size     = 16p
    label_offset   = 0p
    format         = %s
    grid           = yes
    grid_color     = grey
    grid_thickness = 1p
    </tick>
    <tick>
    spacing        = 100u
    size           = 8p
    thickness      = 2p
    color          = black
    show_label     = yes
    suffix = " kb"
    label_size     = 36p
    label_offset   = 5p
    format         = %s
    grid           = yes
    grid_color     = dgrey
    grid_thickness = 1p
    </tick>
    </ticks>
    

  

* * *

