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

# 6 — Links and Relationships

## 10\. Ribbon Twists

[Lesson](/documentation/tutorials/links/twists/lesson)
[Images](/documentation/tutorials/links/twists/images)
[Configuration](/documentation/tutorials/links/twists/configuration)

A ribbon is drawn as a filled path. The corner vertices of the path are the
start and end positions of the spans defined by the link.

    
    
    linkID chr1 start1 end1
    linkID chr2 start2 end2
    

The ribbon path is drawn in this direction

    
    
     >>  start1 >> end1 >> end2 >> start2 >>
     |                                     |
     <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
    

Notice that the start positions of the link spans are connected by a path, and
so are the end positions.

Therefore, depending on the orientation of the ideograms associated with the
link, and the orientation of start/end coordinates, the ribbon _may twist_.
The first example image in this tutorial shows how this twist happens.

### controling twist by ideogram orientation

One way to control the twisting of ribbons is to adjust the orientation of
ideograms. This is particularly effective when you have links between ideogram
pairs, shown in the second example image in this tutorial.

If your links are oriented in the same direction on both ideograms (i.e.
start1>end1 and start2>end2), then ribbons will twist if orientation of
ideograms is the same. This twisted visual representation, however, may be
inappropriate because it suggests that there is an inversion. One way to
untwist the ribbon is to adjust the orientation of the second ideogram

    
    
    chromosomes_reverse = hs2
    

### removing twist with "flat" parameter

If you want all your ribbons untwisted, regardless of ideogram orientation or
their relative start/end positions, set the flat flag in the <link> block

    
    
    <link>
    ribbon = yes
    flat   = yes
    ...
    </link>
    

With the flat flag set, any adjustment to ideogram progression and orientation
will have no effect on the layout of the ribbons, which will always be drawn
untwisted.

You can add the flat parameter individually to a link.

    
    
    linkID chr1 start1 end1 flat=yes
    linkID chr2 start2 end2 flat=yes
    

### forcing twist with "twist" parameter

If you want all your ribbons twisted, regardless of ideogram orientation or
their relative start/end positions, set the twist flag in the <link> block

    
    
    <link>
    ribbon = yes
    twist  = yes
    ...
    </link>
    

Like for "flat", the "twist" flag renders any adjustment to ideogram
progression and orientation independent of the twist appearance of ribbons,
which will always be drawn twisted.

You can individually force a link to be drawn as a twisted ribbon by adding
"twist" to the data file,

    
    
    linkID chr1 start1 end1 twist=yes
    linkID chr2 start2 end2 twist=yes
    

### adding twist with inverted coordinates

The "flat" and "twist" flags specify the twist state for a ribbon. These
parameters are useful when you want a particular twist state, regardless of
the layout of the ideograms and their orientation.

Another way to incorporate twist is to define the link coordinates to be
inverted. Thus, instead of

    
    
    linkID chr1 start1 end1 
    linkID chr2 start2 end2 
    

you would define

    
    
    linkID chr1 end1 start1
    linkID chr2 start2 end2
    

For example, instead of

    
    
    link1 hs1 10 20
    link1 hs2 10 20
    

use

    
    
    link1 hs1 20 10
    link1 hs2 10 20
    

Alternatively, if you want to keep your start coordinate always smaller than
the end, you can use inverted=1, like this

    
    
    link1 hs1 10 20 inverted=1 # this inverts role of start/end for this span (now start=20 end=10)
    link1 hs2 10 20
    

With the link coordinates implicitly defining the orientation of the link, the
correct twist state will be drawn.

