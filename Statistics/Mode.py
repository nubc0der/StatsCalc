
data = collections.Counter(num_list)
data_list = dict(data)

max_value = max(list(data.values()))
mode_val = [num for num, freq in data_list.items() if freq == max_value]