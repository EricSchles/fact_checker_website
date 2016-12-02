# Fake News Detector Backend

This repository's main purpose is to accept connections from the fake news detector browser extension.  It then stores all urls collected.  And finally will pass them to the fact checker website [github repo found here](https://github.com/EricSchles/fact_checker_website)

## Installation

The first thing you'll need to do is clone this repo, it's preferred that you fork it and then submit pull requests from your fork.  This way we have clear providence of who did what, but also, it will be easier to roll back changes, should something be wrong, before committing to the canonical master repository.

You'll need [Python 3](https://www.python.org/downloads/) (Python 3.5 is preferred), [pip3](https://pip.pypa.io/en/stable/
installing/) (1.8.2 is preferred), and the heroku toolbelt and a heroku account to deploy this repository.

After you install Python simply run:

`pip install -r requirements.txt` (which is found in the top level directory of the main repo)

If you have python 2 installed, you might need to do:

`pip3 install -r requirements.txt`

Everything regarding deploying to heroku should be in 

`setup.md` (in the base directory).

