# Copyright (c) 2006-2018 Vitaly Doroshko.
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are
# met:
#
# 1. Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
#
# 2. Redistributions in binary form must reproduce the above copyright
#    notice, this list of conditions and the following disclaimer in the
#    documentation and/or other materials provided with the
#    distribution.
#
# 3. Neither the name of the copyright holder nor the names of its
#    contributors may be used to endorse or promote products derived
#    from this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
# A PARTICULAR PURPOSE ARE DISCLAIMED.  IN NO EVENT SHALL THE COPYRIGHT
# HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
# SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
# LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
# DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
# THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

"""Generate passwords and PIN numbers"""

__author__ = 'Vitaly Doroshko <vdoroshko@mail.ru>'
__version__ = '1.0'

import random
import string
import sys
import types

# Similar looking characters
SIMILAR_CHARS = '01IOl'

if sys.version_info < (3, 0):
    _translation_table = string.maketrans(str(), str())
else:
    _translation_table = dict(zip(SIMILAR_CHARS, [None]*len(SIMILAR_CHARS)))


def generatepass(length=10, chars=string.ascii_letters+string.digits,
                 exclude_similar_chars=True):
    """Generates a password of the specified length and consisting of the
    given characters.  The optional argument exclude_similar_chars
    determines whether the password should not contain similar looking
    characters.
    """

    if sys.version_info < (3, 0):
        if not isinstance(length, (types.IntType, types.LongType)):
            raise TypeError("invalid length: %r" % length)

        if not isinstance(chars, types.StringTypes):
            raise TypeError("invalid chars: %r" % chars)

        if not isinstance(exclude_similar_chars, types.BooleanType):
            raise TypeError("invalid exclude_similar_chars: %r" % exclude_similar_chars)
    else:
        if not isinstance(length, int):
            raise TypeError("invalid length: %r" % length)

        if not isinstance(chars, str):
            raise TypeError("invalid chars: %r" % chars)

        if not isinstance(exclude_similar_chars, bool):
            raise TypeError("invalid exclude_similar_chars: %r" % exclude_similar_chars)

    if length < 1:
        raise ValueError("invalid length: %d" % length)

    if not chars:
        raise ValueError("no chars to use")

    if exclude_similar_chars:
        if sys.version_info < (3, 0):
            available_chars = chars.translate(_translation_table, SIMILAR_CHARS)
        else:
            available_chars = chars.translate(_translation_table)

        if not available_chars:
            raise ValueError("no chars to use: %r" % chars)
    else:
        available_chars = chars

    password = str()
    for i in range(length):
        password += random.choice(available_chars)

    return password


def generatepin(length=4):
    """Generates a PIN number of the specified length."""

    return generatepass(length, string.digits, exclude_similar_chars=False)
