---
author: DoubleCat
date: 2025-04-11
layout: post
category: utilities
title: Generate Link Density Tracks
---

## Generate Link Density Tracks
### lesson
[Lesson](/documentation/tutorials/utilities/density_tracks/lesson)
[Images](/documentation/tutorials/utilities/density_tracks/images)

### script location
```    
    tools/binlinks
```
### script usage
```    
    > cd tools/binlinks
    # bin a link file by size of links on originating chromosome
    > bin/binlinks -links data/segdup.links.txt > data/histogram.txt
    # bin a link file by size of links on target chromosome
    > bin/binlinks -links data/segdup.links.txt -link_end 1 > data/histogram.txt
    # bin a link file by number of links on originating chromosomes
    > bin/binlinks -num -links data/segdup.links.txt > data/histogram.txt
    # color bin values by target chromosome
    > bin/binlinks -num -links data/segdup.links.txt -output_style 1 > data/histogram.txt
    # create stacked histogram data
    > bin/binlinks -num -links data/segdup.links.txt -output_style 3 > data/histogram.txt
```
Any values in the configuration file etc/binlinks.conf are overwritten with
command-line parameters of the same name.

### details
The purpose of this script is to generate data for histogram and highlight
tracks that stores the number, size and consensus position of links. All
chromosomes in the input link file are divided into bins (controlled by
-bin_size), and link statistics are calculated on a bin-by-bin basis.

For the purpose of this script that the first line of a link line pair is
refered to as the originating position and the second line as the target
position. Thus the link given by the lines

```    
    segdup04822 hs2 131691333 131718278
    segdup04822 hs18 14507744 14534120
```
has hs2 as the originating chromosome (or start of link) and hs18 as the
target chromosome (or end of link). For your application, the links may be
bidirectional (such as the segmental duplication used in this example), but
the asymmetry of the start/end position is inherent from the format of the
link data file.

#### counting link size
The default values in the etc/binlinks.conf file make binlinks count the total
size of links on the originating chromosomes.

```    
    > bin/binlinks
    ...
    hs14 18000000 18999999 1739544.0000
    hs14 19000000 19999999 816821.0000
    hs14 20000000 20999999 69080.0000
    ...
```
For example, the links that originate in the bin hs14:14:18-19Mb add up to
1.739Mb. It's important to realize that this sum is the sum of the start of
the links (each link is composed of two spans - a start span on the
originating chromosome and an end span on the target chromosome).

You can use -link_end to tabulate the total size of the end spans for a bin.

```    
    > bin/binlinks -link_end 1
    ...
    hs14 18000000 18999999 2256283.0000
    hs14 19000000 19999999 807211.0000
    hs14 20000000 20999999 78425.0000
    ...
```
In this case, the links that originate in the bin hs14:18-19Mb have end spans
that total 2.256Mb.

You can add both the start and end spans of the links in a bin using -link_end
2.

```    
    > bin/binlinks -link_end 2
    ...
    hs14 18000000 18999999 3995827.0000
    hs14 19000000 19999999 1624032.0000
    hs14 20000000 20999999 147505.0000
    ...
```
Instead of the link span size, you can add up the number of links in a bin
using -num. In this case, each bin that overlaps with the link start and end
span will receive a +1 contribution from the link.

Use -log to logarithmically scale the bin values.

#### applying target chromosome color to bin statistic
Use -color_by_chr to add a color to each bin based on the consensus target
chromosome (the chromosome receiving the largest contribution from the bin).

```    
    > bin/binlinks -color_by_chr
    ...
    hs14 18000000 18999999 1739544.0000 fill_color=hs22
    hs14 19000000 19999999 816821.0000 fill_color=hs22
    hs14 20000000 20999999 69080.0000 fill_color=hs14
    ...
```
#### obtaining consensus chromosome statistics
Typically you will have a large number of links that originate from each bin.
Whereas default output style (-output_style 0) reports the total statistics
for a bin, as described above, if you want to obtain statistics based on
individual chromosomes, use the other output styles described below.

For each bin, statistics for the consensus target chromosome (the chromosome
with the largest contribution of links from the bin) is obtained with
-output_style 1. The output is also annotated with the color of the consensus
chromosome.

```    
    > bin/binlinks -output_style 1
    ...
    hs14 18000000 18999999 688034.0000 fill_color=hs22
    hs14 19000000 19999999 264389.0000 fill_color=hs22
    hs14 20000000 20999999 65213.0000 fill_color=hs14
    ...
```
Note the difference between this output and the corresponding output using
-output_style 0. In the present case, the largest fraction of links from
hs14:18-19Mb terminate on hs22 and total 688kb.

Whereas -output_style 1 shows you the statistic for all links in the bin and
the color of the consensus target chromosome, -output_style 2 gives a value
for the bin for each target chromosome.

