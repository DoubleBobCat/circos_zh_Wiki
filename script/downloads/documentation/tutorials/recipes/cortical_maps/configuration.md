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

## 19\. Cortical Maps

[Lesson](/documentation/tutorials/recipes/cortical_maps/lesson)
[Images](/documentation/tutorials/recipes/cortical_maps/images)
[Configuration](/documentation/tutorials/recipes/cortical_maps/configuration)

### circos.conf

    
    
    <<include ideogram.conf>>
    
    chromosomes_units = 100
    <<include ticks.conf>>
    
    <image>
    angle_offset* = -87
    <<include etc/image.conf>>
    </image>
    
    ### single genomes
    
    karyotype = data/segments.txt
    
    <<include segment.order.conf>>
    
    chromosomes_reverse = /.*-l/
    
    ###
    # HEATMAPS
    # If you aren't using heatmaps in your image (you have no measures associated with
    # parcelation regions), remove this section. Also turn of grids in etc/ticks.conf.
    
    hm_r      = 0.96
    hm_w      = 0.025
    hm_pad    = 0.005
    
    #hm_colors = greys-4-seq,greys-4-seq,greys-4-seq,greys-4-seq,greys-4-seq
    hm_colors = reds-4-seq,oranges-4-seq,greens-4-seq,blues-4-seq,purples-4-seq
    
    # HEATMAPS
    ###
    
    <plots>
    
    # Remove these lines if you don't have heatmaps.
    <<include heatmap.conf>>
    <<include heatmap.conf>>
    <<include heatmap.conf>>
    <<include heatmap.conf>>
    <<include heatmap.conf>>
    
    <plot>
    type       = text
    file       = data/structure.label.txt
    color      = black
    label_font = default
    label_size = 20
    r0         = 1r
    r1         = 1.5r
    rpadding   = 10p
    </plot>
    
    </plots>
    
    <links>
    
    <link>
    file          = data/links.txt
    
    # If you don't have heatmaps, change radius to
    # radius = dims(ideogram,radius_inner) 
    
    radius        = 0.825r # eval(sprintf("%fr",conf(hm_r)-counter(heatmap)*(conf(hm_w)+conf(hm_pad))+conf(hm_w)))
    bezier_radius = 0r
    bezier_radius_purity = 0.5
    crest         = 0.25
    thickness     = 2
    color         = black
    
    <rules>
    <rule>
    # this rule is part of variant #1
    # to use it, set use=yes and also adjust radius above to 0.7r
    use       = no
    condition = var(chr1) eq var(chr2)
    bezier_radius = 1r
    radius    = 0.71r
    flow      = continue
    </rule>
    <rule>
    condition = 1
    thickness = eval(remap_int(var(score),0,1,1,5)) 
    flow      = continue
    </rule>
    <rule>
    condition = var(type) == 0 
    color     = eval(sprintf("greys-5-seq-%d",remap_int(var(score),0,1,1,5)))
    </rule>
    <rule>
    condition = var(type) == 1
    color     = eval(sprintf("reds-5-seq-%d",remap_int(var(score),0,1,1,5)))
    </rule>
    </rules>
    
    </link>
    
    </links>
    
    <<include etc/colors_fonts_patterns.conf>>
    <colors>
    <<include color.brain.conf>>
    </colors>
    
    restrict_parameter_names* = no
    <<include etc/housekeeping.conf>>
    

  

* * *

### bands.conf

    
    
    show_bands            = yes
    fill_bands            = yes
    band_stroke_thickness = 1
    band_stroke_color     = black
    band_transparency     = 0
    

  

* * *

