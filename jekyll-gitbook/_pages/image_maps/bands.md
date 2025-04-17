---
author: DoubleCat
date: 2025-04-11
layout: post
category: image_maps
title: Image Maps
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

# 11 — Image Maps

## 2\. Image Maps - Clickable Cytogenetic Bands

[Lesson](/documentation/tutorials/image_maps/bands/lesson)
[Images](/documentation/tutorials/image_maps/bands/images)
[Configuration](/documentation/tutorials/image_maps/bands/configuration)

Chromosomes can have cytogenetic bands associated with them in the karyotype
file. These bands serve to define distinct regions on the chromosome.
Typically, the bands are used to orient large-scale structures (>5Mb) on the
chromosome and act as visual markers. You can use these bands for any purpose,
however.

To associate a url with each band, use the `band_url` parameter in the
<ideogram> block.

    
    
    <ideogram>
    band_url = script?start=[end]&end=[end]&label=[label]
    ...
    

### parameters for bands

Bands have the following parameters available automatically in their URL

  * chr - chromosome of band 
  * parent - internal field 
  * name - name of the band 
  * start - base position of band start 
  * end - base position of band end 
  * size - size of band 
  * color - color of band 
  * label - the label of the band (this can be different than the name) 

Like for ideograms, you can include an `id` parameter in the band definition
and use it subsequently in the URL. So, in the karyotype file you might have

    
    
    ...
    band hs1 p31.2 p31.2 68700000 69500000 gneg
    band hs1 p31.1 p31.1 69500000 84700000 gpos100 id=treasure_here
    band hs1 p22.3 p22.3 84700000 88100000 gneg
    ...
    

and then use a URL like

    
    
    band_url = script?id=[id]
    

If you have image_map_missing_parameter=removeparam, then all bands without a
defined id parameter will have a URL like

    
    
    script?id=
    

with the exception of chr1p31.1 which will have

    
    
    script?id=treasure_here
    

But, if you define `image_map_missing_parameter=removeurl`, then only bands
with the id parameter defined will have a URL - other bands will not have an
entry in the image map.

### managing overlapping links - ideograms and bands

Bands are drawn on top of ideograms and therefore band image map elements
locally override ideogram map elements. This is accomplished by placing the
band image map element before the ideogram element in the map file. Both
elements are there, but [W3 specification for client-side image
maps](https://www.w3.org/TR/REC-html40/struct/objects.html#h-13.6.1) specifies
that "If two or more defined regions overlap, the region-defining element that
appears earliest in the document takes precedence (i.e., responds to user
input)".

The second image in this tutorial demonstrates the result of defining both an
ideogram and a band url

    
    
    ideogram_url = script?chr=[chr]
    band_url     = script?start=[start]&end=[end]&label=[label]
    

You'll notice that in the region of the ideogram band links are active in the
image map. However, since the ideogram image map also includes the label of
the ideogram, you can still access the link of the ideogram through the label.

In the case of bands without a URL, the ideogram link would be accesible
within the area of the band.

