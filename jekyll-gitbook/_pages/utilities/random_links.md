---
author: DoubleCat
date: 2025-04-11
layout: post
category: utilities
title: Generating Random Link Data
---

## Generating Random Link Data
### lesson
[Lesson](/documentation/tutorials/utilities/random_links/lesson)
[Images](/documentation/tutorials/utilities/random_links/images)

### script location
```    
    tools/randomlinks
```
### script usage
```    
    > cd tools/randomlinks
    > ./run
    Done. Now look in data/links.txt.
```
To get the full manpage, use -man.

```    
    > cd tools/randomlinks
    > bin/randomlinks -man
```
Adjust the configuration file etc/randomlinks.conf to suit your needs.

### details
The purpose of this script is largely for debugging. If you don't have any
link data, you can generate some random link relationships between chrososomes
sampled from a karyotype file.

Bias can be introduced into the placement of the random links through rules
that associate the number of links (average and standard deviation - link copy
number is sampled from a normal distribution) with a pair of regular
expressions that define chromosome pairs.

For example, the following ruleset

```    
    rule = . . 2 0
    rule = chr12 chr14 10 2
    rule = chr15 chr20 r5
```
defines three rules. Rules are evaluated in increasing order of specificity.
The first rule affects all chromosomes and sets the baseline number of links
between any chromosome pair to 2 (avg=2,sd=0). The next rule defines the
number of links between chr12 and chr14 to be avg=10 sd=2. The last rule sets
the number of links between chr15 and chr20 to be 5x the number defined by
previous rules.

The configuration file (etc/randomlinks.conf) defines several rules that can
get you started.

![](/circos/images/circos-random.png)

These random links are a great input to other link-related tools like
bundlelinks and orderchr.

### randomlinks manpage
  * NAME
  * SYNOPSIS
  * DESCRIPTION
    * Link Multiplicity Rules
  * HISTORY
  * BUGS
  * AUTHOR
  * CONTACT

* * *

* * *

## NAME
randomlinks - generate a data file with random links between chromosomes

* * *

## SYNOPSIS
```    
      randomlinks -karyotype KARYOTYPE_FILE 
                  {-chr_rx REGEX } -size AVG[,SD] [-nointra] [-nointer]

* * *

## DESCRIPTION
Generate a Circos link file containing random links between chromosomes.
Chromosomes are sampled from the karyotype file KARYOTYPE_FILE and optionally
further filtered using the regular expression REGEX.

The number of links between any two chromosome pairs is determined by rules
(see below). The size of the ends of each link is determined by the average
and standard deviation values provided by -size. Links with thick ends are
best drawn as ribbons.

Intrachromosomal links can be avoided using -nointra. Similiarly,
interchromosomal links can be avoided using -nointer. The -nointer option is
much less useful.

### Link Multiplicity Rules
Given a filtered set of chromosomes (first sampled from the KARYOTYPE_FILE and
then passed through the regular expression REGEX), the number of links joining
any pair of chromosomes is determined by a set of rules.

Each rule contains two regular expressions, one for each of the chromosomes in
the pair, and these determine which pairs of chromosomes the rule will apply
to.

For example, if the regular expressions are '.' and '.' then all chromosome
pairs are matched. However, if the regular expressions are '.' and 'chr10'
then only pairs of chromosomes for which one contains chr10 are affected.

In addition to the regular expression selection filter, each rule contains
either (a) avg/sd parameters used to generate a normally distributed random
number which is used as the number of links between the selected chromosomes,
or (b) a multiplier which is used to multiply the number of links as
determined by a previous rule.

Optionally, rules may contain a sampling parameter which determines how
frequently the rule is applied.

Rules are applied in increasing order of specificity. Thus, rules that affect
the largest number of chromosome pairs are applied first, followed by rules
that affect fewer pairs.

For more details about the syntax of rules, see etc/randomlinks.conf.

* * *

## HISTORY
  * **10 Feb 2009 v0.3**  

Minor bug fix.

  * **7 Jul 2008 v0.2**  

Added documentation and refined rule set syntax.

  * **2 Jul 2008 v0.1**  

Started and versioned.

* * *

## BUGS
* * *

## AUTHOR
Martin Krzywinski

* * *

## CONTACT
```    
      Martin Krzywinski
      Genome Sciences Centre
      Vancouver BC Canada
      www.bcgsc.ca
      martink@bcgsc.ca
### images
[Lesson](/documentation/tutorials/utilities/random_links/lesson)
[Images](/documentation/tutorials/utilities/random_links/images)

![Circos tutorial image - Generating Random Link
Data](/documentation/tutorials/utilities/random_links/img/01.png)
### configuration
[Lesson](/documentation/tutorials/utilities/random_links/lesson)
[Images](/documentation/tutorials/utilities/random_links/images)
