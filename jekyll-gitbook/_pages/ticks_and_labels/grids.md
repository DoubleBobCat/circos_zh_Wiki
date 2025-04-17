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

## 5\. Grids

[Lesson](/documentation/tutorials/ticks_and_labels/grids/lesson)
[Images](/documentation/tutorials/ticks_and_labels/grids/images)
[Configuration](/documentation/tutorials/ticks_and_labels/grids/configuration)

You can add a radial grid to any set of tick marks. Grids are drawn on top of
highlights, but behind all other data.

The radial start and end position of the grid lines can be controlled globally
within the <ticks> block, or locally, within each <tick> block.

    
    
    show_grid  = yes
    
    <ticks>
    
     grid_start     = 0.5r
     grid_end       = 0.975r
     grid_color     = black
     grid_thickness = 2p
     ...
     <tick>
      spacing = 1u
      ...
      grid           = yes
      grid_color     = grey
      grid_thickness = 1
      grid_start     = 0.55r
      grid_end       = 0.95r
     </tick>
     <tick>
      spacing = 5u
      ...
      grid           = yes
      grid_color     = dgrey
      grid_thickness = 2
      grid_start     = 0.6r
      grid_end       = 0.925r
     </tick>
     <tick>
      spacing = 10u
      ...
      grid           = yes
      grid_color     = black
      grid_thickness = 2
     </tick>
    </ticks>
    

