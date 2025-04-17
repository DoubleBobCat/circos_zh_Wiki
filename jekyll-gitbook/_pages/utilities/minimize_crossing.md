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

## 2\. Reordering Ideograms to Minimize Overlap

[Lesson](/documentation/tutorials/utilities/minimize_crossing/lesson)
[Images](/documentation/tutorials/utilities/minimize_crossing/images)

## script location

    
    
    tools/orderchr
    

## script usage

    
    
    > cd tools/orderchr
    > ./run
    ...
    improvement(minimize) orig 1164 final 124 change 89.35%
    chromosomes_order = chr9,chr5,chr15,chr16,chr18,chr14,chr3,chr20,chr7,chr8,chr10,chr4,chr12,chr6,chr2,chr17,chr1,chr19,chr13,chr11
    

The final line reported by the script provides the suggested chromosomes_order
- copy this line into the circos.conf file.

To get the full manpage, use -man.

    
    
    > cd tools/orderchr
    > bin/orderchr -man
    

Adjust the configuration file etc/orderchr.conf to suit your needs.

You can generate link data randomly using the randomlinks tool.

## details

The script minimizes (or maximizes) the link cross score, which is a quantity
that estimates the number of links that cross in the image. The link score is
influenced solely by the start and end position (chromosome and coordinate) of
each link. The score is an estimate because the link geometry (Bezier curve
settings) are not taken into account. The link score does not include any
crossing between intra-chromosomal links, since no amount of chromosome
shuffling can mitigate these crossings.

The script is currently not capable of working with chromosome ranges and axis
breaks. In other words, you cannot optimize layout of chromosomes which have
been broken into components (e.g. chr2-> chr2a:0-10Mb, chr2b:20-30Mb,
chr2c:30-40Mb, etc). If you want to use axis breaks, you'll have to create new
chromosomes (e.g., chr2a, chr2b, chr2c, ...) that represent the components of
the original chromosome (chr2) and adjust the karyotype and link data file
accordingly.

Given a set of links L, sorted by angular position of link start, the link
cross score is given by

![](/circos/images/eq-crossing.png)

where the terms are as follows. Each link pair (i,j) (angular position of
start of link i is greater than that of j) contributes +1 to the crossing
score if the links cross. Whether they cross is determined by the position of
the angular positions of the links' start/end positions. The links are deemed
to cross if the angular positions are interleaved.

![](/circos/images/circos-cross.png)

### deterministic optimization

One of the ways in which Circos's links can be effectively used to visualize
alignment data between two related structures. These structures could be two
genomes, or two similar regions of the same genome, or even two physically
different representations of the same structure (e.g. a fingerprint map and
sequence assembly).

![](/circos/images/circos-cross-02.png)

When a Circos is used to show alignments, it is very helpful to have the
chromosomes ordered in such a way as to reduce link crossing. Chromosomes
should be ordered so that any link crossing is an indication of real
differences in the underlying structures.

For example, consider this image which shows a comparison between two sets of
structures, arbitrarily named chromosomes a1,a2,... and b1,b2,... It is
obvious that most of the data relate one of the "b" structures to many "a"
structures. For example, these type of data sets are common when comparing a
single contiguous structure (e.g. chromsome sequence assembly, supercontig,
etc) to many smaller structures (e.g., resequencing contigs). However, because
the chromosomes a* and b* are not well ordered, a lot of the links cross and
it is not possible to determine whether the crossing is due to the order or to
irreducible (i.e., leading to crossings that cannot be mitigated by
rearrangement) differences in the chromosomes.

This kind of link relationships can be deconvoluted by using the deterministic
optimization component of the orderchr script. This optimization reorders
chromosomes based on degree of connectivity. Given one chromosome, all
chromosomes connected to it are placed immediately after it, in decreasing
order of the number of shared links. The result of this shuffling quickly
produces a view of the data that is less cluttered.

When applying the deterministic optimization, it is helpful to place all the
chromosomes from one set first (e.g. all the b* chromosomes) to straighten the
links (example). Even though more links cross in the right panel of this
example, it is easier to spot block-level differences. Initial order is
controlled using -init_order* parameters.

