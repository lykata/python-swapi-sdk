import csv
import json
import typing
from sys import stdout

import toolz
from toolz import curried, pipe
from toolz.curried import groupby

from swapi import ClientBuilder


class CounterIterator(typing.Iterator):

    def __init__(self, value):
        self.value = value
        self.index = 0

    def __next__(self) -> int:
        if self.index == self.value:
            raise StopIteration
        self.index = self.index + 1
        return self.index


class Counter(typing.Iterable):

    def __init__(self, value):
        self.value = value

    def __iter__(self) -> CounterIterator:
        return CounterIterator(self.value)


def test(x, item):
    for p in item:
        yield x(p)


if __name__ == '__main__':
    client = ClientBuilder().default()
    planets = pipe(
        client.planet.list().iter(),
        curried.filter(lambda x: x.GetClimate().Get() == "temperate"),
        list)

    # print(json.dumps(planets, default=lambda x: x.Serializable()))

    people = list(map(lambda x: x["eye_color"], client.people.list().iter()))
    people = list(pipe(client.people.list().iter(),
                       # filter(lambda x: x.GetEyeColor().Get() == "brown" )
                       ))
    # print(json.dumps(people,default=lambda x: x.Serializable()))
    #
    # writer = csv.writer(stdout)
    # first, people = toolz.peek(people)

    # writer.writerow(pipe(first.keys()))
    # writer.writerows(
    #     list(pipe(people,
    #               gdict
    # )))

    a = Counter(4)
    map = curried.curry(map)
    test = curried.curry(test)
    list(pipe(a, map(lambda x: print(x))))
