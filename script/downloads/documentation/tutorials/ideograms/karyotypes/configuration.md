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

# 3 — Drawing Ideograms

## 2\. Karyotypes

[Lesson](/documentation/tutorials/ideograms/karyotypes/lesson)
[Images](/documentation/tutorials/ideograms/karyotypes/images)
[Configuration](/documentation/tutorials/ideograms/karyotypes/configuration)

### circos.2.conf

    
    
    <colors>
    <<include etc/colors.conf>>
    </colors>
    
    <fonts>
    <<include etc/fonts.conf>>
    </fonts>
    
    <<include ideogram.conf>>
    <<include ticks.conf>>
    
    # specify the karyotype file here; try also
    #  data/2/karyotype.dog.txt
    #  data/2/karyotype.rat.txt
    #  data/2/karyotype.mouse.txt
    #  data/2/karyotype.all.txt (human+dog+rat+mouse)
    # but reduce frequency of ticks when increasing the 
    # number of ideograms
    karyotype = data/karyotype.human.txt
    
    <image>
    dir = /tmp
    file  = circos-tutorial.png
    # radius of inscribed circle in image
    radius         = 1500p
    background     = white
    # by default angle=0 is at 3 o'clock position
    angle_offset   = -90
    #angle_orientation = counterclockwise
    </image>
    
    chromosomes_units           = 1000000
    
    #chromosomes_display_default = yes
    
    chromosomes = hs1;hs2;hs3
    
    anglestep       = 0.5
    minslicestep    = 10
    beziersamples   = 40
    debug           = no
    warnings        = no
    imagemap        = no
    
    units_ok = bupr
    units_nounit = n
    
    

  

* * *

### circos.conf

    
    
    <<include etc/colors_fonts_patterns.conf>>
    
    <<include ideogram.conf>>
    <<include ticks.conf>>
    
    <image>
    <<include etc/image.conf>>
    </image>
    
    chromosomes_units           = 1000000
    chromosomes_display_default = yes
    
    ### single genomes
    
    # specify the karyotype file here - try other karyotypes in data/karyotype
    karyotype = data/karyotype/karyotype.human.txt
    #karyotype = data/karyotype/karyotype.drosophila.txt
    #karyotype = data/karyotype/karyotype.mouse.txt
    #karyotype = data/karyotype/karyotype.rat.txt
    
    ### multiple genomes
    
    # to draw chromosomes from multiple karyotypes, 
    # provide comma-separated list of files
    #karyotype          = data/karyotype/karyotype.human.txt,data/karyotype/karyotype.mouse.txt,data/karyotype/karyotype.rat.txt
    
    # adjust color using regular expressions matching chromosome names
    #chromosomes_color  = /hs/:red;/mm/:green;/rn/:blue
    
    <<include etc/housekeeping.conf>>
    

  

* * *

### bands.conf

    
    
    show_bands            = yes
    fill_bands            = yes
    band_stroke_thickness = 2
    band_stroke_color     = white
    band_transparency     = 4
    

  

* * *

### ideogram.conf

    
    
    <ideogram>
    
    <spacing>
    
    default = 0.0025r
    break   = 0.5r
    
    </spacing>
    
    <<include ideogram.position.conf>>
    <<include ideogram.label.conf>>
    <<include bands.conf>>
    
    <rules>
    use       = no
    <rule>
    # hide every other ideogram
    condition = var(display_idx) % 2
    show      = no
    </rule>
    <rule>
    condition = var(chr) eq "hs3"
    show_ticks = no
    </rule>
    <rule>
    condition = var(chr) eq "hs5"
    show_bands = no
    </rule>
    <rule>
    condition = var(chr) eq "hs7"
    color     = vdpurple
    </rule>
    <rule>
    condition = var(chr) eq "hs9"
    stroke_thickness = 0
    </rule>
    </rules>
    
    </ideogram>
    
    

  

* * *

### ideogram.label.conf

    
    
    show_label       = yes
    label_font       = default
    label_radius     = 0.95r
    label_with_tag   = yes
    label_size       = 36
    label_parallel   = yes
    label_case       = lower
    
    # you can format the label by using properties
    # of the ideogram, accessible with var(PROPERTY):
    #
    # chr, chr_with_tag, chrlength, display_idx, end, idx, 
    # label, length, reverse, scale, size, start, tag
    
    label_format     = eval(sprintf("chr%s",var(label)))
    

  

* * *

### ideogram.position.conf

    
    
    radius           = 0.90r
    thickness        = 75p
    fill             = yes
    fill_color       = black
    stroke_thickness = 2
    stroke_color     = black
    

  

* * *

### ticks.conf

    
    
    show_ticks          = yes
    show_tick_labels    = yes
    
    <ticks>
    skip_first_label = no
    skip_last_label  = no
    radius           = dims(ideogram,radius_outer)
    tick_separation  = 2p
    label_separation = 5p
    multiplier       = 1e-6
    color            = black
    thickness        = 4p
    size             = 20p
    
    <tick>
    spacing        = 1u
    show_label     = no
    thickness      = 2p
    color          = dgrey
    </tick>
    
    <tick>
    spacing        = 5u
    show_label     = no
    thickness      = 3p
    color          = vdgrey
    </tick>
    
    <tick>
    spacing        = 10u
    show_label     = yes
    label_size     = 20p
    label_offset   = 10p
    format         = %d
    grid           = yes
    grid_color     = dgrey
    grid_thickness = 1p
    grid_start     = 0.5r
    grid_end       = 0.999r
    </tick>
    
    </ticks>
    

  

* * *

