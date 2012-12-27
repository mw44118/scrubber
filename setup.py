from setuptools import find_packages, setup

setup(

    name='scrubber',

    version='0.0.1',

    description="Web data validation",

    author='W. Matthew Wilson',
    author_email='matt@tplus1.com',
    url='http://scrubber.readthedocs.org',
    license='BSD',

    packages=find_packages('src'),

    include_package_data=True,

    package_dir={'': 'src'},

    py_modules=['scrubber'],

    install_requires=[
    ],

)
