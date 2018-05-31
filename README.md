# generatepass

The **generatepass** module provides functions to generate passwords and PIN numbers.

## Prerequisites

Python 2.3 or later.

## Installation

### Installing With pip

The easiest way to install the latest version of the module is to use the `pip` tool:

```
$ pip install --upgrade https://github.com/vdoroshko/generatepass/tarball/master
```

### Installing From Source

Alternatively, you can install the module from the source distribution. The steps below will guide you through the process.

 1. Create a directory for the module files and enter it:

    ```
    $ mkdir generatepass
    $ cd generatepass
    ```

 2. Download the module tarball using `wget` utility:

    ```
    $ wget -O generatepass.tar.gz https://github.com/vdoroshko/generatepass/tarball/master
    ```

    Alternatively, you can use the `curl` tool to download the module tarball:

    ```
    $ curl -L -o generatepass.tar.gz https://github.com/vdoroshko/generatepass/tarball/master
    ```

 3. Extract the tarball and install the module:

    ```
    $ tar -xzf generatepass.tar.gz --strip=1
    $ python setup.py install
    ```

## Usage Examples

Generate a random password 10 characters long consisting of ASCII alphanumeric characters (excluding similar looking characters):

```python
>>> from generatepass import generatepass
>>> generatepass()
'm4x94acEez'
```

Generate a random password 8 characters long consisting of ASCII alphabetic characters (including similar looking characters):

```python
>>> from string import letters
>>> from generatepass import generatepass
>>> generatepass(8, letters, exclude_similar_chars=False)
'ChnPIlrh'
```

Generate a 4-digit PIN number:

```python
>>> from generatepass import generatepin
>>> generatepin()
'4282'
```

Generate a 6-digit PIN number:

```python
>>> from generatepass import generatepin
>>> generatepin(6)
'108970'
```

## Module Contents

generatepass.**generatepass**(*length=10, chars=string.ascii_letters+string.digits, exclude_similar_chars=True*)
> Generates a password of the specified length and consisting of the given characters.  The optional argument *exclude_similar_chars* determines whether the password should not contain similar looking characters.

generatepass.**generatepin**(*length=4*)
> Generates a PIN number of the specified length.

generatepass.**SIMILAR_CHARS**
> String of ASCII characters which are considered having similar look.

## License

Licensed under the [BSD 3-Clause License](http://opensource.org/licenses/BSD-3-Clause).

## Author

Vitaly Doroshko (vdoroshko@mail.ru)
