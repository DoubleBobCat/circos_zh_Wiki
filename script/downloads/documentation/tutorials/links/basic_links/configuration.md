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

# 6 — Links and Relationships

## 1\. Drawing Basic Links

[Lesson](/documentation/tutorials/links/basic_links/lesson)
[Images](/documentation/tutorials/links/basic_links/images)
[Configuration](/documentation/tutorials/links/basic_links/configuration)

### circos.conf

    
    
    <<include colors_fonts_patterns.conf>>
    
    <<include ideogram.conf>>
    <<include ticks.conf>>
    
    <image>
    <<include etc/image.conf>>
    </image>
    
    karyotype   = data/karyotype/karyotype.human.txt
    
    chromosomes_units = 1000000
    chromosomes       = hs1;hs2;hs3
    chromosomes_display_default = no
    
    # If you adjust the radius of the ideograms, links incident
    # on these ideograms will inherit the new radius.
    #chromosomes_radius = hs2:0.9r;hs3:0.8r
    
    # Links (bezier curves or straight lines) are defined in <links> blocks.
    # Each link data set is defined within a <link> block. 
    #
    # As with highlights, parameters defined
    # in the root of <links> affect all data sets and are considered
    # global settings. Individual parameters value can be refined by
    # values defined within <link> blocks, or additionally on each
    # data line within the input file.
    
    <links>
    
    <link>
    file          = data/5/segdup.txt
    radius        = 0.95r
    color         = black_a4
    
    # Curves look best when this value is small (e.g. 0.1r or 0r)
    bezier_radius = 0.1r
    thickness     = 1
    
    # These parameters have default values. To unset them
    # use 'undef'
    #crest                = undef
    #bezier_radius_purity = undef
    
    # Limit how many links to read from file and draw
    record_limit  = 2000
    
    </link>
    
    </links>
    
    <<include etc/housekeeping.conf>>
    data_out_of_range* = trim
    
    # If you want to turn off all track default values, 
    # uncomment the line below. This overrides the
    # value of the parameter imported from etc/housekeeping.conf
    
    #track_defaults* = undef
    # The defaults for links are
    #
    # ribbon           = no
    # color            = black
    # thickness        = 1
    # radius           = 0.40r
    # bezier_radius    = 0r
    # crest                = 0.5
    # bezier_radius_purity = 0.75
    #
    # See etc/tracks/link.conf in Circos distribution
    

  

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
    
    </ideogram>
    
    

  

* * *

### ideogram.label.conf

    
    
    show_label       = yes
    label_font       = default
    label_radius     = dims(ideogram,radius) + 0.075r
    label_with_tag   = yes
    label_size       = 36
    label_parallel   = yes
    label_case       = lower
    label_format     = eval(sprintf("chr%s",var(label)))
    

  

* * *

### ideogram.position.conf

    
    
    radius           = 0.90r
    thickness        = 100p
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
    
    <tick>
    spacing        = 1u
    show_label     = no
    </tick>
    
    <tick>
    spacing        = 5u
    show_label     = yes
    label_size     = 20p
    format         = %d
    </tick>
    
    <tick>
    spacing        = 10u
    show_label     = yes
    label_size     = 24p
    format         = %d
    </tick>
    
    </ticks>
    

  

* * *

