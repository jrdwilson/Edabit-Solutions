def filter_list(lst):
    filtered_lst = []
    for i in lst:
        if isinstance(i,int):
            filtered_lst.append(i)
        else:
            continue
    print(filtered_lst)
    return filtered_lst

filter_list([1, 2, "a", "b"])
filter_list([1, "a", "b", 0, 15])
filter_list([1, 2, "aasf", "1", "123", 123])
filter_list(["jsyt", 4, "yt", "6"])
filter_list(["r", 5, "y", "e", 8, 9])
filter_list(["a", "e", "i", "o", "u"])
filter_list([4, "z", "f", 5])
filter_list(["abc", 123])
filter_list(["$%^", 567, "&&&"])
filter_list(["w", "r", "u", 43, "s", "a", 76, "d", 88])
