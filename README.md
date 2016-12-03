# Fact Checker Website

The fact checker website will be a portal for fact checkers to get urls to fact check

The work flow:

The fact checker signs into the website.
They are presented with a url (or possibly set of urls).
They click on one of the urls.
They are then redirected to the website where the url came from.
They read the url providing notes and feedback as to whether the article is factual and if there are inaccuraries what those inaccuraries are.

## Installation

The first thing you'll need to do is clone this repo, it's preferred that you fork it and then submit pull requests from your fork.  This way we have clear providence of who did what, but also, it will be easier to roll back changes, should something be wrong, before committing to the canonical master repository.

You'll need [Python 3](https://www.python.org/downloads/) (Python 3.5 is preferred), [pip3](https://pip.pypa.io/en/stable/) (1.8.2 is preferred), and the heroku toolbelt and a heroku account to deploy this repository.

After you install Python simply run:

`pip install -r requirements.txt` (which is found in the top level directory of the main repo)

If you have python 2 installed, you might need to do:

`pip3 install -r requirements.txt`

Everything regarding deploying to heroku should be in 

`setup.md` (in the base directory).

