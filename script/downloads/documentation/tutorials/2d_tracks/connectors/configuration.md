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

## 11\. Connectors

[Lesson](/documentation/tutorials/2d_tracks/connectors/lesson)
[Images](/documentation/tutorials/2d_tracks/connectors/images)
[Configuration](/documentation/tutorials/2d_tracks/connectors/configuration)

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
    24bit = yes
    png = yes
    svg = yes
    # radius of inscribed circle in image
    radius         = 3000p
    background     = white
    # by default angle=0 is at 3 o'clock position
    angle_offset   = -90
    
    auto_alpha_colors = yes
    auto_alpha_steps  = 5
    
    </image>
    
    chromosomes_units  = 1000000
    #chromosomes       = hs6;hs20;hs22
    chromosomes        = hs22:14.5-)
    
    chromosomes_display_default = no
    
    <highlights>
    
    stroke_thickness = 0
    stroke_color     = white
    
    <highlight>
    show       = yes
    z          = 10
    file       = data/6/epi.tmp.txt
    r0         = 0.95r
    r1         = 0.8r
    </highlight>
    
    </highlights>
    
    <plots>
    
    <plot>
    
    show = yes
    
    type = connector
    file = data/6/connectors.txt
    
    r0   = 0.8925r
    r1   = 0.999r
    
    #connector_dims = 0,0.3,0.4,0.3,0
    connector_dims = 0.05,0.15,0.6,0.1,0.1
    
    thickness = 1
    color     = black
    
    </plot>
    
    </plots>
    
    anglestep       = 0.5
    minslicestep    = 10
    beziersamples   = 40
    debug           = no
    warnings        = no
    imagemap        = no
    
    units_ok = bupr
    units_nounit = n
    

  

* * *

