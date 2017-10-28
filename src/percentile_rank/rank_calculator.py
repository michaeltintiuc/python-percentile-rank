from collections import Counter


class RankCalculator():
    """
    Calculate percentile rank based on index
    """

    @staticmethod
    def flipUniqueList(list):
        dict = {}
        for i, v in list.iteritems():
            if v not in dict:
                dict[v] = i
        return dict

    @staticmethod
    def calculate(data, index, key):
        # Sort data in ascending order
        data = sorted(data, key=lambda item: item[index])

        # Generate a list of values and cast to same type
        values = {i: float(v[index]) for i, v in enumerate(data)}

        # Number of examinees in the sample
        count = len(values)

        # List to use when checking scores less than the score of interest
        count_less = RankCalculator.flipUniqueList(values)

        # List to use when checking frequency of the score of interest
        count_values = Counter(values.values())

        for i, v in values.iteritems():
            freq = count_values[v]
            rank = ((count_less[v] + 0.5 * freq) / count) * 100

            if type(data[i]) is list:
                data[i].append(rank)
            else:
                data[i][key] = rank

        return data
