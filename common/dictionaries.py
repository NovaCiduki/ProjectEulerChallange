def is_diff_value(dict1: dict, dict2: dict) -> bool:
    for key1 in dict1:
        if key1 in dict2:
            if dict2[key1] == dict1[key1]:
                return False
    return True