### colors.all.conf

    
    
    # RGB color definition. Colors are refered to within configuration files
    # by their name. In order to use a color, you must define it here. 
    # 
    # e.g. if you really must use 'bisque', then add
    #
    # bisque = 255,228,196
    #
    # Many useful colors are already defined. In general, given a HUE, these
    # colors are defined
    #
    # vlHUE (very light HUE, e.g. vlred)
    # lHUE  (light HUE, e.g. red)
    # HUE   (e.g. red)
    # dHUE  (dark HUE, e.g. dred)
    #
    # In addition to hues, two other color groups are defined. 
    #
    # - cytogenetic band colors (e.g. gposNNN, acen, stalk, etc.) which
    #   correspond to colors on ideogram bands
    # - UCSC chromosome color palette (e.g. chrNN, chrUn, chrNA)
    
    optblue   = 55,133,221
    optgreen  = 55,221,125
    optyellow = 221,215,55
    optorange = 221,164,55
    optred    = 221,55,55
    optviolet = 145,55,221
    optpurple = 219,55,221
    
    white     = 255,255,255
    vvvvlgrey = 250,250,250
    vvvlgrey  = 240,240,240
    vvlgrey   = 230,230,230
    vlgrey    = 220,220,220
    lgrey     = 210,210,210
    grey      = 200,200,200
    dgrey     = 170,170,170
    vdgrey    = 140,140,140
    vvdgrey   = 100,100,100
    vvvdgrey  = 70,70,70
    vvvvdgrey = 40,40,40
    black     = 0,0,0
    
    vlred   = 255,193,200
    lred    = 255,122,137
    red     = 247,42,66
    dred    = 205,51,69
    
    vlgreen = 204,255,218
    lgreen  = 128,255,164
    green   = 51,204,94
    dgreen  = 38,153,71
    
    vlblue  = 128,176,255
    lblue   = 64,137,255
    blue    = 54,116,217
    dblue   = 38,82,153
    
    vlpurple= 242,128,255
    lpurple = 236,64,255
    purple  = 189,51,204
    dpurple = 118,32,128
    
    vlyellow = 255,253,202
    lyellow  = 255,252,150
    yellow   = 255,255,0
    dyellow  = 191,186,48
    
    lime     = 186,255,0
    
    vlorange = 255,228,193
    lorange  = 255,187,110
    orange   = 255,136,0
    dorange  = 221,143,55
    
    # karyotype colors
    
    gpos100 = 0,0,0
    gpos    = 0,0,0
    gpos75  = 130,130,130
    gpos66  = 160,160,160
    gpos50  = 200,200,200
    gpos33  = 210,210,210
    gpos25  = 200,200,200
    gvar    = 220,220,220
    gneg    = 255,255,255
    acen    = 217,47,39
    stalk   = 100,127,164
    
    # others
    
    select = 135,177,255
    
    # new york times cmyk-safe
    
    # roygbiv - normal
    nyt_blue   = 104,152,178
    nyt_green  = 137,129,96
    nyt_yellow = 241,221,117
    nyt_orange = 230,146,57
    nyt_red    = 217,47,39
    
    # chromosome color map (UCSC) 
    
    chr1 = 153,102,0
    chr2 = 102,102,0
    chr3 = 153,153,30
    chr4 = 204,0,0
    chr5 = 255,0,0
    chr6 = 255,0,204
    chr7 = 255,204,204
    chr8 = 255,153,0
    chr9 = 255,204,0
    chr10 = 255,255,0
    chr11 = 204,255,0
    chr12 = 0,255,0
    chr13 = 53,128,0
    chr14 = 0,0,204
    chr15 = 102,153,255
    chr16 = 153,204,255
    chr17 = 0,255,255
    chr18 = 204,255,255
    chr19 = 153,0,204
    chr20 = 204,51,255
    chr21 = 204,153,255
    chr22 = 102,102,102
    chr23 = 153,153,153
    chrX  = 153,153,153
    chr24 = 204,204,204
    chrY = 204,204,204
    chrM = 204,204,153
    chr0 = 204,204,153
    chrUn = 121,204,61
    chrNA = 255,255,255
    meth0 = 217,33,33
    meth1 = 217,40,33
    meth2 = 217,47,33
    meth3 = 217,55,33
    meth4 = 217,62,33
    meth5 = 217,69,33
    meth6 = 217,77,33
    meth7 = 217,84,33
    meth8 = 217,91,33
    meth9 = 217,99,33
    meth10 = 217,106,33
    meth11 = 217,114,33
    meth12 = 217,121,33
    meth13 = 217,128,33
    meth14 = 217,136,33
    meth15 = 217,143,33
    meth16 = 217,150,33
    meth17 = 217,158,33
    meth18 = 217,165,33
    meth19 = 217,173,33
    meth20 = 217,180,33
    meth21 = 217,187,33
    meth22 = 217,195,33
    meth23 = 217,202,33
    meth24 = 217,209,33
    meth25 = 217,217,33
    meth26 = 209,217,33
    meth27 = 202,217,33
    meth28 = 195,217,33
    meth29 = 187,217,33
    meth30 = 180,217,33
    meth31 = 173,217,33
    meth32 = 165,217,33
    meth33 = 158,217,33
    meth34 = 150,217,33
    meth35 = 143,217,33
    meth36 = 136,217,33
    meth37 = 128,217,33
    meth38 = 121,217,33
    meth39 = 114,217,33
    meth40 = 106,217,33
    meth41 = 99,217,33
    meth42 = 91,217,33
    meth43 = 84,217,33
    meth44 = 77,217,33
    meth45 = 69,217,33
    meth46 = 62,217,33
    meth47 = 55,217,33
    meth48 = 47,217,33
    meth49 = 40,217,33
    meth50 = 33,217,33
    meth51 = 33,217,40
    meth52 = 33,217,47
    meth53 = 33,217,55
    meth54 = 33,217,62
    meth55 = 33,217,69
    meth56 = 33,217,77
    meth57 = 33,217,84
    meth58 = 33,217,91
    meth59 = 33,217,99
    meth60 = 33,217,106
    meth61 = 33,217,114
    meth62 = 33,217,121
    meth63 = 33,217,128
    meth64 = 33,217,136
    meth65 = 33,217,143
    meth66 = 33,217,150
    meth67 = 33,217,158
    meth68 = 33,217,165
    meth69 = 33,217,173
    meth70 = 33,217,180
    meth71 = 33,217,187
    meth72 = 33,217,195
    meth73 = 33,217,202
    meth74 = 33,217,209
    meth75 = 33,217,217
    meth76 = 33,209,217
    meth77 = 33,202,217
    meth78 = 33,195,217
    meth79 = 33,187,217
    meth80 = 33,180,217
    meth81 = 33,173,217
    meth82 = 33,165,217
    meth83 = 33,158,217
    meth84 = 33,150,217
    meth85 = 33,143,217
    meth86 = 33,136,217
    meth87 = 33,128,217
    meth88 = 33,121,217
    meth89 = 33,114,217
    meth90 = 33,106,217
    meth91 = 33,99,217
    meth92 = 33,91,217
    meth93 = 33,84,217
    meth94 = 33,77,217
    meth95 = 33,69,217
    meth96 = 33,62,217
    meth97 = 33,55,217
    meth98 = 33,47,217
    meth99 = 33,40,217
    meth100 = 33,33,217
    

  

