# -*- coding: utf-8 -*-
"""
@Time ： 2020/12/16 0:17
@Auth ： 大侠
@File ：conftest.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
"""
import pytest
from pythoncode.calculater import Calculator


@pytest.fixture(autouse=True, scope='module')
def myfixture():
    print("计算开始")
    yield
    print("计算结束")