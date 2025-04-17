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

## 3\. Highlight Parameters - Part II - Using z-depth

[Lesson](/documentation/tutorials/highlights/z-depth/lesson)
[Images](/documentation/tutorials/highlights/z-depth/images)
[Configuration](/documentation/tutorials/highlights/z-depth/configuration)

z-depth, which controls the order in which highlights are drawn, is a critical
parameter in creating effective images. Judiciously layering your data can
make the difference between a good figure and a great figure.

By default, Circos will draw data, such as highlights, in a consistent, but
unspecified, order for a given z-depth. This means that the order isn't
random, but I reserve the right to change the way it's computed between
versions.

### avoiding occlusion

If you have a large set of overlapping highlights of various sizes, you stand
the chance of having smaller highlights covered by larger highlights. To avoid
this, set the z-depth to be inversely proportional to the higlight size, so
that the highlights are drawn in order of decreasing size.

The random.highlights.txt file associated with this tutorial contains 100
random highlights on chromosome 1. The highlight size is distributed normally
with avg = sd = 5 Mb.

The highlights are colored based on size, with the size range mapped into
evenly sized bins that correspond to colors chr0 ... chr24. This is the
conventional chromosome-based color scheme, which I've subverted for the
current purpose.

    
    
    hs1 1725862 8379128 fill_color=chr7
    hs1 4080887 11075336 fill_color=chr8
    hs1 5183662 14345280 fill_color=chr10
    hs1 10044837 11066617 fill_color=chr1
    hs1 10565297 13980978 fill_color=chr4
    hs1 11557401 23262460 fill_color=chr13
    hs1 12870075 25724192 fill_color=chr15
    hs1 13920706 18409477 fill_color=chr5
    hs1 25404101 33003848 fill_color=chr8
    
    ...
    

As you can see, highlight not only overlap but also subsume each other. Track
1 inside the circle in this tutorial's image shows the highlights drawn in the
default order, without using z-depth to control how they're drawn.

The largest highlight is max(size) = 20.4 Mb, so let's add a z-depth to each
highlight and define it by the integer component of z =
100-100*size/max(size).

    
    
    hs1 1725862 8379128 fill_color=chr7,z=68
    hs1 4080887 11075336 fill_color=chr8,z=66
    hs1 5183662 14345280 fill_color=chr10,z=55
    hs1 10044837 11066617 fill_color=chr1,z=95
    hs1 10565297 13980978 fill_color=chr4,z=84
    hs1 11557401 23262460 fill_color=chr13,z=43
    hs1 12870075 25724192 fill_color=chr15,z=37
    hs1 13920706 18409477 fill_color=chr5,z=78
    hs1 25404101 33003848 fill_color=chr8,z=63
    ...
    

Track 2 in this tutorial image shows the highlights as ordered by these
z-depth values. Using z-depth to prevent small highlights from being draw over
by larger ones is highly recommended. Keep in mind that a large number of
small highlights draw in the foreground can completely cover a larger
highlight drawn in the background.

You can also avoid occlusion by adjusting the radial position of the highlight
elements. Using the same data file as above, I created another track in which
the r0,r1 values were defined based on the size of the highlight region. I set
r0 = 0.4r - 200*k and r1 = 0.4r + 200*k, where k = size/max(size).

    
    
    hs1 1725862 8379128 fill_color=chr7,z=68,r0=0.4r-65.3669p,r1=0.4r+65.3669p
    hs1 4080887 11075336 fill_color=chr8,z=66,r0=0.4r-68.719p,r1=0.4r+68.719p
    hs1 5183662 14345280 fill_color=chr10,z=55,r0=0.4r-90.011p,r1=0.4r+90.011p
    hs1 10044837 11066617 fill_color=chr1,z=95,r0=0.4r-10.0388p,r1=0.4r+10.0388p
    hs1 10565297 13980978 fill_color=chr4,z=84,r0=0.4r-33.5584p,r1=0.4r+33.5584p
    hs1 11557401 23262460 fill_color=chr13,z=43,r0=0.4r-115p,r1=0.4r+115p
    hs1 12870075 25724192 fill_color=chr15,z=37,r0=0.4r-126.289p,r1=0.4r+126.289p
    hs1 13920706 18409477 fill_color=chr5,z=78,r0=0.4r-44.1012p,r1=0.4r+44.1012p
    hs1 25404101 33003848 fill_color=chr8,z=63,r0=0.4r-74.6659p,r1=0.4r+74.6659p
    

Track 3 in the image shows the highlights with this additional formatting. By
scaling the radial extent logarithmically, it's possible to reduce the radial
size difference and make the track more attractive, while still retaining
visibility of larger highlights drawn in the background.

