Problems installing monit and munin on Ubuntu
#############################################
:date: 2012-03-15 11:04
:category: Server
:tags: ubuntu, munin, mysql
:slug: problems-installing-monit-and-munin-on-ubuntu

To monitor mysql, you need to activate the mysql pid file creation. In
``/etc/mysql/my.cnf``, in the ``[mysqld]`` section add

.. sourcecode:: console

    pid-file = /var/run/mysqld/mysqld.pid

To run munin with apache and mysql monitoring, you need to install two
perl modules.

.. sourcecode:: console

    aptitude install libwww-perl libcache-cache-perl

Or else ``munin-node-configure --suggest`` will report ``LWP::UserAgent not
found`` and ``Missing dependency Cache::Cache``