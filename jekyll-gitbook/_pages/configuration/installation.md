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

## 2\. Distribution and Installation

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

For an overview of the installation process, and how it differs between UNIX
and Windows, please also refer to the [UNIX vs Windows
section](/documentation/tutorials/configuration/unix_vs_windows).

### Installing Circos

First, [download Circos](/software/download). The contents of the distribution
are described below.

You don't need to move or edit any files in the main distribution.

#### Installing Circos on UNIX

Assuming that you want to install in `ROOT=~/software/circos`,

    
    
    > cd ~
    > mkdir software
    > mkdir software/circos
    > cd software/circos
    # download Circos and place the archive in the directory
    > ls
    -rw-r--r-- 1 martink users 26725778 Jun  6 11:04 circos-0.67-pre4.tgz
    # unpack
    > tar xvfz circos-0.67-pre4.tgz
    ...
    circos-0.67-pre4/data/karyotype/karyotype.arabidopsis.txt
    circos-0.67-pre4/data/karyotype/karyotype.zeamays.txt
    circos-0.67-pre4/data/karyotype/karyotype.oryzasativa.txt
    # make a symlink to current
    > ln -s circos-0.67-pre4 current
    > ls
    drwxr-xr-x 10 martink users     4096 Jun  6 11:06 circos-0.67-pre4/
    -rw-r--r--  1 martink users 26725778 Jun  6 11:04 circos-0.67-pre4.tgz
    lrwxrwxrwx  1 martink users       16 Jun  6 11:07 current -> circos-0.67-pre4/
    # delete the tarball, if you want
    

To install GD and Perl modules on Ubuntu, use `apt-get`.

    
    
    sudo apt-get -y install libgd2-xpm-dev
    

#### Installing Circos on Mac

If you're using Homebrew, you can use [Shaun Jackman's
formula](https://groups.google.com/forum/#!topic/circos-data-
visualization/qOIjmy4_wnM)

    
    
    brew tap homebrew/science
    brew remove gd
    brew install gd --with-freetype
    brew install cpanminus
    sudo chown "$USER":admin /Library/Perl/5.16 # on Mac OS
    cpanm Config::General Font::TTF::Font Math::Bezier Math::VecStat Readonly Set::IntSpan Text::Format
    cpanm --force GD::Polyline
    brew install circos
    brew test circos
    

#### Installing Perl Modules on Mac

Thanks to Paul Nuin for this section. It references an older version of
Circos, but the process is the same for newer versions.

This short tutorial gives a step-by-step overview on how to make Circos work
on OS X, but it should be similar to other *nix flavours. I just installed on
my Mountain Lion box, but, again, it should be identical to previous versions
of OS X.

Assume Circos has been installed to `/Applications/circos-0.55/`. If you run
it and get

    
    
    $ perl /Applications/circos-0.55/bin/circos
    Can't locate Config/General.pm in @INC (@INC contains: /Applications/circos-0.55/bin/lib /Applications/circos-0.55/bin/../lib
     /Applications/circos-0.55/bin /Library/Perl/5.12/darwin-thread-multi-2level /Library/Perl/5.12
     /Network/Library/Perl/5.12/darwin-thread-multi-2level /Network/Library/Perl/5.12
     /Library/Perl/Updates/5.12.4/darwin-thread-multi-2level /Library/Perl/Updates/5.12.4
     /System/Library/Perl/5.12/darwin-thread-multi-2level /System/Library/Perl/5.12
     /System/Library/Perl/Extras/5.12/darwin-thread-multi-2level /System/Library/Perl/Extras/5.12 .) at
     /Applications/circos-0.55/bin/../lib/Circos.pm line 53.
    BEGIN failed--compilation aborted at /Applications/circos-0.55/bin/../lib/Circos.pm line 53.
    Compilation failed in require at /Applications/circos-0.55/bin/circos line 184.
    BEGIN failed--compilation aborted at /Applications/circos-0.55/bin/circos line 184.
    So, a lot of things going wrong, we need to check what is missing and install. Circos has a couple 
    of commands bundled in its package that help us working through the errors. Best way to run them is 
    to cd into Circos bin directory
    

