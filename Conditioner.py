print("\nCONDITIONER START")
result = None
indication = ""
init_data = input("Введите через пробел фактическую и желаемую температуры в комнате"
                  "\nв диапазоне от -50\u00b0С до +50\u00b0С включительно\nв формате: XX XX; -XX -XX; -XX XX; XX -XX:\n")
mode = input("""Введите один из четырёх режимов:
 - freeze
 - heat
 - auto
 - fun\n""")
if init_data[0] == "-" and init_data[4] == "-":
    t_room = int(init_data[0] + init_data[1] + init_data[2])
    t_cond = int(init_data[4] + init_data[5] + init_data[6])
elif init_data[0] != "-" and init_data[3] == "-":
    t_room = int(init_data[0] + init_data[1])
    t_cond = int(init_data[3] + init_data[4] + init_data[5])
elif init_data[0] == "-" and init_data[4] != "-":
    t_room = int(init_data[0] + init_data[1] + init_data[2])
    t_cond = int(init_data[4] + init_data[5])
else:
    t_room = int(init_data[0] + init_data[1])
    t_cond = int(init_data[3] + init_data[4])
if t_room < -50 or t_room > 50 or t_cond < -50 or t_cond > 50:
    print("Введите корректные данные")
elif (init_data[0] != "-" and init_data[2] != " ") or (init_data[0] == "-" and init_data[3] != " "):
    print("Введите данные через пробел")
else:
    match (mode):
        case "freeze":
            if t_room > t_cond:
                result = t_cond
            else:
                result = t_room
        case "heat":
            if t_room < t_cond:
                result = t_cond
            else:
                result = t_room
        case "auto":
            if t_room < t_cond or t_room > t_cond:
                result = t_cond
            else:
                result = t_room
        case "fun":
            result = t_room
        case _:
            print("Вы ошиблись при вводе режима!")
if result is None:
    print("")
else:
    if result > 0:
        indication = "+"
    print(f"Через час температура в комнате будет равна: {indication}{result}\u00b0С")