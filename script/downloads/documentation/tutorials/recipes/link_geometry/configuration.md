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

## 2\. Link Geometry - Detailed Bezier Control

[Lesson](/documentation/tutorials/recipes/link_geometry/lesson)
[Images](/documentation/tutorials/recipes/link_geometry/images)
[Configuration](/documentation/tutorials/recipes/link_geometry/configuration)

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
    
    chromosomes_units = 1000000
    chromosomes       = hs1;hs2;hs3;hs4
    chromosomes_display_default = no
    
    <links>
    
    radius = 0.98r
    
    crest         = 2.5
    bezier_radius = 0.5r
    
    <link segdup>
    show         = yes
    color        = grey
    thickness    = 2p
    file         = data/5/segdup.txt
    
    <rules>
    <rule>
    importance = 110
    condition  = _CHR1_ eq _CHR2_ 
    show       = no
    </rule>
    # the next two rules must contain flow=continue because it 
    # always matches and you do not want it to terminate
    # the rule chain (otherwise the color rule would
    # never be checked)
    <rule>
    importance = 100
    condition  = 1
    thickness  = eval(max(1,min(6,exp(_SIZE1_/50000))))
    flow       = continue
    </rule>
    
    <rule>
    importance = 90
    condition  = (_CHR1_ eq "hs2" && _CHR2_ eq "hs4" && abs(_START1_ - 90Mb) < 30Mb) || (_CHR2_ eq "hs2" && _CHR1_ eq "hs4" && abs(_START2_ - 100Mb) < 20Mb)
    color      = red
    thickness  = eval(_thickness_*2)
    z          = 5
    
    crest         = 2
    bezier_radius = 0.5r
    
    </rule>
    
    <rule>
    importance = 90
    condition  = (_CHR1_ eq "hs1" && _CHR2_ eq "hs3" && abs(_START1_ - 160Mb) < 20Mb) || (_CHR2_ eq "hs1" && _CHR1_ eq "hs3" && abs(_START2_ - 160Mb) < 20Mb)
    color      = blue
    thickness  = eval(_thickness_*2)
    z          = 10
    crest         = 4
    bezier_radius = 0.75r
    
    </rule>
    
    <rule>
    importance = 90
    condition  = (_CHR1_ eq "hs1" && _CHR2_ eq "hs2" && abs(_START1_ - 10Mb) < 20Mb) || (_CHR2_ eq "hs1" && _CHR1_ eq "hs2" && abs(_START2_ - 10Mb) < 20Mb)
    color      = orange
    thickness  = eval(_thickness_*2)
    z          = 15
    crest         = 5
    bezier_radius = 0.8r
    
    </rule>
    
    </rules>
    
    </link>
    
    </links>
    
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

### circos.image-01.conf

    
    
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
    
    chromosomes_units = 1000000
    chromosomes       = hs1;hs2;hs3;hs4
    chromosomes_display_default = no
    
    <links>
    
    radius = 0.98r
    #crest  = 0.25
    #bezier_radius        = 0.9r
    #bezier_radius_purity = 0.5
    
    <link segdup>
    show         = yes
    color        = vdgrey
    thickness    = 2p
    file         = data/5/segdup.txt
    #record_limit = 500
    
    <rules>
    <rule>
    importance = 110
    condition  = _SIZE1_ < 1.5kb || _SIZE2_ < 1.5kb
    show       = no
    </rule>
    # the next rule must contain flow=continue because it 
    # always matches and you do not want it to terminate
    # the rule chain (otherwise the next color rule would
    # never be checked)
    <rule>
    importance = 100
    condition  = 1
    thickness  = eval(max(1,min(6,exp(_SIZE1_/50000))))
    flow       = continue
    </rule>
    <rule>
    importance = 90
    condition  = (_CHR1_ eq "hs2" && abs(_START1_ - 100Mb) < 20Mb) || (_CHR2_ eq "hs2" && abs(_START2_ - 100Mb) < 20Mb)
    color      = red
    </rule>
    </rules>
    
    </link>
    
    </links>
    
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

### circos.image-02.conf

    
    
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
    
    chromosomes_units = 1000000
    chromosomes       = hs1;hs2;hs3;hs4
    chromosomes_display_default = no
    
    <links>
    
    radius = 0.98r
    
    #bezier_radius         = 0r
    #bezier_radius         = 0.25r
    bezier_radius         = 0.5r
    #bezier_radius         = 0.75r
    
    <link segdup>
    show         = yes
    color        = vdgrey
    thickness    = 2p
    file         = data/5/segdup.txt
    
    <rules>
    <rule>
    importance = 110
    condition  = _SIZE1_ < 1.5kb || _SIZE2_ < 1.5kb
    show       = no
    </rule>
    # the next rule must contain flow=continue because it 
    # always matches and you do not want it to terminate
    # the rule chain (otherwise the next color rule would
    # never be checked)
    <rule>
    importance = 100
    condition  = 1
    thickness  = eval(max(1,min(6,exp(_SIZE1_/50000))))
    flow       = continue
    </rule>
    <rule>
    importance = 90
    condition  = (_CHR1_ eq "hs2" && abs(_START1_ - 100Mb) < 20Mb) || (_CHR2_ eq "hs2" && abs(_START2_ - 100Mb) < 20Mb)
    color      = red
    </rule>
    </rules>
    
    </link>
    
    </links>
    
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

