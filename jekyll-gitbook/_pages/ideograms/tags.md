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

# 3 — Drawing Ideograms

## 7\. Tags

[Lesson](/documentation/tutorials/ideograms/tags/lesson)
[Images](/documentation/tutorials/ideograms/tags/images)
[Configuration](/documentation/tutorials/ideograms/tags/configuration)

Up to now, ideograms have been defined solely by their corresponding
chromosomes' IDs. For example, if in your karyotype file you have entries for
IDs hs1, hs2, hs3, and so on, then the `chromosomes`, `chromosomes_order` and
`chromosomes_breaks` string uses the same IDs.

Ideogram tags allow you to uniquely label ideogram regions to allow custom
ordering of regions derived from the same chromosome. Let's look at an
example.

Consider the following block

    
    
    chromosomes        = hs1;hs2;hs3
    chromosomes_breaks = -hs1:50-150;-hs2:50-150
    

The ideograms drawn will be `hs1:0-50`, `hs1:150-)`, `hs2:0-50`, `hs2:150-)`
and `hs3`, by default in that order.

If you want to adjust the order of pieces of `hs1` and `hs2` you must
explicitly define these regions in the chromosomes string and assign tags to
them. This is done as follows

    
    
    chromosomes = hs1[a]:0-50;hs1[b]:150-);hs2[c]:0-50;hs2[d]:150-);hs3[e]
    

Each region is now associated with a unique tag (`a b c d e`). The name of the
tag is arbitrary—they could have been named `hs1a hs1b hs2a hs2b hs3a`.

Tags can be used to specify the order of the cropped ideogram regions

    
    
    chromosomes_order = ^,a,c,e,|,b,$
    

This order string requests that the figure begins with ideogram tagged by `a c
e` and ends with ideogram tagged by `b`. The final order is `a c e d b`.

By default, the tag is added to the ideogram's label. If you do not want this,
set

    
    
    <ideogram>
    label_with_tag = no
    </ideogram>
    

### debugging

If Circos' behaviour when using tags and cropping seems strange, you can see
what's going on under he hood in more detail using `-debug_group chrfilter`.
This option can be set at the command line

    
    
    > circos -debug_group chrfilter
    

or the value of the `debug_group` parameter can be overridden in the
configuration file.

    
    
    <<include etc/housekeeping.conf>>
    debug_group* = chrfilter
    

For a list of debug groups, run Circos with the flag but no argument.

    
    
    > circos -debug_group
    

For more details about debugging, see the
[Configuration—Debugging](//documentation/tutorials/configuration/debugging)
tutorial.

The debug report for this tutorial is

    
    
    debuggroup chrfilter 0.56s karyotypeorder hs1 hs2 hs3 hs4 hs5 hs6 hs7 hs8 hs9 hs10 hs11 hs12 hs13 hs14 hs15 
    	                                  hs16 hs17 hs18 hs19 hs20 hs21 hs22 hsX hsY
    debuggroup chrfilter 0.56s nativesort hs1 hs2 hs3 hs4 hs5 hs6 hs7 hs8 hs9 hs10 hs11 hs12 hs13 hs14 hs15 
                                          hs16 hs17 hs18 hs19 hs20 hs21 hs22 hsX hsY
    debuggroup chrfilter 0.56s effective 'chromosomes' parameter hs1[a]:1-50;hs1[b]:150-);hs2[c]:0-50;hs2[d]:150-);hs3[e]
    debuggroup chrfilter 0.56s parsed chr record hs1[a]:1-50 chr hs1 tag a reject 0 runlist 1-50 rx _undef_ rx? 0
    debuggroup chrfilter 0.56s parsed chr record hs1[b]:150-) chr hs1 tag b reject 0 runlist 150-) rx _undef_ rx? 0
    debuggroup chrfilter 0.56s parsed chr record hs2[c]:0-50 chr hs2 tag c reject 0 runlist 0-50 rx _undef_ rx? 0
    debuggroup chrfilter 0.56s parsed chr record hs2[d]:150-) chr hs2 tag d reject 0 runlist 150-) rx _undef_ rx? 0
    debuggroup chrfilter 0.56s parsed chr record hs3[e] chr hs3 tag e reject 0 runlist _undef_ rx _undef_ rx? 0
    debuggroup chrfilter 0.56s parsed chr record hs1[a]:1-50 chr hs1 tag a reject 0 runlist 1-50 rx _undef_ rx? 0
    debuggroup chrfilter 0.56s chrrx hs1[a]:1-50 rx? 0 accept 1 tag a chrs hs1
    debuggroup chrfilter 0.56s parsed chromosome range hs1 1000000-50000000
    debuggroup chrfilter 0.56s parsed chr record hs1[b]:150-) chr hs1 tag b reject 0 runlist 150-) rx _undef_ rx? 0
    debuggroup chrfilter 0.56s chrrx hs1[b]:150-) rx? 0 accept 1 tag b chrs hs1
    debuggroup chrfilter 0.56s parsed chromosome range hs1 150000000-)
    debuggroup chrfilter 0.56s parsed chr record hs2[c]:0-50 chr hs2 tag c reject 0 runlist 0-50 rx _undef_ rx? 0
    debuggroup chrfilter 0.56s chrrx hs2[c]:0-50 rx? 0 accept 1 tag c chrs hs2
    debuggroup chrfilter 0.56s parsed chromosome range hs2 0-50000000
    debuggroup chrfilter 0.56s parsed chr record hs2[d]:150-) chr hs2 tag d reject 0 runlist 150-) rx _undef_ rx? 0
    debuggroup chrfilter 0.56s chrrx hs2[d]:150-) rx? 0 accept 1 tag d chrs hs2
    debuggroup chrfilter 0.56s parsed chromosome range hs2 150000000-)
    debuggroup chrfilter 0.56s parsed chr record hs3[e] chr hs3 tag e reject 0 runlist _undef_ rx _undef_ rx? 0
    debuggroup chrfilter 0.56s chrrx hs3[e] rx? 0 accept 1 tag e chrs hs3
    debuggroup chrfilter 0.56s parsed chromosome range hs3 -
    debuggroup chrfilter 0.56s chrlist  0  hs1    a 1    1000000   49999999
    debuggroup chrfilter 0.56s chrlist  1  hs1    b 1  150000000         -)
    debuggroup chrfilter 0.56s chrlist  2  hs2    c 1          0   49999999
    debuggroup chrfilter 0.56s chrlist  3  hs2    d 1  150000000         -)
    debuggroup chrfilter 0.56s chrlist  4  hs3    e 1          0  198022430
    

