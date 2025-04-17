---
author: DoubleCat
date: 2025-04-11
layout: post
category: utilities
title: Helper Tools
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

# 10 — Helper Tools

## 3\. Bundling Links

[Lesson](/documentation/tutorials/utilities/bundling_links/lesson)
[Images](/documentation/tutorials/utilities/bundling_links/images)

## script location

    
    
    tools/bundlelinks
    

## script usage

    
    
    > cd tools/bundlelinks
    > ./run
    num_links 39978
    num_links_in_init_bundles 39839
    num_init_bundles 524
    num_passed_bundles 277 (52.86%)
    num_links_in_passed_bundles 36732 (92.20%)
    

The script sends a new links file to STDOUT and the report shown above to
STDERR.

To get the full manpage, use -man.

    
    
    > cd tools/bundlelinks
    > bin/bundlelinks -man
    

Adjust the configuration file etc/bundlelinks.conf to suit your needs.

## details

The purpose of the bundlelinks tool is to reduce the number of links in a
dataset by merging (or bundling) adjacent links together. By merging links,
you can distill a visually complex representation into one which effectively
summarizes the link structure of your data. A bundle is encoded as a new link
with a single start and end position, which are formed by the boundaries of
the merged links. Bundles are best shown using the ribbon feature.

I will use an example data set to motivate the need for bundlelinks and to
show how effective it can be to glean patterns. I will be using the synteny
data that relates the dog and human genomes. This data set has nearly 40,000
links which represent individual syntenic relationships between the dog and
human genomes (bundlelinks/data/dog.vs.human.txt).

### merging adjacent links and the -max_gap parameter

The first image of this tutorial shows the complexity of an image that has
40,000 links. There are certain patterns that are obvious (e.g., high
similarity beween all of human chrX and dog chrX, as well as, to a lesser
extent, human chr14 and dog chr8), but these patterns are visible due to the
fact that individual link lines are thick enough for adjacent links to merge
together in the final image. The bundlelinks tool attempts to encode these
patterns in a new link data set.

I will bundle the dog-vs-human links with progressively looser grouping, to
reduce the number of links. First, let's try a very strict bundling, which
merges links that are within 1Mb of one another (-max_gap 1000000). The bundle
report for this merging shows that 2,720 bundles were created. In effect, the
number of links has dropped to 7% of its original number.

    
    
    # -max_gap 1e6 
    num_links 39978
    num_links_in_init_bundles 39978
    num_init_bundles 2720
    num_passed_bundles 2720 (100.00%)
    num_links_in_passed_bundles 39978 (100.00%)
    

The second image in this tutorial shows these bundles. Note that these bundles
are now drawn as ribbon links since their start and end spans can be large.

Note that bundles may overlap at one end - this is a result of the fact that
when links are merged, a given region can give rise to multiple bundles with
different end points.

### bundling with -strict

By using the -strict setting, any one-link bundles are rejected and about 200
such bundles are removed.

    
    
    # -strict -max_gap 1e6 
    num_links 39978
    num_links_in_init_bundles 39788
    num_init_bundles 2530
    num_passed_bundles 2530 (100.00%)
    num_links_in_passed_bundles 39788 (100.00%)
    

### filtering small bundles

This is still a lot of bundles, however, and the image, though less complex
than before, is still looking very busy. At this point, you can reduce the
number of bundles by either (a) increasing the gap_size, and thereby merging
more distant links together, (b) making the bundle minimum size and membership
filter more aggressive, or (c) both.

For example, by adding a minimum size filter using -min_bundle_size 200000,
filters bundles down to 478 (example).

    
    
    # -strict -max_gap 1e6 -min_bundle_size 2e5
    num_links 39978
    num_links_in_init_bundles 39788
    num_init_bundles 2530
    num_passed_bundles 478 (18.89%)
    num_links_in_passed_bundles 11875 (29.85%)
    

Tightening the filter further, only 13 bundles are passed if the minimum
bundle size is 1Mb. In this case, these 13 bundles represent the largest
regions of the respective genomes that harboured tightly (within 1Mb) spaced
links.

If size of links is less important than the number of links in a bundle, you
can filter bundles based on the number of links they comprise using
-min_bundle_membership (example).

### filtering gappy bundles

