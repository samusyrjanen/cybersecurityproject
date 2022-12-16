# Memo project

This web application stores memos created by users. Users can register and login to create new memos and see their previous memos.

## Installation instructions

Clone the repository into your computer:
```
git clone git@github.com:samusyrjanen/cybersecurityproject.git
```

Make sure you have Django installed.
For other requirements, see pyproject.toml:
```
cat pyproject.toml
```

Install dependencies:
```
poetry install
```

Initialize database:
```
python3 myproject/notepad/initialize_database.py
```

Start a local server:
```
python3 myproject/manage.py runserver
```

Navigate to the site that is given.
To stop the server, press ctrl + c.
