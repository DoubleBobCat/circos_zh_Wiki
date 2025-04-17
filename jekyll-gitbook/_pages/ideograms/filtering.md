---
author: DoubleCat
date: 2025-04-11
layout: post
category: ideograms
title: Drawing Ideograms
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

# 3 — Drawing Ideograms

## 3\. Filtering

[Lesson](/documentation/tutorials/ideograms/filtering/lesson)
[Images](/documentation/tutorials/ideograms/filtering/images)
[Configuration](/documentation/tutorials/ideograms/filtering/configuration)

To remove ideograms from the image, the "chromosomes" and
"chromosomes_display_default" configuration parameters are used.

### chromosomes_display_default

If this is set, then any ideograms not explicitly excluded will be drawn.
Setting this flag is useful if you want to exclude a few ideograms, but draw
the majority of others.

### chromosomes

This field is used identify which ideograms to draw and/or exclude. When
referring to ideograms, always use the ID of the ideogram as defined in the
karyotype file (not the ideogram's text label).

For example,

    
    
    chromosomes = hs1;hs2;hs3
    

will draw only the ideograms listed. To exclude an ideogram, preceed the ID
with "-". Thus, to draw all ideograms but exclude those drawn above

    
    
    chromosomes = -hs1;-hs2;-hs3
    chromosomes_display_default = yes
    

The order in which the ideogram IDs appear in the "chromosomes" parameter does
not influence the order in which they are drawn. To apply a different order,
use chromosomes_order, discussed in another tutorial. Without specifying the
order, the ideograms are drawn in the order of appearance in the karyotype
file.

