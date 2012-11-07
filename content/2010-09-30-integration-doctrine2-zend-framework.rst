Integration of Doctrine2 and Zend Framework
###########################################
:date: 2010-09-30 11:54
:category: PHP
:tags: autoloader, doctrine, zend framework
:slug: integration-doctrine2-zend-framework
:wide: true

*Update*: Meanwhile, Doctrine2 is stable, integration into Zend
Framework has slightly changed. I have incorporated the changes into the
article.

Integrating Doctrine2 into Zend Framwork (1.11) has
cost me some time. Enough to write about it, and maybe make it easier
for others. 

The procedure is actually easy:

#. download Zend Framework and Doctrine2
#. create project e.g. via Zend\_Tool :

   ::

       zf create project quickstart

#. link Zend Framework and Doctrine libraries with the newly created
   project, either via symlink in the library folder, or just copy and
   paste
#. configure web server

In case of problems with the above steps, Zend Framework's `quickstart
guide`_ is recommendable. `Doctrin's install guide`_ helps with
installing Doctrine2. My problem was with integrating the Doctrine2
autoloader into the Zend Framework autoloader.I was able to make it work
with support from the web. First the relevant excerpt from
bootstrap.php, in this context it is important that the application
namespace is configured before the doctrine namespace, sources are
inserted in the comments:

.. raw:: html

    <script src="https://gist.github.com/4032609.js?file=bootstrap.php"></script>

then you simply build a model:

.. raw:: html

    <script src="https://gist.github.com/4032609.js?file=Controller.php"></script>

and use it in an action, voila! (first create the table in the database
;) )

.. raw:: html

    <script src="https://gist.github.com/4032609.js?file=Model.php"></script>

.. _quickstart guide: http://framework.zend.com/manual/en/learning.quickstart.create-project.html
.. _Doctrin's install guide: http://www.doctrine-project.org/docs/orm/2.0/en/reference/introduction.html#github
