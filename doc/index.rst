Thrustcurve documentation
-------------------------

Thrustcurve is a Python module designed to make it easy to parse amateur
rocketry file formats.

Example usage
=============

The following example shows loading a RockSim format file from
http://www.thrustcurve.org/ into a Pandas DataFrame object:

.. plot::
   :include-source:

   import requests
   import thrustcurve
   import matplotlib.pyplot as plt

   rse_data = requests.get('http://www.thrustcurve.org/download.jsp?id=1800').text
   engines = thrustcurve.loads(rse_data)

   e = engines[0]

   plt.figure()
   plt.plot(e.data['time'], e.data['force'], '-or')
   plt.xlabel('Time [s]')
   plt.ylabel('Force [N]')
   plt.grid()
   plt.title('Force/time curve for {} {}'.format(e.manufacturer, e.code))

   plt.figure()
   plt.plot(e.data['time'], e.data['mass'], '-or')
   plt.xlabel('Time [s]')
   plt.ylabel('Mass [kg]')
   plt.grid()
   plt.title('Force/mass curve for {} {}'.format(e.manufacturer, e.code))

Reference
=========

.. automodule:: thrustcurve
   :members:

