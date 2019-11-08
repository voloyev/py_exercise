def max_sum_subvector(vector):
    if len(set(vector)) == 1:
        return vector[0]

    if vector:
        current_sum = 0
        max_sum = vector[0]

        for element in vector:
            current_sum = max(current_sum + element, element)
            max_sum = max(max_sum, current_sum)

        return max_sum
    return 0