* * *

### colors.conf

    
    
    # RGB color definition. Colors are refered to within configuration files
    # by their name. In order to use a color, you must define it here. 
    # 
    # e.g. if you really must use 'bisque', then add
    #
    # bisque = 255,228,196
    #
    # Many useful colors are already defined. In general, given a HUE, these
    # colors are defined
    #
    # vlHUE (very light HUE, e.g. vlred)
    # lHUE  (light HUE, e.g. red)
    # HUE   (e.g. red)
    # dHUE  (dark HUE, e.g. dred)
    #
    # In addition to hues, two other color groups are defined. 
    #
    # - cytogenetic band colors (e.g. gposNNN, acen, stalk, etc.) which
    #   correspond to colors on ideogram bands
    # - UCSC chromosome color palette (e.g. chrNN, chrUn, chrNA)
    
    optblue   = 55,133,221
    optgreen  = 55,221,125
    optyellow = 221,215,55
    optorange = 221,164,55
    optred    = 221,55,55
    optviolet = 145,55,221
    optpurple = 219,55,221
    
    white     = 255,255,255
    vvvvlgrey = 250,250,250
    vvvlgrey  = 240,240,240
    vvlgrey   = 230,230,230
    vlgrey    = 220,220,220
    lgrey     = 210,210,210
    grey      = 200,200,200
    dgrey     = 170,170,170
    vdgrey    = 140,140,140
    vvdgrey   = 100,100,100
    vvvdgrey  = 70,70,70
    vvvvdgrey = 40,40,40
    black     = 0,0,0
    
    vlred   = 255,193,200
    lred    = 255,122,137
    red     = 247,42,66
    dred    = 205,51,69
    
    vlgreen = 204,255,218
    lgreen  = 128,255,164
    green   = 51,204,94
    dgreen  = 38,153,71
    
    vlblue  = 128,176,255
    lblue   = 64,137,255
    blue    = 54,116,217
    dblue   = 38,82,153
    
    vlpurple= 242,128,255
    lpurple = 236,64,255
    purple  = 189,51,204
    dpurple = 118,32,128
    
    vlyellow = 255,253,202
    lyellow  = 255,252,150
    yellow   = 255,255,0
    dyellow  = 191,186,48
    
    lime     = 186,255,0
    
    vlorange = 255,228,193
    lorange  = 255,187,110
    orange   = 255,136,0
    dorange  = 221,143,55
    
    # karyotype colors
    
    gpos100 = 0,0,0
    gpos    = 0,0,0
    gpos75  = 130,130,130
    gpos66  = 160,160,160
    gpos50  = 200,200,200
    gpos33  = 210,210,210
    gpos25  = 200,200,200
    gvar    = 220,220,220
    gneg    = 255,255,255
    acen    = 217,47,39
    stalk   = 100,127,164
    
    # others
    
    select = 135,177,255
    
    # new york times cmyk-safe
    
    # roygbiv - normal
    nyt_blue   = 104,152,178
    nyt_green  = 137,129,96
    nyt_yellow = 241,221,117
    nyt_orange = 230,146,57
    nyt_red    = 217,47,39
    
    # chromosome color map (UCSC) 
    
    chr1 = 153,102,0
    chr2 = 102,102,0
    chr3 = 153,153,30
    chr4 = 204,0,0
    chr5 = 255,0,0
    chr6 = 255,0,204
    chr7 = 255,204,204
    chr8 = 255,153,0
    chr9 = 255,204,0
    chr10 = 255,255,0
    chr11 = 204,255,0
    chr12 = 0,255,0
    chr13 = 53,128,0
    chr14 = 0,0,204
    chr15 = 102,153,255
    chr16 = 153,204,255
    chr17 = 0,255,255
    chr18 = 204,255,255
    chr19 = 153,0,204
    chr20 = 204,51,255
    chr21 = 204,153,255
    chr22 = 102,102,102
    chr23 = 153,153,153
    chrX  = 153,153,153
    chr24 = 204,204,204
    chrY = 204,204,204
    chrM = 204,204,153
    chr0 = 204,204,153
    chrUn = 121,204,61
    chrNA = 255,255,255
    

  

* * *

