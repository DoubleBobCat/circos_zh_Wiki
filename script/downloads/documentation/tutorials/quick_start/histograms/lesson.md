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

# 2 — Quick Start

## 5\. Histograms

[Lesson](/documentation/tutorials/quick_start/histograms/lesson)
[Images](/documentation/tutorials/quick_start/histograms/images)
[Configuration](/documentation/tutorials/quick_start/histograms/configuration)

In addition to links, which associate two genomic positions, Circos supports
several data tracks, which associate a position with a value.

These tracks include line plots, scatter plots, histograms and heat maps. The
text track is a special kind of data track, which associates a position with a
text label.

### data format

The line plot, scatter plot, heat map and histogram share the same data
format.

    
    
    #chr start end value [options]
    ...
    hs3 196000000 197999999 71.0000
    hs3 198000000 199999999 57.0000
    hs4 0 1999999 28.0000
    hs4 2000000 3999999 40.0000
    hs4 4000000 5999999 59.0000
    ...
    

The `options` field can associate a parameter with a data point, such as a
color or identifier. Format parameters are used to override how the data point
is displayed (e.g. instead of using rules)

    
    
    hs3 196000000 197999999 71.0000 fill_color=blue
    

User parameters, such as `id` can be used in conjunction with rules to select
and modify the data point.

    
    
    # in data file
    hs3 196000000 197999999 71.0000 id=abc
    
    # in rule block
    <rule>
    condition  = var(id) eq "abc"
    fill_color = blue
    </rule>
    

### plot blocks

Each histogram is defined in a `<plot>` block within an enclosing `<plots>`
block.

    
    
    <plots>
    
    <plot>
    type = histogram
    ...
    </plot>
    
    <plot>
    type = histogram
    ...
    </plot>
    
    ...
    </plots>
    

### histograms

This tutorial defines two histograms: a regular histogram and a stacked
histogram.

In addition to the `type` and `file` parameters, you need to define the inner
and outer radius of the track using `r0` and `r1`. Usually these values are
relative — in case the radial position of the ideogram changes, the track will
be automatically moved.

    
    
    type = histogram
    file = data/5/segdup.hs1234.hist.txt
    r1   = 0.88r
    r0   = 0.81r
    

### joining bins

A histogram is composed of bins. If the bins do not abut, such as in the case

    
    
    hs1 10 20 0.5
    hs1 30 40 0.25
    

you have the option of extending the bins outward until they meet their
neighbour.

    
    
    extend_bin = no | yes
    

### fill and outline colors

Histograms can have both a fill and outline. In this example, the bins will be
filled a very dark grey. fill_color = vdgrey

All tracks have default formatting settings, defined in `etc/tracks/*.conf`.
For the histogram, the defaults are

    
    
    # etc/tracks/histogram.conf
    color            = black
    thickness        = 1
    r1               = 0.89r
    r0               = 0.8r
    orientation      = out
    

### histogram orientation

A histogram can be oriented out or in.

    
    
    orientation = in | out
    

### managing defaults

To turn off default outline, set the outline thickness to zero.

    
    
    thickness = 0p
    

or undefine the parameter

    
    
    thickness = undef
    

You can edit the defaults by editing the `etc/tracks/histogram.conf` file, or
permanently disable the use of defaults by commenting out the `track_default`
directory in `etc/housekeeping.conf`.

### rules

Like for links, rules are used to dynamically alter formatting of each data
point (i.e. histogram bin). In this tutorial, I include a rule that hides
histogram bins on chromosome hs1.

    
    
    <rule>
    condition = on(hs1)
    show      = no
    </rule>
    

#### importing rules

Because the rule is reused, I store this rule in a file, `exclude.hs1.rule`,
and the import it

    
    
    <rules>
    <<include exclude.hs1.rule>>
    </rules>
    

#### changing format parameters

Rules can change the visibility, format and value of data points. For example,
by setting `show=no`, as in the rule above, a data point is hidden.

Similarly you can set any format parameter

    
    
    <rule>
    condition  = on(hs1)
    fill_color = blue
    color      = vdblue
    thickness  = 2p
    </rule>
    

The rule will overwrite any parameter values from the `<plot>` block.

#### rule conditions

The condition in a rule is expected to be Perl code. This expression is
automatically evaluated — you do not need `eval()` here. Examples of
conditions are

    
    
    # applies to every data point - always true
    1
    
    # check whether a data point is on a chromosome
    var(chr) eq "hs1"
    on(hs1) # shortcut
    
    # check whether a data point is not on a chromosome
    var(chr) ne "hs1"
    !on(hs1)
    
    # combine tests with or (||)
    on(hs1) || on(hs2)
    var(chr) =~ /hs(1|22)$/;
    
    # check position
    var(start) > 10Mb
    
    # use the value
    var(value) < 0.05
    
    # use any parameter
    var(color) eq "red"
    var(stroke_color) eq "vdred"
    

If a rule has multiple conditions, all of them must be satisfied for the rule
to trigger.

    
    
    <rule>
    # data point must be on hs1 and value < 0.05
    condition = on(hs1)
    condition = var(value) < 0.05
    ...
    </rule>
    

#### referencing data point parameters in rules

You can reference parameters defined in the data file using `var(X)`. For
example, you can define parameters `id` and `mult` in the data file

    
    
    # in data file
    hs3 196000000 197999999 71.0000 id=abc,mult=5
    

and then use them in a rule

    
    
    <rule>
    condition  = var(id) eq "abc"
    fill_color = blue
    value      = eval(var(value)*var(mult))
    </rule>
    

The `value` parameter refers to the data point's value. Yes, it is possible to
change the value using a rule! Here we multiply the value by the data point's
`mult` parameter.

In order for the expression to be evaluated as code, it must be enclosed in
`eval()` (otherwise the `value` will be set to the string
`"var(value)*var(mult)"`).

### stacked histograms

The second histogram in the tutorial is a stacked histogram. It shows several
values for a given position by stacking bins. This is a special kind of 2D
data track which uses the data format

    
    
    #chr start end value,value,value,... [options]
    ...
    hs3 196000000 197999999 0.0000,7.0000,64.0000,0.0000
    hs3 198000000 199999999 21.0000,6.0000,18.0000,12.0000
    hs4 0 1999999 5.0000,3.0000,1.0000,19.0000
    hs4 2000000 3999999 1.0000,6.0000,16.0000,17.0000
    hs4 4000000 5999999 1.0000,13.0000,25.0000,20.0000
    ...
    

Circos will automatically format the track as a stacked histogram when
type=histogram and multiple values in the data file are found.

The `fill_color` for a stacked histogram is expected to be a list of colors,
each corresponding to a given value. For example, for the data line

    
    
    hs3 198000000 199999999 21.0000,6.0000,18.0000,12.0000
    

and the `fill_color` list

    
    
    fill_color  = hs1,hs2,hs3,hs4
    

the colors for the bins will be hs1 (21.0000), hs2 (6.0000), hs3 (18.0000),
hs4 (12.0000).

