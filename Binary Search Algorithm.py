#Binary search algorithm

def binary_search(sequence, item):
    begin_index = 0
    end_index = len(sequence) - 1

    while begin_index <= end_index:
        midpoint = begin_index + (end_index - begin_index) // 2
        midpoint_value = sequence[midpoint]
        if midpoint_value == item:
            return midpoint
        elif item < midpoint_value:
             end_index = midpoint - 1
        else:
            begin_index = midpoint + 1

    return None

sequence_a = [1, 2, 5, 6, 10, 12, 15]
item_a = 15

print("Return position of item:", binary_search(sequence_a, item_a))