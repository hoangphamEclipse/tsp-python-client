# The MIT License (MIT)
#
# Copyright (C) 2020 - Ericsson
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

"""ColumnDescriptor class file."""

TEXT_KEY = "text"
TOOLTIP_KEY = "tooltip"


# pylint: disable=too-few-public-methods
class ColumnDescriptor:
    '''
    Basic entry
    '''

    def __init__(self, params):
        '''
        Text of header for the entry
        '''
        self.text = ''
        if TEXT_KEY in params:
            self.text = params.get(TEXT_KEY)
            del params[TEXT_KEY]

        # Label of tooltip of the header
        self.tooltip = ''
        if TOOLTIP_KEY in params:
            self.tooltip = params.get(TOOLTIP_KEY)
            del params[TOOLTIP_KEY]
