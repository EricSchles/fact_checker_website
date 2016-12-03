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

To migrate the database, please see:

`manager.py` (in the base directory).

## Contribution

To contribute to this application, please fork from the canonical master and create pull requests.

To configure a remote for a fork:
    * `git remote add upstream https://github.com/EricSchles/fact_checker_website.git`
    * For more: https://help.github.com/articles/configuring-a-remote-for-a-fork/

To sync a fork
    * `git fetch upstream`
    * `git pull`
    * `git checkout master` (or whatever branch)
    * For more: https://help.github.com/articles/syncing-a-fork/

To make a pull request
    * `git pull origin master`
    * Go to main repository and create a pull request

### Troubleshooting

## Unable to create db

If you try creating a db:
 * `createdb news_admin`

    and you get:

    ```
    createdb: could not connect to database template1: could not connect to server: No such file or directory
        Is the server running locally and accepting
        connections on Unix domain socket "/tmp/.s.PGSQL.5432"?
    ```

Try: 
* `pg_ctl -D /usr/local/var/postgres -l /usr/local/var/postgres/server.log start`

## Unable to install pyscopg2 

Try installing xcode-setup and re-run the Installation
Please see here: https://www.moncefbelyamani.com/how-to-install-postgresql-on-a-mac-with-homebrew-and-lunchy/

