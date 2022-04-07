class NewtonPolynomial:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def point(self, param):
        if param < self.x[0] or param > self.x[-1]:
            return None

        result1 = 0
        for i in range(1, len(self.x) + 1):
            result = 0
            for j in range(i):
                resultraz1 = self.y[j]
                for k in range(i):
                    if j != k:
                        resultraz1 /= (self.x[j] - self.x[k])
                result += resultraz1
            for j in range(i - 1):
                result *= param - self.x[j]
            result1 += result
        return result1
