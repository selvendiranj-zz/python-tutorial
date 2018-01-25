[![Build Status][travis-img]][travis-url]
[![Coverage Status][coverall-img]][coverall-url]
[![Weppy Version](https://img.shields.io/badge/weppy-1.1-blue.svg)](https://github.com/gi0baro/weppy)


# Py Web
 
A [Weppy](http://weppy.org) application.

hello world python web application

## Run

**Requirements**:
- Python 3.6.1+

For virtualenv setup and activation:

```
virtualenv --python=$(which python3.6) env
. ./env/bin/activate
pip install -r requirements.txt
python run.py
```

Otherwise:

```
pip install -r requirements.txt
python run.py
```

***If pip fails on ubuntu, try `sudo apt-get install libyaml-dev libyaml-python3.6-dev`**

### Docker

To make your application available at ```http://localhost/```:

```
docker build -t py-web .
docker run -it -p 80:8000 --rm --name py-web py-web
```


## Develop

Running in development mode will enable debug pages and
automatically create test users in multiple states.
Test users will be removed from the DB after stopping.

To start the app in development mode, do:

```
python run.py --dev
```

See ```py-web/cli.py``` for cli commands. 

## Test

```
py.test -v -s --cov-report term-missing --cov=py-web -r w tests
```


## License

[MIT](LICENSE) 2017 selvendiranj


[travis-img]: https://travis-ci.org/selvendiranj/py-web.svg?branch=master
[travis-url]: https://travis-ci.org/selvendiranj/py-web
[coverall-img]: https://coveralls.io/repos/github/selvendiranj/py-web/badge.svg?branch=master
[coverall-url]: https://coveralls.io/github/selvendiranj/py-web?branch=master
