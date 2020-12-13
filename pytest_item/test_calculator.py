# -*- coding: utf-8 -*-
"""
@Time ： 2020/12/9 21:22
@Auth ： guoweifeng
@File ：test_calculator.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
"""
import pytest
from pythoncode.calculater import Calculator


class TestCalc:
    def setup_class(self):
        self.calc = Calculator()
        print("开始计算")

    def teardown_class(self):
        print("结束计算")

    @pytest.mark.parametrize("a,b,expect", [
        (3, 5, 8),
        (-1, -2, -3),
        (100, 300, 400)],
        ids=["int", "minus", "bigint"]
                             )
    def test_add(self, a, b, expect):
        assert expect == self.calc.add(a, b)

    @pytest.mark.parametrize("a,b,expect", [
        (3, 5, -2), (-1, -2, 1), (300, 100, 200)
    ], ids=["int", "minus", "bigint"])
    def test_sub(self, a, b, expect):
        assert expect == self.calc.sub(a, b)

    @pytest.mark.parametrize('a, b, expect', [(1.0, 2, 2),
                                              (4.5, 2, 9.0),
                                              (100, 2, 200)],
                             ids=["float", "int", "bigint"]
                             )
    def test_multi(self, a, b, expect):
        assert expect == self.calc.multi(a, b)

    @pytest.mark.parametrize('a, b, expect', [(1.0, 2, 0.5),
                                              (4.5, 2, 2.25),
                                              (100, 2, 50)],
                             ids=["float", "int", "bigint"]
                             )
    def test_div(self, a, b, expect):
        assert expect == self.calc.devise(a, b)