def find_common_participants(string_1, string_2, separator=","):
    string_1 = set(string_1.split(separator))
    string_2 = set(string_2.split(separator))
    res = list(string_1.intersection(string_2))
    res.sort()
    return res


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

print(find_common_participants(participants_first_group, participants_second_group, "|"))
