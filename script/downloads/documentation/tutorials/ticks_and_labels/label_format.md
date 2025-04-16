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

# 5 — Tick Marks, Grids and Labels

## 6\. Label Formats

[Lesson](/documentation/tutorials/ticks_and_labels/label_format/lesson)
[Images](/documentation/tutorials/ticks_and_labels/label_format/images)
[Configuration](/documentation/tutorials/ticks_and_labels/label_format/configuration)

In previous tutorials, tick marks have been formatted by a combination of the
multiplier and format parameters. The multiplier served to derive a value for
the tick label (value = position * multiplier) and the format string
controlled how the value was shown.

For example, if multiplier = 1/1u (it can be expressed in units of
chromosomes_units; e.g., 1/1u = 1e-6 if chromosomes_units = 1000000) and
format %d, then the tick mark at 10,000,000 will be labeled 10. If format is
%.2f, then the label will be 10.00.

### multiplier

The multiplier is useful to avoid the presence of large number of non-
significant zeroes in the labels. You can change the format for each <tick>
block. For example, with a multiplier of 1/1u, the ticks spaced every 1 Mb
should have a format of %d, whereas ticks spaced every 0.1 Mb should receive a
format of %.1f. Note that there is no relation between the "multiplier" and
"chromosomes_unit" parameters.

    
    
    <ticks>
    multiplier   = 1/1u
    ...
    
    <tick>
     format = %d
     ...
    </tick>
    
    <tick>
     format = %.1f
     ...
    </tick>
    ...
    </ticks>
    

You can adjust the multipler for each tick level. For example, the second tick
level in the configuration below uses a 1000/1u multiplier instead of 1/1u.
This would result in a label "100000" (or "100,000" if thousands_sep=yes)
instead of "100".

    
    
    <ticks>
    multiplier   = 1/1u
    ...
    
    <tick>
     ...
    </tick>
    
    <tick>
     multiplier    = 1000/1u
     thousands_sep = yes
     ...
    </tick>
    ...
    </ticks>
    

### modulo ticks

If defined, the value of "mod" is used to adjust the label by performing
modulo arithmetic on the tick mark value based on the formula.

    
    
    given
    
      mod = M
    
    then
    
      tick_label = mod(tick_value,M) * multiplier
    

The "mod" parameter is expected to be defined locally within each <tick>
block. Its purpose is to further reduce the complexity of the tick labels for
finer ticks. For example, if you have ticks every 1u and every 0.1u (e.g., u =
1,000,000) and set

    
    
    multiplier = 1/1u
    
    <tick>
    spacing = 0.1u
    mod = 1u
    </tick>
    
    

Then the label at tick mark 10,100,000 would be

    
    
    mod(10,100,000 , 1,000,000) * 1e-6 = 100,000 * 1e-6 = 0.1
    

rather than 10.1. If you redefine the multiplier for this tick block to 10/1u,
then your ticks would progress as follows

    
    
    0 1 2 ... 8 9 10 1 2 ... 8 9 20 1 2 ... 8 9 30 1 2 ...
    

### note on units of tick spacing

You should always define your tick mark parameters in units of "u" (the value
of the chromosomes_units parameter). Doing so will give the context of your
configuration file the same length scale as your ideograms (e.g. mammalian
genome images might use 1u=1000000 whereas smaller genomes might use 1u=1000).

### prefix and suffix

You can additionally alter the tick mark label with a suffix and prefix by
defining a "suffix" and "prefix" parameters.

    
    
    ...
    <tick>
    suffix = kb
    prefix = +
    ...
    </tick>
    

You can also add a prefix or suffix by adjusting the format of the tick.

    
    
    <tick>
    format = position %.1f kb
    ...
    </tick>
    
    
    
    
    
    
    
    
    

