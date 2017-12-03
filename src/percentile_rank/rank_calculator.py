from collections import Counter


class RankCalculator():
    """
    Calculate percentile rank based on index
    """

    @staticmethod
    def flipUniqueList(list):
        """
        Parse passed list
        Return a dict of unique values
        """
        dict = {}
        for i, v in list.iteritems():
            if v not in dict:
                dict[v] = i
        return dict

    @staticmethod
    def calculate(data, index, key):
        """
        Sort data in ascending order
        Generate a list of values, cast to same type
        Calculate scores less than the score of interest
        """
        data = sorted(data, key=lambda item: item[index])
        values = {i: float(v[index]) for i, v in enumerate(data)}
        examinees = len(values)
        count_values = Counter(values.values())
        count_less = RankCalculator.flipUniqueList(values)

        for i, v in values.iteritems():
            freq = count_values[v]
            rank = ((count_less[v] + 0.5 * freq) / examinees) * 100

            if type(data[i]) is list:
                data[i].append(rank)
            else:
                data[i][key] = rank

        return data
