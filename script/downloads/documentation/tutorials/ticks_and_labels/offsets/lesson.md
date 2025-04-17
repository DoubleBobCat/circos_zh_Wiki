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

## 4\. Tick Marks - Offsets

[Lesson](/documentation/tutorials/ticks_and_labels/offsets/lesson)
[Images](/documentation/tutorials/ticks_and_labels/offsets/images)
[Configuration](/documentation/tutorials/ticks_and_labels/offsets/configuration)

The radial position of ticks and labels can be adjusted by the offset
parameter.

### tick mark offset

The tick mark offset can be specified in the <ticks> and/or <tick> blocks. The
offset can be in pixels, or specified relatively (in which case it is relative
to ideogram thickness) and controls the degree of radial shift applied to both
the tick mark and its label (it would not be wise to shift the tick mark
without applying the same offset to the label). Both the tick mark and the
label are shifted by the same amount (independent offset can be applied to the
label - read below).

    
    
    <ticks>
    ...
    offset = 2p
    ...
      <tick>
      offset = 1p
      ...
      </tick>
    </ticks>
    

### tick label offset

The label offset is an additional offset that can be applied to the label,
without further disturbing the radial position of the tick mark.

Both global and local label offsets are allowed, and they are cumulative.

A label offset expressed in relative form (label_offset=0.5r) is relative to
the size of the corresponding tick.

    
    
    <ticks>
    ...
    # all labels offset by 0.4x their tick size
    label_offset = 0.4r
    ...
      <tick>
      # this label has an additional 2 pixel offset
      label_offset = 2p
      ...
      </tick>
    </ticks>
    

