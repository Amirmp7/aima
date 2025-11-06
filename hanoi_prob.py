from core import St, Prob

class HanoiProb(Prob):
    def __init__(self, n=3, sp=0, gp=2):
        init = St([sp]*n)
        goal = St([gp]*n)
        super().__init__(init, goal)
        self.n = n
        self.p = 3
        self.gp = gp

    def succ(self, st):
        nxt = []
        td = [None]*self.p
        for d, peg in enumerate(st.s):
            if td[peg] is None or d < td[peg]:
                td[peg] = d
        for fp in range(self.p):
            disk = td[fp]
            if disk is None: continue
            for tp in range(self.p):
                if tp == fp: continue
                dt = td[tp]
                if dt is None or dt > disk:
                    nd = list(st.s)
                    nd[disk] = tp
                    nxt.append(St(nd))
        return nxt