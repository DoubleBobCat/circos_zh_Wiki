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

## 20\. Cell Cycle — Part 1

[Lesson](/documentation/tutorials/recipes/cell_cycle_part_1/lesson)
[Images](/documentation/tutorials/recipes/cell_cycle_part_1/images)
[Configuration](/documentation/tutorials/recipes/cell_cycle_part_1/configuration)

### circos.conf

    
    
    <<include etc/colors_fonts_patterns.conf>>
    
    <<include ideogram.conf>>
    <<include ticks.conf>>
    
    <image>
    <<include etc/image.conf>>
    </image>
    
    chromosomes_units           = 10
    chromosomes_display_default = yes
    chromosomes_scale           = g1=0.45,s=0.35,g2=0.15,m=0.05
    
    karyotype         = phases.txt
    
    palette           = greys-6-seq
    <phases>
    g1 = 3
    s  = 4
    g2 = 5
    m  = 6
    </phases>
    
    chromosomes_color = g1=conf(palette)-conf(phases,g1),s=conf(palette)-conf(phases,s),g2=conf(palette)-conf(phases,g2),m=conf(palette)-conf(phases,m)
    
    #don't show phase m
    chromosomes                 = -m          
    
    <links>
    
    # connections between genes
    <link>
    file          = links.txt
    
    radius        = 0.95r
    bezier_radius = 0r
    
    # shorter links will be drawn closer
    # to the edge of the circle
    bezier_radius_purity = 0.1
    crest                = 1
    thickness            = 3
    
    <rules>
    
    <rule>
    condition = var(type) == 1
    color     = red
    </rule>
    <rule>
    condition = var(type) == 2
    color     = blue
    </rule>
    </rules>
    
    </link>
    </links>
    
    <plots>
    
    <plot>
    # gene labels
    
    type = text
    file = genes.txt
    
    r0   = 0.95r
    r1   = 1.5r
    
    label_size     = 36
    label_font     = bold
    
    show_links     = yes
    link_dims      = 0p,200p,20p,10p,20p
    link_thickness = 3
    link_color     = black
    
    <rules>
    <rule>
    condition = 1
    value     = eval(var(name))
    </rule>
    </rules>
    
    </plot>
    
    <plot>
    # circular glyph at start of gene label
    
    type = scatter
    file = genes.txt
    
    r0   = 0.95r
    r1   = 0.95r
    
    glyph = circle
    
    glyph_size       = 36
    color            = white
    stroke_color     = black
    stroke_thickness = 2
    
    <rules>
    <rule>
    condition = var(type) == 1
    color     = blues-5-seq-4
    </rule>
    <rule>
    condition = var(type) == 2
    color     = reds-5-seq-4
    </rule>
    </rules>
     
    </plot>
    
    </plots>
    
    <<include etc/housekeeping.conf>>
    restrict_parameter_names* = no
    

  

* * *

### ideogram.conf

    
    
    <ideogram>
    
    <spacing>
    
    default = 0.005r
    
    </spacing>
    
    <<include ideogram.position.conf>>
    <<include ideogram.label.conf>>
    
    </ideogram>
    
    

  

* * *

### ideogram.label.conf

    
    
    show_label       = yes
    label_font       = bold
    label_radius     = (dims(ideogram,radius_inner)+dims(ideogram,radius_outer)-conf(ideogram,label_size))/2
    label_with_tag   = yes
    label_size       = 72
    label_color      = white
    label_parallel   = yes
    label_case       = upper
    
    # you can format the label by using properties
    # of the ideogram, accessible with var(PROPERTY):
    #
    # chr, chr_with_tag, chrlength, display_idx, end, idx, 
    # label, length, reverse, scale, size, start, tag
    
    #label_format     = eval(sprintf("chr%s",var(label)))
    

  

* * *

### ideogram.position.conf

    
    
    radius           = 0.90r
    thickness        = 100p
    fill             = yes
    fill_color       = black
    stroke_thickness = 2
    stroke_color     = dgrey
    

  

* * *

### ticks.conf

    
    
    show_ticks          = yes
    show_tick_labels    = yes
    show_grid           = yes
    
    <ticks>
    radius         = dims(ideogram,radius_outer)
    
    color          = dgrey
    thickness      = 2p
    size           = 15p
    
    grid           = yes
    grid_start     = dims(ideogram,radius_outer)
    grid_end       = dims(ideogram,radius_inner)
    grid_color     = white
    
    spacing_type   = relative
    label_relative = yes
    format         = %d
    rmultiplier    = 100
    suffix         = %
    
    <tick>
    rspacing       = 0.05
    grid_thickness = 1p
    </tick>
    
    <tick>
    rspacing       = 0.10
    show_label     = yes
    label_size     = 26p
    label_offset   = 5p
    grid_thickness = 2p
    </tick>
    
    </ticks>
    

  

* * *

