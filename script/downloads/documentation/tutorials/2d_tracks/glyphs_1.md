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

# 7 — 2D Data Tracks

## 9\. Glyphs — Part I

[Lesson](/documentation/tutorials/2d_tracks/glyphs_1/lesson)
[Images](/documentation/tutorials/2d_tracks/glyphs_1/images)
[Configuration](/documentation/tutorials/2d_tracks/glyphs_1/configuration)

Rules can be used to adjust the text of the label. This is done by setting the
`value` parameter in the rule. The rule below sets all labels to `X`,
regardless of their original text.

    
    
    <rule>
    condition  = 1
    value      = X
    </rule>
    

You can combine this with other rules. For example, if the text is sequence,
you can set the color of the character based on its identity and then change
it to another value. The color rules must have `flow=continue` to allow the
downstream label-changing rule to also be evaluated (recall that without this
`flow=continue statement`, triggered rules terminate the rule chain).

    
    
    # first change color
    <rule>
    condition  = var(value) eq "A"
    color      = red
    flow       = continue
    </rule>
    
    <rule>
    condition  = var(value) eq "T"
    color      = blue
    flow       = continue
    </rule>
    
    <rule>
    condition  = var(value) eq "C"
    color      = green
    flow       = continue
    </rule>
    
    # change label text, for all data points
    <rule>
    condition  = 1
    value      = X
    </rule>
    

You can turn a text track into a glyph track by changing the font and
adjusting the text label to the desired glyph. For example, using the symbol
font (fonts/symbols/symbols.ttf, defined under the font name `glyph` in
`etc/fonts.conf`), you can obtain square glyphs like so

    
    
    <plot>
    label_font = glyph
    
    <rules>
    ...
    <rule>
    condition = 1
    value     = m
    </rule>
    ...
    </rules>
    

The symbols font defines the following characters

    
    
     small
     | medium
     | | large
     | | |
     a b c   square
     d e f   rhombus
     g h i   triangle up
     j k l   triangle down
     m n o   circle
    
    upper case - solid
    lower case - hollow
    

By adjusting the padding more tightly, you can pack the square glyphs to
touch. By adjusting the color and glyph shape, you can create attractive
tracks.

