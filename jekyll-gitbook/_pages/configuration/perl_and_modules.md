---
author: DoubleCat
date: 2025-04-11
layout: post
category: configuration
title: Required Perl Modules
---

## Required Perl Modules
### lesson
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

To run Circos, you need [Perl](https://www.perl.org). Perl, like languages
such as Python or Ruby, is an interpreted language. This means that you do not
need to compile the Circos code — it is read in by the Perl executable (that
ships with, or has been installed, for your operating system), which in turn
interprets it, compiles it and runs the code.

#### Checking for Perl
##### Checking for Perl on UNIX
For UNIX and Mac OS X users, Perl is likely already installed on your system,
as part of the base installation.

To check this, run this command at the terminal

```    
    > which perl
```
If you have perl installed and the executable is in your `PATH` (it is
unlikely that Perl is installed but not in your `PATH`, the `which` command
will return something like

```    
    > which perl
    /usr/bin/perl
    # or perhaps
    /usr/local/bin/perl
```
or some other location, depending on your installation. If the `which` command
returns nothing, it's likely that you do not have Perl installed.

To check the version of installed Perl

```    
    > perl -v
    This is perl, **v5.10.0** built for ...
```
Anything earlier than 5.8 should be upgraded.

Circos will use the perl binary in your `PATH`. If you are on a UNIX system,
whatever `which` returns

```    
    > which perl
```
will be the interpreter that is used.

##### managing multiple perl installations on UNIX
You can have installations of various versions of Perl, helpful if you want to
test out a new version without disturbing production versions.

For example, I have Perl 5.8, 5.10, 5.14 and 5.18 installed in

```    
    ~/perl/perl.5.8.7
    ~/perl/perl.5.10.0
    ~/perl/perl.5.14.2
    ~/perl/perl.5.18.1
```
To easily call any of these versions, I have symbolic links set up from
`~/bin`, which is in my `PATH`

```    
    ~/bin/perl58  -> ~/perl/perl/5.8.7/bin/perl
    ~/bin/perl510 -> ~/perl/perl/5.10.0/bin/perl
    ~/bin/perl514 -> ~/perl/perl/5.14.2/bin/perl
    ~/bin/perl518 -> ~/perl/perl/5.18.1/bin/perl
```
For example,

```    
    # use Perl 5.10
    > perl510 script.pl
    # use Perl 5.14
    > perl514 script.pl
```
My production Perl is 5.14.2, so

```    
    ~/bin/perl -> ~/bin/perl514
```
which calls Perl 5.14 when I use the `perl` command.

```    
    # run the production version, Perl 5.14
    > perl script.pl
```
If you are managing multiple versions of Perl, you'll need to install modules
for each version of Perl you have installed. This is inconvenient but required
because the modules compiled by one version may not be compatible with
another.

Using the CPAN shell makes installation relatively painless. Make sure you
call it with the right version!

```    
    # install with production version, Perl 5.14
    > perl -MCPAN -e shell
    ...
    cpan[1]> install Config::General
    
    # install with 5.10
    > perl510 -MCPAN -e shell
    ...
    cpan[1]> install Config::General
```
You can also use `cpanminus`. On Ubuntu, use `apt-get`

```    
    # if you need cpanminus
    sudo apt-get install cpanminus
    # now install any missing modules
    sudo cpanm Clone Config::General Font::TTF::Font GD GD::Polyline Math::Bezier Math::Round Math::VecStat 
               Params::Validate Readonly Regexp::Common SVG Set::IntSpan Statistics::Basic Text::Format
```
##### Checking for Perl on Windows
If you are running Windows, it is unlikely that you have Perl installed. Perl
installation is described in the [Perl and
Modules](/documentation/tutorials/configuration/perl_and_modules) section.

To check the version of installed Perl,

```    
    C:> perl -v
    This is perl, **v5.10.0** built for ...
```
#### Installing Perl Modules
Even if you already have perl, chances are good that you are going to need a
few additional modules to make Circos run. Perl modules are third-party code
that adds functionality to the core language.

Your installation of Perl will include [core
modules](https://perldoc.perl.org/index-modules-A.html). In addition to these,
you'll likely need to install some modules, such as

```    
    [Config::General](https://search.cpan.org/~tlinden/Config-General-2.51/General.pm) (v2.50 or later)
    [Font::TTF](https://search.cpan.org/~mhosken/Font-TTF-1.02/)
    [GD](https://search.cpan.org/~lds/GD-2.46/GD.pm)
    [List::MoreUtils](https://search.cpan.org/~adamk/List-MoreUtils-0.33/lib/List/MoreUtils.pm)
    [Math::Bezier](https://search.cpan.org/~abw/Math-Bezier-0.01/Bezier.pm)
    [Math::Round](https://search.cpan.org/~grommel/Math-Round-0.06/Round.pm)
    [Math::VecStat](https://search.cpan.org/~aspinelli/Math-VecStat-0.08/VecStat.pm)
    [Params::Validate](https://search.cpan.org/~drolsky/Params-Validate-1.07/lib/Params/Validate.pm)
    [Readonly](https://search.cpan.org/~roode/Readonly-1.03/Readonly.pm)
    [Regexp::Common](https://search.cpan.org/~abigail/Regexp-Common-2011121001/lib/Regexp/Common.pm)
    [Set::IntSpan](https://search.cpan.org/~swmcd/Set-IntSpan-1.16/IntSpan.pm) (v1.16 or later)
    [Text::Format](https://search.cpan.org/~shlomif/Text-Format-0.58/lib/Text/Format.pm)
```
To list all the required modules and check whether they are installed, use
`-modules`.

```    
    > circos -modules
    ok       1.26 Carp
    ok       0.37 Clone
    ok       2.50 Config::General
    ok       3.33 Cwd
    ok      2.145 Data::Dumper
    ok       2.52 Digest::MD5
    ok       2.76 File::Basename
    ok       3.33 File::Spec::Functions
    ok       0.22 File::Temp
    ok       1.49 FindBin
    ok       0.39 Font::TTF::Font
    ok       2.43 GD
    ok        0.2 GD::Polyline
    ok       2.37 Getopt::Long
    ok       1.14 IO::File
    ok       0.33 List::MoreUtils
    ok       1.38 List::Util
    ok       0.01 Math::Bezier
    ok       1.59 Math::BigFloat
    ok       0.06 Math::Round
    ok       0.08 Math::VecStat
    ok    1.01_02 Memoize
    ok       1.13 POSIX
    ok       0.95 Params::Validate
    ok       1.36 Pod::Usage
    ok       1.03 Readonly
    ok 2010010201 Regexp::Common
    ok       2.49 SVG
    ok       1.16 Set::IntSpan
    ok     1.6607 Statistics::Basic
    ok       2.30 Storable
    ok       1.11 Sys::Hostname
    ok       2.02 Text::Balanced
    ok       0.53 Text::Format
    ok     1.9725 Time::HiRes
```
##### Installing Perl Modules on UNIX
To install these modules, use the [CPAN
module](https://search.cpan.org/~andk/CPAN-1.9600/lib/CPAN.pm) to quickly
download, compile and install them. CPAN will follow dependencies and
generally do the right thing. Windows users should use their Perl's
installation package manager (see below).

```    
    > perl -MCPAN -e shell
    ...
    cpan[1]>install Math::Bezier
    ...
```
If the process above fails, or you prefer to do it yourself, download each
module from [CPAN](https://search.cpan.org). Many [module installation
tutorials](https://perldoc.perl.org/perlmodinstall.html) are already
available.

Modules use either the `Makefile.PL` system, or the
[Build](https://search.cpan.org/~dagolden/Module-
Build-0.3800/lib/Module/Build.pm) system. For purposes here, these are
equivalent but require slightly different commands.

To install a module that uses the `Makefile.PL` system, such as
[Set::IntSpan](https://search.cpan.org/~swmcd/Set-IntSpan-1.16/IntSpan.pm).

```    
    # download module
    > wget https://search.cpan.org/CPAN/authors/id/S/SW/SWMCD/Set-IntSpan-1.16.tar.gz
    # unpack archive
    > tar xvfz Set-IntSpan-1.16.tar.gz
    > cd Set-IntSpan-1.16
    # configure and compile
    > **perl Makefile.PL**
    Checking if your kit is complete...
    Looks good
    Writing Makefile for Set::IntSpan
    > **make**
    cp IntSpan.pm blib/lib/Set/IntSpan.pm
    Manifying blib/man3/Set::IntSpan.3
    > **make test**
    >» make test
    PERL_DL_NONLAZY=1 /home/martink/perl/5.10.0/bin/perl "-MExtUtils::Command::MM" 
       "-e" "test_harness(0, 'blib/lib', 'blib/arch')" t/*.t
    t/binary.t .... ok       
    t/bsearch.t ... ok       
    ...
    t/spans.t ..... ok       
    t/subclass.t .. ok     
    t/unary.t ..... ok     
    All tests successful.
    Files=18, Tests=1931,  0 wallclock secs ( 0.28 usr  0.03 sys +  0.36 cusr  0.06 csys =  0.73 CPU)
    Result: PASS
    # install (keep in mind file permission requirements, as described below)
    > **make install**
```
Modules like [Params::Validate](https://search.cpan.org/~drolsky/Params-
Validate-0.95/) use the [Build
system](https://search.cpan.org/~dagolden/Module-
Build-0.3800/lib/Module/Build.pm) and are installed as follows.

```    
    # download module
    > wget https://search.cpan.org/CPAN/authors/id/D/DR/DROLSKY/Params-Validate-0.95.tar.gz
    # unpack archive
    > tar xvfz Params-Validate-0.95.tar.gz
    > cd Params-Validate-0.95
    # configure and compile
    > **perl Build.PL**
    Creating new 'MYMETA.yml' with configuration results
    Creating new 'Build' script for 'Params-Validate' version '0.95'
    > **./Build**
    Building Params-Validate
    cc -Ic -I/home/martink/perl/5.10.0/lib/5.10.0/x86_64-linux/CORE -DXS_VERSION="0.95" 
       -DVERSION="0.95" -fPIC -c -fno-strict-aliasing -pipe -D_LARGEFILE_SOURCE 
       -D_FILE_OFFSET_BITS=64 -I/usr/include/gdbm -O2 -o lib/Params/Validate.o lib/Params/Validate.c
    ExtUtils::Mkbootstrap::Mkbootstrap('blib/arch/auto/Params/Validate/Validate.bs')
    cc -shared -O2 -o blib/arch/auto/Params/Validate/Validate.so lib/Params/Validate.o
    > **./Build test**
    t/01-validate.t ............ ok     
    t/02-noop.t ................ ok     
    t/03-attribute.t ........... ok    
    ...
    t/30-hashref-alteration.t .. ok   
    t/kwalitee.t ............... skipped: This test is only run for the module author
    t/pod-coverage.t ........... skipped: This test is only run for the module author
    t/pod.t .................... skipped: This test is only run for the module author
    All tests successful.
    Files=32, Tests=497,  1 wallclock secs ( 0.10 usr  0.04 sys +  0.78 cusr  0.13 csys =  1.05 CPU)
    Result: PASS
    # install (keep in mind file permission requirements, as described below)
    > **./Build install**
```
##### Installing Perl Modules on Mac OS X
CPAN should work seamlessly. Many users have difficulty with the GD module,
which has numerous dependencies. Paulo Nuin has a nice blog entry that shows
how he [handled his Mac OS X Circos
installation](https://zientzilaria.heroku.com/blog/2012/06/03/installing-
circos-on-os-x/).

##### Installing Perl Modules on Windows
Both [Strawberry Perl](https://www.strawberryperl.com) and [ActiveState
Perl](https://www.activestate.com/activeperl) have package managers that help
you install, update and remove modules. Where possible, use the manager to
install modules instead of the CPAN shell.

#### Installing `libpng`, `freetype`, `libgd` and `GD`
About half of the support questions in the [Google
Group](https://groups.google.com/forum/#!forum/circos-data-visualization) are
about installing Perl's `GD` module, which is the interface to the `libgd`
system graphics library.

The installation process is not robust because of dependencies and the
possibility of their being different versions of these dependencies on your
system. Below I show the process of installing `GD` on a new Mac OS Mavericks
system (10.9.4).

Below I link to my local copies of the versions of each library that I
installed. These are mature libraries and newer versions are likely to be
minor bug releases. The exception is `GD`—I was unable to successfully compile
v2.56 (`boot_GD` symbol warning which I could not fix). However v2.53 worked.

```    
    > tar xvfz [libpng-1.6.14.tar.gz](/distribution/lib/libpng-1.6.14.tar.gz)
    > cd libpng-1.6.14
    > ./configure —prefix=/usr/local
    > make
    > make install
    
    > tar xvfz [jpegsrc.v9.tar.gz](/distribution/lib/jpegsrc.v9.tar.gz)
    > cd jpeg-9
    > ./configure —prefix=/usr/local
    > make
    > make install
    
    > tar xvfz [freetype-2.4.0.tar.gz](/distribution/lib/freetype-2.4.0.tar.gz)
    > cd freetype-2.4.0
    > ./configure —prefix=/usr/local
    > make
    > make install
```
You should now have libraries in `/usr/local/lib` as we as some header files
in `/usr/local/include`.

```    
    -rwxr-xr-x  1 root  wheel   650336 21 Nov 11:15 libfreetype.6.dylib
    -rw-r--r--  1 root  wheel  3676456 21 Nov 11:15 libfreetype.a
    lrwxr-xr-x  1 root  wheel       19 21 Nov 11:15 libfreetype.dylib -> libfreetype.6.dylib
    -rwxr-xr-x  1 root  wheel      957 21 Nov 11:15 libfreetype.la
    -rwxr-xr-x  1 root  wheel   275736 21 Nov 11:14 libjpeg.9.dylib
    -rw-r--r--  1 root  wheel  1492952 21 Nov 11:14 libjpeg.a
    lrwxr-xr-x  1 root  wheel       15 21 Nov 11:14 libjpeg.dylib -> libjpeg.9.dylib
    -rwxr-xr-x  1 root  wheel      920 21 Nov 11:14 libjpeg.la
    lrwxr-xr-x  1 root  wheel       10 21 Nov 11:13 libpng.a -> libpng16.a
    lrwxr-xr-x  1 root  wheel       14 21 Nov 11:13 libpng.dylib -> libpng16.dylib
    lrwxr-xr-x  1 root  wheel       11 21 Nov 11:13 libpng.la -> libpng16.la
    -rwxr-xr-x  1 root  wheel   240580 21 Nov 11:13 libpng16.16.dylib
    -rw-r--r--  1 root  wheel  1077240 21 Nov 11:13 libpng16.a
    lrwxr-xr-x  1 root  wheel       17 21 Nov 11:13 libpng16.dylib -> libpng16.16.dylib
    -rwxr-xr-x  1 root  wheel      924 21 Nov 11:13 libpng16.la
    drwxr-xr-x  6 root  wheel      204 21 Nov 11:15 pkgconfig/
```
Now install `libgd`, linking to the libraries installed above

```    
    > tar xvfz [libgd-2.1.0.tar.gz](/distribution/lib/libgd-2.1.0.tar.gz)
    > cd libgd-2.1.0
    > ./configure --with-png=/usr/local --with-freetype=/usr/local --with-jpeg=/usr/local —prefix=/usr/local
    
    …
    ** Configuration summary for libgd 2.1.0:
    
       Support for Zlib:                 yes
       Support for PNG library:          yes
       Support for JPEG library:         yes
       Support for VPX library:          no
       Support for TIFF library:         no
       Support for Freetype 2.x library: yes
       Support for Fontconfig library:   no
       Support for Xpm library:          no
       Support for pthreads:             yes
    …
    
    > make
    > make install
```
You now have libgd in `/usr/local/lib`

```    
    -rwxr-xr-x  1 root  wheel   389372 19 Nov 14:47 libgd.3.dylib
    -rw-r--r--  1 root  wheel  1217200 19 Nov 14:47 libgd.a
    lrwxr-xr-x  1 root  wheel       13 19 Nov 14:47 libgd.dylib -> libgd.3.dylib
    -rwxr-xr-x  1 root  wheel     1139 19 Nov 14:47 libgd.la
```
as well as some binaries in `/usr/local/bin`. In particular, you have
`/usr/local/bin/glib-config`, which provides the configuration for your libgd
installation

The `--with-*` parameters during the `configure` stage of `gdlib` installation
sets the sources of the dependencies that will be build into `gdlib`. If you
used a different `-prefix` in compiling these dependencies (see above), adjust
these parameters accordingly. For example, if you compiled `libpng` with
`-prefix=/my/path` then use `--with-png=/my/path/`.

```    
    > /usr/local/bin/gdlib-config —all
    
    GD library  2.1.0
    includedir: /usr/local/include
    cflags:     -I/usr/local/include
    ldflags:     -L/usr/local/lib
    libs:       -ljpeg -lz  -L/usr/local/lib -lpng16 -L/usr/local/lib -lfreetype -lz -liconv
    libdir:     /usr/local/lib
    features:   GD_JPEG GD_FREETYPE GD_PNG GD_GIF GD_GIFANIM GD_OPENPOLYGON
```
You must have `GD_FREETYPE` and `GD_PNG` for Circos to run. The other
features, such as support for JPEG and TIFF are optional. In this example,
I’ve included the JPEG library in the installation.

Now, install the Perl interface to libgd — the GD module.

```    
    > tar xvfz [GD-2.53.tar.gz](/distribution/lib/GD-2.53.tar.gz)
    > perl Makefile.PL
    
    Configuring for libgd version 2.1.0.
    Checking for stray libgd header files...none found.
    
    Included Features:          GD_JPEG GD_FREETYPE GD_PNG GD_GIF GD_GIFANIM GD_OPENPOLYGON
    GD library used from:       /usr/local
    Checking if your kit is complete...
    Looks good
    Writing Makefile for GD
    Writing MYMETA.yml and MYMETA.json
    
    During the installation GD will look for libgd-config (see above) for libgd configuration. 
    
    > make
    > make install
    
    > perl -MGD -e 'print $GD::VERSION,”\n”’
    > 2.53
```
Test that the modules are installed using

```    
    > circos -modules
    …
    ok       0.39 Font::TTF::Font
    ok       2.53 GD
    ok        0.2 GD::Polyline
    ok       2.39 Getopt::Long
    ok       1.16 IO::File
    …
```
#### Errors
##### Missing modules
If you are missing a module, you'll see an error like the following when you
run Circos.

```    
    *** REQUIRED MODULE(S) MISSING ***
    
    You are missing one or more Perl modules, or these modules failed to load. Use CPAN to install it as described in this tutorial
    
    https://www.circos.ca/documentation/tutorials/configuration/perl_and_modules
    
    missing List::MoreUtils
```
In the rare case that the internal error checking doesn't catch the missing
module, you'll see something like this.

```    
    Can't locate **List/MoreUtils.pm** in @INC (@INC contains: /usr/lib/perl5/5.14.2/i386-linux
    -thread-multi/usr/lib/perl5/5.14.2/usr/lib/perl5/site_perl/5.14.2/i386-linux-thread-multi
    /usr/lib/perl5/site_perl/5.14.2 /usr/lib/perl5/site_perl/usr/lib/perl5/vendor_perl
    /5.14.2/i386-linux-thread-multi /usr/lib/perl5/vendor_perl/5.14.2/usr/lib/perl5/vendor_
    perl .) at ./bin/circos line 121.
```
In this case Perl is complaining that the module `List::MoreUtils` cannot be
found, which you'll need to install.

##### Permission errors
On UNIX systems, if during installation you obtain a file or directory
creation permission error, you are likely attempting to write the module files
into your system's perl install tree which is owned by root (administrative
user).

```    
    ...
    Running make test
    PERL_DL_NONLAZY=1 /usr/bin/perl "-MExtUtils::Command::MM" "-e"  
    "test_harness(0, 'blib/lib', 'blib/arch')" t/*.t
    t/run....ok
    All tests successful.
    Files=1, Tests=68,  1 wallclock secs ( 0.27 cusr +  0.26 csys =  0.53  
    CPU)
       /usr/bin/make test -- OK
    Running make install
    **mkdir /usr/local/share/man: Permission denied at /System/Library/Perl/**
    5.8.8/ExtUtils/Install.pm line 112
    make: *** [pure_site_install] Error 13
       /usr/bin/make install  -- NOT OK
```
Repeat the installation as root (administrator)

```    
    > sudo su
    > perl -MCPAN -e shell
    ...
```
#### `make` on Mac OS X
If modules won't install because your system complains that it doesn't have
`make`.

```    
    bash: make command not found
```
you need to install [Xcode](https://developer.apple.com/xcode) development
tools, an optional component available on your Mac OS X DVD. Be aware that
there have been [reports of Xcode 4 causing problems with
Perl](https://www.perlmonks.org/?node_id=896789).

To test whether you have make

```    
    > which make
    /usr/bin/make
```
Sometimes an unsuccessful make can be due to an error during the compilation.

```    
    Could not make: Unknown error
```
If you know you have Xcode (`which make` confirms this typically as
`/usr/bin/make`), but are having trouble installing the module with CPAN,
install (or attempt to, paying close attention to the errors) the module
manually.

For example, if `Params::Validate` was giving problems,

```    
    > wget https://search.cpan.org/CPAN/authors/id/D/DR/DROLSKY/Params-Validate-0.95.tar.gz
    > tar xvfz Params-Validate-0.95.tar.gz
    > cd Params-Validate-0.95
    > ./Build
    # pay attention to any the build errors in the next step
    > Build make
```### images
### configuration
