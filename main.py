import ruamel.yaml


def update(obj, path, value):
    if not path:
        return obj

    if path[0].isdigit():
        path[0] = int(path[0])

    if len(path) == 1:
        obj[path[0]] = value
        return obj
    else:
        new_type = dict
        if type(path[0]) is int:
            new_type = list

        if new_type is dict:
            obj[path[0]] = update(
                obj.get(path[0], new_type()), path[1:], value)
        else:
            if len(obj) > path[0]:
                obj[path[0]] = update(dict(), path[1:], value)
            else:
                obj.append(update(dict(), path[1:], value))

        return obj


def yaml(stream, set_string):
    doc = ruamel.yaml.load(
        stream,
        ruamel.yaml.RoundTripLoader,
        preserve_quotes=True,
    )

    path = set_string.split('=')[0].split('.')
    if type(path) is not list:
        path = [path]

    value = set_string.split('=')[1]

    doc = update(doc, path, value)

    return ruamel.yaml.dump(doc, Dumper=ruamel.yaml.RoundTripDumper)
