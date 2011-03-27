# Themes by Me

## About
This is (or will be) a collection of themes I've made for various projects. 
I'm in the process of converting layouts for various projects into themes 
that can be managed through this repo.

## How It Works
The repository is set up so that it can basically be dropped into a project 
and used right away with just a few extra template tags dropped in to match 
the application.

There is a small build script written in Python that will set up layouts 
based on any of the themes.

For example, to build all available layouts for the "nice" theme:

    $ python build.py buildall nice

To list available layouts for a theme:

    $ python build.py list nice


