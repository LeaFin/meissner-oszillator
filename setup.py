from distutils.core import setup

setup(
    name='meissner-oszillator',
    version='0.1.1',
    author='L.Finger, M.Brodmann',
    packages=['meissner_oszillator'],
    url='http://github.com/LeaFin/meissner-oszillator',
    description='Meissner oszillator simualtion',
    long_description='Meissner oszillator simualtion',
    license='BSD License',
    install_requires=[
        "PyOpenGL == 3.0.2",
        "numpy == 1.8.1",
        "visvis == 1.9",
        "wsgiref == 0.1.2"
    ],
)
