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

## 1\. Ideograms

[Lesson](/documentation/tutorials/ideograms/ideograms/lesson)
[Images](/documentation/tutorials/ideograms/ideograms/images)
[Configuration](/documentation/tutorials/ideograms/ideograms/configuration)

### circos.conf

    
    
    # MINIMUM CIRCOS CONFIGURATION 
    #
    # The 'hello world' Circos tutorial. Only required
    # configuration elements are included.
    #
    # Common optional elements are commented out.
    
    # Defines unit length for ideogram and tick spacing, referenced
    # using "u" prefix, e.g. 10u
    #chromosomes_units           = 1000000
    
    # Show all chromosomes in karyotype file. By default, this is
    # true. If you want to explicitly specify which chromosomes
    # to draw, set this to 'no' and use the 'chromosomes' parameter.
    # chromosomes_display_default = yes
    
    # Chromosome name, size and color definition
    karyotype = data/karyotype/karyotype.human.txt
    
    <ideogram>
    
    <spacing>
    # spacing between ideograms
    default = 0.005r
    </spacing>
    
    # ideogram position, thickness and fill
    radius           = 0.90r
    thickness        = 10p
    fill             = yes
    
    #stroke_thickness = 1
    #stroke_color     = black
    
    # ideogram labels
    # <<include ideogram.label.conf>>
    
    # ideogram cytogenetic bands, if defined in the karyotype file
    # <<include bands.conf>>
    
    </ideogram>
    
    # image size, background color, angular position
    # of first ideogram, transparency levels, output
    # file and directory
    #
    # it is best to include these parameters from etc/image.conf
    # and override any using param* syntax
    #
    # e.g.
    # <image>
    # <<include etc/image.conf>>
    # radius* = 500
    # </image>
    <image>
    <<include etc/image.conf>> # included from Circos distribution 
    </image>
    
    # RGB/HSV color definitions, color lists, location of fonts,
    # fill patterns
    <<include etc/colors_fonts_patterns.conf>> # included from Circos distribution
    
    # debugging, I/O an dother system parameters
    <<include etc/housekeeping.conf>> # included from Circos distribution
    
    # <ticks> blocks to define ticks, tick labels and grids
    #
    # requires that chromosomes_units be defined
    #
    # <<include ticks.conf>>
    

  

* * *

### bands.conf

    
    
    # optional
    
    show_bands            = yes
    fill_bands            = yes
    band_transparency     = 4
    

  

* * *

### ideogram.label.conf

    
    
    # optional
    
    show_label       = yes
    label_radius     = dims(ideogram,radius) + 0.075r
    label_size       = 24
    label_parallel   = yes
    
    

  

* * *

### ticks.conf

    
    
    # ticks are optional
    
    show_ticks          = yes
    show_tick_labels    = yes
    
    <ticks>
    radius           = dims(ideogram,radius_outer)
    multiplier       = 1e-6
    color            = black
    thickness        = 2p
    size             = 15p
    
    <tick>
    spacing        = 20u
    show_label     = yes
    label_size     = 20p
    label_offset   = 10p
    format         = %d
    </tick>
    
    <tick>
    spacing        = 5u
    color          = grey
    size           = 10p
    </tick>
    
    </ticks>
    

  

* * *

