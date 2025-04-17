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

## 8\. Text

[Lesson](/documentation/tutorials/quick_start/text/lesson)
[Images](/documentation/tutorials/quick_start/text/images)
[Configuration](/documentation/tutorials/quick_start/text/configuration)

### circos.conf

    
    
    # 1.8 TEXT TRACKS
    
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
    
    <plot>
    type  = text
    file  = data/6/genes.labels.txt
    
    # Like with other tracks, text is limited to a radial range by setting
    # r0 and r1.
    #
    # Individual labels can be repositioned automatically with in a
    # position window to fit more labels, without overlap. This is an
    # advanced feature - see the 2D Track text tutorials.
    
    r1    = 0.8r
    r0    = 0.6r
    
    # For a list of fonts, see etc/fonts.conf in the Circos distribution.
    
    label_font = light
    label_size = 12p
    
    # padding  - text margin in angular direction
    # rpadding - text margin in radial direction
    
    rpadding   = 5p
    
    # Short lines can be placed before the label to connect them to the
    # label's position. This is most useful when the labels are
    # rearranged.
    
    show_links     = no
    link_dims      = 0p,2p,5p,2p,2p
    link_thickness = 2p
    link_color     = black
    
    <rules>
    <<include rule.exclude.hs1.conf>>
    
    # Text can be tested with var(value).
    
    <rule>
    condition  = var(value) =~ /a/i
    label_font = bold
    flow       = continue
    </rule>
    <rule>
    condition  = var(value) =~ /b/i
    color      = blue
    </rule>
    </rules>
    
    </plot>
    
    <plot>
    type  = heatmap
    file  = data/5/segdup.hs1234.heatmap.txt
    r1    = 0.89r
    r0    = 0.88r
    color = hs1_a5,hs1_a4,hs1_a3,hs1_a2,hs1_a1,hs1
    scale_log_base = 0.25
    
    <rules>
    <<include rule.exclude.hs1.conf>>
    </rules>
    
    </plot>
    
    <plot>
    type  = heatmap
    file  = data/5/segdup.hs1234.heatmap.txt
    r1    = 0.90r
    r0    = 0.89r
    color = hs2_a5,hs2_a4,hs2_a3,hs2_a2,hs2_a1,hs2
    scale_log_base = 0.25
    
    <rules>
    <<include rule.exclude.hs1.conf>>
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
    radius        = 0.6r
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

