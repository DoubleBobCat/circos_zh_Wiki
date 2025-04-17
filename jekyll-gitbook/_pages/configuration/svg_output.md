---
author: DoubleCat
date: 2025-04-11
layout: post
category: configuration
title: SVG Output
---

## SVG Output
### lesson
Circos is capable of producing both PNG and SVG images. This section discusses
SVG files.

### SVG Output
SVG stands for _scalable vector graphics_ and it is a format that defines an
image using vector-based primitives (lines, squares, rectangles, etc) rather
than pixels. SVG images can be turned into a bitmap (rasterized) at any
resolution, which makes them appealing for creating figures for publication.
You can edit and rasterize SVG files using applications such as Illustrator or
Inkscape.

To turn SVG output on, set the `svg` flag in the <image> block

```    
    <image>
    ...
    svg = yes
    ...
    </image>
```
or use the `-svg` command-line flag

```    
    bin/circos -svg
```
You can also suppress the creation of the SVG file using

```    
    bin/circos -nosvg 
```
### Fonts in SVG files
Text elements in SVG files have the `font-family` attribute, which specifies
the font for the text element.

Make sure that you have all the fonts used by your image installed on your
system. Circos uses [CMU Modern](https://canopus.iacp.dvo.ru/~panov/cm-
unicode/download.html) (see `fonts/modern`) for all its labels and a custom
symbols font (see `fonts/symbols`). I've had reports from Windows users that
Illustrator failed to load the SVG file unless all the fonts used by the
figure were installed.

If your text appears smaller than expected, increase the `svg_font_scale`
parameter in `etc/housekeeping.conf`.
### images
### configuration
#### circos.conf
```    
    <image>
    
    ...
    
    # png on
    png = yes
    # svg on
    svg = yes
    
    ...
    
    </image>
``````
  

* * *
