#!/usr/bin/env python
# -*- coding: utf-8 -*-

import ruamel.yaml


def update(obj, path, value):
    new_type = dict
    if obj is None:
        obj = dict()

    if not path:
        return value

    if path[0].isdigit():
        path[0] = int(path[0])
        new_type = list

    if path[0] == '[]':
        obj.append(update(dict(), path[1:], value))
        return obj

    if new_type is dict:
        if type(obj) is str:
            obj = new_type()
            obj[path[0]] = update(new_type(), path[1:], value)
        elif type(obj) is new_type:
            obj[path[0]] = update(
                obj.get(path[0], new_type()), path[1:], value)
        else:
            if type(obj) is list and len(obj) == 0:
                obj.append(update(new_type(), path[1:], value))
            else:
                obj[path[0]] = update(
                    obj.get(path[0], new_type()), path[1:], value)

    else:
        if len(obj) > path[0]:
            obj[path[0]] = update(
                obj[path[0]], path[1:], value)
        elif hasattr(obj, 'append'):
            obj.append(update(dict(), path[1:], value))
        elif len(obj) == 0:
            obj = []
            obj.append(update(dict(), path[1:], value))
        else:
            obj[path[0]] = update(dict(), path[1:], value)

    return obj


def yaml(stream, query):
    doc = ruamel.yaml.load(
        stream,
        ruamel.yaml.RoundTripLoader,
        preserve_quotes=True,
    )

    path = query.split('=')[0].split('.')
    if type(path) is not list:
        path = [path]

    value = query.split('=')[1]

    doc = update(doc, path, value)

    return ruamel.yaml.dump(doc, Dumper=ruamel.yaml.RoundTripDumper)


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(
        description='Set in a yaml file some values.',
    )
    parser.add_argument(
        'path_to_file', metavar='path_to_file', type=str,
        help='YAML path to file')
    parser.add_argument(
        '--query',
        metavar='query',
        type=str, action='append', required=True,
        help='a query in format path=value e.g. users.0.name=Bogdan')
    parser.add_argument('--overwrite-file', dest='overwrite_file', action='store_true', required=False)

    path_to_file = parser.parse_args().path_to_file

    with open(path_to_file, mode='r') as f:
        content = f.read()

    for query in parser.parse_args().query:
        content = yaml(content, query)

    with open(path_to_file, mode='w') as f:
        content = f.read()
