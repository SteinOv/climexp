README file for the Climate Explorer.

Where is the code, where is the data, how can it be maintained, what tends to go wrong?

Please note that the Climate Explorer grew out of efforts to answer questions on the effects on the 1997/98 El Niño. It has never been designed, just grown, by a scientist. The code is somewhat commented, but until this document no specifications or documentation existed. Driven be necessity this file is an attempt to outline the gross features so that if somebody would take over maintenance (s)he would have a fighting chance.

There are 4 computers involved:
- gatotkaca, my MacBook running Mac OSX 11.3 is currently the development machine
- zuidzee.knmi.nl (currently pc200270.knmi.nl) with Fedora has most of the unchanging data (CMIP3, CMIP5, old seasonal hindcasts) and the KNMI data. This server also contains all the data that is updated monthly
- climexp.climexp-knmi.surf-hosted.nl with Ubuntu 18.04.3 LTS is the current server.
All code is (should) be mirrored among the development and machine and server via three projects on my KNMI GitLab account: climexp for the CGI scripts, climexp_numerical for the Fortran code and climexp_update for the data update scripts. For mirroring to my workstation I still use ancient scripts around gtar.


A. Where is the code?

1) Fortran code that does the actual computations, fairly heavily optimised, some work in progress (cross-validation, 3D sections, better error models).
Source code: GitLab climexp_numerical, old place NINO/Fortran/*.f90, a few C files.
Makefiles: The objects live in $(PVM_ARCH) (this is LINUX on the linux machines, NEXT on the Mac for historical reasons). The first Makefile jumps to this subdirectory, where specific flags for that environment are set and Makefile.common included that has the actual targets
Make process: first makes climexp.a, link main programs against this and netcdf, (old) Numerical or (new) FGSL / GSL Recipes.
All executables are installed to from climexp/bin/ with a "make install". This part is reasonably coded but needs to be parallelised.

2) CGI code that draw the web pages, processes the forms, calls the Fortran, draws the pictures. Most are in bash, a few modern ones (and one ancient one) in python, one still in ancient PERL (should be replaced very soon).
Source code: GitLab climexp, climexp/*.cgi (is actually a symlink to NINO/climexp/ for synch'ing purposes).
There is very little javascript in there, most generates plain HTML.
These scripts are not very well coded as they have been grown rather than designed, lots of global variables, some of which have been repurposed when new functionality was added so that the names do not make sense (especially the code to draw the titles above the plots is very hairy)

3) Wrappers around the Fortran code that store default values, apply the Fortran to each ensemble member etc: ~/climexp/bin/*.sh. These are almost all bash scripts.

4) Fortran code that retrieves time series from their native Format into the Climate Explorer standard format, usually called get*. The source code often lives in the data directory, the executable is link from climexp/bin/. The make process for these is not as sophisticated.

5) R code that computed verification indices in climexp/r, the data is first processed by Fortran into the required format, next handed over to R. The line plots are drawn in R itself, the maps are drawn by the standard Climate Explorer routine (currently GrADS, a drop-in replacement in NCL is in the Atlas section).

6) Update scripts are located in most data-directories NINO/*Data, a few reanalysis directories do not end in Data. These scripts also copy the data to the external server. In NINO/ itself there are two scripts that call the separate scripts for each data sources; update_10.sh is executed at the beginning of the month; update_25.sh around the 15th. These scripts fail regularly when datasets have been updated, location or formats changed.

A partial list of dependencies
- netcdff4, netcdf4
- Gnu Scientific Library for Fortran
- nco
- cdo
- grads
- gnuplot
plus the usual unix tools (sed, wc, gzip, ...). A full list of packages I had to install on Ubunutu is in the script Cloud/configure_ubunu.sh.

B. Where is the data?

The standard updates are automatic. If a dataset has moved, updated or changed location, it is necessary to
1) edit the update*.sh script and sometimes the Fortran code that is called from it
2) edit the table in selectfield_*.html
3) edit the "database" in queryfield.cgi that associates the key in selectfield*.html with a file, two names, optionally land/sea mask and frequency.

Frequency convention: the Climate Explorer counts how many intervals there are per year in the variable NPERYEAR:
1: annual data
2: bi-annual data: Oct-Mar and Apr-Sep
4: seasonal data: DJF, MAM, JJA, SON
12: monthly data: Jan, ..., Dec
36: decadal data (not used)
360: daily data in 360-day calender
365: daily data in 365-dy calendar (no-leap)
366: daily data in Gregorian calendar, Feb 29 is set to undefined in non-leap years.
Data arrays are in the form data(1:nperyear,yr1:yr2)

Add a new field:
1) create an update.sh that fetches the data and if necessary converts to netcdf
2) edit selectfield_obs.html to add it, including a reference to the data source
3) edit queryfield.cgi to associate the key with file, two names and optional properties.

Add a new time series:
1) create an update.sh that fetches the data and if necessary converts to netcdf or Climate Explorer ASCII format.
2) edit selectindex.cgi (or one of the other scripts) to add name and filename and possibly other properties

A section that does not currently work is the opendap virtual directories under "External data". This can probably be fixed by upgrading to the latest netcdf4 library, which the system people will not do & I did not have time for.


C. Things that go wrong

1) Full disks. Data is stored in climexp/data for three days after last use, this is so large it very rarely fills up. Some scripts and notably opendap store data in /tmp/ and /var/tmp, these are so small that they can cause a full disk and failure of the Climate Explorer so in fact they have been moved to the data disk and symlinked. There are two commands to clean up disks (and possibly kill jobs that depend on the data):
- http://climexp.knmi.nl/cleanup_tmp.cgi cleans the /tmp and /var/tmp directories that are most often the cause of problems
- http://climexp.knmi.nl/cleanup.cgi is the general grim reaper script that is run every nihgt to enforce the 3-day limit, but can be invoked at other times as well.

2) A failed update script because the data has moved, been upgraded to a new version or changed in format (or all three at times). Usually a user complains that dataset XXX no longer works. The output of the general update script is in NINO/*.log on the zuidzee (except KNMIData), this normally gives a clue. A visit to the web site that the [i] after the dataset points to also often gives a clue. Update the update-script in the data directory...

3) Bit rot in the Fortran or CGI scripts. This happens a lot to me as I continually improve the code, but should be no problem when you do not touch it.
