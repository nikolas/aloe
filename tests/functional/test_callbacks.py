# Lychee - Cucumber runner for Python based on Lettuce and Nose
# Copyright (C) <2015> Alexey Kotlyarov <a@koterpillar.com>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

"""
Test callbacks.
"""

from __future__ import unicode_literals
from __future__ import print_function
from __future__ import division
from __future__ import absolute_import
from future import standard_library
standard_library.install_aliases()

from nose.tools import assert_equals

from . import (
    FeatureTest,
    in_directory,
)


@in_directory('tests/callbacks_app')
class CallbackTest(FeatureTest):
    """
    Test callbacks functionality.
    """

    def test_step_callbacks(self):
        """
        Test step callbacks execution order.
        """

        self.assert_feature_success('features/step_callbacks.feature')

    def test_example_callbacks(self):
        """
        Test example callbacks execution order.
        """

        self.assert_feature_success('features/example_callbacks.feature')

    def test_feature_callbacks(self):
        """
        Test feature callbacks execution order.
        """

        self.assert_feature_success('features/feature_callbacks_1.feature',
                                    'features/feature_callbacks_2.feature')

    def test_all_callbacks(self):
        """
        Test 'all' callbacks.
        """

        self.assert_feature_success('features/all_callbacks_1.feature',
                                    'features/all_callbacks_2.feature')

        from lychee import world
        assert_equals(''.join(world.all), '{[ABCD]}')
