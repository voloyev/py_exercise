def max_sum_subvector(vector):
    if len(vector) == len([i for i in vector if i < 0]):
        vector = [i * -1 for i in vector]

    if vector:
        current_sum = 0
        max_sum = 0

        current_start_index = 0
        start_index = 0
        end_index = 0

        for index, element in enumerate(vector):
            if current_sum <= 0:  # max_sum:
                current_start_index = index
                current_sum = element
            else:
                current_sum += element

            if current_sum > max_sum:
                max_sum = current_sum
                start_index = current_start_index
                end_index = index + 1

        return vector[start_index:end_index]

    return []
