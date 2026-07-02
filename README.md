This projects demonstrates how to use the modern python framework fastapi to perform crud operations.
prerequisites
  You will need the following locally installed in your machine to be able to run and demonstrate the crud operations
    -->Python3
    -->Pydantic
    -->FastApi
    -->Uvicorn
    -->Python environment
    -->Pip package manager
You can use a folder structure like this to successfully run this project and demontrate the crud operation

FastApi(parent-folder)
  >app
  >python env

Steps of successfully running this project
1. Inside the parent folder create a python env using this command python3 -m venv your_env(input a random name)
2. Navigate into the python env and activate it using this command source/scripts/bin/activate
3. Inside the python env install fastapi and all its packages using this command pip install "fastapi[all]" -- this will install pydantic, fastapi, and other packages
4. Navigate back to the parent folder and you can now run your project using this uvicorn command uvicorn app.main:app --reload --port 8000 - this will open the project in port 8000 , just add /docs to the port opened and swagger ui will open up and you can perform the crud operations
(Note that the above commands are linux based commands - you will use other commands for other OS)