On the other hand, by loosening the maximum gap parameter, links which were
previously in different bundles (or unbundled) because their ends were not
sufficiently close to another link, are now brought into the same bundle. As
you grow the gap parameter, bundles become more gappy. That is, the spatial
relationship between bundled links grows weaker because more distant links are
accepted into the bundle. To avoid excessively gappy bundles, use
-min_bundle_identity, which filters bundles based on the size of their links
relative to the extent of the bundle.

For example, with a maximum gap of 10Mb and a min_bundle_identity of 0.25,
there are 81 bundles that are passed (example).

    
    
    num_links 39978
    num_links_in_init_bundles 39839
    num_init_bundles 524
    num_passed_bundles 81 (15.46%)
    num_links_in_passed_bundles 2194 (5.51%)
    

### bundlelinks and orderchr

The bundlelinks script is very useful when you want to use orderchr to
optimize chromosome order, but have such a large data set that the
optimization takes a very long time.

First, use bundlelinks to merge links together and then run orderchr on the
bundled data set. By reducing the number of links to 1,000-2,000 the orderchr
optimization can proceed relatively quickly. After you've refined the order,
you can use the new chromosome arrangement on the original, unbundled dataset
(example).

## bundlelinks manpage

  * NAME
  * SYNOPSIS
  * DESCRIPTION
  * OUTPUT
  * OPTIONS
    * -max_gap
    * -min_bundle_membership, -strict
    * -min_bundle_size
    * -min_bundle_identity
  * HISTORY
  * BUGS
  * AUTHOR
  * CONTACT

* * *

* * *

# NAME

bundlelinks - bundle neighbouring links together in an effort to reduce
complexity of link structure

* * *

# SYNOPSIS

    
    
      bundlelinks -links linkfile.txt -max_gap NUM
                  {-min_bundle_membership NUM | -strict }
                  {-min_bundle_size NUM}
                  {-min_bundle_identity FRACTION}
    
    
    
      bundlelinks -links data/dog.vs.human.all.txt > data/dog.vs.human.bundles.txt
    

* * *

# DESCRIPTION

The purpose of this script is to turn a large set of links into a smaller one
by merging neighbouring links.

* * *

# OUTPUT

The script produces a new link file to STDOUT.

A tally is sent to STDERR that lists the following

    
    
      # total number of links read in
      num_links 39978
      # number of links in initial bundles (filtered for membership)
      num_links_in_init_bundles 39839
      # total number of initial bundles
      num_init_bundles 524
      # number of accepted bundles (filtered for both size and membership)
      num_passed_bundles 277 (52.86%)
      # number of links in accepted bundles
      num_links_in_passed_bundles 36732 (92.20%)
    

* * *

# OPTIONS

* * *

## -max_gap

Adjacent links are merged into bundles if their start/end coordinates are
sufficiently close. Given two links L1 and L2, they are merged into a bundle
if

    
    
      chr( start(L1) ) == chr( start(L2) )
      chr( end(L1) ) == chr( end(L2) )
    
    
    
      distance( start(L1), start(L2) ) <= MAX_GAP
      distance( end(L1), end(L2) ) <= MAX_GAP
    

If a link does not have any acceptable adjacent neighbouring links, it forms a
single-link bundle.

* * *

## -min_bundle_membership, -strict

These parameters filter bundles with few links. You can set the minimum number
of links required in a bundle for the bundle to be accepted
(-min_bundle_membership).

The -strict option is equivalent to -min_bundle_membership 2.

* * *

## -min_bundle_size

In addition to, or in place of, filtering bundles based on the number of links
they comprise, you can accept bundles based on the size of the links in the
bundle.

The minimum size parameter is applied independently to both ends of all links
in a bundle.

* * *

## -min_bundle_identity

This parameter filters bundles based on the bundle identity, which is defined
as

    
    
     identity = size(merged links) / extent(merged links)
    

Both ends of the bundle are evaluated independently.

* * *

# HISTORY

  * **16 July 2008**

Started and versioned.

* * *

# BUGS

* * *

# AUTHOR

Martin Krzywinski

* * *

# CONTACT

    
    
      Martin Krzywinski
      Genome Sciences Centre
      Vancouver BC Canada
      www.bcgsc.ca
      martink@bcgsc.ca
    

