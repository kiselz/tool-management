# tool-management
A task for swedex application

# Running The Project
```console
# setting up the virtual environment
python3 -m venv venv

# activating the environment
source ./venv/bin/activate

# installing all needed packages
pip3 install -r requirements.txt

# initalizing the database (create tables and add admin user)
make init-db

# starting the server
make run
```
Aftet that you can type `https://127.0.0.1:PORT` in your browser to see the site.

# Project Strucutre
+ `src`: the folder that contains all the source code
+ `src/database`: the database package. All database methods are in `dp.py`, the schema of db is `schema.sql` and one helper function in `utils.py`
+ `src/server`: the server package
+ `src/server/main.py`: the module for setting up the server and running it up
+ `src/server/util.py`: utils module for helper functions
+ `src/server/blueprints`: Flask's blueprints (see [here](https://flask.palletsprojects.com/en/2.3.x/blueprints/) for more info)
+ `src/server/static`: Static files such as css and javascript files
+ `src/server/templates`: html views

# Application Stack
Flask + SQLite3 + Bootstrap + Plain JS

# API Endpoints
All API Endpoints expect a POST request with JSON object in the body. If some of the expected keys are missing an error message is sent back. None of these require an authentication or cookie header.

+ `api/user/take_tool`: Take a tool for the user. 
Expected json:
```json
{
    firstname (str): Firstname of the user,
    toolname (str): Tool's name to take,
    ammount (int): Ammount to take
}
```
If an user or tool does not exist, no changes will be made

+ `api/user/return_tool`: Return the tool
```json
Expected json:
{
    firstname (str): Firstname of the user
    toolname (str): Tool's name to return
    ammount (int): ammount of the tool to return
}
```
If an user or tool does not exist, no changes will be made

+ `api/user/add`: Add new user
Expected json:
```json
{
    firstname (str): the user's firstname
}
```

+ `api/user/delete`: Delete the user
Expected json:
```json
{
    firstname (str): Firstname of the user to delete
}
```
If the user does not exit, no changes will be made

+ `api/user/tool_ammount`: Change how many tools are acquired by the user
Expected json:
```json
{
    firstname (str): firstname of the user,
    toolname (str): tool's name,
    ammount (str): ammount of the tool,
}
```
If an user or tool does not exist, no changes will be made. If ammount is negative then `0` will be set

+ `tool/add`: Add new tool
Expected json:
```json
{
    toolname (str): tool's name to add
}
```

+ `tool/delete`: Delete the tool
Expected json:
```json
{
    toolname (str): tool's name to delete
}
```
If the tool does not exit, no changes will be made.