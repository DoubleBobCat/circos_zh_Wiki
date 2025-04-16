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

## 10\. Progression and Orientation

[Lesson](/documentation/tutorials/ideograms/progression_and_orientation/lesson)
[Images](/documentation/tutorials/ideograms/progression_and_orientation/images)
[Configuration](/documentation/tutorials/ideograms/progression_and_orientation/configuration)

### angle offset

The angle offset determines the angular position of the first ideogram.

    
    
          -90
           |
     180 --+-- 0
           |
           90
    

The default value is 0, which makes the first ideogram appear at 3 o'clock. I
like to use -90 to make the first ideogram appear at the top of the circle.

    
    
    <image>
    angle_offset = -90
    ...
    </image>
    

### ideogram progression

The progression of ideograms around the circle is controlled by the
angle_orientation parameter in the <image> block, which can be either
`clockwise` (this is the default) or `counterclockwise`.

    
    
    <image>
    angle_orientation = counterclockwise
    ...
    </image>
    

Don't forget that if you've included your image parameters from another file,
you can override the any of those parameters using the `*` suffix.

    
    
    <image>
    <<include etc/image.conf>>
    angle_orientation* = counterclockwise
    ...
    </image>
    

The direction of the scale of each ideogram will, by default, be the same as
the orientation. For example, if `angle_orientation=counterclockwise` the
direction of the scale of each ideogram will counterclockwise.

### ideogram orientation

The orientation of ideograms is globally controlled by `angle_orientation`. To
adjust the orientation of the scale for individual ideograms, use

    
    
    chromosomes_reverse = hs1,hs2,...
    

This setting reverses the ideogram orientation relative to the default
orientation, which is controlled by the ideogram progression set by
angle_orientation.

Why would you want to reverse individual ideograms? If you are using ribbon
links to show alignments, you can have control whether the ribbon twists or
not by adjusting the ideogram orientation. Or, if you are only showing two
ideograms (e.g. a sample and a reference), it may be more instructive to show
the ideograms with their start, and end, points near each other, respectively.
This would be achieved by

    
    
    chromosomes = hs1;hs2
    chromosomes_reverse = hs2
    

