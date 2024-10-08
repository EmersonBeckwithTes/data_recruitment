# Data Engineering Sample Project

This is a sample project to cover some data engineering concepts; we're going to 
extract some data, transform it and save it locally.

## Setup
This project will not require any tools beyond any python installation of
version 3.9 or greater, [Poetry](https://python-poetry.org/) for packaging and an IDE/text editor of your choosing.

## Installation
### Poetry
`poetry install`

### Pip with venv (if not using Poetry)
```
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Running Code
1. Edit SQL in `tes_recruitment/edit_this.sql`

2. Run
    - Poetry:  `poetry run python tes_recruitment/main.py`

    - Pip with venv: `python tes_recruitment/main.py`

## Considerations
This is a very basic example, but should have the same thoughts and considerations as 
would be applied to a production, real-world project. As such it should include the
tests, documentation, and any modularity or extensibility that you would develop for
a real project, as well as follow any coding standards or best practices and styles or
formatting that you would submit in a production pull request.

## Instructions

### Extract

Target endpoint is `https://restcountries.com/v3.1/all`.

### Transform

Take part of the response object to be saved in a local flat file (exact details to be shared
during live exercise).
