from allpairspy import AllPairs


def generate_testcases():
    parameters = [
        [1, 2, 9, 10, 11, 20, 21, 30, 31],  # distance
        ["small", "large"],  # size
        [False, True],  # fragile
        ["normal", "increased", "high", "very high"],  # workload
    ]

    def is_valid_combination(row):
        if len(row) == 3:
            distance, size, fragile = row
            if fragile and distance > 30:
                return False
            return True
        return True

    # Generate pairwise test cases
    pairwise_testcases = list(AllPairs(parameters, filter_func=is_valid_combination))

    return pairwise_testcases


if __name__ == "__main__":
    print(generate_testcases())
