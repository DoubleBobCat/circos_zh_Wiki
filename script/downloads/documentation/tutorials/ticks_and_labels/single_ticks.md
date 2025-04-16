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

## 8\. Ticks at Specific Positions

[Lesson](/documentation/tutorials/ticks_and_labels/single_ticks/lesson)
[Images](/documentation/tutorials/ticks_and_labels/single_ticks/images)
[Configuration](/documentation/tutorials/ticks_and_labels/single_ticks/configuration)

Up to now, each tick block defined a tick series, with the positions of ticks
in a series defined by the spacing (absolute or relative). In this tutorial,
you'll see how to define ticks at specific positions.

### Ticks at specific absolute positions

To define a tick at a given absolute position, use `position` instead of
`spacing`.

    
    
    <ticks>
    
    ...
    
    <tick>
    # define position 
    position     = 25u
    # no spacing definition necessary
    ...
    </tick>
    
    <tick>
    # define multiple positions
    position     = 30u,32u,34u,40u
    ...
    </tick>
    
    ...
    
    </ticks>
    

Do not define `spacing` when `position` is used.

### Ticks at specific relative positions

To place at specific relative positions, use `rposition` and set
`spacing_type=relative`.

    
    
    <tick>
    # define multiple positions
    rposition      = 0.5,0.7,0.9
    spacing_type   = relative
    color          = blue
    label_relative = yes
    format         = %.2f
    </tick>
    

Note the difference between `position` (for absolute positions) and
`rposition` (for relative positions).

Do not define `rspacing` when `rposition` is used.

### Ticks at start and end of ideogram

Two special positions are defined. These are `start` and `end`. Using these
strings you can place a tick at the start or end of the ideogram. This tick
can have a label. In addition, you can define the label to be any string by
using the `label` parameter. This parameter is supported for all ticks, but is
particularly useful for start/end ideogram ticks.

    
    
    <tick>
    position = start
    label    = 3'
    ...
    </tick>
    
    <tick>
    position = end
    label    = 5'
    ...
    </tick>
    

