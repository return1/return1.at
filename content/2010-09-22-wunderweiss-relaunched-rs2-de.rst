wunderweiss relaunched rs2.de
#############################
:date: 2010-09-22 11:51
:category: Projects
:tags: kronehit, rs2, silverstripe, zend framework
:slug: wunderweiss-relaunched-rs2-de

`wunderweiss`_ has performed the technical relaunch of `RS2 - Berlin, 94,3 RS2
- Der Supermix`_. Like `Kronehit`_, this site relies heavily on Ajax, in
order to have the radio station's web player continue playing during new
page requests. The relaunch was based on `Zend Framework`_ and
`Silverstripe`_. 

What I find interesting is the new approach to
communication between the two frameworks. In the Kronehit project, data
was read directly from Silverstripe's SQL tables, which has proved to be
not overly maintenance-friendly. At `Matthias Schelling's`_ urging, a
new approach was developed for RS2: XMLify. Thereby, a query is put to
Silverstripe via Zend Framwork and HTTP GET requests, Silverstripe
responds with the desired data in XML format. 

This approach is many
times more flexible and straightforward, those who are acquainted with
the structure of Silverstripe's tables know why. Besides, the
development can be encapsulated better, with XMLify you don't need much
knowledge about Silverstripe itself. I am curious whether this solution
will soon be available as a module. 

Good work!

.. _wunderweiss: http://wunderweiss.com/
.. _RS2 - Berlin, 94,3 RS2 - Der Supermix: http://rs2.de/
.. _Kronehit: http://test.return1.at/projects/kronehit/
.. _Zend Framework: http://framework.zend.com/
.. _Silverstripe: http://www.silverstripe.org/
.. _Matthias Schelling's: https://twitter.com/schellmax
