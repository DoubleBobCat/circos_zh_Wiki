---
author: DoubleCat
date: 2025-04-11
layout: post
category: configuration
title: Debugging
---

### lesson
If Circos is not behaving as you expect, the first thing to do is to run it
with a `-debug` flag. For example,

```    
    > bin/circos -debug 
```
This will create high-level summary debug reporting about I/O operations and
show you some timings. To generate in-depth debugging of specific components,
see the section about `-debug_group`.

#### configuration dump
Once the configuration file is parsed, you can ask for a full dump of the
entire configuration tree.

```    
    > bin/circos -cdump 
```
This is very useful in cases when you are not sure how your configuration
files are being parsed. For example, you are receiving errors about parsing a
specific parameter, use `-cdump` to make sure that (a) the parameter is indeed
defined and (b) it is defined only once.

```    
    > bin/circos -cdump | grep default_color
    default_color => 'black',
```
You can create a dump of only one part of the configuration tree by providing
an argument

```    
    # show only the <ideogram> block
    > bin/circos -cdump ideogram
```
### Group Debugging
To obtain debug information about specific components, use `-debug_group` with
one or more of these strings separated by a comma (e.g. `-debug_group
cache,chrfilter,rule`).

  * angle 
  * anglepos 
  * bezier 
  * brush 
  * cache 
  * chrfilter 
  * color 
  * conf 
  * counter 
  * heatmap 
  * ideogram 
  * image 
  * io 
  * karyotype 
  * layer 
  * link 
  * png 
  * rule 
  * scale 
  * spacing 
  * summary (default) 
  * svg 
  * test 
  * text 
  * textplace 
  * tick 
  * tile 
  * timer 
  * unit 
  * url 
  * zoom 

By default, the `summary` group is shown. If you want to add other groups

```    
    > circos -debug_group +timer,+io
```
Or if you want just a specific group

```    
    > circos -debug_group timer
```
To show debug for all groups

```    
    > circos -debug_group _all
```
On UNIX, you can use `grep` to parse out the debug reports for specific
groups. For example,

```    
    # store all debug output in circos.debug.txt and display only karyotype 
    > circos ... -group_debug _all | tee circos.debug.txt | egrep "debuggroup karyotype"
    # extract other debug reports
    > egrep "debuggroup rule" circos.debug.txt
    > egrep "debuggroup (rule|scale)" circos.debug.txt
```
#### Benchmarking
If you are concerned about performance, use the `timer` debug group to turn on
timing information. The time taken to execute Circos' components is reported
in the following format. Not every part of the code is timed at the moment —
this section is likely to expand in the future to include other components. If
the image takes more than 30 seconds to run, or if you use `-debug_group
timer`, you will see a list of component timings. For instance, if you run the
example

```    
    > cd example
    > ../bin/circos -debug_group +timer
    debuggroup summary 0.08s welcome to circos v0.67-pre5 12 May 2014
    debuggroup summary 0.08s guessing configuration file
    debuggroup summary 0.09s found conf file /home/martink/work/circos/svn/example/etc/circos.conf
    debuggroup summary 0.46s debug will appear for these features: summary
    debuggroup summary 0.46s parsing karyotype and organizing ideograms
    debuggroup summary 0.85s applying global and local scaling
    debuggroup summary 1.01s allocating image, colors and brushes
    debuggroup summary 1.89s drawing highlights and ideograms
    ...
    debuggroup summary,output 59.87s generating output
    debuggroup summary,output 60.97s created PNG image ./circos.png (2437 kb)
    debuggroup summary,output 60.99s created SVG image ./circos.svg (2377 kb)
    **debuggroup timer 60.99s report circos 60.880 s
    debuggroup timer 60.99s report color 0.812 s
    debuggroup timer 60.99s report colorcache 0.006 s
    debuggroup timer 60.99s report colordefinitions 0.181 s
    debuggroup timer 60.99s report colorfetch 0.174 s
    debuggroup timer 60.99s report colorlists 0.011 s
    debuggroup timer 60.99s report colorlookups 0.007 s
    debuggroup timer 60.99s report colortransparency 0.379 s
    debuggroup timer 60.99s report datarules 2.403 s
    debuggroup timer 60.99s report graphic_png_polygon 0.800 s
    debuggroup timer 60.99s report graphic_slice 2.465 s
    debuggroup timer 60.99s report graphic_slice_polygon_coord 0.442 s
    debuggroup timer 60.99s report graphic_slice_polygon_svg 0.876 s
    debuggroup timer 60.99s report graphic_slice_preprocess 0.225 s
    debuggroup timer 60.99s report highlights 0.000 s
    debuggroup timer 60.99s report ideograms_draw 2.838 s
    debuggroup timer 60.99s report ideograms_processing 0.029 s
    debuggroup timer 60.99s report ideograms_ticks_draw 2.237 s
    debuggroup timer 60.99s report ideograms_zoom 0.152 s
    debuggroup timer 60.99s report io 0.625 s
    debuggroup timer 60.99s report karyotype 0.350 s
    debuggroup timer 60.99s report parameter_seek 4.853 s
    debuggroup timer 60.99s report track_heatmap 2.129 s
    debuggroup timer 60.99s report track_highlight 0.070 s
    debuggroup timer 60.99s report track_histogram 0.663 s
    debuggroup timer 60.99s report track_preprocess 0.196 s
    debuggroup timer 60.99s report track_scatter 1.213 s
    debuggroup timer 60.99s report track_text_ashift 29.814 s
    debuggroup timer 60.99s report track_text_ashiftiter 14.621 s
    debuggroup timer 60.99s report track_text_draw 1.791 s
    debuggroup timer 60.99s report track_text_place 39.445 s
    debuggroup timer 60.99s report track_text_preashift 8.362 s
    debuggroup timer 61.00s report track_text_preprocess 0.607 s
    debuggroup timer 61.00s report track_text_refine 0.004 s
    debuggroup timer 61.00s report unitconvert 0.055 s
    debuggroup timer 61.00s report unitconvert_decision 0.004 s
    debuggroup timer 61.00s report unitconvert_delegate 0.016 s
    debuggroup timer 61.00s report unitparse 0.189 s**
```
Some of the component timing groups are nested. For example, any time spent on
`ideograms_ticks_draw` is included in `ideograms_draw`.

Extensive debug reporting will make Circos run more slowly.
### images
### configuration
