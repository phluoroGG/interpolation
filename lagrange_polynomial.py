class LagrangePolynomial:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def point(self, param):
        if param < self.x[0] or param > self.x[-1]:
            return None

        result = 0
        for i in range(len(self.x)):
            temp_value = 1
            for j in range(len(self.x)):
                if i != j:
                    temp_value *= (param - self.x[j]) / (self.x[i] - self.x[j])
            temp_value *= self.y[i]
            result += temp_value
        return result
