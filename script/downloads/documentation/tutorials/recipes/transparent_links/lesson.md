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

## 9\. Transparent Links

[Lesson](/documentation/tutorials/recipes/transparent_links/lesson)
[Images](/documentation/tutorials/recipes/transparent_links/images)
[Configuration](/documentation/tutorials/recipes/transparent_links/configuration)

This tutorial shows how you can improve the layout of your links using color
transparency. The data for this tutorial was created using tools/randomlinks.
This script generates random links between chromosomes based on your karyotype
file and a flexible configuration which controls how many links to create, how
large their spans should be, and so on. The configuration file,
randomlinks.conf, can be found in this tutorial's directory.

### using z-depth

If you have many ribbon links that overlap, one way to bring important (e.g.
large) links to the foreground is to use z-depth.

This rule will set the z-depth for each link independently, as a function of
its size. Larger links (i.e. those with large start/end spans) will have a
high z-depth and therefore be shown on top.

    
    
    <rules>
    <rule>
    condition  = 1
    z          = eval( scalar min(var(size1),var(size2) ) )
    </rule>
    </rules>
    

The problem of link occlusion still remains—if you have a lot of links you
won't be able to see them all.

### defining transparent colors

To define a transparent color, add a fourth value to its RGB triplet. This
value will be the transparency and it is a number between 0 (opaque) and 127
(fully transparent). For example, in addition to the default colors, I add a
transparent black

    
    
    <<include colors_fonts_patterns.conf>>
    <colors>
    blackweak = 0,0,0,100
    </colors>
    

The transparency is 100/127, which gives blackweak an RGB value of 200,200,200
when drawn on white. When links are assigned this color,

    
    
    <link>
    ribbon = yes
    color  = blackweak
    ...
    </link>
    

the ribbons are drawn with transparency.

The blackweak color is black with 79% transparency. The alpha blending in GD
results in multiplication of overlapping RGB colors. Thus, for every
overlapping ribbon the RGB values are scaled from 200,200,200 by 79% (two
overlapping ribbons result in 157,157,157, three in 123,123,123, and so on).

### automatic definition of colors with transparency

By default, Circos defines 5 levels of transparency for each color you define.

Each color (e.g. pure red, `pred=255,0,0`) will yield 5 new color definitions
`pred_a1`, `pred_a2`, `pred_a3`, `pred_a4`, and `pred_a5` with each `_aN`
color having a transparency `N/(5+1`). Thus `pred_a1` will have a 17%
transparency, `pred_a2` 33%, `pred_a3` 50%, `pred_a4` 67% and `pred_a5` 83%.

Note that `pred_a0` is not defined (you already have it in `pred`) and
`pred_a5` is not 100% transparent.

With the automatic allocation of these colors, you can immediately use them

    
    
    <link>
    ribbon = yes
    color  = black_a5 # black with 83% transparency
    ...
    </link>
    

You can change the number of transparency steps using `auto_alpha_steps` in
the <image> block.

    
    
    <image>
    <<include etc/image.conf>>
    # overwrite auto_alpha_steps from default value included in etc/image.conf
    auto_alpha_steps* = 10
    </image>
    

### adding transparency with rules

You can easily make elements that use opaque colors (e.g. `red`) to use
transparent versions (e.g. `red_a5`) by writing rules to rewrite the color
value.

For this example, I generated random links across all chromosomes in the human
genome.

    
    
    e.g.
    hs7 127586339 141410899 hsY 30737607 31414129
    

The rule below assigns each link a color derived from three components:
luminance prefix, chromosome name and transparency suffix.

    
    
    <rule>
    condition = 1
    # derive the color name from the chromosome name
    # lum80 + chr_name + _a2
    #
    # lum70*, lum80* and lum90* colors are normalized
    # to a given luminance and are predefined at etc/colors.ucsc.conf
    #
    # _a2 adds transparency (2/6 = 33%) where the denominator
    # is derived from auto_alpha_steps+1=6
    color     = eval(lc sprintf("%s%s_a%d",'conf(luminance)',var(chr1),4))
    </rule>
    

With this rule, all links color names are modified (e.g. `hs7` to
`lum80hs7_a4`) and shown at 67% transparency (default value of
`auto_alpha_steps=5`). The `lum80` prefix is referenced using the `conf()`
function which accesses the value of the parameter `luminance`. This parameter
is conveniently defined at the top of the configuration file. You can alter it
at the command line using `-param` flag

    
    
    > circos -param luminance=lum70
    

The images for this tutorial show links (i) without transparency, (ii) with
transparency (`_a4`) and (iii) with additional luminance normalization
(`lum80`), where the chromosome colors also have this luminance normalization.

### coloring chromosomes

The definition below derives the chromosome color from its name and the
`luminance` prefix

    
    
    # change the color of each chromosome to lum80 + chr_name
    # where the lum80 prefix references a predefined color
    # with normalized luminance
    chromosomes_color = /./=conf(luminance)var(chr)
    

### transparency in bitmaps vs svg

Transparency in SVG for outlines is not available.

