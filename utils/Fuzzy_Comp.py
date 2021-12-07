from fuzzywuzzy import fuzz

class Fuzzy_Comp:

    def __init__(self, s1, s2):
        self.s1 = s1
        self.s2 = s2

    def compare_aut(self):
        return fuzz.partial_ratio(self.s1, self.s2)

    def compare_tit(self):
        return fuzz.partial_token_set_ratio(self.s1, self.s2)

    def choose_aut(self):
        if (self.compare_aut() > 75):
            if(len(self.s2) > len(self.s1)):
                return self.s2
            else:
                return self.s1

    def choose_aut(self):
        if (self.compare_tit() > 75):
            if(len(self.s2) > len(self.s1)):
                return self.s2
            else:
                return self.s1