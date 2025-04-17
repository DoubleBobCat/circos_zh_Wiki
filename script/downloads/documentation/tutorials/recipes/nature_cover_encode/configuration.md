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

## 22\. Nature Cover Encode Diagram

[Lesson](/documentation/tutorials/recipes/nature_cover_encode/lesson)
[Images](/documentation/tutorials/recipes/nature_cover_encode/images)
[Configuration](/documentation/tutorials/recipes/nature_cover_encode/configuration)

### circos.conf

    
    
    <<include etc/colors_fonts_patterns.conf>>
    
    <colors>
    chr1*  = 163,132,130
    chr2*  = 188,162,118
    chr3*  = 216,196,96
    chr4*  = 233,212,56
    chr5*  = 229,229,50
    chr6*  = 212,222,56
    chr7*  = 195,215,57
    chr8*  = 177,209,58
    chr9*  = 160,204,61
    chr10* = 139,198,61
    chr11* = 128,193,95
    chr12* = 115,186,126
    chr13* = 102,183,152
    chr14* = 91,178,176
    chr15* = 61,174,199
    chr16* = 36,170,224
    chr17* = 75,129,194
    chr18* = 85,111,180
    chr19* = 92,92,168
    chr20* = 98,70,156
    chr21* = 101,45,145
    chr22* = 121,74,141
    chrx*  = 140,104,137
    </colors>
    
    <<include ideogram.conf>>
    #<<include ticks.conf>>
    
    <image>
    <<include etc/image.conf>>
    background* = black
    </image>
    
    chromosomes_units           = 1000000
    chromosomes_display_default = yes
    chromosomes                 = -hsY
    
    karyotype = data/karyotype/karyotype.human.txt
    
    plot_width   = 80 # 35 if drawing 20 plots
    plot_padding = 25 # 20 if drawing 20 plots
    num_plots    = 6  # 20 if drawing 20 plots
    
    <plots>
    
    type             = highlight
    file             = bins.txt
    stroke_thickness = 0
    
    <<include plot.conf>>
    <<include plot.conf>>
    <<include plot.conf>>
    <<include plot.conf>>
    <<include plot.conf>>
    <<include plot.conf>>
    
    # To draw 20 plots, comment the <<include plot.conf>> lines above and use these:
    
    #<<include plot.10.conf>>
    #<<include plot.10.conf>>
    
    </plots>
    
    <<include etc/housekeeping.conf>>
    

  

* * *

### ideogram.conf

    
    
    <ideogram>
    
    <spacing>
    
    default = 0.0030r
    
    </spacing>
    
    <<include ideogram.position.conf>>
    
    </ideogram>
    
    

  

* * *

### ideogram.label.conf

    
    
    show_label       = no
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

    
    
    radius           = dims(image,radius)-35p
    thickness        = 80p
    fill             = yes
    fill_color       = black
    stroke_thickness = 0
    stroke_color     = black
    

  

* * *

### plot.10.conf

    
    
    <<include plot.conf>>
    <<include plot.conf>>
    <<include plot.conf>>
    <<include plot.conf>>
    <<include plot.conf>>
    <<include plot.conf>>
    <<include plot.conf>>
    <<include plot.conf>>
    <<include plot.conf>>
    <<include plot.conf>>
    

  

* * *

### plot.conf

    
    
    <plot>
    r1   = dims(ideogram,radius_inner)-conf(plot_padding)*eval(remap(counter(plot),0,conf(num_plots),1,0.9))-eval((conf(plot_width)+conf(plot_padding))*counter(plot)*eval(remap(counter(plot),0,conf(num_plots),1,0.9)))
    r0   = conf(.,r1)-conf(plot_width)*eval(remap(counter(plot),0,conf(num_plots),1,0.9))
    post_increment_counter = plot:1
    <<include rules.conf>>
    </plot>
    

  

* * *

### rules.conf

    
    
    <rules>
    <rule>
    
    # Multiple conditions are evaluated using AND. That is, they all
    # have to be true for the rule to trigger.
    
    # The first condition tests that bins are further than 5 Mb from the
    # start and end of each ideogram.  This ensures that the color
    # for the first/last bin will be the same as the ideogram.
    
    condition  = var(start) >= 5e6 && var(end) < chrlen(var(chr))-5e6 
    
    # The probability that the second condition is true is proportional to
    # the track counter. Bins in inner tracks are more likely to trigger
    # this rule.  Here, rand() is a uniformly distributed random number in
    # the range [0,1).
    
    condition  = rand() < remap(counter(plot),0,conf(num_plots)-1,1/conf(num_plots),1)
    
    # If this rule is true, the color of the bin is changed to that of a
    # random ideogram.
    
    fill_color = eval("chr" . (sort {rand() <=> rand()} (1..22,"x"))[0])
    </rule>
    
    # If the above rule is not true, the color of the bin is assigned to
    # that of its ideogram.
    
    <rule>
    condition  = 1
    fill_color = eval("chr" . lc substr(var(chr),2))
    </rule>
    </rules>
    

  

* * *

### ticks.conf

    
    
    show_ticks          = no
    show_tick_labels    = no
    
    <ticks>
    radius           = dims(ideogram,radius_outer)
    tick_separation  = 3p
    label_separation = 1p
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