### circos.image-03.conf

    
    
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
    
    chromosomes_units = 1000000
    chromosomes       = hs1;hs2;hs3;hs4
    chromosomes_display_default = no
    
    <links>
    
    radius = 0.98r
    
    bezier_radius         = 0.5r
    
    <link segdup>
    show         = yes
    color        = vdgrey
    thickness    = 2p
    file         = data/5/segdup.txt
    
    <rules>
    <rule>
    importance = 110
    condition  = _SIZE1_ < 1.5kb || _SIZE2_ < 1.5kb
    show       = no
    </rule>
    # the next two rules must contain flow=continue because it 
    # always matches and you do not want it to terminate
    # the rule chain (otherwise the color rule would
    # never be checked)
    <rule>
    importance = 100
    condition  = 1
    thickness  = eval(max(1,min(6,exp(_SIZE1_/50000))))
    flow       = continue
    </rule>
    
    <rule>
    importance = 95
    condition  = _CHR1_ eq _CHR2_ && abs(_START1_-_START2_) < 100Mb
    #bezier_radius = 0.75r
    bezier_radius = eval( (0.5 + 0.4*(1-abs(_START1_-_START2_) / 100Mb)) . "r")
    flow = continue
    </rule>
    
    <rule>
    importance = 90
    condition  = (_CHR1_ eq "hs2" && abs(_START1_ - 100Mb) < 20Mb) || (_CHR2_ eq "hs2" && abs(_START2_ - 100Mb) < 20Mb)
    color      = red
    </rule>
    </rules>
    
    </link>
    
    </links>
    
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

### circos.image-04.conf

    
    
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
    
    chromosomes_units = 1000000
    chromosomes       = hs1;hs2;hs3;hs4
    chromosomes_display_default = no
    
    <links>
    
    radius = 0.98r
    
    crest = 2.5
    bezier_radius         = 0.5r
    
    <link segdup>
    show         = yes
    color        = vdgrey
    thickness    = 2p
    file         = data/5/segdup.txt
    
    <rules>
    <rule>
    importance = 110
    condition  = _SIZE1_ < 1.5kb || _SIZE2_ < 1.5kb
    show       = no
    </rule>
    # the next two rules must contain flow=continue because it 
    # always matches and you do not want it to terminate
    # the rule chain (otherwise the color rule would
    # never be checked)
    <rule>
    importance = 100
    condition  = 1
    thickness  = eval(max(1,min(6,exp(_SIZE1_/50000))))
    flow       = continue
    </rule>
    
    <rule>
    importance = 95
    condition  = _CHR1_ eq _CHR2_ && abs(_START1_-_START2_) < 100Mb
    #bezier_radius = 0.75r
    bezier_radius = eval( (0.5 + 0.4*(1-abs(_START1_-_START2_) / 100Mb)) . "r")
    flow = continue
    </rule>
    
    <rule>
    importance = 90
    condition  = (_CHR1_ eq "hs2" && abs(_START1_ - 100Mb) < 20Mb) || (_CHR2_ eq "hs2" && abs(_START2_ - 100Mb) < 20Mb)
    color      = red
    </rule>
    </rules>
    
    </link>
    
    </links>
    
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

### circos.image-05.conf

    
    
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
    
    chromosomes_units = 1000000
    chromosomes       = hs1;hs2;hs3;hs4
    chromosomes_display_default = no
    
    <links>
    
    radius = 0.98r
    
    <link segdup>
    show         = yes
    color        = vdgrey
    thickness    = 2p
    file         = data/5/segdup.txt
    
    <rules>
    
    # adjust thickness for all links
    <rule>
    importance = 100
    condition  = 1
    thickness  = eval(max(1,min(6,exp(_SIZE1_/50000))))
    flow       = continue
    </rule>
    
    # closely spaced intrachromosomal links
    # go outside ideogram circle
    
    <rule>
    importance = 90
    condition  = _CHR1_ eq _CHR2_ && abs(_START1_-_START2_) < 40Mb
    radius        = 1r+125p
    bezier_radius = 1r+225p
    crest         = 1
    color         = red
    </rule>
    
    # all other intrachromosomeal links hidden
    
    <rule>
    importance = 80
    condition  = _CHR1_ eq _CHR2_
    show       = no
    </rule>
    
    # interchromosomeal links involving start
    # of chromosome are inside circle
    
    <rule>
    importance = 70
    condition  = _CHR1_ ne _CHR2_ && (_START1_ < 20Mb || _START2_ < 20Mb)
    color      = black
    radius     = 0.99r
    bezier_radius = 0.5r
    crest         = 1
    </rule>
    
    # all remaining links are hidden
    
    <rule>
    importance = 10
    condition  = 1
    show       = no
    </rule>
    
    </rules>
    
    </link>
    
    </links>
    
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

