class LagrangePolynomial:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def point(self, param):
        if param < self.x[0] or param > self.x[-1]:
            return None

        result1 = 0
        for i in range(len(self.x)):
            result = 1
            for j in range(len(self.x)):
                if i != j:
                    result *= (param - self.x[j]) / (self.x[i] - self.x[j])
            result *= self.y[i]
            result1 += result
        return result1
