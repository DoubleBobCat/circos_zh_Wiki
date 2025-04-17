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

# 9 — Recipes

## 10\. ID Fields

[Lesson](/documentation/tutorials/recipes/data_id/lesson)
[Images](/documentation/tutorials/recipes/data_id/images)
[Configuration](/documentation/tutorials/recipes/data_id/configuration)

In this tutorial, I will demonstrate how to apply formatting to data based on
its identifier stored in the `id` field.

As you've seen, each data point can have values set for format parameters such
as `color`, `stroke_thickness`, `fill_color`, and so on. These elements can be
defined in (a) the data file itself, independently for each data point (b) in
rule blocks or (c) as global settings for the entire data set.

However, it may be convenient to assign an annotation to your data points and
then calculate format values based on the annotation. This is where the `id`
field is useful—this field does not directly impact the way the data point is
displayed, but tags it with a string which you can use in rule blocks.

### Formatting Tiles

In the first example, I'll show you how to dynamically format tiles.

There is a variety of repeat element types (LINE, SINE, Satellite, simple,
etc) and these may be stored as follows

    
    
    ...
    chr21 30003462 30003712 AluSx SINE Alu
    chr21 30003734 30003925 L1MD LINE L1
    chr21 30004082 30004207 L1ME4a LINE L1
    chr21 30004229 30004286 AT_rich Low_complexity Low_complexity
    chr21 30004378 30004615 L1ME4a LINE L1
    chr21 30004781 30004872 AT_rich Low_complexity Low_complexity
    chr21 30004942 30005099 CT-rich Low_complexity Low_complexity
    chr21 30005358 30005634 MER7A DNA MER2_type
    chr21 30006113 30006265 L1ME4a LINE L1
    ...

with each element having multiple, independent classifications (e.g. AluSx,
SINE, Alu). To use these classifications, you will need to parse the data and
associate a `id` parameter with each data point. The value of the `id`
parameter is up to you. I used this script

    
    
    #!/usr/bin/perl
    use strict;
    $,=" ";
    $\="\n";
    while(<>) {
        chomp;
        my $id;
        s/chr/hs/;
        if(/L(\d+)/) {
            $id = "LINE$1";
        } elsif (/S(\d+)/ || /SINE(\d?)/) {
            #my $num = $1 || 0;
            $id = "SINE" . ($1||0);
        } elsif (/low/i || /simple/i) {
            $id = "SIMPLE";
        } elsif (/LTR/) {
            $id = "LTR";
        } else {
            $id = "OTHER";
        }
        my @tok = split;
        print @tok[0..2],"id=$id";
    }

to transform the data file above into the following

    
    
    ...
    hs21 30003462 30003712 id=SINE0
    hs21 30003734 30003925 id=LINE1
    hs21 30004082 30004207 id=LINE1
    hs21 30004229 30004286 id=SIMPLE
    hs21 30004378 30004615 id=LINE1
    hs21 30004781 30004872 id=SIMPLE
    hs21 30004942 30005099 id=SIMPLE
    hs21 30005358 30005634 id=OTHER
    hs21 30006113 30006265 id=LINE1
    ...

Define a tile block to show these elements

    
    
    <plot>
    type = tile
    file = repeats.withid.txt
    r0   = 0.8r
    r1   = 0.98r
    orientation = in
    layers      = 50
    thickness   = 20p
    padding     = 6p
    margin      = 0.001u
    color       = black
    # for very small tiles a stroke is useful because
    # it ensures that tiles associated with very small
    # spans will be visible
    stroke_thickness = 2p
    stroke_color = black
    
    # RULES WILL GO HERE
    
    </plot>
    
    

With this block, all repeat tiles will have the same formatting. To apply
formatting specific to `id` values, use

    
    
    # test with regular expression
    condition = var(id) =~ /LINE/
    

or

    
    
    # test string equality
    condition = var(id) eq "LINE"
    

