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

# 4 — Highlights

## 5\. Ideogram Highlights

[Lesson](/documentation/tutorials/highlights/ideogram_highlights/lesson)
[Images](/documentation/tutorials/highlights/ideogram_highlights/images)
[Configuration](/documentation/tutorials/highlights/ideogram_highlights/configuration)

Ideogram highlights are placed on top of the ideograms in the figure. You do
not need to specify the radial position of these highlights, because these
parameters are fixed by the size and position of the ideograms.

In this section, I have used the same data file to draw to highlight tracks.
One is an ideogram track and one is a wedge-style track, with radial positions
specified.

    
    
    <highlights>
     <highlight>
     file       = data/3/random.highlights.z_by_size.txt
     ideogram   = yes
     </highlight>
    
     <highlight>
     file       = data/3/random.highlights.z_by_size.txt
     r0 = 0.5r
     r1 = 0.6r
     </highlight>
    </highlights>
    

In the example above, the highlights cover each ideogram completely, obscuring
the cytogenetic bands. In this kind of situation, it's best to use wedge-style
highlights.

Ideogram highlights are very effective when they are used to highlight
specific positions on the genome.

When the radial position of individual ideograms is set with
chromosome_radius, the position of highlights is automatically adjusted.
Relative highlight radial position is computed relative to the new ideogram
position. Highlights drawn on the ideogram (ideogram=yes) are drawn at the new
ideogram position.

### adding transparency to ideogram highlights

It is possible to make ideogram highlights transparent. This is done in the
same way as for wedge highlights, and any other elements that require
transparency.

Note that if you have colored ideograms, cytogenetic bands with transparency
and transparent ideogram highlights these three colors will blend.

To make ideogram highlights transparent, add _aN to their fill_color. Below is
the part of circos.conf that achieves this.

    
    
    <highlights>
    
    # transparent wedge highlights at radial position 0.85-0.95
    <highlight>
    file        = highlight.txt
    fill_color  = blue_a5
    r0 = 0.85r
    r1 = 0.95r
    </highlight>
    
    # transparent ideogram highlights, using the same data file as for wedge highlights
    <highlight>
    file        = highlight.txt
    fill_color  = blue_a2
    ideogram = yes
    </highlight>
    
    </highlights> 
    

