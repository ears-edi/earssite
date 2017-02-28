EaRS Site Configuration Files
==============================

The University of Edinburgh Embedded and Robotics Society website source is here. The website is built using [Pelican](http://getpelican.com) 3.7.1. 

Prerequisites
-------------

 - Git
 - Python
 - Pelican >= 3.7
 - markdown

To install these, you can run the following commands:

```
sudo apt-get install python3 git
pip install pelican markdown
```

Getting Started
---------------

**Clone the repository**

You can do this your preferred way, or if you've never done it before, head to the directory above where you want the site files to be stored and then run:

`git clone https://github.com/ears-edi/earssite`

This will create a folder called earssite and place all of the content in the repository in there. 

**Generating site**

To generate the static site itself, just run `pelican` in the `earssite` directory.

**Contributing to ears-edi.github.io**

If you are developing with the intention of publishing to ears-edi.github.io then make sure to clone the [pages repo](https://github.com/ears-edi/ears-edi.github.io) into `earssite` before you run `pelican`.

```
cd earssite
git clone https://github.com/ears-edi/ears-edi.github.io
```

This way you can just push any changes from that repo and they will appear on the actual site.

Tips
----

While developing, try running `pelican -r` in a separate terminal. This will rebuild the site every time you make a change.

Pelican comes by default with a development server. You can start it using `develop-server.sh` but this will put the server in the background of your session and any time a request comes in it will spam your terminal which can mess with whatever you are doing currently. It can be better to run `python -m pelican.server` in the output directory in a separate terminal. This will show you all requests coming in and will serve whatever is in the directory, so doesn't need to be restarted on code changes.