### colors.values.conf

    
    
    meth0 = 230,230,0
    meth1 = 222,228,1
    meth2 = 214,227,2
    meth3 = 206,226,3
    meth4 = 199,225,4
    meth5 = 191,224,4
    meth6 = 184,223,5
    meth7 = 177,222,6
    meth8 = 170,221,7
    meth9 = 163,220,8
    meth10 = 156,219,9
    meth11 = 149,218,10
    meth12 = 143,217,10
    meth13 = 136,216,11
    meth14 = 130,215,12
    meth15 = 124,214,13
    meth16 = 117,213,14
    meth17 = 111,212,14
    meth18 = 105,211,15
    meth19 = 99,210,16
    meth20 = 94,209,17
    meth21 = 88,208,17
    meth22 = 82,207,18
    meth23 = 77,206,19
    meth24 = 72,205,20
    meth25 = 66,204,20
    meth26 = 61,203,21
    meth27 = 56,202,22
    meth28 = 51,201,23
    meth29 = 46,200,23
    meth30 = 41,199,24
    meth31 = 37,198,25
    meth32 = 32,197,25
    meth33 = 28,196,26
    meth34 = 26,195,30
    meth35 = 27,194,35
    meth36 = 28,193,41
    meth37 = 28,192,46
    meth38 = 29,191,52
    meth39 = 30,190,57
    meth40 = 30,189,62
    meth41 = 31,188,67
    meth42 = 31,187,72
    meth43 = 32,186,77
    meth44 = 32,185,81
    meth45 = 33,184,86
    meth46 = 34,183,90
    meth47 = 34,182,95
    meth48 = 35,181,99
    meth49 = 35,180,103
    meth50 = 36,179,107
    meth51 = 36,177,111
    meth52 = 37,176,115
    meth53 = 37,175,119
    meth54 = 38,174,122
    meth55 = 38,173,126
    meth56 = 39,172,130
    meth57 = 39,171,133
    meth58 = 40,170,136
    meth59 = 40,169,140
    meth60 = 40,168,143
    meth61 = 41,167,146
    meth62 = 41,166,149
    meth63 = 42,165,152
    meth64 = 42,164,154
    meth65 = 42,163,157
    meth66 = 43,162,160
    meth67 = 43,160,161
    meth68 = 44,155,160
    meth69 = 44,151,159
    meth70 = 44,147,158
    meth71 = 45,142,157
    meth72 = 45,138,156
    meth73 = 45,134,155
    meth74 = 46,130,154
    meth75 = 46,126,153
    meth76 = 46,122,152
    meth77 = 46,119,151
    meth78 = 47,115,150
    meth79 = 47,111,149
    meth80 = 47,108,148
    meth81 = 48,104,147
    meth82 = 48,101,146
    meth83 = 48,97,145
    meth84 = 48,94,144
    meth85 = 49,91,143
    meth86 = 49,88,142
    meth87 = 49,85,141
    meth88 = 49,82,140
    meth89 = 49,79,139
    meth90 = 50,76,138
    meth91 = 50,73,137
    meth92 = 50,70,136
    meth93 = 50,68,135
    meth94 = 50,65,134
    meth95 = 50,63,133
    meth96 = 51,60,132
    meth97 = 51,58,131
    meth98 = 51,56,130
    meth99 = 51,53,129
    meth100 = 51,51,128
    

  

* * *

### fonts.conf

    
    
    default       = /home/martink/work/circos/dev/fonts/LTe50046.ttf
    normal        = /home/martink/work/circos/dev/fonts/LTe50046.ttf
    bold          = /home/martink/work/circos/dev/fonts/LTe50048.ttf
    condensed     = /home/martink/work/circos/dev/fonts/LTe50050.ttf
    condensedbold = /home/martink/work/circos/dev/fonts/LTe50054.ttf
    mono          = /home/martink/work/circos/dev/fonts/pragmata.ttf
    glyph         = /home/martink/work/circos/dev/fonts/wingding.ttf
    

  

* * *

### ideogram.conf

    
    
    <ideogram>
    
    <spacing>
    
    default = 0.1u
    
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
    show_label     = no
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
    
    <ticks>
    
    radius               = dims(ideogram,radius_outer)
    offset     = 0p
    label_size = 16p
    multiplier = 1e-6
    color      = black
    
    <tick>
    spacing        = .1u
    size           = 4p
    thickness      = 3p
    color          = black
    show_label     = no
    </tick>
    
    <tick>
    spacing        = 1u
    size           = 6p
    thickness      = 3p
    color          = black
    show_label     = yes
    label_size     = 32p
    format         = %d
    </tick>
    
    <tick>
    spacing        = 5u
    size           = 10p
    thickness      = 3p
    color          = black
    show_label     = yes
    label_size     = 32p
    format         = %d
    </tick>
    
    <tick>
    spacing        = 10u
    size           = 16p
    thickness      = 3p
    color          = black
    show_label     = yes
    label_size     = 32p
    format         = %d
    </tick>
    </ticks>
    

  

* * *

