---
author: DoubleCat
date: 2025-04-11
layout: post
category: configuration
title: Common Errors
---

### lesson
If Circos halts with an error, before contacting me or posting to the
[discussion group](https://groups.google.com/group/circos-data-visualization),
please read the error message first.

I know it seems odd to ask, but I have tried to make many of the error
messages very verbose and clear to understand.

If the error message doesn't make sense to you make sure that you understand
how Circos works. Read the following pages

  * [Windows vs UNIX use](/documentation/tutorials/configuration/unix_vs_windows/)
  * [Circos installation](/documentation/tutorials/configuration//installation/)
  * [Perl modules](/documentation/tutorials/configuration//perl_and_modules/)
  * [configuration file format and use](/documentation/tutorials/configuration/configuration_files/)

To help you diagnose the problem, use Circos' [debugging
facility](/documentation/tutorials/configuration/debugging/) to track the
program as it runs. Turn on full debugging, if necessary

```    
    > circos -debug_group _all
```
#### reporting bugs and obtaining support
If you still cannot resolve the issue, please [write to the discussion
group](https://groups.google.com/group/circos-data-visualization).

  * state what version of Circos you are using (if it is substantially older than [the current version](/software/download/circos), upgrade first) 
  * provide the command you executed and the directory you executed it in 
  * provide the full error report 

If you need help with an image, provide

  * all configuration files (don't forget `ideogram.conf`, `ticks.conf` and others) 
  * all data files (don't forget your karyotype file!) 

#### contacting me
If I think you haven't read this section then you may assume I won't read your
message.

If you are unable to obtain an answer from the discussion group, or are
pressed for time (submitting a manuscript is one good example), [contact
me](mailto:martink@bcgsc.ca). Because I get a lot of direct requests, the more
you help me diagnose your problem the faster I can respond and help you.

When you contact me please be specific about what is happening, why you think
it should not be happening, and what you expect to happen. Include debug
output and all your configuration and data files in your email so that I can
reproduce the problem.

If you are successful in creating an image, but find that it is not what you
expect please send me the image.

If you email me before posting to the group I will tell you to post to the
group.

#### common errors and problems
##### Perl on Windows—can't figure it out?
If you are running Circos on Windows, you may be unfamiliar with Perl. Please
read the [Windows vs
UNIX](/documentation/tutorials/configuration/unix_vs_windows/) tutorial before
you read the [Distribution and
Installation](/documentation/tutorials/configuration/distribution_and_installation/)
tutorial.

There are plenty of excellent Perl tutorials online for both UNIX and Windows.
Make use of them. Remember, you don't need to know any Perl, only how to
install it and call it to run Circos.

##### Circos errors
This is what a typical Circos error looks like. I have tried to make them
clear.

```    
      *** CIRCOS ERROR ***
    
      CONFIGURATION FILE ERROR
    
      You did not define a karyotype file. Are you sure your configuration file is
      well formed?
    
      If you are having trouble debugging this error, use this tutorial to learn how
      to use the debugging facility
    
          https://www.circos.ca/documentation/tutorials/configuration/debugging
    
      If you're still stumped, get support in the Circos Google Group
    
          https://groups.google.com/group/circos-data-visualization
    
      Stack trace:
     at /home/martink/work/circos/svn/bin/../lib/Circos/Error.pm line 271
    	Circos::Error::fatal_error('configuration', 'no_karyotype') called at 
               /home/martink/work/circos/svn/bin/../lib/Circos/Configuration.pm line 468
    	Circos::Configuration::validateconfiguration() called at 
               /home/martink/work/circos/svn/bin/../lib/Circos.pm line 149
    	Circos::run('Circos') called at /home/martink/bin/circos line 229
```
##### configuration file error
This is one of the most common errors reported by users.

```    
      *** CIRCOS ERROR ***
    
      CONFIGURATION FILE ERROR
    
      Circos could not find the configuration file. To run Circos, you need to
      specify this file using the -conf flag. The configuration file contains all
      the parameters that define the image, including input files, image size,
      formatting, etc.
    
      If you do not use the -conf flag, Circos will attempt to look for a file
      circos.conf in several reasonable places such as . etc/ ../etc
```
This error appears because Circos cannot find a configuration file, required
to generate the image, anywhere within the current directory or
subdirectories.

Windows users experience this error frequently. For example, if you've
unpacked Circos in `D:\circos-0.67` and run this command

```    
    C:\My Documents>perl D:\circos-0.67\bin\circos 
```
Circos will look within `C:\My Documents` for a configuration file. If you've
just installed Circos, no configuration file will be found.

Instead, you want to run Circos in a directory from which the configuration
file can be easily referenced. There is an example image that is bundled with
the distribution, found in `example/`.

```    
    C:\My Documents>cd D:\circos-0.67\example
    D:\circos-0.67\example>perl D:\circos-0.67\bin\circos -conf etc\circos.conf
```
##### configuration file import
If you are importing configuration files using <<include ...>>, make sure you
understand how the path resolution works. This is described in the
[Configuration Files
tutorial](/documentation/tutorials/configuration/configuration_files).

##### missing units
Many configuration parameters require units (see tutorial 1.2). An error like
this

```    
      Unable to convert a value [0.005] from one unit [n] to another [b]. The
      following from->to combinations were expected: r->b u->b
```
means that the value `0.005` was expected to have a unit `r` (relative) or `u`
(chromosome unit) for conversion to `b` (base), but was found to have unit `n`
(explicit code for no unit).

If you do not define a required parameter the error will look like this

```    
      The parameter [ideogram/thickness] was not defined. It needs to be defined and
      have one of these units [r,p].
```
##### slow performance
Some parts of the code are less (or more) optimized than others. In
particular, text tracks can take a long time to render. For example, if you've
asked to draw 50,000,000 data points, prepare to wait (and be disappointed
with the output).

Turn on benchmarking using `-debug_group +timer` to add timings to the debug
reportingoutput. See the
[Debugging](/documentation/tutorials/configuration/debugging/) tutorial for
more information.
### images
### configuration
