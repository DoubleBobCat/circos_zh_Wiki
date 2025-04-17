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

## 9\. Ribbons

[Lesson](/documentation/tutorials/links/ribbons/lesson)
[Images](/documentation/tutorials/links/ribbons/images)
[Configuration](/documentation/tutorials/links/ribbons/configuration)

In all previous examples links where drawn as curves of uniform thickness. The
thickness was set using a parameter and was unrelated to the size of the spans
defined in the link file. Thus, although the thickness of the line could be
individually set to a certain pixel value, fundamentally the visual
representation of links by simple curves does not convey the size of the
link's spans.

By using ribbon links, demonstrated in this example, you can create links that
convey the size of the linked regions. This is very useful when the size of
the regions is sufficiently large, relative to the size of the image, as to
have various sizes distinguishable.

### normal vs ribbon link

A normal link is a bezier curve, whose control points are customizable using
bezier_radius and crest parameters. The curve curve connects the two spans of
a link, with the ends of the curve placed in the middle of each span.

When a link is turned into a ribbon, the link's thickness is variable, scaling
smoothly across its length. You can toggle a link to be a ribbon using

    
    
    ribbon = yes
    

On each end, the ribbon's thickness is the same as the size of the
corresponding link span.

### formatting ribbons

Once a link becomes a ribbon, you can use stroke_color and stroke_thickness to
outline the link.

Adjusting the z-depth for ribbons is extremely effective in layering the data
- the resulting interweaving of ribbons is visually appealing.

### twisting ribbons

The next tutorial in this section discusses how to control ribbon twisting.

