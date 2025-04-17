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

## 7\. Text—Stacking

[Lesson](/documentation/tutorials/2d_tracks/text_2/lesson)
[Images](/documentation/tutorials/2d_tracks/text_2/images)
[Configuration](/documentation/tutorials/2d_tracks/text_2/configuration)

### circos.conf

    
    
    <<include colors_fonts_patterns.conf>>
    
    <<include ideogram.conf>>
    <<include ticks.conf>>
    
    karyotype = data/karyotype/karyotype.human.txt
    
    <image>
    <<include etc/image.conf>>
    </image>
    
    chromosomes_units           = 1000000
    chromosomes                 = hs1:0-50
    chromosomes_display_default = no
    
    <plots>
    
    type       = text
    color      = black
    label_font = condensed
    
    <plot>
    
    file = data/6/text.genes.txt
    r1   = 0.2r+300p
    r0   = 0.2r
    
    label_size = 8p
    
    show_links     = yes
    link_dims      = 1p,1p,2p,1p,1p
    link_thickness = 1p
    link_color     = red
    
    padding        = 2p
    rpadding       = 2p
    
    label_snuggle         = yes
    max_snuggle_distance  = 1r
    snuggle_tolerance     = 0.25r
    snuggle_sampling      = 2
    
    <rules>
    <rule>
    condition  = var(value) =~ /5/i
    color      = red
    </rule>
    </rules>
    
    </plot>
    
    <plot>
    
    file = data/6/text.genes.txt
    r1   = 0.975r
    r0   = 0.5r
    
    label_size = 12p
    
    show_links     = yes
    link_dims      = 2p,2p,4p,2p,2p
    link_thickness = 2p
    link_color     = red
    
    label_snuggle         = yes
    max_snuggle_distance  = 1r
    snuggle_tolerance     = 0.25r
    snuggle_sampling      = 2
    
    <rules>
    <rule>
    condition  = var(value) =~ /ZNF/i
    label_font = condensedbold
    </rule>
    </rules>
    
    </plot>
    
    <plot>
    
    file = data/6/text.genes.txt
    r1   = 1r+200p
    r0   = 1r
    
    label_size = 24p
    
    show_links     = yes
    link_dims      = 0p,0p,100p,0p,0p
    link_thickness = 2p
    link_color     = blue
    
    <rules>
    <rule>
    condition = var(value) =~ /znf/i
    color     = red
    </rule>
    <rule>
    condition = var(value) =~ /ifi/i
    color     = green
    </rule>
    <rule>
    condition  = var(value) =~ /orf/;
    color      = grey
    link_color = grey
    label_size = 16p
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

    
    
    show_ticks          = yes
    show_tick_labels    = yes
    
    <ticks>
    
    radius           = dims(ideogram,radius_outer)
    orientation      = out
    label_multiplier = 1e-6
    color            = black
    size             = 20p
    thickness        = 3p
    label_offset     = 5p
    format           = %d
    
    <tick>
    spacing        = 1u
    show_label     = no
    size           = 10p
    </tick>
    
    <tick>
    spacing        = 5u
    show_label     = yes
    label_size     = 20p
    size           = 15p
    </tick>
    
    <tick>
    spacing        = 10u
    show_label     = yes
    label_size     = 24p
    </tick>
    
    </ticks>
    

  

* * *

