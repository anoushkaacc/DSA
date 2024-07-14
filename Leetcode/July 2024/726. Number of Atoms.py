from collections import Counter
class Solution:
    def countOfAtoms(self, formula: str) -> str: 
        self.i = 0
        self.formula = formula
        self.n = len(formula)
        count = self.plus()
        return "".join([el + str(count[el]) if count[el] > 1 else el for el in sorted(count)] )
    
    def plus(self):
        count = Counter()
        while self.i < self.n:
            multi = self.multiply() 
            if not multi: break 
            count += multi
        return count

    def element(self):
        p = None
        if self.i < self.n and self.formula[self.i] == "(":
            self.i += 1
            p = self.plus()
            return p
        if self.i < self.n and self.formula[self.i] == ")":
            self.i += 1
            return 
        el = self.formula[self.i]
        self.i += 1
        while self.i < self.n and self.formula[self.i].islower():
            el += self.formula[self.i]
            self.i += 1
        return Counter({el: 1})

    def multiply(self):
        count = self.element()
        if count:
            times = self.number()
            for el in count:
                count[el] *= times
        return count

    def number(self):
        number = ''
        while self.i < self.n and self.formula[self.i].isdigit():
            number += self.formula[self.i]       
            self.i += 1
        return int(number) if number else 1