```    
    > bin/binlinks -output_style 2
    hs14 18000000 18999999 688034.0000 fill_color=hs22
    hs14 18000000 18999999 303434.0000 fill_color=hs14
    hs14 18000000 18999999 257791.0000 fill_color=hs18
    hs14 18000000 18999999 235624.0000 fill_color=hs15
    hs14 18000000 18999999 218463.0000 fill_color=hs21
    hs14 18000000 18999999 18850.0000 fill_color=hs17
    hs14 18000000 18999999 17348.0000 fill_color=hs16
    hs14 18000000 18999999 0.0000 fill_color=hsx
    hs14 18000000 18999999 0.0000 fill_color=hsy
    hs14 18000000 18999999 0.0000 fill_color=hs1
    hs14 18000000 18999999 0.0000 fill_color=hs2
    hs14 18000000 18999999 0.0000 fill_color=hs3
    hs14 18000000 18999999 0.0000 fill_color=hs4
    hs14 18000000 18999999 0.0000 fill_color=hs5
    hs14 18000000 18999999 0.0000 fill_color=hs6
    hs14 18000000 18999999 0.0000 fill_color=hs7
    hs14 18000000 18999999 0.0000 fill_color=hs8
    hs14 18000000 18999999 0.0000 fill_color=hs9
    hs14 18000000 18999999 0.0000 fill_color=hs10
    hs14 18000000 18999999 0.0000 fill_color=hs11
    hs14 18000000 18999999 0.0000 fill_color=hs12
    hs14 18000000 18999999 0.0000 fill_color=hs13
    hs14 18000000 18999999 0.0000 fill_color=hs19
    hs14 18000000 18999999 0.0000 fill_color=hs20
```
The advantage of -output_style 2 is that it can be filtered for a chromosome
of interest to determine its contribution to the links.

```    
    > bin/binlinks -output_style 2 | grep =hs22
    ...
    hs14 18000000 18999999 688034.0000 fill_color=hs22
    hs14 19000000 19999999 264389.0000 fill_color=hs22
    hs14 20000000 20999999 0.0000 fill_color=hs22
    ...
```
#### creating stacked histograms
Finally, -output_style 3 generates track data for stacked histograms.

```    
    > bin/binlinks -output_style 3
    fill_color=hsx,hsy,hs1,hs2,hs3,hs4,hs5,hs6,hs7,hs8,hs9,hs10,hs11,hs12,hs13,hs14,hs15,hs16,hs17,hs18,hs19,hs20,hs21,hs22
    ...
    hs14 18000000 18999999 0.0000,0.0000,0.0000,0.0000,0.0000,0.0000,
    		       0.0000,0.0000,0.0000,0.0000,0.0000,0.0000,
    	               0.0000,0.0000,0.0000,303434.0000,235624.0000,
    		       17348.0000,18850.0000,257791.0000,0.0000,0.0000,
    		       218463.0000,688034.0000
    ...
```
The data is written to STDOUT and the color list to STDERR, so you should
redirect them appropriately.

```    
    # redirect histogram values to a file and send STDERR to terminal - cut and paste 
    # the color values into the histogram  block
    > bin/binlinks -output_style 3 > data.txt 
```
The colors will be named after the target chromosomes. I typically use hsNNN
for human chromosomes (to distinguish them from chromosomes of other species
such as mouse (mmNNN), rat (rnNNN), and so on). However, chromosome colors are
encoded with names chr1, chr2, chr3, and so on. You'll need to either change
(or add) color definitions in etc/colors.conf in the Circos distribution or
rename the colors from CHRPREFIXNNN to chrNNN.
### images
[Lesson](/documentation/tutorials/utilities/density_tracks/lesson)
[Images](/documentation/tutorials/utilities/density_tracks/images)

![Circos tutorial image - Generate Link Density
Tracks](/documentation/tutorials/utilities/density_tracks/img/01.png) ![Circos
tutorial image - Generate Link Density
Tracks](/documentation/tutorials/utilities/density_tracks/img/02.png) ![Circos
tutorial image - Generate Link Density
Tracks](/documentation/tutorials/utilities/density_tracks/img/03.png) ![Circos
tutorial image - Generate Link Density
Tracks](/documentation/tutorials/utilities/density_tracks/img/04.png) ![Circos
tutorial image - Generate Link Density
Tracks](/documentation/tutorials/utilities/density_tracks/img/05.png) ![Circos
tutorial image - Generate Link Density
Tracks](/documentation/tutorials/utilities/density_tracks/img/06.png) ![Circos
tutorial image - Generate Link Density
Tracks](/documentation/tutorials/utilities/density_tracks/img/07.png)
### configuration
[Lesson](/documentation/tutorials/utilities/density_tracks/lesson)
[Images](/documentation/tutorials/utilities/density_tracks/images)
