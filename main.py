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
