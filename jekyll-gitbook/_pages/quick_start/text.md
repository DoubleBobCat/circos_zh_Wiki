---
author: DoubleCat
date: 2025-04-11
layout: post
category: quick_start
title: Quick Start
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

# 2 — Quick Start

## 8\. Text

[Lesson](/documentation/tutorials/quick_start/text/lesson)
[Images](/documentation/tutorials/quick_start/text/images)
[Configuration](/documentation/tutorials/quick_start/text/configuration)

Text tracks are a special 2-dimensional data track, which associates a text
label with a genomic position.

Like with other tracks, text is limited to a radial range by setting `r0` and
`r1`

    
    
    <plot>
    type  = text
    file  = data/6/genes.labels.txt
    r1    = 0.8r
    r0    = 0.6r
    ...
    </plot>
    

You must set the font for the track, as well as the size of the labels. You
can put in optional `padding` and `rpadding` to give the text margins.

    
    
    label_font = light
    label_size = 12p
    rpadding   = 5p
    

### text track rules

Rules for text tracks work in the same way as for all other track types.

In this example, I test the text label, via `var(value)`, with a regular
expression to make labels that contain "a" bold and those that contain "b"
blue. I combine the rules by using `flow=continue` for the first rule. This
way, a label can be both bold and blue.

    
    
    <rules>
    
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
    

