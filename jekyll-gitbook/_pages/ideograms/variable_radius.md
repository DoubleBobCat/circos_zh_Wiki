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

## 8\. Variable Radius

[Lesson](/documentation/tutorials/ideograms/variable_radius/lesson)
[Images](/documentation/tutorials/ideograms/variable_radius/images)
[Configuration](/documentation/tutorials/ideograms/variable_radius/configuration)

By default, every ideogram is placed at the same radial position. This is
controlled by the radius parameter within the <ideogram> block (conventionally
found in `ideogram.conf`).

    
    
    <ideogram>
    ...
    radius = 0.85r
    ...
    </ideogram>
    

The value is relative to the image radius.

You can place individual ideograms at different radial positions by using the
`chromosomes_radius` parameter in the root of the configuration tree.

    
    
    chromosomes_radius = hs1:0.5r;hs2:0.55r;hs3:0.6r;hs4:0.65r;hs5:0.7r;hs6:0.75r;hs7:0.8r;hs8:0.85r;hs9:0.9r;hs10:0.95r
    

The radial position values in this parameter are relative to the default
ideogram radius, defined by radius in the <ideogram> block.

For example, if the image radius is `1500p` and the default ideogram radius is
`0.9r`, then all ideograms are at 1350 pixels (1500×0.9) from the center. Now,
if chromosomes_radius further specifies `hs1:0.5r`, then `hs1` will appear at
675 pixels from the center (1500×0.9×0.5).

Once the radial position of an ideogram has been redefined using
`chromosomes_radius`, all features associated with that ideogram (plots,
links, text, etc) will be automatically relocated to match the new ideogram
position. In other words, you do not need to remember that specific ideograms
may be at different positions.

### setting radius for tagged ideograms

If you've tagged your ideograms when creating regions,

    
    
    chromosomes = hs1[a]:0-50;hs1[b]:150-);hs2[c]:0-50;hs2[d]:150-);hs3[e]
    

then adjusting the radius of any region can be done by using the tag

    
    
    chromosomes_radius = hs1:0.8r;a:0.9r;d:0.8r
    

The radius values will be processed in order, with subsequent radius values
overriding previous ones. For example, each region of `hs1` will be set to
0.8r, but the region tagged by `a` will be 0.9r.

### suppressing ticks and tick labels

When decreasing the radius of an ideogram you may find that the ticks and
their labels crowd together. In these cases, it is useful to use the
`tick_separation` and `label_separation` parameters in the <ticks> block to
define the minimum distance between ticks and their labels.

