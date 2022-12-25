# Contributing

This file is describing our code style and some other documentation about contributions. You must read it before your
first contribution.

Also note that this all is just recommendations, you can use anything in some cases, if it will be better than solution
that we propose here. However, we will prefer these recommendations when we will review your contribution.

## Language

All contributions, all code, all comments, all commits and everything else **must** be in English. 

## Commit naming style

Every commit must have **one** small change. We also use the [Tim Pope commit message template](https://tbaggery.com/2008/04/19/a-note-about-git-commit-messages.html)
for commits' messages.

If you worry about clean `git log` - just don't. We use squash strategy for merging PRs.

## `make test`

This "magic" command collects almost all of our CI. If you're on Windows, try [Chocolatey](https://chocolatey.org) to
run `make`.

Also, because of conflict between `pytest-testmon` and `pytest-cov` we use option `--no-cov` in `pytest`, so in this
way we give prioritize to `pytest-testmon`. If you want to generate a report with `pytest-cov`, use `make test ci=1`.

## Other Help

You can contribute by spreading a word about this library. It would also be a huge contribution to write a short article
on how you are using this project. You can also share your best practices with us.
