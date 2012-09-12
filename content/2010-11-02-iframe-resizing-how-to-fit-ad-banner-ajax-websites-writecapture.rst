Painful iframe resizing or how to fit ad banners into ajax heavy web sites with writeCapture
############################################################################################
:date: 2010-11-02 11:56
:category: Javascript, jQuery
:tags: ads, iframe, jquery
:slug: iframe-resizing-how-to-fit-ad-banner-ajax-websites-writecapture

Or: The crux with online advertising
====================================

The online advertising industry is seemingly not yet up to date. To my
knowledge, so far no AJAX APIs are provided, all services have to be
embedded into one's website as external java scripts, which execute
several nested ``document.write()`` instructions. (The first JS loads a
second one, which in turn loads another JS, often with even deeper
structures). For a web application, where content is reloaded
dynamically, this is catastrophic because ``document.write()`` after
building the DOM destroys the page, displaying e.g. just an empty white
page.

**iFrame solution?**
--------------------

This problem leads to amazing workarounds , like e.g. loading the
advertisement in an iFrame. The trouble with that, however, is that the
iFrame does not know what kind of content the ad-suppliers may provide
at some point. A "context sensitive" iFrame is needed, i.e. it adapts to
the size of the external content. A simple and efficient method by
jQuery is the following:

.. sourcecode:: javascript

    //auto-resizing ad-banners
    var resizeInterval = window.setInterval(function () {
        $iframe = $('#bigbanner iframe');
        $iframe.attr('width', '100%').attr('height', '100%'); //reset
        $doc = $($iframe.get(0).contentWindow.document);
        $iframe.attr('width', $doc.width()).attr('height', $doc.height());
    }, 1000);

Thereby, the iFrame's size is simply checked every x seconds (in this
example every second). Since it is not possible to determine correctly,
with rapid and simple means - and functionally in every browser - when
an iFrame has finished loading its content (please post it if you know
an efficient method!), this is a legitimate solution which is of course
only sensible when you have just a few of those iFrames on your page
(apart from the fact that iFrames are "naughty" anyway). 

**BUT**:

Rescue is at hand: simply overwrite ``document.write()``. Simple? If it were, I
would have done it myself, resp. there would have been functional
solutions on the web a long time ago. Hints can be found that developers
have been `struggling`_ `with`_ the difficulty of finding such a
solution for all current browsers for several years. But in the web's
abysses the solution exists, for which I had to quest a really long
time. `Newsweek.com`_ baptized the script "Jesus script", a little
pathetically, but I can understand the emotion because it works and
saves a lot of work and trouble:

**writeCapture**
----------------

:Github: 
	`http://github.com/iamnoah/writeCapture/`_ 
:my test:
	`http://return1.at/sandbox/writeCapture/`_ 

**Problems?** 

Problems occur only when the externally loaded ad-scripts build on the ``load`` event,
because writeCapture intercepts ``document.write()`` instructions and
executes them after the DOM has been established. But for that it can
wait a very long time indeed, since the ``load`` event has already passed.
Relief is produced by the call-back functionality of writeCapture, in
which the ``window.load()`` event can just be triggered again.


.. _struggling: http://ajax.phpmagazine.net/2006/11/xhtml_and_documentwrite_replac.html
.. _with: http://www.intertwingly.net/blog/2006/11/10/Thats-Not-Write
.. _Newsweek.com: http://newsweek.com/
.. _`http://github.com/iamnoah/writeCapture/`: http://github.com/iamnoah/writeCapture/
.. _`http://return1.at/sandbox/writeCapture/`: sandbox/writeCapture/
