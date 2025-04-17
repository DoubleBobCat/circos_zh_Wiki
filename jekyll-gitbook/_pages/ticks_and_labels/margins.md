---
author: DoubleCat
date: 2025-04-11
layout: post
category: ticks_and_labels
title: Tick Marks, Grids and Labels
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

# 5 — Tick Marks, Grids and Labels

## 2\. Tick Marks - Margins

[Lesson](/documentation/tutorials/ticks_and_labels/margins/lesson)
[Images](/documentation/tutorials/ticks_and_labels/margins/images)
[Configuration](/documentation/tutorials/ticks_and_labels/margins/configuration)

If your ticks are densely spaced, they may overlap and form dreaded tick
blobs. Likewise, tick labels can start to overlap and lose their legibility.
To mitigate this problem, you can insist that adjacent ticks (or labels) are
separated by a minimum distance.

Here I show how to manage spacing between tick marks. The next tutorial
discusses label spacing.

### minimum tick mark separation

The tick_separation parameter controls the minimum distance between two ticks
marks. Note that this parameter applies to tick marks only, not to labels.
Labels have their own minimum distance parameter, covered in the next session.
Of course, if a tick mark is not drawn, neither will its label.

    
    
    <ticks>
      # define minimum separation for all ticks
      tick_separation = 3p
      ...
    
      <tick>
      # define minimum separation for a specific tick group
      tick_separation = 2p
        ...
      </tick>
    
      ...
    
    </ticks>
    

The primary purpose of the tick_separation parameter is to allow automatic
supression of ticks if you shrink the image size, change the ideogram position
radius, change the ideogram scale or, in general, perform any adjustment to
the image that changes the base/pixel resolution.

Since Circos supports local scale adjustments (at the level of ideogram, or
region of ideogram), the the tick separation parameter is used to dynamically
show/hide ticks across the image. You should keep this value at 2-3 pixels at
all times, so that your tick marks do not run into each other.

Tick marks are suppressed on a group-by-group basis. In other words, tick
separation is checked separately for each <tick> block. For example, if you
define 1u, 5u and 10u ticks, these will be checked for overlap independently
(Circos does not check if the 10u tick overlaps with a tick from another
group, such as the 1u tick).

This approach is slightly different than the method that was initially
implemented, which compared inter-tick distances across tick groups.

The tick mark thickness plays no role in determining the distance between
ticks. The tick-to-tick distance is calculated based on the positions of the
ticks.

In the first example image in this tutorial, three ideograms are drawn, each
at a different scale. Depending on the magnification, ticks are suppressed for
some ideograms because they are closer than the tick_separation parameter. For
example, 0.25u and 0.5u ticks do not appear on hs1 and 0.25u ticks do not
appear on hs2.

In the second example image, only one chromosome is shown but its scale is
smoothly expanded. Region 100-110 Mb is magnified at 10x and with the scale in
the neighbourhood decreasing smoothly from 10x to 1x. All tick marks are shown
within the magnified area and away from it, as the scale returns to 1x, some
ticks disappear.

### minimum tick distance to ideogram edge

To suppress ticks near the edge of the ideogram, use min_distance_to_edge.
This parameter can be used globally in the <ticks> block to affect all ticks,
or locally with a <tick> block to affect an individual tick group.

    
    
    <ticks>
    min_distance_to_edge = 10p
    ...
    <tick>
    min_distance_to_edge = 5p
    ...
    </tick>
    ...
    </ticks>
    

The corresponding parameter to suppress labels near an ideogram edge is
min_label_distance_to_edge.

