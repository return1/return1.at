Painful iframe resizing, or: how to fit ad banners into ajax heavy web sites with writeCapture
##############################################################################################
:date: 2010-11-02 11:56
:category: Javascript
:tags: ads, iframe, jquery, javascript
:slug: iframe-resizing-how-to-fit-ad-banner-ajax-websites-writecapture
:summary: The crux with online advertising.

The crux with online advertising
================================

The online advertising industry seems not quite up to date yet.
To my knowledge, no AJAX APIs are being so far provided, all services must be embedded as external javascripts,
executing several nested ``document.write()`` instructions. 
(The first JS loads a second one, which in turn loads another, often structured even further.)
For a web application where content is reloaded dynamically, this is a catastrophe because ``document.write()`` 
destroys the page after building the DOM, displaying just an empty page.

**iFrame solution?**
--------------------

This problem leads to amazing workarounds, like loading the ad in an iFrame.
Unfortunately, the iFrame does not know what kind of content the ad-supplier is going to  provide at some point. 
"Context sensitive" iFrames are called for, which can adapt to the external content's size. 
A simple and efficient jQuery method is the following:

.. raw:: html

    <script src="https://gist.github.com/4032581.js?file=jquery-ad-iframe-resize.js"></script>

iFrame size is simply checked every x seconds (every second in this example). 
Since it is impossible to determine correctly, easily and rapidly - and working in every browser - the moment when an
iFrame has finished loading its content, this is a legit solution, which of course only makes sense when you have just
a few of those iFrames on your page (apart from the fact that iFrames are "naughty" anyway).

**BUT**:

Rescue is at hand: just overwrite ``document.write()``. 
If it were indeed that easy, I would have done it myself, resp. there would have been functional solutions on the web
a long time ago. There is evidence that for several years, developers have `struggled`_ `with`_  such a solution for
all current browsers. It took me a while to find it, but the solution does exist, somewhere out there on the net.
`Newsweek.com`_ baptized it the "Jesus script". This may seem a bit lofty, but it's okay because it works and it saves
a lot of trouble:

**writeCapture**
----------------

:Github: 
	`http://github.com/iamnoah/writeCapture/`_ 
:my test:
	`http://return1.at/sandbox/writeCapture/`_ 

**Problems?** 

Problems just occur when the externally loaded ad-scripts depend on the ``load`` event,
because writeCapture intercepts ``document.write()`` instructions and executes them after the DOM has been established. 
But that will never happen, since the ``load`` event has already passed.
The day is saved by the call-back functionality of writeCapture, which can trigger the ``window.load()`` event once more.

.. _struggled: http://ajax.phpmagazine.net/2006/11/xhtml_and_documentwrite_replac.html
.. _with: http://www.intertwingly.net/blog/2006/11/10/Thats-Not-Write
.. _Newsweek.com: http://newsweek.com/
.. _`http://github.com/iamnoah/writeCapture/`: http://github.com/iamnoah/writeCapture/
.. _`http://return1.at/sandbox/writeCapture/`: sandbox/writeCapture/
