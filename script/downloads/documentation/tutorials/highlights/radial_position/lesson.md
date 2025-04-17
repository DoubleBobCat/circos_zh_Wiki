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

## 4\. Highlight Parameters - Part III - Radial Position

[Lesson](/documentation/tutorials/highlights/radial_position/lesson)
[Images](/documentation/tutorials/highlights/radial_position/images)
[Configuration](/documentation/tutorials/highlights/radial_position/configuration)

In the previous section I demonstrated how you can adjust the radial extent,
by setting r0,r1 in the data file, to encode information about the highlight.
In that example, I used the highlight region size to control the radial
extent.

There are three data files for this section. All highlights regions are
randomly generated. Highlight color is encoded by the chromosome color scheme.

  * random.highlights.r.txt - random radial start 
  * random.highlights.rr.txt - radial start inversely proportional to size (largest highlights at the edge) 
  * random.highlights.rrr.txt - radial start inversely proportional to size (largest highlights at the center) 

From the images you can see that a little planning when it comes to radial
position can produce a much cleaner figure. The first figure is a mess, of
course. The last image, in which the small highlights are near the ideograms
presents the data clearly. Smaller features are best shown at larger radial
positions because they will subtend a larger angular distance along the circle
than if drawn closer to the center, and therefore are more clearly visible.
Larger structures can be drawn at smaller radial values.

### formatting radial position

Here is an excerpt of one of the data files used in this section
(random.highlights.rrr.txt).

    
    
    ...
    hs1 135818329 137808916 fill_color=chr7,z=67,r0=0.709600r,r1=0.759600r
    hs1 107513875 108981462 fill_color=chr5,z=76,r0=0.772761r,r1=0.822761r
    hs1 227449772 228946659 fill_color=chr5,z=75,r0=0.769223r,r1=0.819223r
    hs1 24598766 26578839 fill_color=chr7,z=68,r0=0.710869r,r1=0.760869r
    hs1 145258423 147866442 fill_color=chr10,z=58,r0=0.635033r,r1=0.685033r
    hs1 110729772 111813392 fill_color=chr4,z=82,r0=0.819133r,r1=0.869133r
    hs1 136155686 138376393 fill_color=chr8,z=64,r0=0.681808r,r1=0.731808r
    ...
    

All the radial positions are specified as relative values, indicated by the
"r" suffix. The relative value is expressed in terms of the inner ideogram
radius, if the value is <1, and in terms of the outer radius, if the value is
>1\. This way, highlights don't ever cross ideograms. By the way, if you would
like highlights inside the ideograms, use ideogram highlights, covered in the
next section.

In addition to relative radial positions, you can specify absolute positions
(suffix is "p", for pixel), or a combination of the two. Here are some
examples

    
    
    # absolute positioning
    r0 = 500p      # start at 500 pixels from center
    r1 = 600p      # end at 600 pixels from center
    
    # relative positioning - helpful when resizing figure
    r0 = 0.5r      # start at 0.5*inner_ideogram_radius
    r0 = 0.6r      # end at 0.6*inner_ideogram_radius
    
    # relative radial position start, but absolute size
    r0 = 0.5r      # start at 0.5*inner_ideogram_radius
    r1 = 0.5r+100p # start at 0.5*inner_ideogram_radius + 100 pixels
    
    # like above, but centered at a radial position
    r0 = 0.5r-50p  # start at 0.5*inner_ideogram_radius
    r1 = 0.5r+50p  # start at 0.5*inner_ideogram_radius + 100 pixels
    

