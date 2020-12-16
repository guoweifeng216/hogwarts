# -*- coding: utf-8 -*-
"""
@Time ： 2020/12/16 22:24
@Auth ： 大侠
@File ：check_calculator.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
"""
# -*- coding: utf-8 -*-
"""
@Time ： 2020/12/9 21:22
@Auth ： guoweifeng
@File ：test_calculator.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
"""
import pytest
import yaml
from pythoncode.calculater import Calculator


def get_data():
    with open("./date.yaml") as f :
        data = yaml.safe_load(f)
        print(data)
        add_date = data['add_date']
        sub_data = data['sub_date']
        multi_data = data['multi_date']
        div_data = data['div_date']
        date_ids = data['my_id']
        return [add_date, sub_data, multi_data, div_data, date_ids]


class CheckCalc():
    def setup(self):
        self.calc = Calculator()

    @pytest.mark.run(order=3)
    @pytest.mark.parametrize('a, b, expect', get_data()[2], ids=get_data()[4])
    def check_multi(self, a, b, expect):
        assert expect == self.calc.multi(a, b)

    @pytest.mark.run(order=4)
    @pytest.mark.parametrize('a, b, expect', get_data()[3], ids=get_data()[4])
    def check_div(self, a, b, expect):
        assert expect == self.calc.devise(a, b)

    @pytest.mark.run(order=1)
    @pytest.mark.parametrize("a,b,expect", get_data()[0], ids=get_data()[4])
    def check_add(self, a, b, expect):
        print(a,b,expect)
        # print(Calculator.add(a, b))
        assert expect == self.calc.add(a, b)

    @pytest.mark.run(order=2)
    @pytest.mark.parametrize("a,b,expect", get_data()[1], ids=get_data()[4])
    def check_sub(self, a, b, expect):
        assert expect == self.calc.sub(a, b)

