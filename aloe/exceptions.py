"""
Exception classes
"""

from __future__ import unicode_literals
from __future__ import print_function
from __future__ import division
from __future__ import absolute_import
# pylint:disable=redefined-builtin
from builtins import super
# pylint:enable=redefined-builtin
from future import standard_library
standard_library.install_aliases()

from aloe.utils import PY3


class LettuceSyntaxError(SyntaxError):
    """A syntax error in a feature file."""
    def __init__(self, filename, string):
        self.filename = filename
        self.string = string

        msg = "Syntax error at: {filename}\n{string}".format(
            filename=filename, string=string)

        super().__init__(msg)


class LettuceSyntaxWarning(SyntaxWarning):
    """A warning about syntax in a feature file."""
    pass


class StepLoadingError(Exception):
    """Raised when a step cannot be loaded."""
    pass


class NoDefinitionFound(Exception):
    """
    Exception raised when there is no suitable step definition for a step.
    """

    def __init__(self, step):
        self.step = step
        super().__init__('The step r"%s" is not defined' % self.step.sentence)


# Step definitions can contain Unicode, and that will propagate to the
# exception message. On Python 2, this makes handling such exceptions tricky,
# so force encoding the message as Unicode.
if not PY3:
    NoDefinitionFound.__str__ = lambda self: self.message.encode('utf-8')
