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

# 7 — 2D Data Tracks

## 11\. Connectors

[Lesson](/documentation/tutorials/2d_tracks/connectors/lesson)
[Images](/documentation/tutorials/2d_tracks/connectors/images)
[Configuration](/documentation/tutorials/2d_tracks/connectors/configuration)

Connectors are articulated line segments that relate two positions on an
ideogram between two radial positions.

The definition of a connector track is done as a plot type

    
    
    <plot>
    
    type = connector
    file = data/6/connectors.txt
    
    r0   = 0.8925r
    r1   = 0.999r
    
    connector_dims = 0,0.3,0.4,0.3,0
    
    thickness = 2
    color     = black
    </plot>
    

The data file defines the positions at r0 and r1 to be linked by lines

    
    
    # connectors.txt
    ...
    hs22 15116257 16046604
    hs22 15136864 16056568
    ...
    

The example images in this section show how the connector_dims parameter
controls the shape of the connector line. The line has five segments and the
five connector_dims parameters define the size of each of the segments
relative to (r1-r0).

