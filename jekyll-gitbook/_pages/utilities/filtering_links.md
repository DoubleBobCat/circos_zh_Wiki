---
author: DoubleCat
date: 2025-04-11
layout: post
category: utilities
title: Filtering Links
---

### lesson
### script location
```    
    tools/filterlinks
```
### script usage
```    
    > cd tools/filterlinks
    > ./run
    Processing data/dog.vs.human.subset.txt
    Now look in data/dog.vs.human.subset.filtered.txt
```
The script sends a new links file to STDOUT and the report shown above to
STDERR.

To get the full manpage, use -man.

```    
    > cd tools/filterlinks
    > bin/filterlinks -man
```
Adjust the configuration file etc/filterlinks.conf to suit your needs.

### details
This script is used to generate a new link file, composed of links that pass
certain rules.

Although Circos supports rules in its configuration file, which you can use to
alter data formatting on the fly, you may find that creating a new link file
is more convenient.

For example, if you are using Circos in an interactive web page, you want to
generate the image as quickly as possible. Since Circos' built-in rule engine
is slower than this script, filterlinks is handy way to eliminated unwanted
data upstream of Circos.

Another situation in which filterlinks is useful is to generate an input file
to orderchr, which minimizes crossing of links by shuffling chromosomes around
the image circle. Since the speed of orderchr proportional (in a nasty way) to
the number of links, it's important to pass it as many links as you need to
get the job done, but no more than that.

You filter on any property of the link with filterlinks:

  * link id 
  * chromosome 
  * start and end position 
  * size 
  * span (intersect with genomic region) 
  * format options (color, thickness, z, etc) 

and any property can be tested with one of these rules

  * regular expression (e.g. chr1 matches "x") 
  * exact string match (e.g. chr1 is "hs1") 
  * smaller and greater than (numerical or string order) (e.g. start < 10Mb) 
  * integer span (e.g. link span intersects 10-20Mb) 

Briefly (read the manpage below for all the details), the results of each rule
test are all OR'ed together. Thus, it is sufficient for one rule to pass to
pass the link.

Thus, if you have three rules, the link will be passed if

```    
        RULE1 or RULE2 or RULE3
```
By assigning IDs to sets of rules, you can group rules together to build up a
complex filter which includes AND. In the example below, rules 1-3 have been
assigned a distinct ID (0) and rules 4-5 were given ID 1. These IDs control
how rule results are combined: intra-ID rules are AND'ed and inter-ID rules
are OR'ed.

```    
      ( RULE1 and RULE2 and RULE3 ) OR ( RULE4 and RULE5 )
        _________________________        _______________
        ^ rule set 1 (e.g. ID=0)         ^ rule set 2 (e.g. ID=1)
```
### filterlinks manpage
  * NAME
  * SYNOPSIS
  * DESCRIPTION
  * RULES
    * Link Parameters
    * Conditions
  * EXAMPLES
    * Filtering by Chromosomes
    * Filtering by Position
    * Filtering by Link Options
    * Mixing Conditions and IDs
  * HISTORY
  * BUGS
  * AUTHOR
  * CONTACT

* * *

* * *

## NAME
filterlinks - filter the link file based on link parameters

* * *

## SYNOPSIS
```    
      filterlinks -links linkfile.txt [-nointer] [-nointra] [-debug]
```
* * *

## DESCRIPTION
* * *

## RULES
A filter rules contains two parts: the link parameter which is tested and a
list of acceptable conditions.

The two exceptions are the -nointer and -nointra flags. These can be used to
filter out inter-chromosomal links (ends of link are on different chromosomes)
and intra-chromosomal links (ends of link are on the same chromosome). These
two rules are strict, meaning that if a link does not pass them, no other
rules are tested and the link is immediately rejected.

* * *

### Link Parameters
```    
      link_param = condition1,condition2,...
```
Because each link has two ends, each link parameter may give rise to three
distinct rules

