---
author: DoubleCat
date: 2025-04-11
layout: post
category: highlights
title: Highlights
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

# 4 — Highlights

## 6\. Recipe 1 - Ideogram Highlights

[Lesson](/documentation/tutorials/highlights/recipe1/lesson)
[Images](/documentation/tutorials/highlights/recipe1/images)
[Configuration](/documentation/tutorials/highlights/recipe1/configuration)

Ideogram highlights are particularly suitable for data that draws attention to
some parts of the ideograms, leaving most of the ideogram uncovered. Remember
that ideogram highlights obscure the cytogenetic bands, if any, that you've
drawn. Thus, as you increase highlight coverage, you are actually obscuring
one data set (cytogenetic bands) in favour of display another (the highlights
themselves).

In this example, I've created highlights from two gene lists. One gene list is
the set of genes in the OMIM database, which lists genes associated with any
kind of disease. The other list is a set of genes that have been implicated in
cancers. The latter list is much smaller than the former.

I've defined two ideogram highlight tracks, the OMIM genes drawn in orange and
the cancer genes in blue. Since the cancer genes are a proper subset of the
OMIM genes, I've drawn the cancer genes on top by assigning them a higher
z-depth.

    
    
    <highlights>
    
    ideogram   = yes
    z          = 5
    
     <highlight>
     file       = data/3/genes.omim.txt
     fill_color = orange
     </highlight>
    
     <highlight>
     file       = data/3/genes.cancer.txt
     z          = 10
     fill_color = blue
     </highlight>
    
    </highlights>
    

Since both higlight data sets are of the ideogram type, I've put the ideogram
parameter in the outer <highlights> block. This applies the parameter value to
all inner <highlight;> blocks.

I've set the default z-depth to be 5, and gave the cancer gene highlights a
higher z-depth, 10. It's good to space your z-depths by steps of 5 or 10,
because this allows you to insert highlight data sets at any relative position
to existing higlights without changing existing z-depth values. It's also a
good idea not to start z-depth at 0, because you can then insert a data set
behind all others, without using a negative z-depth, which is acceptable but
simply less aesthetically pleasing than all-positive z-depths.

One of the two fill_color parameters could have been global to both
<highlight> blocks. It's up to you how to manage parameter values in a way
that's reasonable for your application. Depending on your use, one of the two
statements below may be more intuitive

  * all genes are orange, but cancer genes are blue 
  * all genes are blue, but disease genes are orange 
  * disease genes are orange and cancer genes are blue 

