users = ['user1', 'user2', 'user3', 'user1', 'user4', 'user2']
dict_users = {"Общее количество": 0, "Уникальные посещения": 0}
dict_users["Общее количество"] = len(users)
dict_users["Уникальные посещения"] = len(set(users))
print(dict_users)