```    
      link_param   = condition1,condition2,...
      link_param_1 = condition1,condition2,...
      link_param_2 = condition1,condition2,...
```
which test, respectively, both ends with the condition (both ends must pass),
the first end, and the second end. The first end of the link corresponds to
the first line of the link line pair. For example, given the link ...
link018136 cf12 9800000 9900000 link018136 hs6 37914056 37916509 ...

the first end is cf12:9800000-9900000 and the second end is
hs6:37914056-37916509.

  * **chr**

Applies the condition to the chromosome of the link.

    
          chr   = 1
      chr_2 = x
    

  * **start, end, size**

Applies the condition to the start, end or size of the link. The link size is
end-start+1.

    
          start = [?<]10000000
      end   = [?>]50000000
    

  * **span**

Applies the condition to the span of the link and should be used with the s''
condition TYPE.

    
          span = [?i]1000-2000
    

  * **id**

Applies the condition to the id of the link.

  * **color, thickness, z, etc.**

Any condition that is not one of id, chr, start, end, size, span is assumed to
be a link option and is applied to the option of the link. For example,
options include color, thickness, and z.

    
          color = [?e]chr12
      z = [?>]10
    

* * *

### Conditions
A condition has the following format

```    
      { [?TYPE {ID} {!} ] } CONDITION
```
where elements in { } are optional. Briefly, TYPE is used to indicate how the
CONDITION text should be applied (e.g. regular expression, integer range,
exact match, etc). The ID is used to combine rules so that their match status
is AND'ed together to determine whether the link passes. The trailing !'' is
used to negate the rule (i.e. for the link to pass, the rule must fail).

  * **Default Condition is a Regular Expression**

If no optional elements in the condition are specified, it is treated as a
regular expression. For example,

    
          LINK_PARAM = 12
    

would apply the regular expression 12'' to the link parameter. You can provide
a list of conditions with ;; as a delimiter (you can adjust the delimiter in
the configuration file).

    
          LINK_PARAM = 12;;x;;y
    

which are interpreted as a series of regular expressions used to test the link
parameter. The link will be passed if ANY condition matches (i.e. match
results are OR'ed). If you want match results to be AND'ed (i.e. multiple
rules must match for the link to pass, read below).

The regular expression is case-insensitive.

  * **Adjusting Condition Type**

The following conditions types are possible

    * **r - regular expression (default)**
        
                  LINK_PARAM = 12
          LINK_PARAM = 12;;x;;y
        

You can specify the type as a regular expression explicitly with [?r] but this
is not necessary because that is the default.

        
                  LINK_PARAM = [?r]12;;[?r]x;;[?r]y
        

    * **s - integer span**

The syntax of the integer range is any string supported by Set::IntSpan.

        
                  LINK_PARAM = [?s]1000-2000
          LINK_PARAM = [?s]1000-2000,3000-4000
          LINK_PARAM = [?s]1000-2000,3000-)
          LINK_PARAM = [?s](-1000,2000,3000-)
          LINK_PARAM = [?s](-1000,2000,3000-4000,5000-)
        

    * **e - exact match**

The exact match is useful for matching chromosome names in cases where regular
expressions might match other chromosomes (and you don't want to include
anchors in your regular expression).

        
                  LINK_PARAM = [?e]chr1
          LINK_PARAM = [?e]chr1;;[?e]chr2
        

Note that the condition type must be prefixed to each individual condition, if
a list of conditions is supplied.

The exact match is not case-sensitive.

    * **< \- less than**

If the value is a number, numerical < is used, otherwise the values are
compared based on asciibetic order (e.g. le).

        
                  # LINK_PARAM must be less than 100
          LINK_PARAM = [?<]100
        
        
                  # LINK_PARAM must be less (in the asciibetic sense) than chr20 (e.g. chr1, chr11, chr111, chr19, etc)
          LINK_PARAM = [?<]chr20
        

    * **> \- greater than**

