class St:
    def __init__(self, stuff):
        self.s = tuple(stuff)

    def __eq__(self, o):
        return isinstance(o, St) and self.s == o.s

    def __hash__(self):
        return hash(self.s)

    def __str__(self):
        return str(self.s)


class Prob:
    def __init__(self, init, goal=None):
        self.i = init
        self.g = goal

    def goal_test(self, st):
        return st == self.g

    def succ(self, st):
        raise NotImplementedError("succ not impl")

    def res(self, st, act):
        return act