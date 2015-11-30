"""
The :py:mod:`thrustcurve` module contains functions and objects designed to
be useful to those parsing rocket motor thrust curve files.

"""
import contextlib
import codecs
import io
import xml.etree.ElementTree as ET

import numpy as np
import pandas
from past.types import basestring

class ParseError(RuntimeError):
    """Raised when an input file could not be parsed."""

def load(fn_or_fobj):
    """Load a RockSim (.rse) format engine database.

    Args:
        fn_or_fobj (str or file like object): file containing .rse format data

    Returns:
        A list of :py:class:`.Engine` instances, one per engine in the file.

    Raises:
        ParseError: if the file is of the wrong format

    """
    with _as_file_obj(fn_or_fobj) as f:
        tree = ET.parse(f)
    root = tree.getroot()
    _assert_tag(root, 'engine-database')
    engine_list = _find_or_throw(root, 'engine-list')

    return [
        _engine_from_element(e) for e in engine_list.iter('engine')
    ]

def loads(string):
    """Load engine data from string.

    Like :py:func:`load` except that the parameter is the textual content of the
    file as a string.

    """
    return load(io.BytesIO(codecs.encode(string, 'utf8')))

_ENGINE_DF_COLUMNS = ['time', 'force', 'mass']

class Engine(object):
    """Class representing a rocket engine.

    The rocket engine thrust curve is contained within the *data* attribute.
    This is a :py:class:`pandas.DataFrame` instance with the columns "time"
    (seconds), "force" (Newtons) and mass (kg).

    See also: the `Pandas documentation`_.

    .. _Pandas documentation: http://pandas.pydata.org/pandas-docs/stable/10min.html

    Attributes:
        manufacturer (str or None): manufacture of rocket
        code (str or None): manufacturer's code for this engine
        comments (str or None): additional comments
        data (pandas.DataFrame): thrust curve data

    """
    def __init__(self, manufacturer=None, code=None):
        self.manufacturer = manufacturer
        self.code = code
        self.comments = None
        self.data = None

def _engine_from_element(elem):
    engine = Engine(
        manufacturer=elem.get('mfg', None),
        code=elem.get('code', None)
    )
    engine.comments = elem.findtext('comments', None).strip()
    data = _find_or_throw(elem, 'data')

    data_items = []
    for eng_data in data.iter('eng-data'):
        data_items.append(tuple(
            np.float(eng_data.get(k, np.nan)) for k in ['t', 'f', 'm']
        ))
    engine.data = pandas.DataFrame.from_records(
        data_items, columns=_ENGINE_DF_COLUMNS
    )

    return engine

@contextlib.contextmanager
def _as_file_obj(fn_or_fobj, mode='rb'):
    if isinstance(fn_or_fobj, basestring):
        f = open(fn_or_fobj, mode)
        yield f
        f.close()
    else:
        yield fn_or_fobj

def _assert_tag(e, name):
    if e.tag != name:
        raise ParseError('Expected tag {} to be {}'.format(e, name))

def _find_or_throw(e, name):
    f = e.find(name)
    if f is None:
        raise ParseError(
            'Could not find expected child {} of {}'.format(name, e)
        )
    return f
