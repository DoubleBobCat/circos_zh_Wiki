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

## 9\. Tick Rings

[Lesson](/documentation/tutorials/ticks_and_labels/rings/lesson)
[Images](/documentation/tutorials/ticks_and_labels/rings/images)
[Configuration](/documentation/tutorials/ticks_and_labels/rings/configuration)

A tick set can be automatically drawn at multiple radial positions if you
define more than one radius for the set.

    
    
    <tick>
    # drawn at one radius
    radius = dims(ideogram,radius_outer)
    ...
    </tick>
    
    <tick>
    # drawn at two radii
    radius = dims(ideogram,radius_outer)
    radius = 0.8r
    ...
    </tick>
    
    <tick>
    # drawn at three radii
    radius = dims(ideogram,radius_outer)
    radius = 0.8r
    radius = 0.6r
    ...
    </tick>
    

Tick rings are useful when your image has many tracks and you'd like to have
multiple instances of tick marks.