![](/circos/images/circos-cross-03.png)

This optimization is termed "deterministic" because the algorithm always
produces the same layout, and in part, to contrast the other type of
optimization, which is stochastic (read below). The order created by the
deterministic optimization is suitable as input to the stochastic optimization
routine, and for this reason the deterministic ordering is refered to as
"warmup" in the documentation and configuration of orderchr.

### stochastic optimization

The stochastic routine uses simulated annealing (SA) to derive an chromosome
layout that minimizes (or maximizes) the link score function. The best
solution is not guaranteed, however, and I encourage you to run the simulation
several times to determine the convergence of the solution. Ideally, all
instances of the simulation should return layouts whose score is very similar
(e.g. with in 1-2%).

The stochastic routine can be initialized with the order from the
deterministic optimization, or initialized with an arbitrary order. The
-init_order* parameters control the order. Furthermore, certain chromosomes
can be forced to remain static during the shuffling using -static* parameters.
This is helpful when you wish to keep the order of certain structures fixed.

In this example image, I show the same link data with six different chromosome
layouts. The link score function is shown in the center of the image.

Depending on the nature of the data, you may not be able to significantly
reduce link crossing. When the majority of your chromosomes are highly inter-
connected, then any order results in a lot of crossings. The link crossing
score in the above example could be reduced from 835 to 262, a 70%
improvement. However, in this segmental duplication data set, the score cannot
be reduced by more than about 50%.

## orderchr manpage

  * NAME
  * SYNOPSIS
  * DESCRIPTION
  * DEFINING WHICH CHROMOSOMES TO SHUFFLE
    * MODE 1 - shuffle set defined by link data
    * MODE 2 - shuffle set defined by file
    * MODE 3 - shuffle set defined by regular expression
    * MODE 4 - shuffle set defined by list
    * MODE 5 - multimode
  * DEFINING INITIAL ORDER
  * DEFINING WHICH CHROMOSOMES TO REMAIN ANCHORED
  * CONTROLING THE OPTIMIZATION
    * Warmup Round
    * Stochastic Optimization Round
  * SIMULATED ANNEALING
    * iterations
    * max_flips, min_flips
    * temp0
    * optimize = minimize|maximize
  * SIMULATION SCHEDULE
    * No Warmup, Single Stochastic Round
    * No Warmup, Multiple Stochastic Rounds
    * Warmup, Multiple Stochastic Rounds
  * HISTORY
  * BUGS
  * AUTHOR
  * CONTACT

* * *

* * *

# NAME

orderchr - determine a chromosome order to minimize cross-over of links

* * *

# SYNOPSIS

    
    
      orderchr -links linkfile.txt 
               -karyotype karyotype.txt 
               { -shuffle_file chrs_to_shuffle.txt | -shuffle LIST | -shuffle_rx REGEX_LIST } 
               {-static LIST} {-static_rx REGEX_LIST}
               {-init_order LIST} {-init_order_rx REGEX_LIST}
    

* * *

# DESCRIPTION

By examining the frequencies of chromosome-chromosome relationships defined in
the link file, this script suggests a new order for chromosomes that results
in fewer cross-overs between links. Simulated annealing is used to optimize
the chromosome order (read below about parameters). Run the simulation a
couple of times to check convergence (finding a global minimum is not
guaranteed).

* * *

# DEFINING WHICH CHROMOSOMES TO SHUFFLE

The set of chromosomes to shuffle is specified by either (a) link data,
whereby all chromosomes that have links are subject to shuffling (b)
-shuffle_file, whereby only those chromosomes listed in the file are shuffled
(c) -shuffle, whereby the set of chromosomes to shuffle is specified by a
list, and (d) -shuffle_rx, whereby only those chromosomes that match a regular
expression are shuffled. Any chromosome that is not identified by one of these
methods does not participate in the shuffling process. Specifically, any links
to/from such chromosomes are not considered when minimizing link crossing.

* * *

## MODE 1 - shuffle set defined by link data

    
    
      > orderchr -links linkfile.txt
    

All chromosomes mentioned in the -links file will be subject to reordering.
The initial order will be taken from order of appearance in the karyotype
file.

* * *

