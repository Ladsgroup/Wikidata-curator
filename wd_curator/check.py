

class Check(object):
    """docstring for Check"""
    def __init__(self, name, check_str, target_str):
        super(Check, self).__init__()
        self.name = name
        self.check = check_str
        self.target_str = target_str

    def run(self):
        if eval(self.check_str):
            exec(self.target_str)
