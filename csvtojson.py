import csv
import json

class Node(object):
    def __init__(self, name, size=None, extra=None):
        self.name = name
        self.children = []
        self.size = size
        self.extra = extra

    def child(self, cname, size=None, extra=None):
        child_found = [c for c in self.children if c.name == cname]
        if not child_found:
            _child = Node(cname, size, extra)
            self.children.append(_child)
        else:
            _child = child_found[0]
        return _child

    def as_dict(self):
        res = {'name': self.name}
        if self.size is None:
            res['children'] = [c.as_dict() for c in self.children]
        else:
            res['size'] = self.size

        if self.extra:
            res.update(self.extra)

        return res

root = Node('Flare')

with open('datastructure.csv', 'r') as f:
    reader = csv.reader(f)
    header = next(reader)

    for row in reader:
        no, example, most_detailed_description, verb, verb2, object1, object2, object3, media1, media2 = row
        root.child(verb, extra={'test' : 'Verb 1'}) \
            .child(verb2, extra={'test' : 'Verb 2'}) \
            .child(object1, extra={'test' : 'Object 1'}) \
            .child(object2, extra={'test' : 'Object 2'}) \
            .child(object3, extra={'test' : 'Object 3'}) \
            .child(media1, extra={'test' : 'Media 1'}) \
            .child(media2, extra={'test' : 'Media 2'}) \
            .child(example, extra={'test' : 'Example'})


with open('json_file_name.json', 'w') as jsonFile:
    jsonFile.write(json.dumps(root.as_dict(), indent=4))