then you are missing the Config::General module and possibly other modules.

    
    
    $ cd /Applications/circos-0.55/bin/
    /Applications/circos-0.55/bin$ ./list.modules
    In my case, running this script gave me a list of the required modules for Circos
    
    Circos requirements
    Carp
    Config::General
    Data::Dumper
    Digest::MD5
    File::Basename
    File::Spec::Functions
    FindBin
    GD
    GD::Polyline
    Getopt::Long
    Graphics::ColorObject
    IO::File
    List::MoreUtils
    List::Util
    Math::Bezier
    Math::BigFloat
    Math::Round
    Math::VecStat
    Memoize
    POSIX
    Params::Validate
    Pod::Usage
    Readonly
    Regexp::Common
    Set::IntSpan
    Storable
    Time::HiRes
    

Another script checks for the current status of each module (still from the
same dir)

    
    
    /Applications/circos-0.55/bin$ ./test.modules
    Circos: requirements
    ok   Carp
    fail Config::General is not usable (it or a sub-module is missing)
    ok   Data::Dumper
    ok   Digest::MD5
    ok   File::Basename
    ok   File::Spec::Functions
    ok   FindBin
    fail GD is not usable (it or a sub-module is missing)
    fail GD::Polyline is not usable (it or a sub-module is missing)
    ok   Getopt::Long
    fail Graphics::ColorObject is not usable (it or a sub-module is missing)
    ok   IO::File
    ok   List::MoreUtils
    ok   List::Util
    fail Math::Bezier is not usable (it or a sub-module is missing)
    ok   Math::BigFloat
    ok   Math::Round
    fail Math::VecStat is not usable (it or a sub-module is missing)
    ok   Memoize
    ok   POSIX
    ok   Params::Validate
    ok   Pod::Usage
    fail Readonly is not usable (it or a sub-module is missing)
    ok   Regexp::Common
    fail Set::IntSpan is not usable (it or a sub-module is missing)
    ok   Storable
    ok   Time::HiRes
    

We have to address everything that failed in the test. In this case, `GD`,
`Graphics::ColorObjects`, `Math::VecStat`, `Readonly` and `Set::IntSpan`. We
leave GD behind for a moment and focus on the other modules (this list might
vary for each Perl installation, so you might need to install more or less
modules, but the commands are similar).

The easiest way to install module in Perl is to use CPAN, the repository of
Perl modules. It has an interactive shell that we can use, and we will see how
to do that. In order to make sure our installation works we use sudo and call
cpan (from any directory)

    
    
    $ sudo cpan
    If this is the first time you are running it, just answer yes to all config questions 
    and you are good to go. Now we have to install the five modules required. 
    By using the command install, that can be achieved
    
    cpan$ install Config::General
    -output omitted-
    
    cpan$ install Graphics::ColorObject
    -output omitted-
    
    cpan$ install Math::Bezier
    -output omitted-
    
    cpan$ install Math::VecStat
    -output omitted-
    
    cpan$ install Readonly
    -output omitted-
    
    cpan$ install Set::IntSpan
    -output omitted-
    

Now, we deal with the last module and usually the most labourious to install,
`GD`. Ideally you should have all possible library support for `GD` and for
this you have to install additional libraries. We are going to start with two
of the most common and see if we need anything else. Usually `libjpeg` and
`libpng` are required by `GD`. So, let’s download both of them

    
    
    $ mkdir srctemp
    $ cd srctemp
    srctemp$ curl -O https://www.ijg.org/files/jpegsrc.v8d.tar.gz
    srctemp$ tar -xzvf jpegsrc.v8d.tar.gz
    srctemp$ cd jpeg-8d
    srctemp/jpeg-8d$ ./configure
    srctemp/jpeg-8d$ make
    srctemp/jpeg-8d$ sudo make install
    
    srctemp/jpeg-8d$ cd ..
    srctemp$ curl -O ftp://ftp.simplesystems.org/pub/libpng/png/src/libpng-1.5.10.tar.gz
    srctemp$ tar -xzvf libpng-1.5.10.tar.gz
    srctemp$ cd libpng-1.5.10
    srctemp/libpng-1.5.10$ ./configure
    srctemp/libpng-1.5.10$ make
    srctemp/libpng-1.5.10$ sudo make install
    