Works just like the less than condition [?<].

    * **mixing condition types**

You can have multiple condition types for a parameter. Remember that results
of each condition will be OR'ed together.

        
                  LINK_PARAM = 1,[?e]chr5,[?e]chr22
        

The first condition is a regular expression (by default). The second and third
conditions are exact text matches for chr5 and chr22. Thus, the LINK_PARAM
will pass if (a) it contains a 1'', or (b) it is chr5'' or (c) it is chr22''.

  * **Negating a Condition**

In order to negate a condition, use !''. When !'' is used, the condition must
fail for the result to be acceptable.

    
          # must not match regular expression "1"
      LINK_PARAM = [?r!]1
```    
          # must not be "chr12"
      LINK_PARAM = [?e!]chr12
```    
          # must not be within the range 1000-2000
      LINK_PARAM = [?i!]1000-2000
```
In order to combine negated conditions with positive ones, you will need to
group conditions so that their results are AND'ed.

  * **Grouping Conditions**

So far, all condition results were evaluated with OR. In other words, if you
had a list of conditions, the successful pass of any of the conditions
resulted in the link being passed. This is useful if you want to accept
multiple values

    
          # chr12 or chr14 
      LINK_PARAM = [?e]chr12;;[?e]chr14
    

However, what if you wanted to match regular expression 1'' but not chr14.
Here's where the ID field comes in. By tagging multiple conditions with the
same ID field the results of each of these conditions is AND'ed together to
determine whether the link passes.

    
          # ID=0 
      # match regular expression "1" AND not be "chr14"
      LINK_PARAM = [?r0]1;;[?e0!]chr14
    

* * *

## EXAMPLES
Below are some examples to get you started. Note the interplay between
conditions with IDs and condition without IDs. The former collate conditions
into AND'ed sets, which are then in turn OR'ed with other sets and with
conditions without IDs.

* * *

### Filtering by Chromosomes
To select links in which both ends match regular expression 1''

```    
      chr = 1
```
So simple. Now, to select links in with either ends matches regular expression
1'',

```    
      chr_1 = 1
      chr_2 = 1
```
The difference between these two cases is that in the first instance, since
the link_parameter does not include a _1 or _2 suffix, the condition is
applied to both ends of the link and both ends must pass. In the second case,
each end is tested independently and the results are OR'ed together.

If you want links where the first chromosome matches x or the second matches
y,

```    
      chr_1 = x
      chr_2 = y
```
The test is (chr_1 match x'') OR (chr_2 match y''). Note, however, that this
set of rules requires that the first chromosome match x'' OR the second
chromosome match y''. It will fail if the first chromosome matches y'' and the
second matches x''. To match both possibilities, you might try

```    
      chr_1 = x;;y
      chr_2 = y;;x
```
In this case the test is (chr_1 match x'') OR (chr_1 match y'') OR (chr_2
match x'') OR (chr_2 match y'').

If you are looking for links between x and y chromosomes, then you require the
results of each condition to be AND'ed. For this, use IDs

```    
      chr_1 = [?r1]x
      chr_2 = [?r1]y
```
Both of these rules have ID=1 and are therefore grouped into a set. Match
results within a set are AND'ed. Thus, the test is (chr_1 match x'') AND
(chr_2 match y''). If you want to match the other order too,

```    
      chr_1 = [?r1]x;;[?r2]y
      chr_2 = [?r1]y;;[?r2]x
```
In this example, there are two IDs. The rules with ID=0 match chr1 to x'' and
chr2 to y'' and the rules with ID=1 match the converse (chr1 to y'' and chr2
to x'').

Now let's suppose we want links that are either cf1-hs6, cf14-hs7 or cfx-hsx.
Here cf is a dog chromosome and hs is a human chromosome. The rule for this is

```    
      chr_1 = [?e1]cf1;;[?e2]cf14;;[?e3]cfx
      chr_2 = [?e1]hs6;;[?e2]hs7;;[?e3]hsx
