# coding=utf-8

prev = ""


def counter_values(string):
    cnt_1, cnt_0 = 0, 0
    for i in string:
        if i == '1':
            cnt_1 += 1
        elif i == '0':
            cnt_0 += 1
    return cnt_1, cnt_0


def correction(lst):
    string = ''.join(lst)
    counter, s_temp, j = 0, '', 0
    temp_lst, check_counter = [], 0
    s, t = '', []
    indx1, indx0 = string.find('111'), string.find('000')
    if indx1 < indx0 and indx1 != -1:
        for i in range(indx1, len(string)):
            s_temp += string[i]
            counter += 1
            if counter % 4 == 0 and counter != 0:
                temp_lst.append(s_temp)
                s_temp = ''
                counter = 0
                check_counter = i + 1
            elif len(string) - check_counter <= 3:
                for j in range(check_counter, len(string)):
                    s += string[j]
                break
    elif indx0 < indx1 and indx0 != -1:
        for i in range(indx0, len(string)):
            s_temp += string[i]
            counter += 1
            if counter % 4 == 0 and counter != 0:
                temp_lst.append(s_temp)
                s_temp = ''
                counter = 0
                check_counter = i + 1
            elif len(string) - check_counter <= 3:
                for j in range(check_counter, len(string)):
                    s += string[j]
                break
    for i in range(0, len(temp_lst)):
        temp_str = temp_lst[i]
        cnt_1, cnt_0 = counter_values(temp_str)
        if cnt_1 == 3:
            temp_lst[i] = '1111'
        elif cnt_0 == 3:
            temp_lst[i] = '0000'
        else:
            continue
    for j in range(0, len(s)):
        t.append(s[j])
    return ''.join(temp_lst), t


def correct(list_cod):
    string = ''.join(list_cod)
    ls, check = [], 0
    s_temp, last, last_list = '', '', []
    main_counter, temp_counter = 0, 0

    while main_counter != len(string):
        s_temp += string[main_counter]
        temp_counter += 1
        main_counter += 1
        if temp_counter % 8 == 0 and temp_counter != 0 and len(ls) > 0:
            if s_temp == '11110000':
                ls.append(s_temp)
                temp_counter = 0
                s_temp = ''
            elif s_temp == '00001111':
                ls.append(s_temp)
                temp_counter = 0
                s_temp = ''
            elif s_temp == '01110000' and ls[len(ls) - 1] == '11110000':
                s_temp = '11110000'
                ls.append(s_temp)
                temp_counter = 0
                s_temp = ''
            elif s_temp == '10001111' and ls[len(ls) - 1] == '00001111':
                s_temp = '00001111'
                ls.append(s_temp)
                temp_counter = 0
                s_temp = ''
            else:
                s_temp = ''
                temp_counter = 0
                main_counter -= 7
            check = len(string) - main_counter
            if check < 8:
                for i in range(main_counter, len(string)):
                    last += string[i]
                for i in range(0, len(last)):
                    last_list.append(last[i])
    return ''.join(ls), last_list


def get_templates(string):
    main_counter, counter, template, lst = 0, 0, '', []
    while main_counter != len(string):
        template += string[main_counter]
        counter += 1
        main_counter += 1
        if counter % 8 == 0 and counter != 0:
            if template == '11110000' or template == '00001111':
                lst.append(template)
                counter = 0
                template = ''
            else:
                main_counter -= 7
                counter = 0
                template = ''
        else:
            continue
    return lst


def to_string_converter(list_cod):
    s_item = ''
    for i in range(0, len(list_cod)):
        if i - 1 >= 0:
            if list_cod[i - 1] == '11110000' and list_cod[i] == '11110000':  # 1 1
                s_item += '1'
            elif list_cod[i - 1] == '00001111' and list_cod[i] == '00001111':  # 0 1
                s_item += '1'
            elif list_cod[i - 1] == '11110000' and list_cod[i] == '00001111':  # 1 0
                s_item += '0'
            elif list_cod[i - 1] == '00001111' and list_cod[i] == '11110000':  # 0 0
                s_item += '0'
        else:
            if list_cod[i] == '11110000':
                s_item += '1'
            elif list_cod[i] == '00001111':
                s_item += '0'
    return s_item


group_3_8 = {
    0: '01010',
    1: '10001',
    2: '01001',
    3: '11000',
    4: '00101',
    5: '10100',
    6: '01100',
    7: '00110',
    8: '00011',
    9: '10010'
}


