---
author: DoubleCat
date: 2025-04-11
layout: post
category: links
title: Links and Relationships
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

# 6 — Links and Relationships

## 6\. Link Rules - Part III

[Lesson](/documentation/tutorials/links/rules3/lesson)
[Images](/documentation/tutorials/links/rules3/images)
[Configuration](/documentation/tutorials/links/rules3/configuration)

Rules can affect the geometry of a link. This example expands on the previous
one and modifies the position of intrachromosomal links to face outward.

The new rules sample intrachromosomal links. The first of these rules, hides
any whose ends are within 1 Mb of each other. Here the `var(pos1)` and
`var(pos2)` are used to sample the middle of the start and end of the link.

The second rule applies to intrachromosomal links whose ends are within 50 Mb.
These are colored blue and made to face outward by setting their
`bezier_radius` larger than 1. The next performs a similar function but for
any links left within 100 Mb.

The last rule suppresses the display of any other intrachromosomal links (i.e.
those whose ends are more than 100 Mb apart).

    
    
    <rule>
    condition  = var(intrachr)
    condition  = abs(var(pos1) - var(pos2)) < 1Mb
    show       = no
    </rule>
    
    <rule>
    condition  = var(intrachr)
    condition  = abs(var(pos1) - var(pos2)) < 50Mb
    color         = dblue_a2
    bezier_radius = 1.1r
    bezier_radius_purity = 0.25
    </rule>
    
    <rule>
    condition  = var(intrachr)
    condition  = abs(var(pos1) - var(pos2)) < 100Mb
    color         = dgreen_a2
    crest         = 2
    bezier_radius = 0.75r
    bezier_radius_purity = 0.25
    </rule>
    
    <rule>
    condition  = var(intrachr)
    show       = no
    </rule>
    

