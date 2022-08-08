# Biosignature Database


The Biosignature Database is an initiative to build a standardized, accessible, and consistent database among the astrobiology community.

Data Source: manual entries from research papers

![App preview](biosignatureDB.gif)

# Startup the project

The initial setup.

Create virtualenv and install the project:
```bash
sudo apt-get install virtualenv python-pip python-dev
deactivate; virtualenv ~/venv ; source ~/venv/bin/activate ;\
    pip install pip -U; pip install -r requirements.txt
```

Unittest test:
```bash
make clean install test
```

Check for biosignature_db in gitlab.com/{group}.
If your project is not set please add it:

- Create a new project on `gitlab.com/{group}/biosignature_db`
- Then populate it:

```bash
##   e.g. if group is "{group}" and project_name is "biosignature_db"
git remote add origin git@github.com:{group}/biosignature_db.git
git push -u origin master
git push -u origin --tags
```

Functionnal test with a script:

```bash
cd
mkdir tmp
cd tmp
biosignature_db-run
```

# Install

Go to `https://github.com/{group}/biosignature_db` to see the project, manage issues,
setup you ssh public key, ...

Create a python3 virtualenv and activate it:

```bash
sudo apt-get install virtualenv python-pip python-dev
deactivate; virtualenv -ppython3 ~/venv ; source ~/venv/bin/activate
```

Clone the project and install it:

```bash
git clone git@github.com:{group}/biosignature_db.git
cd biosignature_db
pip install -r requirements.txt
```
Run the app (locally on your machine):

```
cd biosignature_db
python app.py
```
Running the python file will open a window in your default browser (or copy/paste the URL that poped up in your terminal).
