Analyze and tweak your apache2 mpm settings
###########################################
:date: 2011-11-24 08:43
:category: Server
:tags: apache, perl, ubuntu
:slug: apache2-analyze-tweak-mpm-perl-script
:wide: true
:summary: A handy perl script, which analyzes your
          currently running apache clients and helps you with tweaking your MPM
          settings based on calculations.

Recently I stumbled over a handy perl script, which analyzes your
currently running apache clients and helps you with tweaking your MPM
settings based on calculations:

.. raw:: html

   <script src="https://gist.github.com/4031588.js?file=apache2-mpm-tweak.pl"></script>

The script outputs looks like this:

.. sourcecode:: console

    Total memory available: 7.80G
    Total used by apache2 (97 instances): 2.66G
    Total used by other processes: 2.57G

    Average memory used per apache2 process: 28.03M
    Recommended number of processes based on Average: 191
    Needed memory for 500 processes based on Average: 13.69G

    Max memory used for apache2 process: 45.22M
    Recommended number of processes based on Max: 118
    Needed memory for 500 processes based on Max: 22.08G

    Mean plus two Standard Deviations (bulk of usage under max): 43.11M
    Recommended number of processes based on Mean + 2*Stdev: 124
    Needed memory for 500 processes based on Mean + 2*Stdev: 21.05G