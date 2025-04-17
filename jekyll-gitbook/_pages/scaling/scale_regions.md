---
author: DoubleCat
date: 2025-04-11
layout: post
category: scaling
title: Axis Scaling
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

# 8 — Axis Scaling

## 3\. Adjusting Scale for Regions

[Lesson](/documentation/tutorials/scaling/scale_regions/lesson)
[Images](/documentation/tutorials/scaling/scale_regions/images)
[Configuration](/documentation/tutorials/scaling/scale_regions/configuration)

Before I get into local scale adjustment in the next tutorial, I want to cover
a simple way to adjust the scale in a region of an ideogram.

In this example, I have drawn 0-60 Mb regions of chromosomes 1 and 2, by
breaking them up into three regions each. The resulting image has 6 ideograms,
3 per chromosome. Using chromosomes_scale, the scale for the ideograms is
adjusted like in the previous example.

    
    
    chromosomes = hs1[a]:0-20;hs2[b]:0-20;hs1[c]:20-40;hs2[d]:20-40;hs1[e]:40-60;hs2[f]:40-60
    chromosomes_scale = a:0.5;b:0.5;e:5;f:5
    

Note that ideogram tags (a, b, c, ...) are required because we have multiple
idoegrams per chromosome and it is not sufficient to use the chromosome name
to uniquely specify an ideogram.

For example, if you would like to expand (or contract) the scale on a specific
region of an ideogram using global scale adjustment, break the ideogram into
multiple region that demarcate your region of interst and apply a new scale to
the region. For example, here's a way to zoom in on the 50-60Mb region on chr1
by 10x.

    
    
    chromosomes = hs1[a]:0-50;hs1[b]:50-60;hs1[c]:60-)
    chromosomes_scale = b:10
    

Note the 60-) syntax in the chromosome range field. This means from 60 to the
end of the chromosome, and saves you remembering the exact size of the
chromosome. The size of each chromosome is defined in the karyotype file.

