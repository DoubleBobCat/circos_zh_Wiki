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

## 2\. Highlight Parameters - Part I - Embedded in Data File

[Lesson](/documentation/tutorials/highlights/parameters/lesson)
[Images](/documentation/tutorials/highlights/parameters/images)
[Configuration](/documentation/tutorials/highlights/parameters/configuration)

In this tutorial, I'll cover how to embed highlight parameters in your
highlight data file. This is a convenient way of formatting highlights because
generation of the parameters can be incorporated into your data analysis and
reporting pipeline.

### formatting a gene list

Using the genes.txt file used in the previous section, I added a random fill
color (red, green, blue, purple, yellow, orange, grey) to each entry. For
entries that received a red color, I adjusted the radial start/end positions
to be closer to the center of the circle than other colors. For entries that
received a green color, I similiarly adjusted r0,r1 to format these entries to
fall outside of the circle.

Here is an excerpt of the data file, with the additional formatting option
fields.

    
    
    hs1 1298972 1300443 fill_color=blue
    hs1 1311738 1324571 fill_color=red,r0=0.6r,r1=0.6r+50p
    hs1 1397026 1421444 fill_color=green,r0=1.1r,r1=1.15r
    hs1 1437417 1459927 fill_color=green,r0=1.1r,r1=1.15r
    hs1 1540746 1555847 fill_color=yellow
    hs1 1560962 1645635 fill_color=purple
    hs1 1624179 1645623 fill_color=grey
    

The configuration block for this highlight set defines a default r0,r1 value,
which applies to any entries in the data file that don't have overriding r0,r1
values. Thus, most of the highlights fall between r0,r1 = 0.7r,0.7r+200p, with
the red and green entries shifted inward and outward in the circle,
respectively.

All of the other highlight parameters may be specified in a similar manner in
the data file.

