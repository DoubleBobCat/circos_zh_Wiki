---
author: DoubleCat
date: 2025-04-11
layout: post
category: highlights
title: Highlights
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

# 4 — Highlights

## 8\. Recipe 3 - Plot Axis Range Highlights

[Lesson](/documentation/tutorials/highlights/recipe3/lesson)
[Images](/documentation/tutorials/highlights/recipe3/images)
[Configuration](/documentation/tutorials/highlights/recipe3/configuration)

In this section, I'll look ahead and show how you can use highlights to
annotate 2D data plots (e.g. scatter plots).

By defining highlights to span the entire data domain (e.g. entire genome),
you can draw multiple instances of the highlight using different colors and
radial positions, in effect setting up a set of concentric circles that
provide radial axis highlights.

By drawing a scatter plot, for example, and synchronizing the radial extent of
the scatter plot with the position of the highlights, you can draw attention
to outlying data in your scatter plot.

    
    
    <highlight>
    file       = data/3/chr.highlights.colourless.txt
    r0 = 0.715r
    r1 = 0.725r
    fill_color = lred
    </highlight>
    
    <highlight>
    file       = data/3/chr.highlights.colourless.txt
    r0 = 0.725r
    r1 = 0.75r
    fill_color = lorange
    </highlight>
    
    <highlight>
    file       = data/3/chr.highlights.colourless.txt
    r0 = 0.75r
    r1 = 0.80r
    fill_color = lyellow
    </highlight>
    
    <highlight>
    file       = data/3/chr.highlights.colourless.txt
    r0 = 0.8r
    r1 = 0.9r
    fill_color = lgrey
    </highlight>
    
    <highlight>
    file       = data/3/chr.highlights.colourless.txt
    r0 = 0.9r
    r1 = 0.95r
    fill_color = lyellow
    </highlight>
    
    <highlight>
    file       = data/3/chr.highlights.colourless.txt
    r0 = 0.95r
    r1 = 0.975r
    fill_color = lorange
    </highlight>
    
    <highlight>
    file       = data/3/chr.highlights.colourless.txt
    r0 = 0.975r
    r1 = 0.985r
    fill_color = lred
    </highlight>
    

