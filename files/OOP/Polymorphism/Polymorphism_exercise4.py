import statistics


class Median:

    def calculate_median(self, a=None, b=None, c=None, d=None, e=None):

        initial_list = [a, b, c, d, e]
        final_list = []

        for i in initial_list:
            if i != None:
                final_list.append(i)

        median = statistics.median(final_list)
        return median


m = Median()
print(m.calculate_median(3, 5, 1, 4, 2))
print(m.calculate_median(8, 6, 4, 2))
print(m.calculate_median(9, 3, 7))
print(m.calculate_median(5, 2))