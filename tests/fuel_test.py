# -*- coding: utf-8 -*-
from nose.tools import assert_equal
from libs.fuel.fuel import Fuel


class TestFuel(object):
    def test_add_fuel(self):
        common_fuel = Fuel()
        common_fuel.add_fuel(10)
        assert_equal(10, common_fuel.fuel)

