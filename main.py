import ruamel.yaml


def yaml(stream, set_string):
    doc = ruamel.yaml.load(
        stream,
        ruamel.yaml.RoundTripLoader,
        preserve_quotes=True,
    )

    path = set_string.split('.')
    value = path[-1].split('=')[1]
    path[-1] = path[-1].split('=')[0]

    doc_update = {}

    while path:
        doc_update = { path.pop(): value }
        value = doc_update

    doc.update(doc_update)

    return ruamel.yaml.dump(doc, Dumper=ruamel.yaml.RoundTripDumper)