```
You can add additional conditions without IDs to accept more links. For
example, if you also wanted to add any links for which chr_1 was cf9 or for
which chr_2 matched 3''

```    
      chr_1 = [?e1]cf1;;[?e2]cf14;;[?e3]cfx;;[?e]cf9
      chr_2 = [?e1]hs6;;[?e2]hs7;;[?e3]hsx;;3
```
Remember that [?r]3 is the same as 3, since the default condition type is a
regular expression.

You can take advantage of the !'' flag to negate rules to avoid chromosomes.
For example, if you want links between cfx and any chromosome other than hsx

```    
      chr_1 = [?e1]cfx
      chr_2 = [?e1!]hsx
```
and here the test is (chr_1 is cfx) AND (chr_2 is not hsx).

You can combine chr with chr_1/chr_2 rules

```    
      chr   = 2
      chr_1 = [?e1]cfx
      chr_2 = [?e1!]hsx
```
to produce the test ( (chr_1 is cfx) AND (chr_2 is not hsx) ) OR ( chr_1
matches 2'' AND chr_2 matches 2'' ). Use chr'' as the parameter if you want to
apply the same condition to both ends of th elink and chr_1 and chr_2 to apply
different conditions.

* * *

### Filtering by Position
To test link position, use the parameters start'', end'' and span''. Both
start'' and end'' are ideal for testing with condition type < and >. To select
links for which both ends start before 10,000,000

```    
      start = [?<]1e7
      # or
      start = [?<]10000000
```
to add another OR'ed condition to pass links with start values beyond
100,000,000

```    
      start = [?<]1e7;;[?>]1e8
```
A more complex test for the start'' and end'' values can be leveled by using
the s'' condition type, which tests for membership within a span. This rule

```    
      start = [?i]1e6-2e6,3e6-4e6
```
will pass links for which both ends are within 1-2Mb or 3-4Mb. Note that the
,'' in this condition is part of the span and does not create a new condition.
To have two conditions, use the ;; delimiter.

```    
      start = [?i]1e6-2e6,3e6-4e6;;[?s]1e7-1.1e7,3e6-4e6
```
When using the span'' parameter, you should always use the s'' condition type.
This will check whether the link span intersects the provided span.

```    
      span = [?s]2e7-5e7
```
This will select all links whose spans (at both ends) intersect the
coordinates 20-50Mb. To be more selective, use the _1 and _2 suffixes.

```    
      span_1 = [?s1]2e7-5e7
      span_2 = [?s1]2e7-2.5e7
```
will select links joining 20-50Mb regions to 20-25Mb regions. An ID was
required here to make the results AND'ed. To avoid certain regions, use the
!'' flag

```    
      span = [?s!](-1e7
```
will avoid all links within the first 10Mb.

* * *

### Filtering by Link Options
Any link option such as color'', thickness'', or z'' can be tested in similar
rules.

```    
      # links with z value greater than 10
      z = [?>]10 
``````    
      # links with z value between 5 and 15
      z = [?s]5-15
```
* * *

### Mixing Conditions and IDs
You can write fairly complex rules by combining different link parameter, rule
types and IDs.

For example to apply the following filter

```    
      (
      between (hs1 and cf6) 
      AND
      within 75-80 Mb on hs1
      AND 
      larger than 5kb on hs1
      )
``````    
      OR
``````    
      (
      larger than 500kb on hs1
      )
```
use the following rules

```    
      chr_1   = [?e1]cf6
      chr_2   = [?e1]hs1
      span_2  = [?s1]75e6-80e6
      size_2  = [?>1]5e3;;[?>]500e3
```
* * *

## HISTORY
  * **23 July 2008**

Reworked rules and conditions to include TYPE and ID.

  * **9 July 2008**

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
```### images
### configuration
