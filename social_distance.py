def long_distance(in_string):
    """Поиск наибольшей дистанции до соседа.

    Принятые условия:
    Вход - строка из "0" и "1". "0" означает,
    что место слева от этой позиции свободно.
    Выход - номер места, которое имеет
    наибольшее удаление от соседей. Или "0", если все места заняты.
    Методика поиска.
    Граничный случай 1, все места заняты.
    Возврат "0".
    Граничный случай 2, все места свободны.
    Возврат первого попавшегося места.
    Этап первый. Если крайнее место свободно, то определяется интервал
    от него до первого занятого места внутрь ряда.
    Соответствующий участок ряда исключается из данных для следующего этапа.
    Если конечных интервалов два, выбирается бОльший.
    Этап второй. В оставшейся части строки ищутся интервалы свободных мест.
    Из них выбирается самый длинный. 
    Если его длина больше 1, то расстояние до соседа принимается как длина
    интервала делённая на 2 с отбросом дробной части.
    Этап третий. Из конечного и внутреннего интервалов выбирается один
    с наибольшим расстоянием до соседа.
    Для интервалов используется конструкция вида (len, num_place), где
    num_place - позиция в строке, len - длина интервала. По ней выбирается
    больший.
    На заключительном этапе пересчитываются в дистанции и номер места.
    """
    import random as rnd

    def get_candid_len(in_string, position):
        """Поиск последовательности.
        
        В строке in_string с позиции position ищется непрерывная
        последовательность символов, равных считанному из позиции.
        Возврат - длина последовательности.
        """
        symbol = in_string[position - 1]
        len_range = 1
        for i in range(position, len(in_string)):
            if in_string[i] == symbol:
                len_range += 1
        return len_range

    work_string = in_string[1:] # "отрезаем" первый эл-т, теперь позиция в
                                # строке соответсвует статусу места
    if not '0' in work_string: # все места заняты
        return 0
    if not '1' in work_string: # все места свободны
        return rnd.randint(1, len(work_string))
    
    start_candid = None
    end_candid = None
    edge_candid = None
    candidats = []
    work_pos_start = 0
    work_pos_end = len(work_string)
    if work_string[0] == '0': # есть краевой интервал в начале
        start_candid_len = get_candid_len(work_string, 1)
        start_candid = (start_candid_len - 1, 1)
        work_pos_start += start_candid_len
    
    if work_string[:-1] == '0': # есть краевой интервал в конце
        end_candid_len = get_candid_len(work_string[::-1], 1)
        end_candid = (end_candid_len - 1, len(work_string))
        work_pos_end -= end_candid_len

    # если есть оба краевых кандидата, выбрать больший,
    # если есть один, выбрать его
    if start_candid and end_candid:
        edge_candid = max(start_candid, end_candid)
    elif start_candid:
        edge_candid = start_candid
    elif end_candid:
        edge_candid = end_candid

    current_pos = work_pos_start
    while True:
        if work_string[current_pos] == "0":
            candid_len = get_candid_len(work_string, current_pos)
            candidats.append((candid_len, current_pos)) # в список
                                                        # кандидатов
                                                        # добавляем пару
                                                        # длина, позиция
            current_pos += candid_len
            if current_pos >= work_pos_end: # не кончилась ли строка
                break

    if candidats:
        internal_candid = max(candidats) # внутренний кандидат
                                        # с максимальным интервалом
        
        # пересчёт интервала в номер места и расстояние до соседа
        internal_len, internal_pos = internal_candid
        if internal_len > 1:
            internal_len //= 2
        internal_pos += internal_len
        internal_candid = (internal_len, internal_pos)
    else:
        internal_candid = (0, 0)

    if edge_candid:
        finish = max(internal_candid, edge_candid)
    else:
        finish = internal_candid
    return finish[0][1]
