---
author: DoubleCat
date: 2025-04-11
layout: post
category: configuration
title: Installation and Configuration
---

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

# 1 — Configuration and Installation

## 1\. UNIX vs Windows

If you are having trouble with installation of Perl or modules, use online
resources that explain the details of how to [download
Perl](https://www.perl.org/get.html), get it working
([Linux](https://learn.perl.org/installing/unix_linux.html), [Mac OS
X](https://learn.perl.org/installing/osx.html), Windows [[win32.perl.org
wiki](https://win32.perl.org/wiki/index.php?title=Main_Page<span class=syn-
comment>#Installing_Perl_on_Windows_for_the_First_Time.3F),
[ActiveState](https://perl.about.com/od/gettingstartedwithperl/ss/installperlwin.htm),
[Strawberry](https://damienlearnsperl.blogspot.com/2009/01/install-strawberry-
perl-your-windows.html)]), and how to [install
modules](https://www.cpan.org/modules/INSTALL.html)
([UNIX](https://perldoc.perl.org/perlmodinstall.html), [Windows](install perl
modules windows)). If you're still stuck, post your questions to the [Circos
group](https://groups.google.com/group/circos-data-visualization).

Try the [Active State Perl build for
Circos](https://platform.activestate.com/ReadyMade/Circos/distributions?platformID=78977bc8-0f32-519d-80f3-9043f059398c).
It includes all the necessary modules.

Need to install modules? See [A Guide to Installing
Modules](https://www.perlmonks.org/?node_id=621579) and [its corresponding
tutorial for Windows users](https://www.perlmonks.org/?node_id=434813).

Having trouble with libgd and GD? See the [Perl Monks libgd/GD
Tutorial](https://www.perlmonks.org/?node_id=621579), Shaun Jackman's
[Homebrew formula](https://groups.google.com/forum/#!topic/circos-data-
visualization/qOIjmy4_wnM), Wang's [install zlib/libpng/jpeg/freetype/libgd/GD
on Mavericks](https://wangqinhu.com/install-gd-on-mavericks/) as well as my
own guide for [installation of libpng, freetype, libgd and GD on Mac OS X
Mavericks](/documentation/tutorials/configuration/perl_and_modules/index.mhtml#circos-
libgd-gd). There are some [useful
threads](https://groups.google.com/forum/?hl=en&fromgroups=<span class=syn-
comment>#!topic/circos-data-visualization/MOdx0eKWDeQ) in the Google Group
about this.

Need to run Bash shell batch files in Windows? You'll need to install a [UNIX
command line shell](https://stackoverflow.com/questions/913912/bash-shell-for-
windows), like [Cygwin](https://www.cygwin.com).

Stumped by an error? A good strategy is to Google the error message (e.g.
[mkdir /usr/local/share/man: permission
denied](https://www.google.ca/search?hl=en&q=%2Fbin%2Fenv+not+found&sourceid=navclient-
ff&rlz=1B7GGLL_enCA396CA396&ie=UTF-8<span class=syn-
comment>#sclient=psy&hl=en&rlz=1B7GGLL_enCA396CA396&source=hp&q=mkdir+%2Fusr%2Flocal%2Fshare%2Fman:+permission+denied&aq=f&aqi=&aql=&oq=&pbx=1&fp=58653f3aee9cd59b))
to find the solution.

Want to learn more about Perl? Try [learn.perl.org](https://learn.perl.org/)
or read through the [Perl Journal
archive](https://mk.bcgsc.ca/books/sapj/tpj).

To run Circos, you need [Perl](https://www.perl.org/get.html). Perl is an
interpreted language, which means that you _do not need to compile Circos_ to
run it. The code is read in by the Perl executable, which takes care of
interpreting, compiling and running it. To install Circos, nothing other than
unpacking the archive is required.

Circos has been designed with an approach that should be familiar to UNIX
users: no interface, plain-text configuration and command-line utilities. If
you are a Windows user, this might seem a little unusual at first. The
tutorials in this section that cover
[installation](/documentation/tutorials/configuration/distribution_and_installation),
[configuration](/documentation/tutorials/configuration/configuration_files),
and [Perl modules](/documentation/tutorials/configuration/perl_and_modules)
discuss the differences between Circos usage on UNIX and Windows.

You do not need to know Perl to run Circos, but you do need to be familiar
with

  * concept of directories and files 
  * navigating directories at the command prompt 
  * creating and deleting directories at the command prompt 
  * concept of absolute and relative paths (e.g. `/path/file.txt` vs `../file.txt` vs `file.txt`) 

You'll be working entirely on the command-line and text editor in UNIX.
Windows users unfamiliar with the DOS command-line should read the following
tutorials

  * [Windows command-line tutorial](https://www.bleepingcomputer.com/tutorials/tutorial76.html)
  * [Windows command-line prompt in 15 minutes](https://www.cs.princeton.edu/courses/archive/spr05/cos126/cmd-prompt.html)

### Perl Installation

UNIX has Perl installed by default, and unless your system is ancient. To
check your Perl version,

    
    
    > perl -v
    

Anything earlier than 5.8 should be upgraded.

If you're a Windows user, it's likely that you're unfamiliar with Perl. There
is nothing to fear—it is just like any other application you have installed.
You'll need to use it from the DOS command-line and know only the basics which
are covered in the two tutorials linked to above.

Windows users should install [Strawberry Perl](https://www.strawberryperl.com)
or [ActiveState Perl](https://www.activestate.com/activeperl). Both have
package managers that help you install, update and remove modules.

Where possible, use the manager to install modules instead of the CPAN shell.
[CPAN](https://www.cpan.org) is the Comprehensive Perl Archive Network and
hosts, among other things, Perl modules contributed by the community. Details
of downloading and installing modules can be found in the [Perl and Modules
section](/documentation/tutorials/configuration/perl_and_modules).

### Circos Installation

On UNIX, you only need to unpack the Circos archive in a suitable location
with `tar`. For example,

    
    
    > tar xvfz circos-0.67-pre4.tgz
    

Windows users should use Windows' built-in handling of `.tgz` files (in
Windows Vista or newer). The `.tgz` extension is a short version of `.tar.gz`,
which more explicitly indicates that the file is a `tar` archive which has
been subsequently compressed with `gzip`.

You can unpack the archive with 3rd party utilities like the free
[7-Zip](https://www.7-zip.org), or the venerable (but not free)
[WinZip](https://www.winzip.com).

Circos installation details are listed in the [Distribution and
Installation](/documentation/tutorials/configuration/distribution_and_installation)
section.

### Running Circos

For UNIX users the `bin/circos` file is executable, so just run that. The
first line of `bin/circos` is

    
    
    #!/bin/env perl
    

which automatically uses the perl binary in your `PATH`. If you don't have
`/bin/env`, it may be in `/bin/usr/env`, such as on Mac OS X.

Windows users will need to run perl explicitly and use the circos script as
the argument.

Windows won't know what to do with the `bin\circos` file otherwise.

    
    
    perl bin\circos
    

Details about running Circos can be found in the [Distribution and
Installation](/documentation/tutorials/configuration/distribution_and_installation)
section. Command-line flags that adjust run-time parameters are described in
the [Runtime
Parameters](/documentation/tutorials/configuration/runtime_parameters)
tutorial.

### path delimiter

Windows file paths use `\`as a directory separator, whereas UNIX uses `/`. The
UNIX convention is used throughout the tutorials.

Windows users should interpret paths like

    
    
    tutorials/2/2/circos.conf

as

    
    
    tutorials\2\2\circos.conf

Circos tutorials are included in a separate package which you will need to
[download](/software/download/tutorials).

### Configuration

Because the directory structure of UNIX and Windows is different, you may need
to adjust the output directory for tutorial examples. For example, on UNIX
`/tmp` is used as a scratch directory (e.g. for creating temporary files). On
Windows this directory does not exist.

You can overwrite the output directory and file defined in the configuration
file using `-outputdir` and `-outputfile` parameters. For more information
about these and other parameters, see the [Runtime
Parameters](/documentation/tutorials/configuration/runtime_parameters)
tutorial.

    
    
    # on Windows, executed from the Circos installation directory
    perl bin\circos -conf tutorials\2\2\circos.conf -outputdir . -outputfile tutorial_image.png
    

### Batch Files

In some tools and tutorial directories you'll come across UNIX batch files
that look something like this

    
    
    # tools/tableviewer/makeimage
    #!/bin/bash
    ...
    cat samples/table-$n.txt | bin/parse-table -conf samples/parse-table-$n.conf | bin/make-conf -dir data
    ...
    

These are written in the BASH shell (a UNIX scripting language) and cannot be
run directly on Windows (e.g. in a DOS window). To run these files you'll need
to install a [UNIX shell
environment](https://stackoverflow.com/questions/913912/bash-shell-for-
windows) for Windows like [Cygwin](https://www.cygwin.com/).

