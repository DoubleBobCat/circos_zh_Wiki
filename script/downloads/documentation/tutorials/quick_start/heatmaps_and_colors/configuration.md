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

# 2 — Quick Start

## 7\. Heat maps

[Lesson](/documentation/tutorials/quick_start/heatmaps_and_colors/lesson)
[Images](/documentation/tutorials/quick_start/heatmaps_and_colors/images)
[Configuration](/documentation/tutorials/quick_start/heatmaps_and_colors/configuration)

### circos.conf

    
    
    # 1.7 HEAT MAPS
    
    karyotype = data/karyotype/karyotype.human.txt
    chromosomes_units = 1000000
    
    chromosomes_display_default = no
    chromosomes                 = /hs[1234]$/
    chromosomes_radius          = hs4:0.9r
    
    <colors>
    chr1* = red
    chr2* = orange
    chr3* = green
    chr4* = blue
    </colors>
    
    chromosomes_reverse = /hs[234]/
    chromosomes_scale   = hs1=0.5r,/hs[234]/=0.5rn
    
    <plots>
    
    # Heat maps are used for data types which associate a value with a
    # genomic position, or region. As such, this track uses the same data
    # format as histograms.
    #
    # The track linearly maps a range of values [min,max] onto a list of colors c[n], i=0..N.
    #
    # f = (value - min) / ( max - min )
    # n = N * f
    
    <plot>
    type  = heatmap
    file  = data/5/segdup.hs1234.heatmap.txt
    r1    = 0.89r
    r0    = 0.88r
    
    # Colors are defined by a combination of lists or CSV. Color lists
    # exist for all Brewer palletes (see etc/colors.brewer.lists.conf) as
    # well as for N-step hue (hue-sN, e.g. hue-s5 =
    # hue000,hue005,hue010,...) and N-color hue (hue-sN, e.g. hue-3 =
    # hue000,hue120,hue140).
    
    color = hs1_a5,hs1_a4,hs1_a3,hs1_a2,hs1_a1,hs1
    
    # If scale_log_base is used, the mapping is not linear, but a power law 
    #
    # n = N * f**(1/scale_log_base)
    #
    # When scale_log_base > 1 the dynamic range for values close to min is expanded. 
    # When scale_log_base < 1 the dynamic range for values close to max is expanded. 
    
    scale_log_base = 0.25
    
    <rules>
    <<include rule.exclude.hs1.conf>>
    </rules>
    
    </plot>
    
    # The other three heatmap tracks are the same as the one above, except
    # that each uses a different color list and var(id) condition to show
    # the number of links to/from hs2, hs3 and hs4.
    
    <plot>
    type  = heatmap
    file  = data/5/segdup.hs1234.heatmap.txt
    r1    = 0.90r
    r0    = 0.89r
    color = hs2_a5,hs2_a4,hs2_a3,hs2_a2,hs2_a1,hs2
    scale_log_base = 0.25
    
    <rules>
    <<include rule.exclude.hs1.conf>>
    
    # Show only data points that have id=hs2
    <rule>
    condition = var(id) ne "hs2"
    show      = no
    </rule>
    
    </rules>
    
    </plot>
    
    <plot>
    type  = heatmap
    file  = data/5/segdup.hs1234.heatmap.txt
    r1    = 0.91r
    r0    = 0.90r
    color = hs3_a5,hs3_a4,hs3_a3,hs3_a2,hs3_a1,hs3
    scale_log_base = 0.25
    
    <rules>
    <<include rule.exclude.hs1.conf>>
    
    # Show only data points that have id=hs3 
    <rule>
    condition = var(id) ne "hs3"
    show      = no
    </rule>
    
    </rules>
    
    </plot>
    
    <plot>
    type  = heatmap
    file  = data/5/segdup.hs1234.heatmap.txt
    r1    = 0.92r
    r0    = 0.91r
    color = hs4_a5,hs4_a4,hs4_a3,hs4_a2,hs4_a1,hs4
    scale_log_base = 0.25
    
    <rules>
    <<include rule.exclude.hs1.conf>>
    
    # Show only data points that have id=hs4
    <rule>
    condition = var(id) ne "hs4"
    show      = no
    </rule>
    
    </rules>
    
    </plot>
    
    <plot>
    type = histogram
    file = data/5/segdup.hs1234.hist.txt
    r1   = 0.88r
    r0   = 0.81r
    
    fill_color = vdgrey
    extend_bin = no
    
    <rules>
    <<include rule.exclude.hs1.conf>>
    </rules>
    
    <<include backgrounds.conf>>
    
    </plot>
    
    <plot>
    type = histogram
    file = data/5/segdup.hs1234.stacked.txt
    r1   = 0.99r
    r0   = 0.92r
    fill_color  = hs1,hs2,hs3,hs4
    orientation = in
    extend_bin  = no
    
    <rules>
    <<include rule.exclude.hs1.conf>>
    </rules>
    
    <<include axes.conf>>
    
    </plot>
    
    </plots>
    
    <links>
    
    <link>
    file          = data/5/segdup.txt
    radius        = 0.8r
    bezier_radius = 0r
    color         = black_a4
    thickness     = 2
    
    <rules>
    <<include rules.link.conf>>
    </rules>
    
    </link>
    
    </links>
    
    <<include ideogram.conf>>
    <<include ticks.conf>>
    
    <image>
    <<include etc/image.conf>>                
    </image>
    
    <<include etc/colors_fonts_patterns.conf>> 
    <<include etc/housekeeping.conf>> 
    data_out_of_range* = trim
    

  

