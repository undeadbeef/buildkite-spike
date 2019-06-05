# buildkite spike
Just a random collection of scripts which help test **buildkite**
builds, plugins and extensions.

# Common Instructions
Since we use [`pipenv`](https://github.com/pypa/pipenv), dependencies
must be installed before running the scripts using:
```
$ pipenv install
```
Additionally, when running the scripts you need to wrap the command
line with `pipenv run`. For example:
```
$ pipenv run python start-build-agent.py
```
