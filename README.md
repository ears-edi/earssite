EaRS Site Configuration Files
==============================

The University of Edinburgh Embedded and Robotics Society website source is here. The website is built using [Pelican](http://getpelican.com) 3.7.1. 

Getting Started
---------------

Firstly you need to install Pelican. Assuming you have python and pip installed, run the following command:

`pip install pelican markdown`

This will install both Pelican and the markdown extension that allows us to write posts in it.

The next step is to clone this repository. You can do this your preferred way, or if you've never done it before, head to the directory above where you want the site files to be stored and then run:

`git clone https://github.com/ears-edi/earssite`

This will create a folder called earssite and place all of the content in the repository in there. If it errors, try installing git.

To generate the static site itself, just run `pelican` in the `earssite` directory.

If you are developing on the main site itself then make sure to clone the [pages repo](https://github.com/ears-edi/ears-edi.github.io) into earssite before you run `pelican`. This way you can just push any changes and they will appear on the actual site.

Tips
----

While developing, try running `pelican -r` in a separate terminal. This will rebuild the site every time you make a change.
