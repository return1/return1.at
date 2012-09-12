Analyze and tweak your apache2 mpm settings
###########################################
:date: 2011-11-24 08:43
:category: Server
:tags: apache, perl, ubuntu
:slug: apache2-analyze-tweak-mpm-perl-script

Recently I stumbled over a handy perl script, which analyzes your
currently running apache clients and helps you with tweaking your MPM
settings based on calculations:

.. sourcecode:: perl

    #!/usr/bin/perl
    # Copyright Erik Jacobson - erik@underhanded.org

    use warnings; use strict;
    use Statistics::Descriptive;

    my $webuser = 'www-data'; # The user your apache children run as.  I ignore the root process.
    my $command = 'apache2'; # The name of your processes as they appear to the "top" command.

    my @top = `top -bn1`;
    my %header;
    my $mem = Statistics::Descriptive::Full->new();
    my $othermem = Statistics::Descriptive::Full->new();
    my $totalmem;

    foreach (@top)
    {
            s/^\s+|\s+$//sg;
            my @line = split(/\s+/, $_);

            if(/mem:\s+(\S+)\s+total/i)
            {
                    $totalmem = convtok($1);
            }

            if(defined $line[3] && exists $header{res} && $line[0] =~ /^\d++$/)
            {
                    next unless (defined $line[$header{user}] && defined $line[$header{res}]
                            && defined $line[$header{shr}] && defined $line[$header{command}]);

                    if(($line[$header{user}] eq $webuser) && ($line[$header{command}] eq $command))
                    {
                            $mem->add_data(convtok($line[$header{res}]) - convtok($line[$header{shr}]));
                    } else {
                            $othermem->add_data(convtok($line[$header{res}]) - convtok($line[$header{shr}]));
                    }
            } elsif (!exists $header{res})
            {
                    my %tempheader;
                    for (0 .. $#line)
                    {
                            $tempheader{lc($line[$_])} = $_;
                    }

                    if(defined $tempheader{user} && defined $tempheader{res}
                            && defined $tempheader{shr} && defined $tempheader{command})
                    {
                            %header = %tempheader;
                    }
            }
    }

    printf "Total memory available: %.2fG\n", ($totalmem / 1024 / 1024);
    printf "Total used by $command (%d instances): %.2fG\n", $mem->count(), ($mem->sum() / 1024 / 1024);
    printf "Total used by other processes: %.2fG\n\n", ($othermem->sum() / 1024 / 1024);

    $totalmem -= $othermem->sum();

    printf "Average memory used per $command process: %.2fM\n", ($mem->mean() / 1024);
    printf "Recommended number of processes based on Average: %d\n", ($totalmem / $mem->mean());
    printf "Needed memory for 500 processes based on Average: %.2fG\n\n", ($mem->mean() / 1024 / 1024 * 500);

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