import re
import subprocess

# If we compare using 'is', then these will return True only if
# they point to these exact objects.
RECURSIVE_OBJ = ['<RECURSIVE>']
LIST_RE = re.compile("^LIST:(.+)$")

class MoiraTree(object):
    @staticmethod
    def is_recursive_ptr(obj):
        return obj is RECURSIVE_OBJ

    def make_list_data(self, name, is_list):
        return dict(name=name, is_list=is_list)

    def __init__(self, name):
        self.lists_seen = set()
        self.unique_members = set() # Just members, not lists; can be used for counting
        # As a boostrapping hack, we start off by walking 
        list_data = self.make_list_data(name=name, is_list=True)
        if list_data['is_list']:
            self.tree = {list_data['name']: {}}
            self.walk(list_data['name'], self.tree[list_data['name']])
        else:
            self.tree = {list_data['name']: True}

    def get_list_data(self, str):
        """
        'LIST:sipb-office' -> {'name': 'sipb-office', 'is_list': True}
        'leonidg' -> {'name': 'leonidg', 'is_list': False}
        """
        m = LIST_RE.match(str)
        if m:
            return self.make_list_data(name=m.group(1), is_list=True)
        else:
            return self.make_list_data(name=str, is_list=False)

    def get_members(self, list_name):
        moira = subprocess.Popen(['blanche', list_name], stdout=subprocess.PIPE)
        output = moira.communicate()[0] # output is (STDOUT, STDERR)
        members = []
        for line in output.split('\n'):
            if line == '':
                continue
            members.append(self.get_list_data(line))
        return members

    def walk(self, list_name, root):
        members = self.get_members(list_name)
        for member in members:
            if member['is_list']:
                if member['name'] in self.lists_seen:
                    root[member['name']] = RECURSIVE_OBJ
                else:
                    self.lists_seen.add(member['name'])
                    root[member['name']] = {}
                    self.walk(member['name'], root[member['name']])
            else:
                root[member['name']] = True
                self.unique_members.add(member['name'])