## MODE 2 - shuffle set defined by file

    
    
      > orderchr -links linkfile.txt -shuffle_file chrs_to_shuffle.txt
    

The set of chromosomes to shuffle is given in the -shuffle_file file, which
contains one chromosome per line. For example

    
    
      > cat chrs_to_shuffle.txt
      chr1
      chr5
      chr12
      chr17
      ...
    

The initial order will be taken from order of appearance in the file.

* * *

## MODE 3 - shuffle set defined by regular expression

    
    
      > orderchr -links linkfile.txt -shuffle_rx chr1
    

Same as MODE 1, except that chromosome list will be filtered using the regular
expression and only those chromosomes that match the regular expression are
shuffled.

In this example, chromosomes matching chr1'' will be shuffled (e.g. chr1,
chr10, chr11, etc).

* * *

## MODE 4 - shuffle set defined by list

    
    
      > orderchr -links linkfile.txt -shuffle chr1,chr2,chr6,chr7,chr10
    

Same as MODE 3, except that chromosomes are specified by a list.

In this example, chromosomes chr1,chr2,chr6,chr7, and chr10 will be shuffled.

* * *

## MODE 5 - multimode

You can combine -shuffle_file, -shuffle_rx and -shuffle to additively define
the shuffle list.

* * *

# DEFINING INITIAL ORDER

The initial order of chromosomes can be defined in two ways. First, the method
that is used to specify which chromosomes to shuffle will dictate the initial
order. Modes 1 and 2 (see above) use the order of chromosomes as they appear
in the karyotype file. Mode 3 (see above) uses the order from the shuffle
file.

You can override the initial order using the -init_order parameter. The value
of this parameter is expected to a comma-delimited list of chromosomes, which
may be the full set or a subset of chromosomes.

For example, if the entire set of chromosomes to shuffle is chr1..chr5, then
you can specify the initial order which explicitly orders each chromosome

    
    
      -init_order chr2,chr5,chr1,chr3,chr4
    

or just a subset

    
    
      -init_order chr2,chr5
    

In the latter case, the final order will be

    
    
      { chr2,chr5 } , { chr1,chr3,chr4 }
    

comprised of two order groups: leading group of chromosomes as ordered by
-init_order and a group of remaining chromosomes, in order of appearance as
set by parameters in the section DEFINING WHICH CHROMOSOMES TO SHUFFLE.

If a chromosome mentioned in -init_order is not a candidate for shuffling, its
mention in the order string will be ignored.

The option -init_order_rx works just like -init_order, except that the list a
list of regular expressions rather than chromsome names. For example,

    
    
      -init_order chr1,chr2
    

is equivalent to

    
    
      -init_order { chrs matching /chr1/ },{ chrs matching /chr2/ }
    

and for the canonical human genome with standard order this would be

    
    
      -init_order chr1,chr10,chr11,chr2,chr20,chr21,chr22
    

Since this is a subset of chromosomes, the final initial order will be
automatically completed by chromosomes from the karyotype file that were not
explicitly ordered

    
    
      chr1, chr10, chr11, chr2, chr20, chr21, chr22, chr3..chr9, chr12..chr19, chrX, chrY
    

If both -init_order_rx and -init_order are defined, order is initially defined
by -init_order_rx and then refined using -init_order. Thus

    
    
      -init_order chr10,chr20,chrx -init_order_rx chr1,chr2
    

will result in

    
    
      chr10, chr20, chrx, chr1, chr11, chr2, chr21, chr22, chr3..chr9, chr12..chr19 ,chrY
    

* * *

# DEFINING WHICH CHROMOSOMES TO REMAIN ANCHORED

After the set of chromosomes to shuffle has been defined, and the initial
order has been set, you can define a subset of chromosomes to remain in the
same order (static) throughout the shuffling process.

The difference between a chromosome (a) not being part of a shuffle set and
(b) being part of a shuffle set, but remain static, is that in the former,
links to chromosomes do not play a role in the ordering process whereas in the
latter case links to these chromosomes contribute to the shuffle score. Thus,
chromosomes which are static have all non-static chromosomes shuffled around
them in order to minimize link crossover.

