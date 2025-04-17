---
author: DoubleCat
date: 2025-04-11
layout: post
category: scaling
title: Axis Scaling
---

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

# 8 — Axis Scaling

## 2\. Global Relative Scale Adjustment

[Lesson](/documentation/tutorials/scaling/global_relative_scale/lesson)
[Images](/documentation/tutorials/scaling/global_relative_scale/images)
[Configuration](/documentation/tutorials/scaling/global_relative_scale/configuration)

In the previous tutorial, I showed how to adjust the magnification of
ideograms. There, you learned how to make an ideogram twice as large (or twice
as small), as others.

However, sometimes it is useful to change the size of an ideogram in an image
so that it fills a given fraction of the image. The first example image shows
the full human and mouse genome, and the second image limits the display to
human chromosomes 1, 2, 3 and mouse chromosomes 14-19. In this image human
chromosome occupies about 20% of the image.

### scaling ideograms relative to image

Now suppose you want to change the scale of human chromosome so that it fills
exactly a quarter of the image (25%). You could compute the required
magnification by requiring that

    
    
    scale(hs1) * size(hs1) / size(all displayed ideograms) = 0.25
    

But there is a simpler way,

    
    
    chromosomes_scale = hs1:0.25r
    

By using the `r` suffix on scale, you indicate that the scale is relative to
the circumference of the ideogram circle.

### scaling multiple ideograms individually relative to image

By using a regular expression you can adjust the scale of multiple ideograms.
When this is combined with relative scale, you can make each ideogram have the
same size on the image, regardless of its physical size.

For example, this will make each of the 6 mouse chromosomes on the image each
occupy 10% of the image.

    
    
    chromosomes_scale = /mm/:0.1r
    

You can mix relative and absolute scales, but be careful that your relative
scales don't add up to more than 1.0. For example,

    
    
    chromosomes_scale = hs1:0.75r;hs2:0.75r
    

will have a strange effect because you've asked that two ideograms each occupy
3/4 of the image. Circos doesn't check the sanity of your scale expressions.

### scaling multiple ideograms as a group relative to image

Now suppose you wanted all the mouse chromosomes to occupy 50% of the image,
as a group. You could to this by calculating the required relative scale for
each (e.g. 0.5/6 = 0.0833)

    
    
    chromosomes_scale           = /mm/:0.0833r
    

But there's a better way. By using the `n` suffix, you indicate that the
fraction of the image should be divided evenly by the number of ideograms that
match the regular expression. Thus,

    
    
    chromosomes_scale           = /mm/:0.5rn
    

scales all ideograms matching `/mm/` to occupy, as a group, 50% of the image.

Note that in this method each ideogram has the same size in the image.

### application to multiple genomes

Consider the image in which three genomes are shown (human, mouse, rat). The
following limits the rat and mouse chromosomes to 1/4 of the image, regardless
how many ideograms from these genomes are shown.

    
    
    chromosomes_color = /hs/:green;/mm/:red;/rn/:blue
    chromosomes_scale = /mm/:0.25rn;/rn/:0.25rn
    

Note that in this method each rat and mouse ideogram has the same size in the
image.

The calculation behind these settings is iterative and sometimes has a hard
time correctly adjusting for ideogram spacing. You may need to adjust the
fractions to accomodate this inaccuracy. It's a shortcoming of the code.