For example, this set of rules applies different formatting to elements with
`id` LINE, SINE, SIMPLE and OTHER. For LINE elements, fill color is set to
green, but LINE1 and LINE2 elements have an additional stroke_color condition.

    
    
    <plot>
    
    ...
    
    <rules>
    
    <rule>
    condition    = var(id) =~ /LINE/
    color        = green
    flow         = continue
    </rule>
    
    <rule>
    condition    = var(id) =~ /LINE[12]/
    stroke_color = red
    </rule>
    
    <rule>
    condition    = var(id) =~ /SINE/
    color        = blue
    stroke_color = blue
    </rule>
    
    <rule>
    condition    = var(id) =~ /SIMPLE/
    color        = dgrey
    </rule>
    
    <rule>
    condition    = var(id) =~ /OTHER/
    color        = lgrey
    </rule>
    
    </rules>
    
    </plot>
    

The first rule makes use of the `flow=continue` directive, which prevents the
rule chain from terminating if this rule matches. This allows a rule for LINE
and another rule for the more specific LINE1 or LINE2 test. To read more about
rule flow, see [Basic Rules Tutorial](/documentation/tutorials/links/rules1).

### Formatting Links

Let's look how link formatting can be adjusted in the same way.

Suppose you have links which have an `id` field that contains your annotation.
In this example, I use an annotation in the format `number-number` (e.g.
87-69). This format is arbitrary and will serve to show how regular
expressions in rules can be used to extract values.

    
    
    ...
    linkid5 hs21 30772491 30777591 id=87-69
    linkid5 hs21 30602230 30607330 id=87-69
    linkid6 hs21 30257977 30263077 id=60-22
    linkid6 hs21 30367808 30372908 id=60-22
    linkid7 hs21 30079003 30084103 id=54-90
    linkid7 hs21 30771970 30777070 id=54-90
    ...
    

We will first set the thickness of the link based on the first number in the
`id` field.

    
    
    <rule>
    # make sure that the id field matches the required number-number format
    condition  = var(id) =~ /(\d+)-(\d+)/
    # extract the two number in 'id' to @match and use remap() function to map
    # the first number in the range 1..100 to thickess in the range 1..10.
    thickness  = eval( my @match = var(id) =~ /(\d+)-(\d+)/; remap($match[0],1,100,1,10) )
    # so that other rules can trigger too
    flow = continue
    </rule>
    

Let expand the rule to remap the z-value (depth), color and transparency as
well.

    
    
    <rule>
    # make sure that the id field matches the required number-number format
    condition  = var(id) =~ /(\d+)-(\d+)/
    # extract the two number in 'id' to @match and use remap_int() function to map
    # the first number in the range 1..100 to integer thickess in the range 1..10.
    thickness  = eval( my @match = "var(id)" =~ /(\d+)-(\d+)/; remap_int($match[0],1,100,1,10) )
    
    # use the first number as the z-value (i.e. thick links will be drawn on top)
    z          = eval( my @match = "var(id)" =~ /(\d+)-(\d+)/; $match_int[0] )
    
    # use the second number for the color and transparency
    color      = eval( my @match = "var(id)" =~ /(\d+)-(\d+)/;  
                       sprintf("spectral-9-div-%d_a%d", remap_int($match[1],1,100,1,9),  
                                                        remap_int($match[1],1,100,5,1 ) ) )
    </rule>
    

Notice that the `id` field, which is text, is set in quotes. This is required
so that the Perl expression for evaluation is

    
    
    # correct - "87-69" treated as string
    my @match = "87-69" =~ /(\d+)-(\d+)/
    

rather than

    
    
    # incorrect - 87-69 treated as literal
    my @match = 87-69 =~ /(\d+)-(\d+)/
    

Remember that you can use `-debug_group rules` as a command-line parameter
when running Circos to obtain debug information about how rules are parsed.

### Formatting Text

To format text labels based on the `id` field the recipe is the same. If your
text data looks like this

    
    
    ...
    hs21 30829740 30829740 tb id=64
    hs21 30405360 30405360 oe id=31
    hs21 30112849 30112849 ps id=74
    hs21 30721834 30721834 dg id=25
    hs21 30325022 30325022 sj id=22
    ...
    

then the rules to change the color and label size based on the `id` field
would be

    
    
    <rule>
    condition  = 1
    color      = eval(sprintf("set2-4-qual-%d",remap_int(var(id),1,100,1,4)))
    label_size = eval(sprintf("%dp",remap_int(var(id),1,100,12,48)))
    </rule>
    

In this case, I've set `condition=1` to apply the rule without checking that
the `id` field matches the right format. Also, the `id` string does not
require quotes because the value of the parameter is a number, which does not
need to be quoted (quoting it won't hurt, though).

