from setuptools import setup

with open('README.rst') as readme:
    r = str(readme.read())

setup(
    name='clpb',
    version='1.0.0',
    url='https://github.com/dmitriiweb/clpb',
    license='MIT',
    author='Dmitrii K',
    author_email='winston_smith_spb@gmail.com',
    description=' Command line progress bar for Python 3',
    long_description=r,
    classifiers=(
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ),
)
