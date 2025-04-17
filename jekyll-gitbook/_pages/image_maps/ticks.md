---
author: DoubleCat
date: 2025-04-11
layout: post
category: image_maps
title: Image Maps
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

# 11 — Image Maps

## 3\. Clickable Tick Marks

[Lesson](/documentation/tutorials/image_maps/ticks/lesson)
[Images](/documentation/tutorials/image_maps/ticks/images)
[Configuration](/documentation/tutorials/image_maps/ticks/configuration)

To create links that access regions of an ideogram, define a `url` parameter
within a <tick> mark block.

    
    
    <tick>
    spacing  = 25u
    size     = 10p
    ...
    url      = script?type=tick&start=[start]&end=[end]
    </tick>
    

With this setting, the area in the image map associated with the tick will be
a slice that extends from the base of the tick (usually outer ideogram
radius), to the end of the tick (defined by the tick size). Since this may be
too small, you can use the `map_size` parameter to extend the area to any
value.

    
    
    <tick>
    spacing  = 25u
    size     = 10p
    ...
    url      = script?type=tick&start=[start]&end=[end]
    map_size = 100p
    </tick>
    

The first image in this tutorial shows the image map with a `map_size=100p`.
This value may take on a negative value, in which case the link area will be
extended inward from the base of the tick. This is shown in the second example
image.

You can precisely control the radial extent of the tick mark link area by
using `map_radius_inner` and `map_radius_outer`.

    
    
    <tick>
    spacing  = 25u
    size     = 10p
    ...
    url      = script?type=tick&start=[start]&end=[end]
    map_radius_inner = 0.5r
    map_radius_outer = 1.2r
    </tick>
    

### multiple tick maps

You can define any number of tick map layers. The fourth image in this example
shows two tick mark layers: one layer of absolute ticks spaced every 25Mb and
one layer of relative ticks spaced every 1/4 of an ideogram. Each layer is at
a different radius and has its own set of links.

If you have multiple tick definitions at the same radius (e.g. one tick
definition for 25Mb ticks, one for 5Mb ticks and one for 1Mb ticks, for
example), I suggest that you attach a url parameter to only one of them.
Although you can create overlapping image map elements for each tick spacing,
this is likely to confuse the user.

