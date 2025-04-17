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

## 6\. Axes & Backgrounds

[Lesson](/documentation/tutorials/quick_start/axes_and_backgrounds/lesson)
[Images](/documentation/tutorials/quick_start/axes_and_backgrounds/images)
[Configuration](/documentation/tutorials/quick_start/axes_and_backgrounds/configuration)

A track's background can be colored using <backgrounds> block and graduated
using <axes> block.

    
    
    <plot>
    ...
    # axes
    <axes>
     <axis>
     ...
     </axis>
     <axis>
     ...
     </axis>
     ...
    </axes>
    
    # backgrounds
    <backgrounds>
     <background>
     ...
     </background>
     <background>
     ...
     </background>
     ...
    </backgrounds>
    
    </plot>
    

### axes

Much like ticks, axes are defined in groups. Each group can be spaced either
with absolute or relative spacing. You can provide an axis line at specific
positions and, for groups which have spacing, skip some positions.

  * `spacing` \- absolute or relative spacing of the axis 
  * `position` \- fixed position (or positions) for axes 
  * `position_skip` \- fixed position (or positions) to skip when drawing axis lines 
  * `y0` \- absolute or relative start of axis lines 
  * `y1` \- absolute or relative start of axis lines 
  * `color` \- color of axis lines 
  * `thickness` \- thickness of axis lines 

    
    
    <axes>
    
    # Show axes only on ideograms that have data for this track
    show = data
    
    thickness = 1
    color     = lgrey
    
    <axis>
    spacing   = 0.1r
    </axis>
    
    <axis>
    spacing   = 0.2r
    color     = grey
    </axis>
    
    <axis>
    position  = 0.5r
    color     = red
    </axis>
    
    <axis>
    position  = 0.85r
    color     = green
    thickness = 2
    </axis>
    
    </axes>
    

### backgrounds

Background elements are color rings within the track boundary between `y0` and
`y1` limits. Multiple background elements can e used to give the track a
striped or gradated look. Each element is defined as a separate <background>
block, which are processed in order of appearance.

If `y0` and `y1` limits are not specified, the boundaries of the track are
used.

    
    
    <backgrounds>
    
    # Show the backgrounds only for ideograms that have data
    show  = data
    
    <background>
    color = vvlgrey
    </background>
    <background>
    color = vlgrey
    # the "r" suffix indicates position relative to track data range
    y0    = 0.2r
    y1    = 0.5r
    </background>
    <background>
    color = lgrey
    y0    = 0.5r
    y1    = 0.8r
    </background>
    <background>
    color = grey
    # if y1 is not specified, the plot maximum is used (e.g. y1=1r)
    y0    = 0.8r
    </background>
    
    </backgrounds>
    

### stand-alone axes and blackground <plot> blocks

In most cases, the purpose of a <plot> block is to show data. Axes and
backgrounds associated with a <plot> block that contains data will always be
drawn _under_ the data.

To precisely control whether axes and backgrounds are placed below or over the
data, use a bare <plot> block (one without `file` or `type` parameter). Doing
so will use the <plot> block to draw the axes and background only, without any
data.

    
    
    <plot>
    
    # no file or type parameter
    
    r0 = 0.5r
    r1 = 0.75r
    
    # use z to determine whether this block (axes,background) will be
    # drawn on top of other plot blocks. 
    
    z  = 10
    
    <axes>
     ...
    </axes>
    
    <backgrounds>
     ...
    </backgrounds>
    
    </plot>
    

Here is an example of how to use this kind of axes <plot> block. Depending on
the `z` parameter of the axis <plot> block, the axes are drawn above or below
the data in the second block. By setting the axis color to have transparency
(`grey_a3`), the axes will blend with the histogram bins when drawn on top of
then.

    
    
    <plots>
    
    # positions are inherited by both <plot> blocks
    
    r0 = 0.5r
    r1 = 0.8r
    
    <plot>
     z = 10 # drawn on top of data
     # z = -10 # drawn below data
     <axes>
      <axis>
       spacing   = 0.1r
       color     = grey_a3
       thickness = 1
      </axis>
     </axes>
    </plot>
    
    <plot>
     # default z value is 0
     type = histogram
     file = data.txt
    </plot>
    
    </plots>
    
    

