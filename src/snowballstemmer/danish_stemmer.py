# self file was generated automatically by the Snowball to Python interpreter

from basestemmer import BaseStemmer
from among import Among


class DanishStemmer(BaseStemmer):
    '''
    self class was automatically generated by a Snowball to Python interpreter
    It implements the stemming algorithm defined by a snowball script.
    '''
    serialVersionUID = 1

    a_0 = [
        Among(u"hed", -1, 1),
        Among(u"ethed", 0, 1),
        Among(u"ered", -1, 1),
        Among(u"e", -1, 1),
        Among(u"erede", 3, 1),
        Among(u"ende", 3, 1),
        Among(u"erende", 5, 1),
        Among(u"ene", 3, 1),
        Among(u"erne", 3, 1),
        Among(u"ere", 3, 1),
        Among(u"en", -1, 1),
        Among(u"heden", 10, 1),
        Among(u"eren", 10, 1),
        Among(u"er", -1, 1),
        Among(u"heder", 13, 1),
        Among(u"erer", 13, 1),
        Among(u"s", -1, 2),
        Among(u"heds", 16, 1),
        Among(u"es", 16, 1),
        Among(u"endes", 18, 1),
        Among(u"erendes", 19, 1),
        Among(u"enes", 18, 1),
        Among(u"ernes", 18, 1),
        Among(u"eres", 18, 1),
        Among(u"ens", 16, 1),
        Among(u"hedens", 24, 1),
        Among(u"erens", 24, 1),
        Among(u"ers", 16, 1),
        Among(u"ets", 16, 1),
        Among(u"erets", 28, 1),
        Among(u"et", -1, 1),
        Among(u"eret", 30, 1)
    ]

    a_1 = [
        Among(u"gd", -1, -1),
        Among(u"dt", -1, -1),
        Among(u"gt", -1, -1),
        Among(u"kt", -1, -1)
    ]

    a_2 = [
        Among(u"ig", -1, 1),
        Among(u"lig", 0, 1),
        Among(u"elig", 1, 1),
        Among(u"els", -1, 1),
        Among(u"l\u00F8st", -1, 2)
    ]

    g_v = [17, 65, 16, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 48, 0, 128]

    g_s_ending = [239, 254, 42, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 16]

    I_x = 0
    I_p1 = 0
    S_ch = ""

    def copy_from(self, other):
        self.I_x = other.I_x
        self.I_p1 = other.I_p1
        self.S_ch = other.S_ch
        super.copy_from(other)
    

    def r_mark_regions(self):
        # (, line 29
        self.I_p1 = self.limit;
        # test, line 33
        v_1 = self.cursor
        # (, line 33
        # hop, line 33
        c = self.cursor + 3
        if 0 > c or c > self.limit:
            return False
        self.cursor = c
        # setmark x, line 33
        self.I_x = self.cursor
        self.cursor = v_1
        # goto, line 34
        try:
            while True:
                v_2 = self.cursor
                try:
                    if not self.in_grouping(DanishStemmer.g_v, 97, 248):
                        raise lab1()
                    self.cursor = v_2
                    raise lab0()
                except lab1: pass
                self.cursor = v_2
                if self.cursor >= self.limit:
                    return False
                self.cursor += 1
        except lab0: pass
        # gopast, line 34
        try:
            while True:
                try:
                    if not self.out_grouping(DanishStemmer.g_v, 97, 248):
                        raise lab3()
                    raise lab2()
                except lab3: pass
                if self.cursor >= self.limit:
                    return False
                self.cursor += 1
        except lab2: pass
        # setmark p1, line 34
        self.I_p1 = self.cursor
        # try, line 35
        try:
            # (, line 35
            if not (self.I_p1 < self.I_x):
                raise lab4()
            self.I_p1 = self.I_x;
        except lab4: pass
        return True

    def r_main_suffix(self):
        # (, line 40
        # setlimit, line 41
        v_1 = self.limit - self.cursor
        # tomark, line 41
        if self.cursor < self.I_p1:
            return False
        self.cursor = self.I_p1
        v_2 = self.limit_backward
        self.limit_backward = self.cursor
        self.cursor = self.limit - v_1
        # (, line 41
        # [, line 41
        self.ket = self.cursor
        # substring, line 41
        among_var = self.find_among_b(DanishStemmer.a_0, 32)
        if among_var == 0:
            self.limit_backward = v_2
            return False
        # ], line 41
        self.bra = self.cursor
        self.limit_backward = v_2
        if among_var == 0:
            return False
        elif among_var == 1:
            # (, line 48
            # delete, line 48
            if not self.slice_del():
                return False

        elif among_var == 2:
            # (, line 50
            if not self.in_grouping_b(DanishStemmer.g_s_ending, 97, 229):
                return False
            # delete, line 50
            if not self.slice_del():
                return False

        return True

    def r_consonant_pair(self):
        # (, line 54
        # test, line 55
        v_1 = self.limit - self.cursor
        # (, line 55
        # setlimit, line 56
        v_2 = self.limit - self.cursor
        # tomark, line 56
        if self.cursor < self.I_p1:
            return False
        self.cursor = self.I_p1
        v_3 = self.limit_backward
        self.limit_backward = self.cursor
        self.cursor = self.limit - v_2
        # (, line 56
        # [, line 56
        self.ket = self.cursor
        # substring, line 56
        if self.find_among_b(DanishStemmer.a_1, 4) == 0:
            self.limit_backward = v_3
            return False
        # ], line 56
        self.bra = self.cursor
        self.limit_backward = v_3
        self.cursor = self.limit - v_1
        # next, line 62
        if self.cursor <= self.limit_backward:
            return False
        self.cursor -= 1
        # ], line 62
        self.bra = self.cursor
        # delete, line 62
        if not self.slice_del():
            return False

        return True

    def r_other_suffix(self):
        # (, line 65
        # do, line 66
        v_1 = self.limit - self.cursor
        try:
            # (, line 66
            # [, line 66
            self.ket = self.cursor
            # literal, line 66
            if not self.eq_s_b(2, u"st"):
                raise lab0()
            # ], line 66
            self.bra = self.cursor
            # literal, line 66
            if not self.eq_s_b(2, u"ig"):
                raise lab0()
            # delete, line 66
            if not self.slice_del():
                return False

        except lab0: pass
        self.cursor = self.limit - v_1
        # setlimit, line 67
        v_2 = self.limit - self.cursor
        # tomark, line 67
        if self.cursor < self.I_p1:
            return False
        self.cursor = self.I_p1
        v_3 = self.limit_backward
        self.limit_backward = self.cursor
        self.cursor = self.limit - v_2
        # (, line 67
        # [, line 67
        self.ket = self.cursor
        # substring, line 67
        among_var = self.find_among_b(DanishStemmer.a_2, 5)
        if among_var == 0:
            self.limit_backward = v_3
            return False
        # ], line 67
        self.bra = self.cursor
        self.limit_backward = v_3
        if among_var == 0:
            return False
        elif among_var == 1:
            # (, line 70
            # delete, line 70
            if not self.slice_del():
                return False

            # do, line 70
            v_4 = self.limit - self.cursor
            try:
                # call consonant_pair, line 70
                if not self.r_consonant_pair():
                    raise lab1()
            except lab1: pass
            self.cursor = self.limit - v_4
        elif among_var == 2:
            # (, line 72
            # <-, line 72
            if not self.slice_from(u"l\u00F8s"):
                return False
        return True

    def r_undouble(self):
        # (, line 75
        # setlimit, line 76
        v_1 = self.limit - self.cursor
        # tomark, line 76
        if self.cursor < self.I_p1:
            return False
        self.cursor = self.I_p1
        v_2 = self.limit_backward
        self.limit_backward = self.cursor
        self.cursor = self.limit - v_1
        # (, line 76
        # [, line 76
        self.ket = self.cursor
        if not self.out_grouping_b(DanishStemmer.g_v, 97, 248):
            self.limit_backward = v_2
            return False
        # ], line 76
        self.bra = self.cursor
        # -> ch, line 76
        self.S_ch = self.slice_to(self.S_ch)
        if self.S_ch == '':
            return False
        self.limit_backward = v_2
        # name ch, line 77
        if not self.eq_v_b(self.S_ch):
            return False
        # delete, line 78
        if not self.slice_del():
            return False

        return True

    def _stem(self):
        # (, line 82
        # do, line 84
        v_1 = self.cursor
        try:
            # call mark_regions, line 84
            if not self.r_mark_regions():
                raise lab0()
        except lab0: pass
        self.cursor = v_1
        # backwards, line 85
        self.limit_backward = self.cursor
        self.cursor = self.limit
        # (, line 85
        # do, line 86
        v_2 = self.limit - self.cursor
        try:
            # call main_suffix, line 86
            if not self.r_main_suffix():
                raise lab1()
        except lab1: pass
        self.cursor = self.limit - v_2
        # do, line 87
        v_3 = self.limit - self.cursor
        try:
            # call consonant_pair, line 87
            if not self.r_consonant_pair():
                raise lab2()
        except lab2: pass
        self.cursor = self.limit - v_3
        # do, line 88
        v_4 = self.limit - self.cursor
        try:
            # call other_suffix, line 88
            if not self.r_other_suffix():
                raise lab3()
        except lab3: pass
        self.cursor = self.limit - v_4
        # do, line 89
        v_5 = self.limit - self.cursor
        try:
            # call undouble, line 89
            if not self.r_undouble():
                raise lab4()
        except lab4: pass
        self.cursor = self.limit - v_5
        self.cursor = self.limit_backward
        return True

    def equals(self, o):
        return isinstance(o, DanishStemmer)

    def hashCode(self):
        return hash("DanishStemmer")

DanishStemmer.methodObject = DanishStemmer()
class lab0(BaseException): pass
class lab1(BaseException): pass
class lab2(BaseException): pass
class lab3(BaseException): pass
class lab4(BaseException): pass