### color.brain.conf

    
    
    trfpogs = 255,153,153
    fmargs = 204,0,51
    mfs = 255,153,51
    lors = 102,0,0
    sbors = 255,51,102
    ors = 255,204,204
    rg = 255,204,153
    inffgorp = 153,51,0
    mfg = 255,255,51
    org = 255,255,153
    inffgtrip = 255,0,0
    inffs = 153,102,0
    medors = 255,102,0
    supfg = 255,102,102
    supfs = 204,153,0
    inffgopp = 255,204,0
    infprcs = 255,153,0
    supprcs = 255,0,102
    prcg = 204,102,0
    sbcgs = 255,102,153
    cs = 255,51,0
    alshorp = 0,255,204
    acirins = 102,255,255
    alsverp = 0,255,255
    shoing = 51,255,204
    supcirins = 0,153,153
    loingcins = 0,204,204
    infcirins = 0,102,102
    posls = 204,255,255
    acggs = 255,255,180
    macggs = 255,240,191
    sbcag = 255,153,200
    percas = 255,164,200
    mposcggs = 255,224,203
    cgsmarp = 255,192,201
    posdcgg = 255,175,201
    posvcgg = 255,208,202
    tpo = 255,204,255
    popl = 204,153,255
    suptglp = 153,51,255
    hg = 102,0,102
    atrcos = 153,0,204
    trts = 255,153,255
    mtg = 255,102,204
    tpl = 153,0,153
    inftg = 255,0,255
    infts = 204,0,153
    supts = 204,51,255
    poscg = 204,255,204
    sumarg = 204,255,102
    pacls = 204,255,153
    poscs = 153,255,0
    js = 153,204,0
    sbps = 102,153,0
    intpstrps = 51,255,51
    suppl = 153,255,153
    prcun = 204,255,0
    angg = 0,255,0
    pocs = 204,255,51
    pahipg = 204,204,255
    coslins = 153,204,255
    locts = 153,153,255
    fug = 102,102,255
    ccs = 102,153,255
    ling = 102,204,255
    aocs = 51,51,255
    infocgs = 51,153,255
    supocstrocs = 0,102,255
    postrcos = 51,102,255
    cun = 0,153,255
    mocg = 0,204,244
    mocslus = 0,51,255
    supocg = 0,0,255
    ocpo = 0,0,153
    pu = 32,32,32
    pal = 64,64,64
    can = 96,96,96
    nacc = 128,128,128
    amg = 159,159,159
    tha = 191,191,191
    hip = 223,223,223
    ceb = 255,64,0
    bst = 207,255,48
    

  

* * *

### heatmap.conf

    
    
    <plot>
    type         = heatmap
    file         = data/measure.counter(heatmap).txt
    color        = eval((split(",","conf(hm_colors)"))[counter(heatmap)])
    r1           = eval(sprintf("%fr",conf(hm_r)-counter(heatmap)*(conf(hm_w)+conf(hm_pad))))
    r0           = eval(sprintf("%fr",conf(hm_r)-counter(heatmap)*(conf(hm_w)+conf(hm_pad))+conf(hm_w)))
    
    stroke_color = white
    stroke_thickness = 3
    </plot>
    

  

* * *

### ideogram.conf

    
    
    <ideogram>
    
    <spacing>
    default = 0.005r
    <pairwise fro-l fro-r>
    spacing = 5r
    </pairwise>
    </spacing>
    
    <<include ideogram.position.conf>>
    <<include ideogram.label.conf>>
    <<include bands.conf>>
    
    </ideogram>
    
    

  

* * *

### ideogram.label.conf

    
    
    show_label       = yes
    label_font       = default
    label_radius     = dims(image,radius)-30p
    label_size       = 24
    label_parallel   = yes
    label_case       = upper
    
    # you can format the label by using properties
    # of the ideogram, accessible with var(PROPERTY):
    #
    # chr, chr_with_tag, chrlength, display_idx, end, idx, 
    # label, length, reverse, scale, size, start, tag
    
    #label_format     = eval(sprintf("region %s",var(label)))
    

  

* * *

### ideogram.position.conf

    
    
    radius           = 0.85r
    thickness        = 75p
    fill             = no
    stroke_thickness = 1
    stroke_color     = black
    

  

* * *

### segment.order.conf

    
    
    chromosomes_order = fro-r,ins-r,lim-r,tem-r,par-r,occ-r,sbc-r,ceb-r,bst,ceb-l,sbc-l,occ-l,par-l,tem-l,lim-l,ins-l,fro-l
    

  

* * *

### ticks.conf

    
    
    show_ticks          = yes
    show_tick_labels    = yes
    show_grid           = yes
    
    <ticks>
    
    radius           = dims(ideogram,radius_outer)
    color            = black
    thickness        = 2p
    size             = 0
    
    <tick>
    spacing        = 0.5u
    size           = 5p
    grid           = yes
    grid_color     = black
    grid_thickness = 1p
    grid_start     = 1r-conf(ideogram,thickness)
    grid_end       = 0.825r
    </tick>
    
    <tick>
    spacing        = 1u
    </tick>
    
    </ticks>
    

  

* * *