### circos.image-06.conf

    
    
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
    
    chromosomes_units = 1000000
    chromosomes       = hs1;hs2;hs3;hs4
    chromosomes_display_default = no
    
    <links>
    
    radius = 0.98r
    
    crest = 2.5
    bezier_radius         = 0.5r
    
    <link segdup>
    show         = yes
    color        = vdgrey
    thickness    = 2p
    file         = data/5/segdup.txt
    
    <rules>
    <rule>
    importance = 110
    condition  = _CHR1_ eq _CHR2_
    show       = no
    </rule>
    # the next two rules must contain flow=continue because it 
    # always matches and you do not want it to terminate
    # the rule chain (otherwise the color rule would
    # never be checked)
    <rule>
    importance = 100
    condition  = 1
    thickness  = eval(max(1,min(6,exp(_SIZE1_/50000))))
    flow       = continue
    </rule>
    
    <rule>
    importance    = 95
    condition     = _CHR1_ eq _CHR2_ && abs(_START1_-_START2_) < 100Mb
    bezier_radius = eval( (0.5 + 0.4*(1-abs(_START1_-_START2_) / 100Mb)) . "r")
    flow          = continue
    </rule>
    
    <rule>
    importance = 90
    condition  = (_CHR1_ eq "hs2" && _CHR2_ eq "hs4" && abs(_START1_ - 90Mb) < 30Mb) || (_CHR2_ eq "hs2" && _CHR1_ eq "hs4" && abs(_START2_ - 100Mb) < 20Mb)
    color      = red
    thickness  = eval(_thickness_*2)
    z          = 5
    </rule>
    
    <rule>
    importance = 90
    condition  = (_CHR1_ eq "hs1" && _CHR2_ eq "hs3" && abs(_START1_ - 160Mb) < 20Mb) || (_CHR2_ eq "hs1" && _CHR1_ eq "hs3" && abs(_START2_ - 160Mb) < 20Mb)
    color      = blue
    thickness  = eval(_thickness_*2)
    z          = 10
    </rule>
    
    </rules>
    
    </link>
    
    </links>
    
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

### circos.image-07.conf

    
    
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
    
    chromosomes_units = 1000000
    chromosomes       = hs1;hs2;hs3;hs4
    chromosomes_display_default = no
    
    <links>
    
    radius = 0.98r
    
    crest         = 2.5
    bezier_radius = 0.5r
    
    <link segdup>
    show         = yes
    color        = grey
    thickness    = 2p
    file         = data/5/segdup.txt
    
    <rules>
    <rule>
    importance = 110
    condition  = _CHR1_ eq _CHR2_ 
    show       = no
    </rule>
    # the next two rules must contain flow=continue because it 
    # always matches and you do not want it to terminate
    # the rule chain (otherwise the color rule would
    # never be checked)
    <rule>
    importance = 100
    condition  = 1
    thickness  = eval(max(1,min(6,exp(_SIZE1_/50000))))
    flow       = continue
    </rule>
    
    <rule>
    importance = 90
    condition  = (_CHR1_ eq "hs2" && _CHR2_ eq "hs4" && abs(_START1_ - 90Mb) < 30Mb) || (_CHR2_ eq "hs2" && _CHR1_ eq "hs4" && abs(_START2_ - 100Mb) < 20Mb)
    color      = red
    thickness  = eval(_thickness_*2)
    z          = 5
    
    crest         = 2
    bezier_radius = 0.5r
    
    </rule>
    
    <rule>
    importance = 90
    condition  = (_CHR1_ eq "hs1" && _CHR2_ eq "hs3" && abs(_START1_ - 160Mb) < 20Mb) || (_CHR2_ eq "hs1" && _CHR1_ eq "hs3" && abs(_START2_ - 160Mb) < 20Mb)
    color      = blue
    thickness  = eval(_thickness_*2)
    z          = 10
    crest         = 4
    bezier_radius = 0.75r
    
    </rule>
    
    <rule>
    importance = 90
    condition  = (_CHR1_ eq "hs1" && _CHR2_ eq "hs2" && abs(_START1_ - 10Mb) < 20Mb) || (_CHR2_ eq "hs1" && _CHR1_ eq "hs2" && abs(_START2_ - 10Mb) < 20Mb)
    color      = orange
    thickness  = eval(_thickness_*2)
    z          = 15
    crest         = 5
    bezier_radius = 0.8r
    
    </rule>
    
    </rules>
    
    </link>
    
    </links>
    
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
    label_radius   = dims(ideogram,radius) + 0.075r
    label_size     = 60p
    
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
    radius               = dims(ideogram,radius_outer)
    multiplier           = 1e-6
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
    label_size     = 20p
    label_offset   = 5p
    format         = %d
    </tick>
    
    </ticks>
    

  

* * *

