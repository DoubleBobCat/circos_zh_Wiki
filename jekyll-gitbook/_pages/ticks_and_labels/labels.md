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

## 3\. Tick Marks - Label Margins

[Lesson](/documentation/tutorials/ticks_and_labels/labels/lesson)
[Images](/documentation/tutorials/ticks_and_labels/labels/images)
[Configuration](/documentation/tutorials/ticks_and_labels/labels/configuration)

If your tick marks are densely spaced, their labels may overlap and lose their
legibility. Like the tick mark margin parameter, tick label margins help you
suppress labels that might overlap.

A tick label will not be drawn if its tick mark is not drawn. Thus, a natural
way to suppress labels is to suppress the tick marks. This is done using
tick_separation and is described in the previous tutorial.

Label separation is controlled independently using label_separation. Like
tick_separation, the label_separation parameter defines a minimum allowed
distance between labels. Labels closer than this distance to another label
will not be drawn. Also, as with tick marks themselves, label overlap is
checked within a tick mark group (i.e. 1u and 5u labels are compared for
overlap).

    
    
    <ticks>
    
      tick_separation  = 2p
      label_separation = 5p
      ...
    
      <tick>
      tick_separation  = 5p
      label_separation = 10p
        ...
      </tick>
    
      ...
    
    </ticks>
    

The mechanics behind label margins work exactly the same way as tick mark
margins. For example, you can define label_separation globally or within
individual <tick> blocks.

Overlap is calculated in the angular direction only. Any tick label offset
does not change the way overlap is calculated, a process in which the radial
position of the label is disregarded. By introducing label offsets (shifting
labels of tick mark sets radially) you can effectively eliminate overlap
without supressing ticks. This is covered in the next section.

If you want to turn off label overlap check for a given tick mark group, set
label_separation=0p.

### minimum label distance to ideogram edge

To suppress tick labels near the edge of the ideogram, use
min_label_distance_to_edge. This parameter can be used globally in the <ticks>
block to affect all ticks, or locally with a <tick> block to affect an
individual tick group.

    
    
    <ticks>
    min_label_distance_to_edge = 10p
    ...
    <tick>
    min_label_distance_to_edge = 5p
    ...
    </tick>
    ...
    </ticks>
    

The corresponding parameter to suppress ticks near an ideogram edge is
min_distance_to_edge. If the tick mark is suppressed with this parmaeter then
no label is shown.

### suppressing first or last label of a group

You can suppress the label of the first tick, or last tick, in a group using
skip_first_label and skip_last_label.

    
    
    <ticks>
    skip_first_label = yes
    skip_last_label  = yes
    ...
    <tick>
    # will overwrite the skip_first_label for this tick group
    skip_first_label = no
    ...
    </tick>
    ...
    </ticks>
    

The purpose of this parameter is to reduce label clutter near the edges of the
ideogram. The effect is similar to using min_label_distance_to_edge, which was
described above, but skip_*_label affects at most one label.

The mechanics of the first/last label suppression is applied on a group-by-
group basis. Thus, if skip_last_label is set for all tick groups, the last
label for _each group_ will be suppressed, and not the last label on the
ideogram.