That should do it for now. We will download `GD` and check if the
configuration we have so far is enough. GD’s website is still down, but we can
get the source from Bitbucket and use identical commands to install is

    
    
    srctemp$ curl -O https://bitbucket.org/pierrejoye/gd-libgd/get/GD_2_0_33.tar.gz
    srctemp$ tar -xzvf GD_2_0_33.tar.gz
    srctemp$ cd pierrejoye-gd-libgd-5551f61978e3/src
    srctemp/pierrejoye-gd-libgd-5551f61978e3/src$ ./configure
    

At the end of the configuration run, you should see something like this

    
    
    ** Configuration summary for gd 2.0.33:
    
       Support for PNG library:          yes
       Support for JPEG library:         yes
       Support for Freetype 2.x library: yes
       Support for Fontconfig library:   yes
       Support for Xpm library:          no
       Support for pthreads:             yes
    

In my case, I’m good to go. But if in your case `Freetype` and `Fontconfig`
are missing, you would have to download, configure, make and install them,
just like `libpng` and `libjpeg`. So now

    
    
    srctemp/pierrejoye-gd-libgd-5551f61978e3/src$ make
    srctemp/pierrejoye-gd-libgd-5551f61978e3/src$ sudo make install
    

We are almost there. The last step is to install `GD` in Perl. Normally, if we
use cpan to install it on OS X, it fails. So, we will have to do it by hand.
We go to CPAN website and download the latest Perl’s GD implementation and
with similar commands to above we install it.

    
    
    srctemp$ curl -O https://search.cpan.org/CPAN/authors/id/L/LD/LDS/GD-2.46.tar.gz (if curl fails copy and past on your browser)
    srctemp$ tar -xzvf GD-2.46.tar.gz
    srctemp$ cd GD-2.46
    srctemp/GD-2.46$ perl Makefile.PL
    srctemp/GD-2.46$ make
    srctemp/GD-2.46$ sudo make install
    

you should see some output, maybe some warnings, but if you followed all the
steps above the installation worked. You can run the `test.modules` script in
order to check.

#### Installing Circos on Windows

Windows users should use Windows' built-in handling of `.tgz` files (in
Windows Vista or newer). The `.tgz` extension is a short version of `.tar.gz`,
which more explicitly indicates that the file is a `tar` archive which has
been subsequently compressed with `gzip`.

