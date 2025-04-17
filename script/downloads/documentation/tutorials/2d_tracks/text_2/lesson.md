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

## 7\. Text—Stacking

[Lesson](/documentation/tutorials/2d_tracks/text_2/lesson)
[Images](/documentation/tutorials/2d_tracks/text_2/images)
[Configuration](/documentation/tutorials/2d_tracks/text_2/configuration)

In the previous example, I had drawn just a few labels. If labels are dense,
they will be automatically stacked to avoid overlap. In other words, if a
label's position results in overlap with another label, the label is drawn at
the same angular position but is radially shifted out.

However, if snuggling is turned on `label_snuggle=yes`, the label's radial
position may be slightly adjusted to reduce the number of layers of text.

Snuggling is heuristic—it is not based on any kind of global optimization.

    
    
    <plot>
    
    ...
    label_snuggle             = yes
    
    # shift label up to 2x its height in pixels in the angular direction
    max_snuggle_distance            = 2r
    
    # sample possible label positions every 2 pixels
    snuggle_sampling                = 2
    
    snuggle_tolerance               = 0.25r
    
    snuggle_link_overlap_test      = yes 
    snuggle_link_overlap_tolerance = 2p
    
    snuggle_refine                 = yes
    
    </plot>
    

### snuggling parameters

To help arrange the labels so that they occupy less space, use label
snuggling. The `max_snuggle_distance` controls how far the label may be
shifted, in the angular direction, to fit better. The distance limit is
expressed in pixels or relative to the label's size along the tangential
direction.

The label is tested at a new angular position every `snuggle_sampling` pixels,
within the `max_snuggle_distance` of its original position. By increasing the
`snuggle_sampling` value, the layout process runs faster, but is less precise.

You can also short-circuit precise placement by setting `snuggle_tolerance`
(absolute or relative to label's tangential size). The larger this value, the
less precise the placement.

If the labels have a link line, you choose to test whether link lines overlap
with previous labels using `snuggle_link_overlap_test`. The extent of
acceptable overlap is set using `snuggle_link_overlap_tolerance`.

The `snuggle_refine` parameter toggles an additional check for crossing of
links of labels that are placed at similar radial positions. Label pairs whose
link lines cross are swapped. This refine parameter is functionaly only if
`show_links=yes`.

### label padding

You can increase the `max_snuggle_distance` to make the label layout more
compact. When snuggling, it can also be helpful to adjust padding, both
angular (via `padding`) and radial (via `rpadding`) directions around the
label. Both can be absolute or relative.

    
    
    <plot>
    ...
    padding  = 2p
    rpadding = 0.1r
    
    </plot>
    

By making padding negative, labels are more tightly spaced. When expressed in
relative units (e.g. `0.1r`), radial padding is relative to label width and
angular padding is relative to label height.

Experiment with the `max_snuggle_distance` and padding parameters to find a
good combination for your data. If you have a large number of labels
(hundreds) then the track may take a while to optimize (several minutes).

### uniformly placed text

If you want text to be placed uniformly don't use snuggling, which will move
labels around.

For example, snuggling works best when label density varies. But if you're
showing text that is defined at specific intervals (e.g. sequence), don't
snuggle. You'll probably want to turn links off (this is the default) and use
a monospaced font

    
    
    label_font = mono
    

All font definitions are in `etc/fonts.conf` in the Circos distribution.

    
    
    # etc/fonts.conf
    
    ...
    mono           = fonts/modern/cmuntt.ttf  # CMUTypewriter-Regular
    mono_light     = fonts/modern/cmunbtl.otf # CMUTypewriter-Light
    
    # same as mono and mono_light
    fixed          = fonts/modern/cmuntt.ttf  # CMUTypewriter-Regular
    fixed_light    = fonts/modern/cmunbtl.otf # CMUTypewriter-Light
    ...
    

### debugging text placement

Text placement can take while, especially if snuggling is turned on and you
have many labels. Run Circos with `-debug_group text` to convince yourself
that something is happening.

    
    
    > circos ... -debug_group text
    ...
    debuggroup text 6.45s label layer 2 snuggle seek - STX12 8.0 d 26 label_min_height 42 global_min_height 28
    debuggroup text 6.45s label layer 2 snuggle seek + PPP1R8 0.0 d 14 label_min_height 42 global_min_height 28
    debuggroup text 6.45s label layer 2 snuggle seek - PPP1R8 0.0 d 14 label_min_height 42 global_min_height 28
    ...
    

Text that does not fit into the track boundaries won't be placed. Run Circos
with `-debug_group textplace` to monitor which labels are not placed.

    
    
    > circos ... -debug_group textplace
    ...
    debuggroup textplace 23.02s placed hs1 40858938 40903911 RIMS3
    debuggroup textplace 23.02s placed hs1 29346951 29380948 SFRS4
    debuggroup textplace 23.03s not_placed hs1 1466916 1500125 SSU72
    debuggroup textplace 23.03s placed hs1 27972280 28023550 STX12
    debuggroup textplace 23.03s placed hs1 40079314 40121764 TRIT1
    ...
    
    

