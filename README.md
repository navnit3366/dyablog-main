# 👿 dyablog
*[Django](https://www.djangoproject.com/) + Blog = `dyablog`*

An inconsequential blog built on Django, vaguely following the instructions of ~~a soon-to-be four-year-old [YouTube tutorial](https://youtu.be/F5mRW0jo-U4?t=11258)~~ the official Django 4.1 [introduction/tutorial](https://docs.djangoproject.com/en/4.1/intro/).

> Warning: The dyablog-project *barely* even qualifies as a proof-of-concept, and should not be used in any serious capacity. If you go through the effort to set this up and run it and find yourself a bug, I'd be honored by a report!

This project is mainly a personal exercise in proper python project management as outlined in [Alex Mitelman](https://twitter.com/alex_mitelman)'s article ["Python Best Practices for a New Project in 2021"](https://mitelman.engineering/blog/python-best-practice/automating-python-best-practices-for-a-new-project/) through the use of tools such as **`pyenv`** and **Poetry**.
*(this is in contrast to my earlier dependency-free, largely version-agnostic [`sudoku-solver`](https://github.com/0xBA5E64/Sudoku-Solver) project)*

See also the ["wiki"](docs/wiki.md) document for additional project information and instructions.

## Dependencies*
- [`pyenv`](https://github.com/pyenv/pyenv) - Python version manager
  - Python `3.10.7` installed
- [Poetry](https://python-poetry.org/) - Python Package and Dependency manager
- [TailwindCSS](https://tailwindcss.com/)'s [CLI tool](https://tailwindcss.com/docs/installation).
  - Available through npm: `npm install -D tailwindcss @tailwindcss/typography`
  - -or [Standalone](https://tailwindcss.com/blog/standalone-cli) (with all first-party extensions included)

\*All remaining project dependencies are managed by Poetry, and are automatically installed through `poetry install`.

## Getting Started
Double-check you fulfill all dependencies listed above, then;
```sh
$ pyenv install 3.10.7 # Install the project's current Python version
$ git clone https://github.com/0xBA5E64/dyablog # Clone the repository
$ cd dyablog # Enter the project directory
$ poetry shell # Open shell in poetry's virtual enviroument
$ poetry install # Install python project dependencies
$ python ./manage.py collectstatic # Populate project static files
$ python ./manage.py migrate # Generate initial empty database
$ python ./manage.py createsuperuser # Create an admin account
$ code . # Open project in vscode.
$ tailwind -i ./blog/static/blog/style.css -o ./blog/static/blog/tailwind.css -w & ./manage.py runserver # start the development server *with* Tailwind CSS
```
