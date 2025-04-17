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

## 19\. Cortical Maps

[Lesson](/documentation/tutorials/recipes/cortical_maps/lesson)
[Images](/documentation/tutorials/recipes/cortical_maps/images)
[Configuration](/documentation/tutorials/recipes/cortical_maps/configuration)

In this example I will show you how to create maps of the brain connectome
using Circos — a _connectogram_. Images of this type have recently appeared in
papers from the [Van Horn group at UCLA](https://ccb.loni.ucla.edu/about/ccb-
organization/ccb-principal-investigators/john-van-horn-phd/).

Irimia A, Chambers MC, Torgerson CM et al. 2012 [Patient-tailored connectomics
visualization for the assessment of white matter atrophy in traumatic brain
injury](https://www.frontiersin.org/Journal/Abstract.aspx?s=772&name=neurotrauma&ART_DOI=10.3389/fneur.2012.00010)
Frontiers in Neurology 3

Irimia A, Chambers MC, Torgerson CM et al. 2012 [Circular representation of
human cortical networks for subject and population-level connectomic
visualization](https://www.ncbi.nlm.nih.gov/pubmed/22305988) NeuroImage.

Van Horn JD, Irimia A, Torgerson CM et al. 2012 [Mapping connectivity damage
in the case of phineas gage](https://www.ncbi.nlm.nih.gov/pubmed/22616011)
PLoS One 7:e37454.

Connectograms they have been used to illustrate the [damage suffered by
Phineas Gage in his traumatic brain
injury](https://www.guardian.co.uk/science/neurophilosophy/2012/may/16/neuroscience-
psychology).

### the connectogram

The connectogram shows regions of the brain, their physical properties and
connectivity.

The image is divided into two halves — the left and right hemisphere. Within
each half, regions are grouped into lobes (frontal, temporal, occipital, etc.)
from anterior (top of image) to posterior (bottom of image). Within each lobe,
fine anatomical and functional divisions (parcelations) are shown as labeled
colored segments. The label of each segment is an abbreviated code. For
example, _SupPrCS_ is the _superior part of the precentral sulcus_.

The order and position of the parcelations is fixed across patients and
composes a static coordinate system.

For each patient, measures of the parcelations are shown as a series of heat
maps. These measures depend on the specific data set and can include grey
matter volume, surface area, cortical thickness, curvature and degree
connectivity (e.g. Fig 4 in [Irimia et al,
2012](https://www.frontiersin.org/Journal/Abstract.aspx?s=772&name=neurotrauma&ART_DOI=10.3389/fneur.2012.00010)).

Within the center of the connectogram are the observed connections between
parcelations, measured _in vivo_ ([Human Connectome Project
(HCP)](https://www.humanconnectomeproject.org/)).

### data input

This tutorial includes a script, `parsemap` (see `tutorials/8/19` directory),
which generates the data files to create a connectogram. This script requires
the list of parcelations and, optionally, a list of connections between them.

#### list of parcelations

This file defines the parcelation region lobe and name, color, (`r g b`), and
measures, `z1...z5`. You'll find an example in `map.txt`. For this example,
the measures data is random and the measures do not correspond to any specific
property. The lobe, parcelation codes and colors are taken from [Irimia et al,
2012](https://www.frontiersin.org/Journal/Abstract.aspx?s=772&name=neurotrauma&ART_DOI=10.3389/fneur.2012.00010).

    
    
    # lobe parcelation r g b z1 z2 z3 z4 z5
    Fro TrFPoG/S 255 153 153 0.910094 0.265257 0.893188 0.220351 0.810623
    Fro FMarG/S 204 0 51 0.631798 0.571077 0.332158 0.104455 0.173531
    Fro MFS 255 153 51 0.502931 0.567394 0.854165 0.0401409 0.484983
    ...
    Ins ALSHorp 0 255 204 0.426026 0.325782 0.104662 0.428916 0.101814
    Ins ACirInS 102 255 255 0.623148 0.6187 0.779997 0.488031 0.482945
    Ins ALSVerp 0 255 255 0.98955 0.925851 0.642174 0.747365 0.254355
    ...
    Lim ACgG/S 255 255 180 0.399686 0.345312 0.201031 0.322008 0.377663
    Lim MACgG/S 255 240 191 0.336171 0.570686 0.437 0.87439 0.899756
    Lim SbCaG 255 153 200 0.643938 0.517941 0.894874 0.839202 0.77888
    ...
    

The `parsemap` script uses the order of the parcelations in the file to
determine their order in the image.

This example uses 5 measures for each parcelation, but the `parsemap` script
will work if you don't have any measures and are only drawing links between
regions.

    
    
    # lobe parcelation r g b
    Fro TrFPoG/S 255 153 153
    Fro FMarG/S 204 0 51
    Fro MFS 255 153 51
    ...
    

In this case, you'll need to adjust `etc/circos.conf` and remove mention of
the heatmaps.

#### list of connections

The second file is the **list of connections** (see `map.links.txt`), which
looks like

    
    
    # hemisphere parcelation hemisphere parcelation connection_type connection_score
    r InfFGOrp l PosCS 1 0.0229917613607071
    l BSt l SbOrS 1 0.213414893099078
    l TPl r Pu 0 0.26688626172767
    ...
    

The connection type and score do not corespond to any specifc property. I have
included them here to show you how to use rules in the Circos configuration
file to change the way the connection links are drawn.

Replace these two files with your data.

You can move the `parsemap` script to another location on your filesystem
(e.g. `/usr/local/bin`) if you plan on using it for other images.

    
    
    > cd /path/to/image
    > /usr/local/bin/parsemap -map map.txt -links map.links.txt
    

### Circos data files

The `parsemap` script generates the data files that are required to create the
image.

To create the data files, run the `parsemap` script ([Windows users should
read this tutorial
first](documentation/tutorials/configuration/unix_vs_windows/))

    
    
    # create the configuration and data files
    > ./parsemap -map map.txt -links map.links.txt -debug
    ...
    debug[1] wrote file etc/color.brain.conf
    debug[1] wrote file data/segments.txt
    debug[1] wrote file etc/segment.order.conf
    debug[1] wrote file data/structure.label.txt
    debug[1] wrote file data/measure.0.txt
    debug[1] wrote file data/measure.1.txt
    debug[1] wrote file data/measure.2.txt
    debug[1] wrote file data/measure.3.txt
    debug[1] wrote file data/measure.4.txt
    debug[1] wrote file data/links.txt
    

You'll need to supply the remaining configuration files that define how the
image is organized — sample configuration can be found in `etc/`. These are
`etc/circos.conf`, `etc/ideogram*conf`, `etc/ticks*conf` and `etc/bands.conf`.

#### parcelation color

The RGB colors for each parcelation were taken from Appendix 1 in [Irimia et
al,
2012](https://www.frontiersin.org/Journal/Abstract.aspx?s=772&name=neurotrauma&ART_DOI=10.3389/fneur.2012.00010).

    
    
    # etc/color.brain.conf
    trfpogs = 255,153,153
    fmargs = 204,0,51
    mfs = 255,153,51
    lors = 102,0,0
    sbors = 255,51,102
    ors = 255,204,204
    rg = 255,204,153
    ...
    

The colors are named after the parcelations, in lowercase form and without any
non-word characters (e.g. `IntPS/TrPS` becomes `intpstrps`).

#### lobe/parcelation axis

The lobe and segment definitions are stored in the `data/segments.txt` file.

Here, you'll have to remember that Circos was originally designed to display
data in genomics, where the axes are typically chromosomes. The segments
(lobes) take place of chromosomes and parcelations take place of cytogenetic
bands, which are visual features on chromosomes.

Each lobe gets a separate entry for the left and right hemisphere. Its size is
determined by the number of parcelations, arbitrary sized at 100.

    
    
    # left frontal lobe (fro-l)
    chr - fro-l Fro 0 2099 black
    # right frontal lobe (fro-r)
    chr - fro-r Fro 0 2099 black
    # left insula (ins-l)
    chr - ins-l Ins 0 799 black
    # right insula (ins-r)
    chr - ins-r Ins 0 799 black
    ...
    

The `fro-l` field is the name of the Circos axis that corresponds to the lobe
and `Fro` is its label. The last field is the color of the lobe, but we will
not be using this because the lobe will be covered with colored parcelations.

Parcelations are registered as bands within each lobe. Each line defines the
parcelation as belonging to a specific Circos axis (e.g. lobe, `fro-l`) with a
start/end position (e.g. 0, 99). The final field is the color of the
parcelation, which was previously defined in `etc/color.brain.conf`. The 3rd
and 4th fields in a `band` definition are currently not being used by Circos
(they exist for legacy reasons).

    
    
    band fro-l TrFPoG/S TrFPoG/S 0 99 trfpogs
    band fro-l FMarG/S FMarG/S 100 199 fmargs
    ...
    band ins-l ALSHorp ALSHorp 0 99 alshorp
    band ins-l ACirInS ACirInS 100 199 acirins
    band ins-l ALSVerp ALSVerp 200 299 alsverp
    ...
    band lim-l ACgG/S ACgG/S 0 99 acggs
    band lim-l MACgG/S MACgG/S 100 199 macggs
    band lim-l SbCaG SbCaG 200 299 sbcag
    ...
    

It's important to note that the parcelations, defined as bands, are not
directly referenced when plotting data. They are properties of the axis — they
are not used to identify positions. See the section on parcelation labels and
measures below for an explanation.

#### lobe order

Once the lobes are defined, their order in the figure is determined by the
`chromosomes_order` field. Again, the genomic origins of Circos show through.

    
    
    chromosomes_order = fro-r,ins-r,lim-r,tem-r,par-r,occ-r,sbc-r,ceb-r,bst,ceb-l,sbc-l,occ-l,par-l,tem-l,lim-l,ins-l,fro-l
    

By design, the brain stem lobe (bst) does not have a left and right version.

#### parcelation labels

Text labeling each parcelation is drawn as a text track. The input data for
this is `data/structure.label.txt`,

    
    
    fro-l 0 99 TrFPoG/S
    fro-l 100 199 FMarG/S
    fro-l 200 299 MFS
    ...
    ins-l 0 99 ALSHorp
    ins-l 100 199 ACirInS
    ins-l 200 299 ALSVerp
    ...
    lim-l 0 99 ACgG/S
    lim-l 100 199 MACgG/S
    lim-l 200 299 SbCaG
    ...
    

The text track stores the name of the parcelation region _independently_ of
the parcelation definitions, which was stored as bands entries. Circos
currently does not support showing the names of the bands directly — you need
to create a separate file with these labels and draw the labels using a data
track.

Notice that the positions of the labels is determined relative to the lobe,
not the parcelation region (e.g. MFS is at position 200-299 on fro-l). This is
a result of the fact that the lobe forms the coordinate axis, not the
parcelation region. The region is just a visual feature on the axis and cannot
be addressed directly.

If you're very keen, you might be asking: why not make each parcelation region
into its own axis? Yes, this is possible, but if the figure was organized this
way there would be no way of organizing the regions into higher-level
structures (e.g. lobes). By making each axis a lobe, and dividing it into
regions, we can later write rules that check whether a data point lies on a
specific lobe.

#### parcelation measures heat maps

The measures for each parcelation are defined in `data/measure.*.txt`

    
    
    fro-l 0 99 0.910094
    fro-l 100 199 0.631798
    fro-l 200 299 0.502931
    ...
    ins-l 0 99 0.426026
    ins-l 100 199 0.623148
    ins-l 200 299 0.989550
    ...
    lim-l 0 99 0.399686
    lim-l 100 199 0.336171
    lim-l 200 299 0.643938
    

#### links

Links are stored as connected pair of axis and coordinates.

    
    
    fro-r 700 799 par-l 300 399 type=1,score=0.022992
    bst 0 99 fro-l 400 499 type=1,score=0.213415
    tem-l 700 799 sbc-r 0 99 type=0,score=0.266886
    ...
    

The `type` and `score` parameters annotate each link and can be referenced in
rules to change the format of the link.

### Circos configuration files

The main configuration file is `etc/circos.conf`. This file contains all of
the parameters that define the position and content of elements in the image,
such as axis position and data tracks. Using <<include ...>> directives in
this file, content from other files can be imported.

#### ideogram layout

The axis segments (here, brain lobes) are called _ideograms_ in Circos. This
vocabular is derived from the term given to a graphical representation of a
chromosome.

The position, thickness and spacing of lobe ideograms is defined in
`etc/ideogram.conf`, which is imported using the <<include ideogram.conf>>
directive.

    
    
    # circos.conf
    <<include ideogram.conf>>
    

The `etc/ideogram.conf` file is

    
    
    # ideogram.conf
    <ideogram>
    
    <spacing>
    # spacing between lobes is 0.5% of figure circumference
    default = 0.005r
    <pairwise fro-l fro-r>
    # spacing between left and right frontal lobe ideogram (top center of image) is
    # 5x default - this provides room for legend
    spacing = 5r
    </pairwise>
    </spacing>
    
    # lobe thickness and position, included from file
    <<include ideogram.position.conf>>
    
    # lobe label size and format, included from file
    <<include ideogram.label.conf>>
    
    # parcelation colors, included from file
    <<include bands>>
    
    </ideogram>
    

The position and thickness of the lobe segments is imported from the
`etc/ideogram.position.conf` file. Storing parameters in multiple files makes
the configuration more modular and allows you to reuse components of one
figure in another.

    
    
    # ideogram.position.conf
    
    # position of the lobe axis segments, relative to radius of image
    radius           = 0.85r
    
    # thickness of lobe axis segments, in pixels
    thickness        = 75p
    
    # the color of each segment is "black" as defined in segments.txt - here we
    # don't want this color applied, so fill=no
    fill             = no
    
    # the segments have a 1 pixel outline
    stroke_thickness = 1
    stroke_color     = black
    

The position and format of labels for each lobe segment are specified in
`etc/ideogram.label.conf`.

    
    
    # ideogram.label.conf
    
    show_label       = yes
    # for a list of fonts, see etc/fonts.conf in Circos distribution
    label_font       = default
    
    # set the label position to be at edge of inscribed circle, less 30 pixels
    label_radius     = dims(image,radius)-30p
    label_size       = 24
    
    # labels can be parallel to axis segments, or perpendicular 
    label_parallel   = yes
    
    # force upper case for labels
    label_case       = upper
    

Recall that the parcelation regions were defined as bands in the
`data/segments.txt` file. Here I toggle the display of the bands.

    
    
    # bands.conf
    
    show_bands            = yes
    
    # fill the bands with the color defined in segments.txt
    fill_bands            = yes
    
    # give the band an outline
    band_stroke_thickness = 1
    band_stroke_color     = black
    
    # 0 - fully opaque
    # 1 - least transparent
    # 5 - most transparent
    band_transparency     = 0
    

The axis progression of left hemisphere lobes is reversed, using a regular
expression that selects all lobes whose names contain `-l`.

    
    
    chromosomes_reverse = /.*-l/
    

#### ticks

The image contains a tick in the center of each paracelation region, together
with a grid line that extends inward to the start of links. This is achieved
with parameters defined in `etc/ticks.conf`.

First, recall that each parcelation region was made to be 100 units in size
(in `data/segments.txt`). This multiplier is arbitrary, but necessary because
Circos works only with integer coordinates. Without the multiplier, it would
not be possible to specify a position in the middle of the region.

We also define the `chromosomes_units` to be 100

    
    
    chromosomes_units = 100
    <<include ticks.conf>>
    

so that we can use this value as a short cut when defining ticks.

Two groups of ticks are defined, spaced every `1u` (100) and every `0.5u`
(50).

    
    
    # ticks.conf
    
    show_ticks          = yes
    show_tick_labels    = yes
    show_grid           = yes
    
    <ticks>
    
    radius           = dims(ideogram,radius_outer)
    color            = black
    thickness        = 2p
    size             = 0
    
    <tick>
    # ticks for middle of parcelation region
    spacing        = 0.5u
    # length of tick, overwrites the default 0 value
    size           = 5p
    # will have a grid
    grid           = yes
    grid_color     = black
    grid_thickness = 1p
    # from inner edge of lobe axis segment to 0.825r
    grid_start     = 1r-conf(ideogram,thickness)
    grid_end       = 0.825r
    </tick>
    
    <tick>
    # 0.5u ticks defined above will also be shown at parcelation
    # boundaries because they are shown every 50 (50, 100, 150, 200,
    # ...). The 1u ticks (100, 200, ...) take precedence (because of
    # larger spacing) and act to suppress the 0.5u ticks (1u tick have
    # default size 0 and no grid).
    spacing        = 1u
    </tick>
    
    </ticks>
    

#### parcelation labels

The parcelation labels are displayed as a text track.

    
    
    <plot>
    type       = text
    file       = data/structure.label.txt
    color      = black
    label_font = default
    label_size = 20
    r0         = 1r
    r1         = 1.5r
    rpadding   = 10p
    </plot>
    

#### parcelation heat maps

Each parcelation has five properties, each displayed as a heat map. The heat
maps are similarly formatted and are therefore patterened after a template.
While it's not required that you use a template in this case, it makes
rearranging track positions easier and the configuration file tidier.

A track template differs from a typical track only in that its parameter
values depend on a dynamic variable. Typically, this variable is a counter—a
variables whose values change in each <plot> block.

The heatmap template looks like this

    
    
    # heatmap.conf
    <plot>
    type         = heatmap
    # use the value of the counter, via counter(heatmap), to determine the file
    # for this block
    #
    # 1st block: data/measure.0.txt
    # 2nd block: data/measure.1.txt
    # ...
    file         = data/measure.counter(heatmap).txt
    # use the value of the counter to select the color for the heat map
    # from the hm_colors configuration parameter
    color        = eval((split(",","conf(hm_colors)"))[counter(heatmap)])
    # the counter value is used to derive the radial position of the track, from
    # hm_r (initial radial position), hm_w (track width) and hm_pad (track padding)
    # parameters
    r1           = eval(sprintf("%fr",conf(hm_r)-counter(heatmap)*(conf(hm_w)+conf(hm_pad))))
    r0           = eval(sprintf("%fr",conf(hm_r)-counter(heatmap)*(conf(hm_w)+conf(hm_pad))+conf(hm_w)))
    stroke_color = white
    stroke_thickness = 3
    </plot>
    

and is used in `etc/circos.conf` like this

    
    
    # define parameters used in the heatmap template
    hm_r      = 0.96  # radial position of first heat map
    hm_w      = 0.025 # heat map width
    hm_pad    = 0.005 # heat map padding
    
    # heat map track colors
    #           1st track  2nd track     3rd track    4th track   5th track
    #hm_colors = greys-4-seq,greys-4-seq,greys-4-seq,greys-4-seq,greys-4-seq
    hm_colors = reds-4-seq,oranges-4-seq,greens-4-seq,blues-4-seq,purples-4-seq
    
    <plots>
    
    <<include heatmap.conf>>
    <<include heatmap.conf>>
    <<include heatmap.conf>>
    <<include heatmap.conf>>
    <<include heatmap.conf>>
    

#### connectogram links

Links are defined in a <link> block.

    
    
    <links>
    <link>
    file   = data/links.txt
    radius = 0.825r 
    
    bezier_radius = 0r
    bezier_radius_purity = 0.5
    crest         = 0.25
    thickness     = 2
    color         = black
    </link>
    </links>
    

The `radius` parameter defines the radial position of the link ends, while the
`bezier_radius` defines the radial position of the control point used to draw
the curve.

The ancillary parameters, `crest` and `bezier_radius_purity`, affect the angle
at which the links terminate and the control point radius for short links,
respectively.

#### link rules

Recall that the link input data included two parameters, `type` and `score`.
We can use <rule> blocks to change how the links are formatted based on these
parameters.

Parameter values are referenced using `var()` and format values can be
expressed as Perl code when passed through `eval()`.

    
    
    <rules>
    
    <rule>
    # this rule will apply to all links, since the condition is always true
    condition = 1
    # map the score [0,1] onto thickness [1,5]
    thickness = eval(remap_int(var(score),0,1,1,5))
    # force continued testing of rules - otherwise a rule that
    # passes a condition short-circuits further testing
    flow      = continue
    </rule>
    
    <rule>
    # select links with type=0
    condition = var(type) == 0
    # map the score [0,1] onto the colors greys-5-seq-1..greys-5-seq-5 
    color     = eval(sprintf("greys-5-seq-%d",remap_int(var(score),0,1,1,5)))
    </rule>
    
    <rule>
    # select links with type=1
    condition = var(type) == 1
    # same as above, except use the reds Brewer palette
    color     = eval(sprintf("reds-5-seq-%d",remap_int(var(score),0,1,1,5)))
    </rule>
    
    </rules>
    

### variants

I've generated a couple of layout variants for the connectogram (see
[images](images)) to give you an idea of other layouts.

#### outward links for intra-lobe connections

Link geometry can be changed with rules.

    
    
    <link>
    ...
    # all links terminate further inward
    radius = 0.7r
    <rules>
    <rule>
    # links between the same lobes have the control point placed
    # further from the center than their ends (1r vs 0.7r), making
    # them curve outward
    condition = var(chr1) eq var(chr2)
    bezier_radius = 1r
    # slight separation between ends of outward and inward links (0.71r vs 0.7r)
    radius    = 0.71r
    # continue with other rules for these links
    flow      = continue
    </rule>
    ...
    

#### focus on parcelation

The second variant (see `etc.2/` directory in this tutorial) has adjusted
geometry to make the parcelation segments more central in the image. To do
this, the ideogram radius is reduced

    
    
    # ideogram.position.conf
    radius = 0.65r
    

Inter-lobe links point inward and terminate at the inner radius of the
parcelation regions. Intra-lobe links point outward, and terminate at the
outer radius.

    
    
    <rule>
    condition = var(chr1) eq var(chr2)
    bezier_radius = 1.25r
    radius    = dims(ideogram,radius_outer)
    flow      = continue
    </rule>
    

The heatmaps, being an annotation of the parcelation regions, are moved
further out together with labels.

    
    
    # circos.conf
    ...
    hm_r      = 1.3
    

The tick grid that connects the parcelation labels with segments is made
lighter, to avoid interference with outward links.

    
    
    # ticks.conf
    
    <ticks>
    
    <tick>
    ...
    grid_color     = black_a3
    </tick>
    
    </ticks>
    

