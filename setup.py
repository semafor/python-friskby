from setuptools import setup

DEPENDENCIES = ['requests', 'pyserial', 'python-dateutil']

setup(
    name='friskby',
    version='0.65.1',
    description='The friskby module',
    url='http://github.com/FriskbyBergen/python-friskby',
    author='Friskby Bergen',
    keywords='friskby bergen frisk by python-friskby a-small-code air',
    author_email='pgdr@statoil.com',
    license='GNU General Public License, Version 3',
    packages=['friskby', 'friskby/sensors'],
    zip_safe=False,
    setup_requires=DEPENDENCIES,
    install_requires=DEPENDENCIES
)
