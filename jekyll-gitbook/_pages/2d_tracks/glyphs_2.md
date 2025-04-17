---
author: DoubleCat
date: 2025-04-11
layout: post
category: 2d_tracks
title: 2D Data Tracks
---

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

## 10\. Glyphs — Part II

[Lesson](/documentation/tutorials/2d_tracks/glyphs_2/lesson)
[Images](/documentation/tutorials/2d_tracks/glyphs_2/images)
[Configuration](/documentation/tutorials/2d_tracks/glyphs_2/configuration)

Modifying labels into symbols is ideal for making a general glyph tracks. For
example, consider a list of genes (`data/6/genes.glyph.txt`).

    
    
    ...
    hs12 56428271 56432431 CDK4_cancer
    hs12 64504506 64595566 HMGA2_cancer
    hs12 64504506 64638901 P52926_cancer
    ...
    hs10 108323411 108914282 SORCS1_omim
    hs10 111614513 111673192 XPNPEP1_omim
    hs10 111755715 111885310 ADD3_omim
    ...
    hs7 139864688 139948811 DENND2A_other
    hs7 140019421 140041377 ADCK2_other
    hs7 140042949 140052913 NDUFB2_other
    ...
    

I've added _cancer to those genes that are in the Cancer Census, _omim to any
others that are in the OMIM list (disease-related), and _other to the
remaining. Using the rules below, genes become glyphs colored by their names.

    
    
    <rules>
    
    flow = continue
    
    <rule>
    condition  = var(value) =~ /cancer/
    color      = red
    </rule>
    
    <rule>
    condition  = var(value) =~ /omim/
    color      = green
    </rule>
    
    <rule>
    condition  = var(value) =~ /other/
    color      = blue
    </rule>
    
    <rule>
    condition  = 1
    value      = N
    </rule>
    
    </rules>
    

Individual gene groups (cancer, omim, other) can be split into multiple tracks
by setting a rule to hide all genes except one. For example, this track shows
only the cancer genes outside the circle

    
    
    <plot>
    
    r0 = 1r+10p
    r1 = 1r+200p
    color = red
    ...
    
    <rules>
    
    <rule>
    condition  = var(value) !~ /cancer/
    # hide anything that doesn't match "cancer"
    show = no
    </rule>
    
    <rule>
    condition  = 1
    # circle
    value = N
    </rule>
    
    </rules>
    
    </plot>
    

### using glyphs to plot density

Finally, let's look at an example where the size of the glyph encodes density
of data points. While Circos won't calculate the density for you, you can pre-
process your data and encode the density as the label size.

In the `data/6/gene.density.txt` file, the number of gene entries for each of
cancer, omim and other groups (per Mb) is reported as the `label_size`.

    
    
    ...
    hs1 3000000 3000000 cancer label_size=1
    hs1 6000000 6000000 cancer label_size=2
    ...
    hs1 1000000 1000000 omim label_size=9
    hs1 2000000 2000000 omim label_size=14
    ...
    hs1 1000000 1000000 other label_size=26
    hs1 2000000 2000000 other label_size=10
    ...
    

Using a rule, you can remap the label_size to another value. The original
label_size values range from 1p to 42p.

    
    
    # linear remap to [6,50]
    label_size = eval(remap_int(var(label_size),1,42,6,50))
    
    # ... with shallower increase
    label_size = eval(remap_int(sqrt(var(label_size)),1,sqrt(42),6,50))
    
    # ... with steeper increase
    label_size = eval(remap_int(var(label_size)**2,1,42**2,6,50))
    

