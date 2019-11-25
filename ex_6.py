#!/usr/bin/env python3
import json
import sys
from librip.ctxmngrs import timer
from librip.decorators import print_result
from librip.gens import field, gen_random
from librip.iterators import Unique as unique

path ="C:\\Users\\Hi\\Desktop\\папка0\\R.I.P\\lab_2_Python\\data_light_cp1251.json"

with open(path) as f:
    data = json.load(f)



@print_result
def f1(arg):
    return sorted(list(unique(field(arg, "job-name"), ignore_case=True)), key=lambda x: str.casefold(x))


@print_result
def f2(arg):
    return list(filter(lambda x: x.casefold().startswith("программист"), arg))


@print_result
def f3(arg):
    return list(map(lambda x: x + " с опытом Python", arg))


@print_result
def f4(arg):
    return dict(zip(arg, gen_random(100000, 200000, len(arg))))


with timer():
    f4(f3(f2(f1(data))))