def templates_finder(string):
    lst_cods_good, lst_cods_bad, lst_good_desc, lst_bad_desc = [], [], [], []
    main_counter, counter = 0, 0
    template = ''
    while main_counter != len(string):
        template += string[main_counter]
        counter += 1
        main_counter += 1
        if counter % 37 == 0 and counter != 0:
            st1 = what_cod_in(template)
            if len(st1) != 0 and len(st1.split(" ")) > 1:
                s1, s2 = st1.split("=")
                if s1 != U"Неизвестный тип":
                    lst_cods_good.append(template)
                    lst_good_desc.append(st1.replace("=", " "))
                    counter = 0
                    template = ''
                else:
                    lst_cods_bad.append(template)
                    lst_bad_desc.append(st1.replace("=", " "))
                    counter = 0
                    template = ''
            else:
                main_counter -= 36
                counter = 0
                template = ''
        else:
            continue
    return lst_cods_good, lst_good_desc, lst_cods_bad, lst_bad_desc


group_3_8_AC = {
    '01010': 0,
    '10001': 1,
    '01001': 2,
    '11000': 3,
    '00101': 4,
    '10100': 5,
    '01100': 6,
    '00110': 7,
    '00011': 8,
    '10010': 9
}

channel = ''

def what_cod_in(string):
    main_counter, counter = 0, 0
    lst_temp, temp = [], ''
    global result
    global channel
    while main_counter != 7:
        temp += string[main_counter]
        main_counter += 1
    lst_temp.append(temp)
    temp = ''
    while main_counter != len(string):
        temp += string[main_counter]
        counter += 1
        main_counter += 1
        if counter % 5 == 0 and counter != 0:
            lst_temp.append(temp)
            temp = ''
            counter = 0
        else:
            continue

    if lst_temp[0] == '1111100':
        if (lst_temp[1] == '00010' or lst_temp[1] == '00100' or lst_temp[1] == '00101'
            or lst_temp[1] == '00110' or lst_temp[1] == '01000' or lst_temp[1] == '01001'
            or lst_temp[1] == '01010' or lst_temp[1] == '01011' or lst_temp[1] == '01100'
            or lst_temp[1] == '01101' or lst_temp[1] == '01110' or lst_temp[1] == '00011'):

            if lst_temp[1] == '00010':
                channel = "1 Канал"
            elif lst_temp[1] == '00100':
                channel = "2 Канал"
            elif lst_temp[1] == '00101':
                channel = "3 Канал"
            elif lst_temp[1] == '00110':
                channel = "4 Канал"
            elif lst_temp[1] == '01000':
                channel = "5 Канал"
            elif lst_temp[1] == '01001':
                channel = "6 Канал"
            elif lst_temp[1] == '01010':
                channel = "7 Канал"
            elif lst_temp[1] == '01011':
                channel = "8 Канал"
            elif lst_temp[1] == '01100':
                channel = "9 Канал"
            elif lst_temp[1] == '01101':
                channel = "10 Канал"
            elif lst_temp[1] == '01110':
                channel = "11 Канал"
            elif lst_temp[1] == '00011':
                channel = "12 Канал"

            # already checked channel, next 3-8 groups seems to be checked

            if lst_temp[2] == group_3_8[8]:
                if lst_temp[3] == group_3_8[0] and lst_temp[4] == group_3_8[1]:
                    if lst_temp[5] == group_3_8[1] and lst_temp[6] == group_3_8[1]:
                        result = "ВКЛ ПРД Команда включения ПРД / ПДТ ВКЛ ПРД Сигнал подтверждения" + "=" + channel
                    elif lst_temp[5] == group_3_8[1] and lst_temp[6] == group_3_8[2]:
                        result = "ВЫКЛ ПРД Команда выключения передатчика / ПДТ ВЫКЛ ПРД Сигнал подтверждения" + "=" + channel
                    elif lst_temp[5] == group_3_8[1] and lst_temp[6] == group_3_8[5]:
                        result = "ВКЛ К1 Команда включения режима КОНТРОЛЬ / ПДТ ВКЛ К1 Сигнал подтверждения" + "=" + channel
                    elif lst_temp[5] == group_3_8[1] and lst_temp[6] == group_3_8[6]:
                        result = "ВЫКЛ К Команда выключения режима КОНТРОЛЬ / ПДТ ВЫКЛ К   Сигнал  подтверждения" + "=" + channel
                    elif lst_temp[5] == group_3_8[1] and lst_temp[6] == group_3_8[3]:
                        result = "ЗПР С Команда Запрос состояния / НОРМА Сигнал Норма" + "=" + channel
                    elif lst_temp[5] == group_3_8[2] and lst_temp[6] == group_3_8[1]:
                        result = "ПЖ Сигнал Пожар" + "=" + channel
                    elif lst_temp[5] == group_3_8[2] and lst_temp[6] == group_3_8[2]:
                        result = "ВД Сигнал Вскрытие дверей" + "=" + channel
                    elif lst_temp[5] == group_3_8[2] and lst_temp[6] == group_3_8[3]:
                        result = "АВ АФУ Сигнал Авария АФУ" + " " + channel
                    elif lst_temp[5] == group_3_8[2] and lst_temp[6] == group_3_8[4]:
                        result = "АВ ФП Сигнал Авария фидера питания" + "=" + channel
                    elif lst_temp[5] == group_3_8[2] and lst_temp[6] == group_3_8[6]:
                        result = "АВ ПРД Сигнал Авария передатчика" + "=" + channel
                    elif lst_temp[5] == group_3_8[2] and lst_temp[6] == group_3_8[7]:
                        result = "АВ ПРМ Сигнал Авария приемника" + "=" + channel
                    else:
                        result = "Неизвестный тип" + "=" + channel
                elif lst_temp[3] == group_3_8[0] and lst_temp[4] == group_3_8[3]:
                    if lst_temp[5] == group_3_8[1] and lst_temp[5] == group_3_8[1]:
                        result = "ВКЛ ПРМ Команда включения ПРМ / ПДТ ВКЛ ПРМ Сигнал подтверждения" + "=" + channel
                    elif lst_temp[5] == group_3_8[0] and lst_temp[6] == group_3_8[0]:
                        result = "ЗПР РЕЖ   Запрос режима работы" + "=" + channel
                    else:
                        result = "Неизвестный тип" + "=" + channel
                elif lst_temp[3] == group_3_8[1] and lst_temp[4] == group_3_8[3] and lst_temp[5] == group_3_8[0] \
                        and lst_temp[6] == group_3_8[0]:
                    result = "РЕЖ  Информация о режиме работы / Дежурный" + "=" + channel
                elif lst_temp[3] == group_3_8[2] and lst_temp[4] == group_3_8[3] and lst_temp[5] == group_3_8[0] \
                        and lst_temp[6] == group_3_8[0]:
                    result = "РЕЖ  Информация о режиме работы / Излучение" + "=" + channel
                elif lst_temp[3] == group_3_8[4] and lst_temp[4] == group_3_8[3] and lst_temp[5] == group_3_8[0] \
                        and lst_temp[6] == group_3_8[0]:
                    result = "РЕЖ  Информация о режиме работы / Переговоры" + "=" + channel
                elif lst_temp[3] == group_3_8[5] and lst_temp[4] == group_3_8[3] and lst_temp[5] == group_3_8[0] \
                        and lst_temp[6] == group_3_8[0]:
                    result = "РЕЖ  Информация о режиме работы / Перег с выкл передатчиком" + "=" + channel
                elif lst_temp[3] == group_3_8[6] and lst_temp[4] == group_3_8[3] and lst_temp[5] == group_3_8[0] \
                        and lst_temp[6] == group_3_8[0]:
                    result = "РЕЖ  Информация о режиме работы / Шлейф" + "=" + channel
                elif lst_temp[3] == group_3_8[0] and lst_temp[4] == group_3_8[0] and lst_temp[5] == group_3_8[0]:
                    if lst_temp[6] == group_3_8[9]:
                        result = "СОИ Сигнал отсутствия информации" + "=" + channel
                    elif lst_temp[6] == group_3_8[8]:
                        result = "СНИ Сигнал наличия информации" + "=" + channel
                    else:
                        result = "Неизвестный тип" + "=" + channel
            elif lst_temp[2] == group_3_8[9]:
                if (lst_temp[3] in group_3_8_AC) and (lst_temp[4] in group_3_8_AC) and (lst_temp[5] in group_3_8_AC) and \
                        (lst_temp[6] in group_3_8_AC):
                    result = "СЗКА Сигнал занятия канала абонентом / КТО / КПВ" + "=" + channel
                else:
                    result = "Неизвестный тип, Возможно СЗКА Сигнал занятия канала абонентом / КТО / КПВ" + "=" + channel
            elif lst_temp[2] == group_3_8[7]:
                if lst_temp[3] == group_3_8[0] and lst_temp[4] == group_3_8[0] and lst_temp[5] == group_3_8[0] and \
                                lst_temp[6] == group_3_8[0]:
                    result = "СОЦ сигнал отбоя центра" + "=" + channel
                else:
                    result = "Неизвестный тип, Возможно СОЦ сигнал отбоя центра" + "=" + channel
            elif lst_temp[2] == group_3_8[6]:
                if lst_temp[3] == group_3_8[0] and lst_temp[4] == group_3_8[0] and lst_temp[5] == group_3_8[0] and \
                                lst_temp[6] == group_3_8[0]:
                    result = "M1 сигнал Маркер М1" + "=" + channel
                else:
                    result = "Неизвестный тип" + "=" + channel
            elif lst_temp[2] == group_3_8[5]:
                if lst_temp[3] == group_3_8[0] and lst_temp[4] == group_3_8[0] and lst_temp[5] == group_3_8[0] and \
                                lst_temp[6] == group_3_8[0]:
                    result = "СМ1 сигнал спецмаркер 1" + "=" + channel
                else:
                    result = "Неизвестный тип" + "=" + channel
            elif lst_temp[2] == group_3_8[4]:
                if lst_temp[3] == group_3_8[0] and lst_temp[4] == group_3_8[0] and lst_temp[5] == group_3_8[0] and \
                                lst_temp[6] == group_3_8[0]:
                    result = "М2 сигнал маркер 2" + "=" + channel
                else:
                    result = "Неизвестный тип" + "=" + channel
            elif lst_temp[2] == group_3_8[3]:
                if lst_temp[3] == group_3_8[0] and lst_temp[4] == group_3_8[0] and lst_temp[5] == group_3_8[0] and \
                                lst_temp[6] == group_3_8[0]:
                    result = "КОД сигнал кодовая" + "=" + channel
                else:
                    result = "Неизвестный тип" + "=" + channel
            elif lst_temp[2] == group_3_8[2]:
                if (lst_temp[3] in group_3_8_AC) and (lst_temp[4] in group_3_8_AC) and (lst_temp[5] in group_3_8_AC) and \
                        (lst_temp[6] in group_3_8_AC):
                    result = "СЗКО сигнал занятия канала" + "=" + channel
                else:
                    result = "Неизвестный тип" + "=" + channel
            elif lst_temp[2] == group_3_8[1]:
                if (lst_temp[3] in group_3_8_AC) and (lst_temp[4] in group_3_8_AC) and (lst_temp[5] in group_3_8_AC) and \
                        (lst_temp[6] in group_3_8_AC):
                    result = "СОА сигнал отбоя абонента" + "=" + channel
                elif lst_temp[3] == group_3_8[0] and lst_temp[4] == group_3_8[0] and lst_temp[5] == group_3_8[0] and \
                                lst_temp[6] == group_3_8[0]:
                    result = "СМ2 сигнал спецмаркер 2" + "=" + channel
                else:
                    result = "Неизвестный тип" + "=" + channel
            elif lst_temp[2] == group_3_8[0]:
                if (lst_temp[3] in group_3_8_AC) and (lst_temp[4] in group_3_8_AC) and (lst_temp[5] in group_3_8_AC) and \
                        (lst_temp[6] in group_3_8_AC):
                    result = "ИВ команда избирательный вызов" + "=" + channel
                elif (lst_temp[3] == group_3_8[9]) and (lst_temp[4] == group_3_8[9]) and (
                            lst_temp[5] in group_3_8_AC) and \
                        (lst_temp[6] in group_3_8_AC):
                    result = "ИВ команда ив циркулярный" + "=" + channel
                elif (lst_temp[3] == group_3_8[0]) and (lst_temp[4] == group_3_8[0]) and (
                            lst_temp[5] == group_3_8[0]) and (lst_temp[6] == group_3_8[0]):
                    result = "СИНХР синхропосылка" + "=" + channel
                else:
                    result = "Неизвстный тип" + "=" + channel
        else:
            if channel == '00000' and (lst_temp[3] in group_3_8_AC) and (lst_temp[4] in group_3_8_AC) and \
                    (lst_temp[5] in group_3_8_AC) and (lst_temp[6] in group_3_8_AC):
                result = "СИНХР синхропосылка без признака частоты" + "=" + channel
            else:
                channel = lst_temp[1] + " " + "Неизвестный канал"
            if lst_temp[2] == group_3_8[8]:
                if lst_temp[3] == group_3_8[0] and lst_temp[4] == group_3_8[1]:
                    if lst_temp[5] == group_3_8[1] and lst_temp[6] == group_3_8[1]:
                        result = "ВКЛ ПРД Команда включения ПРД / ПДТ ВКЛ ПРД Сигнал подтверждения" + "=" + channel
                    elif lst_temp[5] == group_3_8[1] and lst_temp[6] == group_3_8[2]:
                        result = "ВЫКЛ ПРД Команда выключения передатчика / ПДТ ВЫКЛ ПРД Сигнал подтверждения" + "=" + channel
                    elif lst_temp[5] == group_3_8[1] and lst_temp[6] == group_3_8[5]:
                        result = "ВКЛ К1 Команда включения режима КОНТРОЛЬ / ПДТ ВКЛ К1 Сигнал подтверждения" + "=" + channel
                    elif lst_temp[5] == group_3_8[1] and lst_temp[6] == group_3_8[6]:
                        result = "ВЫКЛ К Команда выключения режима КОНТРОЛЬ / ПДТ ВЫКЛ К   Сигнал  подтверждения" + "=" + channel
                    elif lst_temp[5] == group_3_8[1] and lst_temp[6] == group_3_8[3]:
                        result = "ЗПР С Команда Запрос состояния / НОРМА Сигнал Норма" + "=" + channel
                    elif lst_temp[5] == group_3_8[2] and lst_temp[6] == group_3_8[1]:
                        result = "ПЖ Сигнал Пожар" + "=" + channel
                    elif lst_temp[5] == group_3_8[2] and lst_temp[6] == group_3_8[2]:
                        result = "ВД Сигнал Вскрытие дверей" + "=" + channel
                    elif lst_temp[5] == group_3_8[2] and lst_temp[6] == group_3_8[3]:
                        result = "АВ АФУ Сигнал Авария АФУ" + "=" + channel
                    elif lst_temp[5] == group_3_8[2] and lst_temp[6] == group_3_8[4]:
                        result = "АВ ФП Сигнал Авария фидера питания" + "=" + channel
                    elif lst_temp[5] == group_3_8[2] and lst_temp[6] == group_3_8[6]:
                        result = "АВ ПРД Сигнал Авария передатчика" + "=" + channel
                    elif lst_temp[5] == group_3_8[2] and lst_temp[6] == group_3_8[7]:
                        result = "АВ ПРМ Сигнал Авария приемника" + "=" + channel
                    else:
                        result = "Неизвестный тип" + "=" + channel
                elif lst_temp[3] == group_3_8[0] and lst_temp[4] == group_3_8[3]:
                    if lst_temp[5] == group_3_8[1] and lst_temp[5] == group_3_8[1]:
                        result = "ВКЛ ПРМ Команда включения ПРМ / ПДТ ВКЛ ПРМ Сигнал подтверждения" + "=" + channel
                    elif lst_temp[5] == group_3_8[0] and lst_temp[6] == group_3_8[0]:
                        result = "ЗПР РЕЖ   Запрос режима работы" + "=" + channel
                    else:
                        result = "Неизвестный тип" + "=" + channel
                elif lst_temp[3] == group_3_8[1] and lst_temp[4] == group_3_8[3] and lst_temp[5] == group_3_8[0] \
                        and lst_temp[6] == group_3_8[0]:
                    result = "РЕЖ  Информация о режиме работы / Дежурный" + "=" + channel
                elif lst_temp[3] == group_3_8[2] and lst_temp[4] == group_3_8[3] and lst_temp[5] == group_3_8[0] \
                        and lst_temp[6] == group_3_8[0]:
                    result = "РЕЖ  Информация о режиме работы / Излучение" + "=" + channel
                elif lst_temp[3] == group_3_8[4] and lst_temp[4] == group_3_8[3] and lst_temp[5] == group_3_8[0] \
                        and lst_temp[6] == group_3_8[0]:
                    result = "РЕЖ  Информация о режиме работы / Переговоры" + "=" + channel
                elif lst_temp[3] == group_3_8[5] and lst_temp[4] == group_3_8[3] and lst_temp[5] == group_3_8[0] \
                        and lst_temp[6] == group_3_8[0]:
                    result = "РЕЖ  Информация о режиме работы / Перег с выкл передатчиком" + "=" + channel
                elif lst_temp[3] == group_3_8[6] and lst_temp[4] == group_3_8[3] and lst_temp[5] == group_3_8[0] \
                        and lst_temp[6] == group_3_8[0]:
                    result = "РЕЖ  Информация о режиме работы / Шлейф" + "=" + channel
                elif lst_temp[3] == group_3_8[0] and lst_temp[4] == group_3_8[0] and lst_temp[5] == group_3_8[0]:
                    if lst_temp[6] == group_3_8[9]:
                        result = "СОИ Сигнал отсутствия информации" + "=" + channel
                    elif lst_temp[6] == group_3_8[8]:
                        result = "СНИ Сигнал наличия информации" + "=" + channel
                    else:
                        result = "Неизвестный тип" + "=" + channel
            elif lst_temp[2] == group_3_8[9]:
                if (lst_temp[3] in group_3_8_AC) and (lst_temp[4] in group_3_8_AC) and (lst_temp[5] in group_3_8_AC) and \
                        (lst_temp[6] in group_3_8_AC):
                    result = "СЗКА Сигнал занятия канала абонентом / КТО" + "=" + channel
                else:
                    result = "Неизвестный тип" + "=" + channel
            elif lst_temp[2] == group_3_8[7]:
                if lst_temp[3] == group_3_8[0] and lst_temp[4] == group_3_8[0] and lst_temp[5] == group_3_8[0] and \
                                lst_temp[6] == group_3_8[0]:
                    result = "СОЦ сигнал отбоя центра" + "=" + channel
                else:
                    result = "Неизвестный тип" + "=" + channel
            elif lst_temp[2] == group_3_8[6]:
                if lst_temp[3] == group_3_8[0] and lst_temp[4] == group_3_8[0] and lst_temp[5] == group_3_8[0] and \
                                lst_temp[6] == group_3_8[0]:
                    result = "M1 сигнал Маркер М1" + "=" + channel
                else:
                    result = "Неизвестный тип" + "=" + channel
            elif lst_temp[2] == group_3_8[5]:
                if lst_temp[3] == group_3_8[0] and lst_temp[4] == group_3_8[0] and lst_temp[5] == group_3_8[0] and \
                                lst_temp[6] == group_3_8[0]:
                    result = "СМ1 сигнал спецмаркер 1" + "=" + channel
                else:
                    result = "Неизвестный тип" + "=" + channel
            elif lst_temp[2] == group_3_8[4]:
                if lst_temp[3] == group_3_8[0] and lst_temp[4] == group_3_8[0] and lst_temp[5] == group_3_8[0] and \
                                lst_temp[6] == group_3_8[0]:
                    result = "М2 сигнал маркер 2" + "=" + channel
                else:
                    result = "Неизвестный тип" + "=" + channel
            elif lst_temp[2] == group_3_8[3]:
                if lst_temp[3] == group_3_8[0] and lst_temp[4] == group_3_8[0] and lst_temp[5] == group_3_8[0] and \
                                lst_temp[6] == group_3_8[0]:
                    result = "КОД сигнал кодовая" + "=" + channel
                else:
                    result = "Неизвестный тип" + "=" + channel
            elif lst_temp[2] == group_3_8[2]:
                if (lst_temp[3] in group_3_8_AC) and (lst_temp[4] in group_3_8_AC) and (lst_temp[5] in group_3_8_AC) and \
                        (lst_temp[6] in group_3_8_AC):
                    result = "СЗКО сигнал занятия канала" + "=" + channel
                else:
                    result = "Неизвестный тип" + "=" + channel
            elif lst_temp[2] == group_3_8[1]:
                if (lst_temp[3] in group_3_8_AC) and (lst_temp[4] in group_3_8_AC) and (lst_temp[5] in group_3_8_AC) and \
                        (lst_temp[6] in group_3_8_AC):
                    result = "СОА сигнал отбоя абонента" + "=" + channel
                elif lst_temp[3] == group_3_8[0] and lst_temp[4] == group_3_8[0] and lst_temp[5] == group_3_8[0] and \
                                lst_temp[6] == group_3_8[0]:
                    result = "СМ2 сигнал спецмаркер 2" + "=" + channel
                else:
                    result = "Неизвестный тип" + "=" + channel
            elif lst_temp[2] == group_3_8[0]:
                if (lst_temp[3] in group_3_8_AC) and (lst_temp[4] in group_3_8_AC) and (lst_temp[5] in group_3_8_AC) and \
                        (lst_temp[6] in group_3_8_AC):
                    result = "ИВ команда избирательный вызов" + "=" + channel
                elif (lst_temp[3] == group_3_8[9]) and (lst_temp[4] == group_3_8[9]) and (
                            lst_temp[5] in group_3_8_AC) and \
                        (lst_temp[6] in group_3_8_AC):
                    result = "ИВ команда ив циркулярный" + "=" + channel
                elif (lst_temp[3] == group_3_8[0]) and (lst_temp[4] == group_3_8[0]) and (
                            lst_temp[5] == group_3_8[0]) and (lst_temp[6] == group_3_8[0]):
                    result = "СИНХР синхропосылка" + "=" + channel
                else:
                    result = "Неизвстный тип" + "=" + channel
    else:
        result = ""
    return unicode(result, 'UTF-8')