You can unpack the archive with 3rd party utilities like the free
[7-Zip](https://www.7-zip.org), or the venerable (but not free)
[WinZip](https://www.winzip.com).

If you are unfamiliar with the Windows DOS command line, these tutorials
should help.

  * [Windows command-line tutorial](https://www.bleepingcomputer.com/tutorials/tutorial76.html)
  * [Windows command-line prompt in 15 minutes](https://www.cs.princeton.edu/courses/archive/spr05/cos126/cmd-prompt.html)

### Running Circos

Circos uses command-line flags, which are required. In the very least, you
need to specify the image configuration file using `-conf`.

These flags in described in the [Runtime
Parameters](/documentation/tutorials/configuration/runtime_parameters)
tutorial.

#### UNIX

It's a good idea to add the `bin/` directory in the distribution to your
`PATH` so that you can run `bin/circos` from anywhere.

Assuming you have Circos in `ROOT=~/software/circos/current` as described
above, append this to your `~/.bashrc` or `~/.bash_profile`.

    
    
    export PATH=~/software/circos/current/bin:$PATH
    

You'll need to explicitly execute either `~/.bashrc` or `~/.bash_profile` for
this to take effect

    
    
    > . ~/.bashrc
    # or
    > . ~/.bash_profile
    

Finally, test that your `PATH` has been modified,

    
    
    > cd ~
    > echo $PATH
    ~/software/circos/current/bin: ...
    > which circos
    ~/software/circos/current/bin/circos
    

#### Windows

To run Circos, you'll need to invoke perl and pass the Circos script as an
argument, along with any command-line parameters

    
    
    C:>perl C:\path\to\circos\bin\circos [any command-line parameters]
    

Documentation uses UNIX paths and commands. On Windows, if you see instruction
to run a script, such as

    
    
    > tools/bin/binlinks ...
    

interpret it as

    
    
    C:>perl tools\bin\binlinks ...
    

Also note that on UNIX file paths use `/` as a separation (e.g. `/bin/env`)
and on Windows `\` is used (e.g. `C:\perl\bin\perl`).

References to command-line commands like `pwd` and `cat` are specific to UNIX.
It should be clear what is being attempted, such as reporting the current
working directory (`echo %cd%` on Windows) or listing a file (`echo` on
Windows).

### checking for missing perl modules

Check whether you have any missing modules

    
    
    > pwd
    ~/software/circos/current
    > bin/circos -modules
    ok       1.26 Carp
    ok       0.37 Clone
    ok       2.50 Config::General
    ok       3.33 Cwd
    ok      2.145 Data::Dumper
    ...
    

#### missing modules?

If any modules missing, refer to [Perl
Modules](/documentation/tutorials/configuration/perl_and_modules) tutorial for
details about installing them.

On Windows, both [Strawberry Perl](https://www.strawberryperl.com) and
[ActiveState Perl](https://www.activestate.com/activeperl) have package
managers that help you install, update and remove modules.

### `/bin/env`: no such file or directory

On UNIX, if you see an error like this when you try to run Circos

    
    
    -bash: /bin/env: No such file or directory
    

then the location of the `env` binary on your system is not `/bin/env`. For
example, on Mac OS X `env` is in `/bin/usr/env`.

First check where your `env` binary is

    
    
    > which env
    /usr/bin/env
    

Now either change the first line in `bin/circos` and `tools/*/bin` to

    
    
    #!/usr/bin/env perl
    

or (better) make a symlink from `/usr/bin/env` to `/bin/env`

    
    
    > sudo su
    > cd /bin
    > ln -s /usr/bin/env env
    

You should get a man page. On the other hand, if you get an error like

### using the example data set

If you don't yet have any data to use, you can play with running Circos using
the example data set, included in the distribution. The commands below are for
UNIX systems—for Windows, see `README`.

    
    
    > cd example
    
    # run.out will contain debug report
    # image files are circos.png and circos.svg
    > ./run
    
    # explicitly specify configuration file
    > ../bin/circos -conf etc/circos.conf
    # with more debugging
    > ../bin/circos -conf etc/circos.conf -debug_group summary,io,timer
    # with all debugging
    > ../bin/circos -conf etc/circos.conf -debug_group _all
    # silently
    > ../bin/circos -conf etc/circos.conf -silent
    

### Contents of Circos Distribution

When you download and unpack Circos, you'll have a directory structure as
follows

    
    
     circos-x.xx
      CHANGES
      README
      TODO
      bin/
      etc/
      fonts/
      lib/
      tiles/
      tools/
    

Tutorials are available separately and provide the files in

    
    
      data/
      tutorials/
    

#### bin/

The Circos script is located in this directory. Circos is written in Perl and
is comprised of a single executable file `bin/circos`.

#### data/

The distribution includes a large number of data files that are required by
the tutorials. Most of these data files are parsed versions of output of the
[UCSC Genome Viewer Table Browser](https://genome.ucsc.edu/cgi-bin/hgTables).
A few of the data files contain randomly generated data.

#### etc/

Circos global configuration files live here, such as `housekeeping.conf`,
`colors.conf` and `fonts.conf`. These files are imported into other
configuration files (e.g. tutorial configuration files).

The contents of the color and font files are described in the [Configuration
File section](/documentation/tutorials/configuration/configuration_files).

Tutorial configuration files are located in `tutorials/` (see below).

#### fonts/

TrueType (TTF) fonts used by Circos. These fonts are defined in
`etc/fonts.conf`. Circos supports only TTF fonts (not Postscript or OTF).

#### lib/

Code libraries. You don't need to look.

#### tiles/

Tiles for pattern fills.

#### tools/

Various helper tools for Circos to manipulate (e.g. count links with
`tools/binlinks`) and parse (e.g. tabular visualization using
`tools/tableviewer`) data.

#### tutorials/

Tutorials are available separately and are the documentation for Circos. Each
tutorial has an associated image and configuration `s`.

Tutorials are organized into groups and sections. Each group illustrates a
feature set of Circos, and individual sections illustrate the configuration
syntax for specific aspects of the feature set.

    
    
      tutorials/
       ...
       2/
        1/
        2/
         circos.conf
         ticks.conf
         ideogram.conf
        3/
        ...
       ...
    

All of the tutorial configuration files will import global configuration files
from `etc/`, such as `housekeeping.conf` and `colors_fonts_patterns.conf`.

