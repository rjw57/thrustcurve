# thrustcurve: Python amateur rocketry file formats

[![Build
Status](https://travis-ci.org/rjw57/thrustcurve.svg)](https://travis-ci.org/rjw57/thrustcurve)
[![Coverage
Status](https://coveralls.io/repos/rjw57/thrustcurve/badge.svg?branch=master&service=github)](https://coveralls.io/github/rjw57/thrustcurve?branch=master)
[![Documentation
Status](https://readthedocs.org/projects/thrustcurve/badge/?version=latest)](http://thrustcurve.readthedocs.org/en/latest/?badge=latest)


Thrustcurve is a Python module designed to make it easy to parse amateur
rocketry file formats.

## Installation

Install from PyPI via:

```console
$ pip install thrustcurve
```

Install from Git via:

```console
$ pip install git+https://github.com/rjw57/thrustcurve
```

## Documentation

More documentation is available at
http://thrustcurve.readthedocs.org/en/latest/.

## Usage example

The following IPython session demonstrates fetching and parsing a RockSim (.rse)
format file:

```ipython
In [1]: import requests

In [2]: rse_data = requests.get('http://www.thrustcurve.org/download.jsp?id=1800').text

In [3]: import thrustcurve

In [4]: engines = thrustcurve.loads(rse_data)

In [5]: engines
Out[5]: [<thrustcurve.Engine at 0x7f7c5e06da20>]

In [6]: e = engines[0]

In [7]: e.comments
Out[7]: 'Pro29-1G 56F120-VM 14A'

In [8]: e.manufacturer, e.code
Out[8]: ('CTI', 'F120-VM')

In [9]: e.data
Out[9]: 
     time    force       mass
0   0.000    0.000  31.400000
1   0.013   79.242  31.109700
2   0.017   90.427  30.918400
3   0.040  101.422  29.674800
4   0.125  127.583  24.188700
5   0.179  136.114  20.175400
6   0.222  139.905  16.830400
7   0.289  143.507  11.478700
8   0.354  138.578   6.311020
9   0.394  125.498   3.333960
10  0.406  123.602   2.491490
11  0.416  125.118   1.790500
12  0.423  130.047   1.287100
13  0.431  120.569   0.722036
14  0.447   25.592   0.062938
15  0.453    8.720   0.004915
16  0.455    0.000   0.000000
```
