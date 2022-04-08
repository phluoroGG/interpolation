class NewtonPolynomial:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def point(self, param):
        if param < self.x[0] or param > self.x[-1]:
            return None

        result = 0
        for i in range(1, len(self.x) + 1):
            temp_value = 0
            for j in range(i):
                divided_difference = self.y[j]
                for k in range(i):
                    if j != k:
                        divided_difference /= (self.x[j] - self.x[k])
                temp_value += divided_difference
            for j in range(i - 1):
                temp_value *= param - self.x[j]
            result += temp_value
        return result