* * *

### axes.conf

    
    
    <axes>
    # Show axes only on ideograms that have data for this track
    show = data
    
    thickness = 1
    color     = lgrey
    <axis>
    spacing   = 0.1r
    </axis>
    <axis>
    spacing   = 0.2r
    color     = grey
    </axis>
    <axis>
    position  = 0.5r
    color     = red
    </axis>
    <axis>
    position  = 0.85r
    color     = green
    thickness = 2
    </axis>
    
    </axes>
    

  

* * *

### backgrounds.conf

    
    
    <backgrounds>
    # Show the backgrounds only for ideograms that have data
    show  = data
    <background>
    color = vvlgrey
    </background>
    <background>
    color = vlgrey
    y0    = 0.2r
    y1    = 0.5r
    </background>
    <background>
    color = lgrey
    y0    = 0.5r
    y1    = 0.8r
    </background>
    <background>
    color = grey
    y0    = 0.8r
    </background>
    
    </backgrounds>
    

  

* * *

### ideogram.conf

    
    
    <ideogram>
    
    <spacing>
    default = 0.005r
    </spacing>
    
    # Ideogram position, fill and outline
    radius           = 0.90r
    thickness        = 20p
    fill             = yes
    stroke_color     = dgrey
    stroke_thickness = 2p
    
    # Minimum definition for ideogram labels.
    
    show_label       = yes
    # see etc/fonts.conf for list of font names
    label_font       = default 
    label_radius     = 1.075r  # if ideogram radius is constant, and you'd like labels close to image edge, 
                               # use the dims() function to access the size of the image
                               # label_radius  = dims(image,radius) - 60p
    label_size       = 30
    label_parallel   = yes
    
    </ideogram>
    
    

  

* * *

### rule.exclude.hs1.conf

    
    
    <rule>
    condition = on(hs1)
    show      = no
    </rule>
    

  

* * *

### rules.link.conf

    
    
    <rule>
    condition     = var(intrachr)
    show          = no
    </rule>
    <rule>
    condition     = 1
    color         = eval(var(chr2))
    flow          = continue
    </rule>
    <rule>
    condition     = from(hs1)
    radius1       = 0.99r
    </rule>
    <rule>
    condition     = to(hs1)
    radius2       = 0.99r
    </rule>
    

  

* * *

### ticks.conf

    
    
    show_ticks          = yes
    show_tick_labels    = yes
    
    <ticks>
    radius           = 1r
    color            = black
    thickness        = 2p
    
    # the tick label is derived by multiplying the tick position
    # by 'multiplier' and casting it in 'format':
    #
    # sprintf(format,position*multiplier)
    #
    
    multiplier       = 1e-6
    
    # %d   - integer
    # %f   - float
    # %.1f - float with one decimal
    # %.2f - float with two decimals
    #
    # for other formats, see https://perldoc.perl.org/functions/sprintf.html
    
    format           = %d
    
    <tick>
    spacing        = 5u
    size           = 10p
    </tick>
    
    <tick>
    spacing        = 25u
    size           = 15p
    show_label     = yes
    label_size     = 20p
    label_offset   = 10p
    format         = %d
    </tick>
    
    </ticks>
    

  

* * *

