# Contributing


## Dependencies

We use [poetry](https://github.com/python-poetry/poetry) to manage dependencies.

To install them you would need to run `install` command:

```bash
poetry install
```

Also, let's install `pre commit hooks` in `git`:
```bash
poetry run pre-commit install
```

To activate your `virtualenv` run `poetry shell`.


## One magic command

Run `make test` to run everything we have!

Also, because of conflict between `pytest-testmon` and `pytest-cov` we use option `--no-cov` in `make test`, so in this way
we give prioritize to `pytest-testmon`. If you want to generate report with `pytest-cov`, use `make test ci=1`.


## Tests

We use `black`, `flake8` and `pytest` for quality control.

To run formatter:

```bash
black .
```

To run linter (it checks only docstrings, [more info](http://www.pydocstyle.org/en/latest/error_codes.html)):
```bash
flake8 .
```

To run all tests:

```bash
pytest
```

If you want to customize util's parameter, you should do this in `setup.cfg`.
These steps are mandatory during the CI.


## Type checks

We use `mypy` to run type checks on our code:

```bash
mypy .
```

This step is mandatory during the CI.


## Other help

You can contribute by spreading a word about this library. It would also 
be a huge contribution to write a short article on how you are using this 
project. You can also share your best practices with us.