Defining static chromosomes is done by a comma-delimited list of regular
expressions

    
    
      > orderchr -links linkfile.txt -static_rx chr1
    

In this example, all chromosomes matching the regular expression chr1 will not
have their order adjusted. Any links to/from these chromosomes will contribute
to the total link crossing score, but the chromosomes themselves will not be
moved. For example, if the original order of chromosomes is

    
    
      chr1,chr2,chr3,chr10,chr11,chr20,chr21
    

then any shuffle solution will have the order

    
    
      chr1,-,-,chr10,chr11,-,-
    

with chr1, chr10 and chr11 remaining fixed.

To define multiple regular expressions, use a list of regular expressions.

    
    
      > orderchr -links linkfile.txt -static_rx chr1,x,y
    

Like with -init_order, you can use the chromosome names to define static
entries using -static.

    
    
      -static chr1,chr2,chr3
    

will keep chromosomes chr1, chr2 and chr3 always in the same position. You can
combine -static_rx and -static

    
    
      -static_rx chr1,chr2 -static chrx,chry
    

in which case all chromosomes that match either the regular expressions
defined by -static_rx or the names defined by -static will be kept in the same
position during shuffling.

* * *

# CONTROLING THE OPTIMIZATION

The order optimization process comprises one or more rounds. Each round is
defined by a <round> block in the <simulation> block

    
    
      <simulation>
       <round>
        # settings for round 1
       </round>
       <round>
        # settings for round 2
       </round>
       ...
      </simulation>
    

A round can be either a warmup (read below), or a full simulated annealing
process (read below). The outcome of the warmup is deterministic, and thus the
warmup should only be used as the first (optional) round.

* * *

## Warmup Round

During the warmup round, the initial order of the chromosomes is defined based
on the degree of connectivity between chromosome pairs.

This warmup is most suited for data sets in which most relationships between
chromosomes are many-to-one (e.g., chromosome A has links to many chromosomes
B,C,D,... but each of B,C,D generally only links to A). Many-to-one data sets
are common for alignments (e.g. chr A corresponds to the chromosome whereas
and points to ctg A, B, C, ... all sequence contigs that map to disjoint
regions on chr A).

The warmup algorithm is as follows. The chromosome (chrA) with the most links
is selected first and used to initialize the new order. A list of all links to
chrA is created, grouped by chromosome, and sorted based on the average
position of the link on chrA. Chromosomes are added to the new order based on
descending order of grouped link position. Once all chromosomes are placed,
the next unplaced chromosome with the most links is selected and the process
continues until all chromosomes are placed.

The warmup is deterministic - it will result in the same order each time. It
is insensitive to the initial order, or values of -static and -static_rx.

    
    
      <round>
       warmup = yes
      </round>
    

* * *

## Stochastic Optimization Round

After the optional warmup round, all other rounds should be of stochastic type
(this is the default round type, if warmup=yes is not set).

Parameters for the round are defined as follows

    
    
      <round>
        iterations = 1000
        max_flips  = 10
        min_flips  = 2
        temp0      = 0.01
      <round>
    

For the details of each parameter, read the section below. You can set
parameter values to be relative to values of the previous round by prefixing
the parameter with r''. For example,

    
    
      <round>
        iterations = 1000
        ...
        temp0      = 0.01
      <round>
    
    
    
      <round>
        iterations = r2
        ...
        temp0      = r0.5
      <round>
    
    
    
      <round>
        iterations = r2
        ...
        temp0      = r0.5
      <round>
    

defines three rounds. The first round has 1000 iterations with temp0=0.01. The
second round has 2x iterations (2000) and a value of temp0 of 0.5*0.01=0.005.
The third round has again 2x iterations (4000) and temp0 of 0.5*0.005=0.0025.

Relative parameter values are very useful for additional rounds when the
transition probability is decreased (temp0 is lowered). You can decrease temp0
in relative steps, without needing to remember what the previous value was.
This allows you to create a multi-round optimization schedule with all
parameter defined in a single place (first round).

The solution at the end of a round is used as the initial order for the next
round.

* * *

# SIMULATED ANNEALING

