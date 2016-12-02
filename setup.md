#Steps to setting up heroku w/ Flask

1. Write the flask app
 * set up `__init__.py` (as defined in `app/__init__.py`)
 * set up the views.py (as defined in `app/views.py`)
 * set up the models.py (as defined in `app/models.py`)
 * set up the manager.py (as defined in `manager.py`)
 * set up the run_server.py (as defined in `run_server.py`)
 * set up the requirements.txt (as defined in `requirements.txt`)
 * set up the Procfile (as defined in `Procfile`)

2. Set up the github repo
 * remote setup
 	* set up the remote repository via the + button on github.com
 * in the local (from the root level directory of the repository)
    * `git init`
    * `git add --all`
    * `git commit -m "first commit"`
    * `git remote add origin git@github.com:UserName/repository_name.git`
    * `git push -u origin master`  
* for all future commits:
	* `git add --all` or files to push
	* `git commit -m "what was done since last push"`
	* `git push`
3. Sign up for Heroku
 * install the heroku cli
 * login to heroku w/ `heroku login` from the root level directory of your repo
 * `heroku create`
 * `heroku git:remote -a name_of_heroku_app` (given as part of running heroku create)
 * `git push heroku master`
 * `heroku open`
 * if this fails, run - `heroku logs` (to figure out what the error is)
 * you can also test this locally with `heroku local`
 * you might end up trying to do `git push heroku` and it might fail, in such a case, `git push heroku -f` appears to work.

4. Setting up database
  * `heroku addons:create heroku-postgresql:hobby-dev`
  * `heroku pg:promote DATABASE_URL` - (this is defined in the above step by Created postgresql-globular-71299 as DATABASE_URL - specifically whatever is in place of postgresql-globular-71299)
  * `createdb testing`
  * `python manager.py db init`
  * `python manager.py db migrate`
  * `python manager.py db upgrade`
  * `heroku run python`
  	* `from app import db`
  	* `db.create_all()`
