import os
import pytest
import thrustcurve

def _open_data_file(path, mode='rb'):
    data_dir = os.path.join(os.path.dirname(__file__), 'data', path)
    return open(data_dir, mode)

def _assert_close(a, b, epsilon=1e-7):
    assert abs(a - b < epsilon)

@pytest.fixture
def engine1():
    with _open_data_file('engine1.rse') as f:
        return thrustcurve.load(f)[0]

def test_simple_parse():
    with _open_data_file('engine1.rse') as f:
        engines = thrustcurve.load(f)
    assert len(engines) == 1

def test_engine_has_manufacturer(engine1):
    assert engine1.manufacturer == 'CTI'

def test_engine_has_code(engine1):
    assert engine1.code == 'F120-VM'

def test_engine_has_comments(engine1):
    assert engine1.comments == 'Pro29-1G 56F120-VM 14A'

def test_engine_has_times(engine1):
    _assert_close(engine1.data['time'].iloc[-2], 0.453)

def test_engine_has_forces(engine1):
    _assert_close(engine1.data['force'].iloc[-2], 8.72)

def test_engine_has_masses(engine1):
    _assert_close(engine1.data['mass'].iloc[-2], 0.00491524)

def test_loads(engine1):
    with _open_data_file('engine1.rse', 'r') as f:
        data_str = f.read()
    e = thrustcurve.loads(data_str)[0]
    assert (e.data == engine1.data).all().all()
