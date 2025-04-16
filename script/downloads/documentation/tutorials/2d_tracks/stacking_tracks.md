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

## 12\. Putting It All Together

[Lesson](/documentation/tutorials/2d_tracks/stacking_tracks/lesson)
[Images](/documentation/tutorials/2d_tracks/stacking_tracks/images)
[Configuration](/documentation/tutorials/2d_tracks/stacking_tracks/configuration)

In this example, I create an image with a large number of plot tracks that
include all the types previously discussed. The image looks like a heart
attack and I don't recommend that you create such monstrosities for any
reasons other than exploring Circos' syntax.

Several of the idioms in the configuration file are worth exploring in detail.

### placing highlights among data layers

When a highlight is defined as a plot block, you can use the z depth to place
it anywhere within other data layers.

In this figure, the highlight wedges are drawn ontop of the heatmaps, but
under the line, histogram, line and tile plots.

### sampling data randomly

You can choose to hide data points randomly by using a rule that incorporates
a call to a random number generator. The Perl function rand() returns a random
number sampled uniformly from the interval [0,1).

    
    
    <rule>
    condition = rand() < 0.1
    show      = no
    </rule>
    

In this case, 10% of the data points, on average, will not appear. Each time
the image is created, a different set of points will be hidden.

### formatting data randomly

Along the lines of the previous example, you can apply formatting randomly to
data. For example, to make 50% of the points, on average, red:

    
    
    <rule>
    condition = rand() < 0.5
    color     = red
    </rule>
    

### hiding heatmap elements

You can hide heatmap elements using the show=no idiom with a size condition.
You can also subvert the color list and include the background color in the
list.

    
    
    <plot>
    type         = heatmap
    ...
    color        = black,grey,vlgrey,white,lgreen,green,dgreen
    ...
    </plot>
    

### adjacent histograms

You can create a floating bar plot by stacking two histograms against one
another. The outer histogram is oriented "out" and the inner one is oriented
"in".

    
    
    <plot>
    type         = histogram
    ...
    orientation  = in
    r0           = 0.65r
    r1           = 0.75r
    ...
    </plot>
    
    <plot>
    type         = histogram
    ...
    orientation  = out
    r0           = 0.75r
    r1           = 0.85r
    ...
    </plot>
    

### adjusting ideogram radius

Don't forget that you can adjust the radius of individual ideograms, or
regions.

    
    
    chromosomes        = hs2[a]:5-35;hs2[b]:40-75;hs2[c]:80-115;hs2[d]:120-155;hs2[e]:160-195;hs2[f]:200-240
    chromosomes_radius = a:0.95r;b:0.9r;c:0.85r;d:0.8r;e:0.75r;f:0.7r
    

This is very useful if you need to squeeze in a data track, especially outside
of the ideogram, but don't want to disturb the overall circular nature of the
plot. In this case, you would shift the ideogram radius in by, say, 200px, and
then plot a 200px track outside the ideogram.

