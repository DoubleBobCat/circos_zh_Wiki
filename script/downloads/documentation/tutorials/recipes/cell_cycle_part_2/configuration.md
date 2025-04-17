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

## 21\. Cell Cycle — Part 2

[Lesson](/documentation/tutorials/recipes/cell_cycle_part_2/lesson)
[Images](/documentation/tutorials/recipes/cell_cycle_part_2/images)
[Configuration](/documentation/tutorials/recipes/cell_cycle_part_2/configuration)

### circos.conf

    
    
    <<include etc/colors_fonts_patterns.conf>>
    
    <<include ideogram.conf>>
    # choose one
    <<include ticks.absolute.conf>>
    #<<include ticks.relative.conf>>
    
    <image>
    <<include etc/image.conf>>
    </image>
    
    chromosomes_units           = 1
    chromosomes_display_default = yes
    
    karyotype                   = cycle.txt
    
    #chromosomes                 = cycle[g1]:0-45;cycle[s]:45-80;cycle[g2]:80-95;cycle[m]:95-100
    #chromosomes                 = cycle[g1]:0-20;cycle[s]:20-80;cycle[g2]:80-95;cycle[m]:95-100
    #chromosomes                 = cycle[g1]:0-20;cycle[s]:20-40;cycle[g2]:40-95;cycle[m]:95-100
    chromosomes                 = cycle[g1]:0-20;cycle[s]:20-40;cycle[g2]:40-70;cycle[m]:70-100
    
    palette = greys-6-seq
    
    <phases>
    g1 = 3
    s  = 4
    g2 = 5
    m  = 6
    </phases>
    
    # g1, s, g2, m are tags defined in 'chromosomes' above
    chromosomes_color = g1=conf(palette)-conf(phases,g1),s=conf(palette)-conf(phases,s),g2=conf(palette)-conf(phases,g2),m=conf(palette)-conf(phases,m)
    
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

### break.conf

    
    
    axis_break_at_edge = yes
    axis_break         = yes
    axis_break_style   = 2
    
    <break_style 1>
    stroke_color     = black
    fill_color       = blue
    thickness        = 0.25r
    stroke_thickness = 2p
    </break_style>
    
    <break_style 2>
    stroke_color     = black
    stroke_thickness = 5p
    thickness        = 2r
    </break_style>
    

  

* * *

### ideogram.conf

    
    
    <ideogram>
    
    <spacing>
    
    default = 0.005r
    break   = 1r
    
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
    
    label_format     = eval(sprintf("%s",var(tag)))
    

  

* * *

### ideogram.position.conf

    
    
    radius           = 0.90r
    thickness        = 100p
    fill             = yes
    fill_color       = black
    stroke_thickness = 2
    stroke_color     = dgrey
    

  

* * *

### ticks.absolute.conf

    
    
    show_ticks          = yes
    show_tick_labels    = yes
    show_grid           = yes
    
    <ticks>
    
    radius         = dims(ideogram,radius_outer)
    multiplier     = 1
    color          = dgrey
    thickness      = 2p
    size           = 15p
    
    grid           = yes
    grid_start     = dims(ideogram,radius_outer)
    grid_end       = dims(ideogram,radius_inner)
    grid_color     = white
    
    format         = %d
    suffix         = %
    
    label_size     = 26p
    label_offset   = 5p
    
    <tick>
    spacing        = 1u
    grid_thickness = 1p
    </tick>
    
    <tick>
    spacing        = 5u
    grid_thickness = 1p
    show_label     = yes
    </tick>
    
    <tick>
    spacing        = 10u
    show_label     = yes
    grid_thickness = 2p
    </tick>
    
    </ticks>
    
    offsets* = 0,1
    

  

* * *

### ticks.relative.conf

    
    
    show_ticks          = yes
    show_tick_labels    = yes
    show_grid           = yes
    
    <ticks>
    radius         = dims(ideogram,radius_outer)
    multiplier     = 0.1
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
    rdivisor       = ideogram
    suffix         = %
    
    label_size     = 26p
    label_offset   = 5p
    
    <tick>
    rspacing       = 0.05
    grid_thickness = 1p
    </tick>
    
    <tick>
    rspacing       = 0.10
    show_label     = yes
    grid_thickness = 2p
    </tick>
    
    </ticks>
    

  

* * *

