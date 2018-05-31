import sys

if sys.version_info < (2, 3):
    raise RuntimeError("Python 2.3 or later is required")


from distutils.core import setup

setup(
    name='generatepass',
    version='1.0',
    author='Vitaly Doroshko',
    author_email='vdoroshko@mail.ru',
    url='https://github.com/vdoroshko/generatepass',
    license='BSD',
    description='Generate passwords and PIN numbers',
    platforms=['any'],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.3',
        'Programming Language :: Python :: 2.4',
        'Programming Language :: Python :: 2.5',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Topic :: Security',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
    keywords=['generator', 'password'],
    py_modules=['generatepass']
)
