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

## 9\. Transparent Links

[Lesson](/documentation/tutorials/recipes/transparent_links/lesson)
[Images](/documentation/tutorials/recipes/transparent_links/images)
[Configuration](/documentation/tutorials/recipes/transparent_links/configuration)

### circos.conf

    
    
    luminance = lum80
    #luminance = ""
    
    <<include colors_fonts_patterns.conf>>
    
    <colors>
    # r,g,b,a color definition
    #
    # a = 0 fully opaque
    # a = 1 fully transparent
    blackweak = 0,0,0,0.75
    </colors>
    
    <<include ideogram.conf>>
    <<include ticks.conf>>
    
    karyotype   = data/karyotype/karyotype.human.txt
    
    <image>
    <<include etc/image.conf>>
    </image>
    
    chromosomes_units  = 1000000
    
    # change the color of each chromosome to lum80 + chr_name
    # where the lum80 prefix references a predefined color
    # with normalized luminance
    chromosomes_color = /./=conf(luminance)var(chr)
    
    # restrict image to hs1-hs9
    #chromosomes        = /hs[1-9]$/
    #chromosomes_display_default = no
    
    <links>
    
    <link>
    
    file   = data/8/chrall-random.txt
    ribbon = yes
    flat   = yes # untwist all ribbons
    radius = 0.98r
    color  = blackweak
    bezier_radius    = 0r
    stroke_color     = vdgrey_a4
    stroke_thickness = 2
    
    <rules>
    
    <rule>
    condition = 1
    # derive the color name from the chromosome name
    # lum80 + chr_name + _a2
    #
    # lum70*, lum80* and lum90* colors are normalized
    # to a given luminance and are predefined at etc/colors.ucsc.conf
    #
    # _a2 adds transparency (2/6 = 33%) where the denominator
    # is derived from auto_alpha_steps+1=6
    color     = eval(lc sprintf("%s%s_a4",'conf(luminance)',var(chr1),4))
    z         = eval(average(var(size1),var(size2)))
    </rule>
    
    </rules>
    
    </link>
    
    </links>
    
    <<include etc/housekeeping.conf>>
    data_out_of_range* = trim
    

  

* * *

### ideogram.conf

    
    
    <ideogram>
    
    <spacing>
    
    default = 10u
    
    </spacing>
    
    # thickness (px) of chromosome ideogram
    thickness        = 50p
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
    label_font     = light
    label_radius   = dims(ideogram,radius) + 0.075r
    label_size     = 60p
    label_parallel = yes
    label_case     = upper
    
    # cytogenetic bands
    band_stroke_thickness = 2
    
    # show_bands determines whether the outline of cytogenetic bands
    # will be seen
    show_bands            = no
    # in order to fill the bands with the color defined in the karyotype
    # file you must set fill_bands
    fill_bands            = no
    
    </ideogram>
    
    

  

* * *

### randomlinks.conf

    
    
    karyotype = /home/martink/work/circos/dev/data/karyotype.human.txt
    
    ################################################################
    # 50 links on chr1 only
    
    #chr_rx = hs1$
    #size = 10e6,5e6
    #ruleset = links1
    
    <rules links1>
    rule = . . 50 0
    </rules>
    
    ################################################################
    # links between all chromosomes
    
    nointra = yes
    size    = 20e6,10e6
    ruleset = links2
    
    <rules links2>
    rule = . . 1 1 0.2
    rule = hs12 . 2 1 0.5
    rule = hs5 . 2 1 0.5
    </rules>
    

  

* * *

### ticks.conf

    
    
    show_ticks          = yes
    show_tick_labels    = yes
    
    <ticks>
    radius               = dims(ideogram,radius_outer)
    multiplier           = 1e-6
    
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

