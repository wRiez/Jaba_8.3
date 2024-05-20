def calc_stat(listened):  # От англ. calculate statistics, посчитать статистику
    # Напишите код функции calc_stat()
    M = 0
    for i in listened:
        M += i
    return f"Вы прослушали {len(listened)} песен общей продолжительностью {M} минут."


print(calc_stat([189, 148, 210, 144, 174, 158, 163, 189, 227, 198]))