def codogramm_counter(lst, lst_desc, cnt_err):
    main_counter, counter = 0, 0
    lst_indx_1, lst_indx_2 = [], []
    check = 1
    global prev
    st, s1, s2 = ''.join(lst), '', ''
    while main_counter != len(lst):
        counter = main_counter - 1
        if counter >= 0:
            if lst[counter] != lst[main_counter]:
                s1 += lst[main_counter]
                lst_indx_1.append(main_counter)
            else:
                s2 += lst[counter]
                lst_indx_2.append(counter)
        main_counter += 1
    cnt_1, cnt_2 = s1.count(s1[0:37:1]), s2.count(s2[0:37:1]) + 1
    if cnt_2 >= 3 > cnt_1:
        st = lst_desc[lst_indx_2[0]]
        cnt_err = 0
        prev = U"Кодограмма : *" + unicode(s2[0:37:1], 'utf-8') + U"* Колличество : *" + unicode(str(cnt_2),
                                                                                                 'utf-8') + U"* " + st
        return U"Кодограмма : *" + unicode(s2[0:37:1], 'utf-8') + U"* Колличество : *" + unicode(str(cnt_2),
                                                                                                 'utf-8') + U"* " + st, cnt_err
    elif cnt_1 >= 3 > cnt_1:
        st = lst_desc[lst_indx_1[0]]
        cnt_err = 0
        prev = U"Кодограмма : *" + unicode(s2[0:37:1], 'utf-8') + U"* Колличество : *" + unicode(str(cnt_2),
                                                                                                 'utf-8') + U"* " + st
        return U"Кодограмма : *" + unicode(s1[0:37:1], 'utf-8') + U"* Колличество : *" + unicode(str(cnt_1),
                                                                                                 'utf-8') + U"* " + st, cnt_err
    elif cnt_1 >= 3 and cnt_2 >= 3:
        if cnt_1 > cnt_2:
            st = lst_desc[lst_indx_1[0]]
            cnt_err = 0
            prev = U"Кодограмма : *" + unicode(s2[0:37:1], 'utf-8') + U"* Колличество : *" + unicode(str(cnt_2),
                                                                                                     'utf-8') + U"* " + st
            return U"Кодограмма : *" + unicode(s1[0:37:1], 'utf-8') + U"* Колличество : *" + unicode(str(cnt_1),
                                                                                                     'utf-8') + U"* " + st, cnt_err
        else:
            st = lst_desc[lst_indx_2[0]]
            cnt_err = 0
            prev = U"Кодограмма : *" + unicode(s2[0:37:1], 'utf-8') + U"* Колличество : *" + unicode(str(cnt_2),
                                                                                                     'utf-8') + U"* " + st
            return U"Кодограмма : *" + unicode(s2[0:37:1], 'utf-8') + U"* Колличество : *" + unicode(str(cnt_2),
                                                                                                     'utf-8') + U"* " + st, cnt_err
    else:
        cnt_err += 1
        if cnt_err <= 1:
            return prev, cnt_err
        else:
            return U"Кодограмм *нет* или *отсутствует сигнал*", cnt_err
