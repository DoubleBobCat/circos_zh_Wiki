---
author: DoubleCat
date: 2025-04-11
layout: post
category: configuration
title: Data Files
---

### lesson
Circos uses plain-text data input files. The data format is very
simple—arguably the simplest that it could be. Creating data files for Circos
is easy.

Chromosome definition, data tracks (<plot> blocks), links (<link> blocks) and
highlights (<highlight> blocks) all require external files for their content.

Depending on the track, the format of the input data file is slightly
different.

#### file format
##### karyotype — biology applications
The karyotype file defines the chromosomes. By default, all chromosomes will
be drawn.

Each chromosome has a name, label, start and end position and a color. For
example, the human karyotype file looks like this

```    
    chr - hs1 1 0 249250621 chr1
    chr - hs2 2 0 243199373 chr2
    chr - hs3 3 0 198022430 chr3
    ...
```
Circos uses species prefix for chromosome names (e.g. human: hs1, hs2, ... ;
mouse: mm1, mm2, ... ) instead of the generic "chr" prefix. Chromosome colors,
however, use the "chr" prefix, because they're not meant to be species
specific.

The karyotype file can optionally define cytogenetic bands for each
chromosome.

```    
    band hs1 p36.33 p36.33 0 2300000 gneg
    band hs1 p36.32 p36.32 2300000 5400000 gpos25
    band hs1 p36.31 p36.31 5400000 7200000 gneg
    ...
```
You can find karyotype files for common reference genomes in `data/karyotype`
in the Circos distribution.

See [karyotype tutorial](/documentation/tutorials/ideograms/karyotypes/) for
more details.

##### karyotype — general applications
If your data is not based on chromosomes, then use the karyotype file to
define whatever axes you need to display them.

For example, this will define 3 segments of size 1000, 2000 and 3000 named
`axis1`, `axis2` and `axis3`.

```    
    chr - axis1 1 0 1000 black
    chr - axis2 1 0 1500 blue
    chr - axis3 1 0 2000 green
```
##### line, scatter, histogram, heat map
[Line](/documentation/tutorials/2d_tracks/line_plots),
[scatter](/documentation/tutorials/2d_tracks/scatter_plots),
[histogram](/documentation/tutorials/2d_tracks/histograms) and [heat
map](/documentation/tutorials/2d_tracks/heat_maps) tracks are 2D data tracks
that associate a value with a genomic position.

```    
    #chr start end value [options]
    hs5 50 75 0.75
```
##### tile
A [tile](circos/tutorials/lessons/2d_tracks/tiles) track defines an interval
on the same chromosome. It is used to display coverage elements like reads or
clones.

```    
    #chr start end [options]
    hs5 50 75 
```
##### text
A [text](/documentation/tutorials/2d_tracks/text_labels1) track associates any
string with a genomic position, typically used for text labels.

```    
    #chr start end label [options]
    hs5 50 75 ABC
```
If you would like to use multi-word text labels, use a tab as a delimiter (see
below).

##### connector
A [connector](/documentation/tutorials/2d_tracks/connectors) track two
positions on the same chromosome, which are connected by a beveled connector.

```    
    #chr start end [options]
    hs5 50 1500
```
A connector must start and end on the same chromosome.

##### links
[Links](/documentation/tutorials/links/basic_links/) associate two intervals
between the same or different chromosomes. They can be drawn as lines or
[ribbons](/documentation/tutorials/links/ribbons/).

```    
    # chr1 start1 end1 chr2 start2 end2 [options]
    hs1 200 300 hs10 1100 1300
    hs7 50 150 hs 5000 6000 color=blue
```
`[binlinks](/documentation/tutorials/utilities/density_tracks)`,
`[bundlelinks](/documentation/tutorials/utilities/bundling_links)` and
`[filterlinks](/documentation/tutorials/utilities/filtering_links)` tools (all
found in the [tools distribution](/software/download/tools)) are used to
manipulate and analyze link files.

#### options
Any formatting option specific to a data point (shape, size, color, etc)
defined in the <plot>, <link>, or <highlight> block individually set for a
data point in the input file.

In the file formats shown above, the `[options]` string is a comma-delimiter
set of `variable=value` pairs.

```    
    chr start end var1=value1,var2=value2,...
```
For options that are passed as a list (e.g. color RGB values), you'll need to
delimit the option value with `(` and `[`]

```    
    chr start end color=(R,G,B)
```
##### options with and without data values
Input files that associate a value with a genomic position have the options
field in the 5th column

```    
    chr start end value options
```
For files that do not have a value (e.g. tile, highlight), the field is in the
4th column

```    
    chr start end options
```
If you attempt to use a file with values as input to tracks that do not expect
values, Circos will attempt to parse the value field (4th column) as an
options string and will report an error.

```    
    Error parsing data point options. Saw parameter assignment [0.75] but expected it to be in the format x=y.
```
#### file delimiter
By default, the delimiter is any whitespace. To change this define
`file_delim` at the root of the configuration file. A good place to put this
parameter is in `etc/housekeeping.conf`

```    
    # etc/housekeeping.conf
    file_delim = \t
```
If you want to have multi-word text labels, set the delimiter to a tab. The
same delimiter is used for _all_ input files (data files and karyotype).

#### file location
When you specify the file using an absolute path, Circos will not try to find
it anywhere else. For example, in the case of

```    
    file = /path/to/file.txt
```
if file `/path/to/file.txt` does not exist, an error will be produced.

However, if you specify the file as a relative path

```    
    file = data/file.txt
```
Circos will attempt to look for it in several directories in this order:

  * any directory defined in `data_path` (see `etc/housekeeping.conf`) 
  * `CWD/`
  * `CWD/etc`
  * `CWD/data`
  * `CWD/../`
  * `CWD/../etc`
  * `CWD/../data`
  * `CWD/../..`
  * `CWD/../../etc`
  * `CWD/../../data`

It is better to use relative paths everywhere in your configuration file. This
will make the file portable.

I suggest that you keep the data files in a separate directory (e.g. `data/`),
distinct from your configuration files. See the [best practices
tutorial](/documentation/tutorials/reference/best_practices/) for details.
### images
### configuration
