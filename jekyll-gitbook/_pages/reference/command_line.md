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

# 12 — Circos Reference

## 3\. Command Line Parameters

### using command-line flags

Circos is driven by a configuration file, but accepts several command-line
flags that change how it runs (e.g. format and location of output files).

    
    
    # no flags - Circos guesses location if configuration file
    > circos
    
    # specific configuration file
    > circos -conf etc/circos-fig1.conf
    
    # additional debugging
    > circos -debug 
    
    # additional debugging, by group
    > circos -debug_group io,chrfilter
    
    # brief usage
    > circos -h
    
    # man page
    > circos -man
    
    # version check
    > circos -v
    
    # module diagnostics
    > circos -modules
    
    # run and shut up
    > circos -silent
    

Configuration flags can be shortened, as long as the shortened version is
unambigous.

    
    
    > circos -cdump image
    > circos -cdum image
    > circos -cdu image
    > circos -cd image
    # -c is not ok because it is 
    > circos -c image
    Option c is ambiguous (cdump, chromosomes, chromosomes_display_default, chromosomes_order, 
    chromosomes_radius, chromosomes_scale, color_cache_rebuild, color_cache_static, configfile)
    

The `-param` flag allows you to conveniently change the value of any
configuration parameter.

    
    
    # change image size
    > circos -param image/radius=2000p
    # do not draw ideograms
    > circos -param ideogram/show=no
    # draw only two chromosomes
    > circos -param chromosomes_display_default=no -param chromosomes=hs1;hs2
    

### Circos command-line flags

#### configuration

flag

description

comment

  

-conf FILE

Name of configuration file.  
DEFAULT `circos.conf`

Circos will attempt to guess the location of this file, searching in `.`, `..`
and `../..`. In other words  
`> circos`  
is equivalent to  
`> circos -conf etc/circos.conf`.  
Use  
`> circos -debug_group +io`  
to include debug information about where files are being searched.

  

-param PATH/PARAM=VALUE

Sets the value of parameter `PARAM` in configuration path `PATH` to `VALUE`.
You can use multiple `-param` flags. The `PATH` must point to a unique block.
The flag can be used multiple times.  
_e.g._ `-param chromosomes=hs1`  
_e.g._ `-param ideogram/show=no`  
_e.g._ `-param ideogram/spacing/default=0.01r`  
_e.g._ `-param a=10 -param b=20 -param c=30`

This is useful for temporary override a configuration parameter, such as in a
batch job were you are running Circos several times with different parameters.
Within the configuration parameter, value of parameters can be referenced
using `conf()`.

  

-cdump [BLOCK1/[BLOCK2/...]][:REGEX]

Report a dump of the configuration. If `BLOCK` is specified, only show that
block. To show nested blocks, specify a block path delimited by `/`. To limit
the output to parameters that match a regular expression, include `:REGEX`  
_e.g._ `-cdump image`  
_e.g._ `-cdump ideogram/spacing`  
_e.g._ `-cdump ideogram/spacing:def`

  

* * *

#### usage

flag

description

comment

  

-help 

Display usage synopsis.

  

-man 

Show man page.

  

-version 

Print the version.

  

* * *

#### debugging

flag

description

comment

  

-debug 

Obtain additional debugging.

  

-debug_group GROUP,[GROUP,...]

Toggle report of debug messages for various modules. Prefix the group with `+`
to add to the default list, `-` to remove it. To show debuging from all
groups, use `_all`. To get a list of groups, use the flag without an argument.  
DEFAULT `summary`  
_e.g._ `-debug_group`  
_e.g._ `-debug_group=+timer`  
_e.g._ `-debug_group=-summary`  
_e.g._ `-debug_group=+io,+png`  
_e.g._ `-debug_group _all`

If the image takes more than 30 seconds to generate, Circos will report timers
for code components (group: timer). For reference, see the [list of all debug
groups](https://www.circos.ca/documentation/tutorials/configuration/debugging).
Groups with a + or - prefix require the use of = in the flag, otherwise
they'll be interpreted as flags themselves.

  

-fakeerror GROUP,ERROR 

Simulate error `ERROR` from error group `GROUP`.  
_e.g._ `-fakeerror`  
_e.g._ `circos -fakeerror io`

  

-modules 

Diagnose required modules..

Success means that the module was found and successfully loaded.

  

-paranoid 

Make all warnings fatal.  
DEFAULT `-paranoid`  
OPTION `-noparanoid`

  

-silent 

Generate no runtime messages.

  

-time 

Report code timings.

Same as  
`> circos -debug_group=+timer`

  

-version 

Report the version and quit.

  

-warnings 

Enable warnings.  
DEFAULT `-warnings`  
OPTION `-nowarnings`

  

* * *

#### I/O

flag

description

comment

  

-outputdir DIR   
-dir DIR

Image output directory  
DEFAULT `.`  
_e.g._ `-dir ..`

  

-outputfile FILE   
-file FILE

Output image filename. Can include a path. Extention (png, svg) will be
automatically added.  
DEFAULT `circos`  
_e.g._ `-file otherfile`  
_e.g._ `-file ../otherfile`

Extention .png or .svg will be added.

  

-png 

Create a PNG file.  
DEFAULT `-png`  
OPTION `-nopng`

  

-svg 

Create a SVG file.  
DEFAULT `-svg`  
OPTION `-nosvg`

  

* * *

#### color

flag

description

comment

  

-color_cache_rebuild 

Forces a rebuild of the color cache.

See `etc/housekeeping.conf` for color* parameters.

  

-color_cache_static 

Forces the use of an existing color cache, even if colors have been redefined.

See `etc/housekeeping.conf` for color* parameters.

  

-randomcolor [COLOR1,COLOR2,...]

Generates an image in which all colors except for those listed are randomized.  
_e.g._ `-randomcolor white,black`

  