This method is an optimization method that encourages the discovery of a
global minimum by traversing the space of solutions with a small (and
decreasing as simulation runs) chance of visiting less desirable solutions.

There are three parameters that control the optimization.

* * *

## iterations

The number of iterations to perform. At each iteration, the current solution
is randomly modified and either accepted or rejected.

* * *

## max_flips, min_flips

The optimization run is split into max_flips-min_flips+1 equal-sized
intervals. During each iterval, the number of random chromosome pair swaps in
the solution is given by

    
    
      min_flips + (max_flips-min_flips)*(1-t)
    

where t is a relative round completion time t=0..1 at the current iteration.

For example, if max_flips is 5 and min_flips is 2 and iterations=1000. Then
the number of random pair swaps is

    
    
      iteration 1-249    5
      iteration 250-499  4
      iteration 500-749  3
      iteration 750-1000 2
    

I suggest starting with a value that corresponds to 5% of the chromosomes. For
example, if you have 100 chromosomes, use max_flips=5 to start. It's also a
good idea to set min_flips=1 for the last round to avoid abandoning the
solution (remember that in simulated annealing it is possible to discard a
solution for a worse solution).

* * *

## temp0

This parameter determines the probability of a transition to a less desirable
solution. The transition probability is

    
    
      p(dE) = temp0*exp( - dE/t )
    

where t=1..0 over the length of the simulation and dE is the relative change
in the desirability of two solutions.

If temp0=1, then the probability of accepting a solution that is 10% worse
(e.g. dE=0.1) is

    
    
      p(0.1) = exp (-0.1/1)   = 90%    at start of simulation
             = exp (-0.1/0.5) = 82%    half way through simulation
             = exp (-0.1/0.1) = 37%    90% of the way through simulation
    

By lowering temp0, you lower the probability of transition to a less desirable
solution.

Do not adjust temp0 unless you feel that the simulation is (a) not traversing
the solution space sufficiently - in which case make temp0 larger or (b) too
many low-quality solutions are accepted - in which case make temp0 smaller.

* * *

## optimize = minimize|maximize

Most of the time you'll want to adjust the chromosome order in a way to
minimize the number of crossing links. However, you can set to maximize the
number of crossing links by setting

    
    
      optimize = maximize
    

* * *

# SIMULATION SCHEDULE

* * *

## No Warmup, Single Stochastic Round

    
    
      <simulation>
      <round>
       iterations = 1000
       max_flips  = 10 # or set this to ~5% of your chromosomes
       min_flips  = 1
       temp0      = 0.01
      </round>
      </simulation>
    

* * *

## No Warmup, Multiple Stochastic Rounds

The purpose of rounds 2 and 3 is to successively decrease the transition
probability to worse solutions and also decrease the degree to which
successive candidate solutions vary from the current solution. In these
rounds, a more careful search is carried out around the solution provided in
round 1.

    
    
      <simulation>
      <round>
       iterations = 1000
       max_flips  = 10 # or set this to ~5% of your chromosomes
       min_flips  = 1
       temp0      = 0.01
      </round>
      </simulation>
      <simulation>
      <round>
       iterations = r2    # 2000
       max_flips  = 2
       min_flips  = 1
       temp0      = r0.5  # 0.005
      </round>
      <round>
       iterations = r2    # 4000
       max_flips  = 1
       min_flips  = 1
       temp0      = r0.1 # 0.0005
      </round>
      </simulation>
    

* * *

## Warmup, Multiple Stochastic Rounds

    
    
      <simulation>
      <round>
       warmup = yes
      </round>
      <round>
       iterations = 1000
       max_flips  = 10 # or set this to ~5% of your chromosomes
       min_flips  = 1
       temp0      = 0.01
      </round>
      </simulation>
      <simulation>
      <round>
       iterations = r2    # 2000
       max_flips  = 2
       min_flips  = 1
       temp0      = r0.5  # 0.005
      </round>
      <round>
       iterations = r2    # 4000
       max_flips  = 1
       min_flips  = 1
       temp0      = r0.1 # 0.0005
      </round>
      </simulation>
    

* * *

# HISTORY

  * **14 July 2008**

Expanded documentation and added _rx parameters.

  * **8 July 2008**

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
    

