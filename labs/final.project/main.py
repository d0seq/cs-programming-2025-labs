from azs import AZS
from storage import load_data, save_data
from config import COLUMNS_CONFIG, FUEL_PRICES
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def input_int(prompt, min_val=None, max_val=None):
    while True:
        try:
            val = int(input(prompt))
            if min_val is not None and val < min_val:
                print(f"Значение должно быть >= {min_val}")
                continue
            if max_val is not None and val > max_val:
                print(f"Значение должно быть <= {max_val}")
                continue
            return val
        except ValueError:
            print("Введите целое число.")

def input_float(prompt, min_val=None):
    while True:
        try:
            val = float(input(prompt))
            if min_val is not None and val < min_val:
                print(f"Значение должно быть >= {min_val}")
                continue
            return val
        except ValueError:
            print("Введите число.")

def show_header(azs):
    clear_screen()
    print("="*50)
    print("АЗС <<СеверНефть>>")
    print("Система управления заправочной станцией")
    print("="*50)

    if azs.emergency:
        print("\n АВАРИЙНЫЙ РЕЖИМ! Все операции кроме выхода и отключения аварии заблокированы.")
    else:
        inactive = azs.get_inactive_tanks()
        if inactive:
            print("\nВНИМАНИЕ!")
            print("Обнаружены отключённые цистерны:")
            for name in inactive:
                print(f" - {name}")

    print("-"*50)

def menu_serve_client(azs):
    print("--- Обслуживание клиента ---\n")
    print("Доступные колонки:")
    for i in range(1, 9):
        print(f"{i}) Колонка {i}")
    col = input_int("Выберите колонку: ", 1, 8)

    fuels = COLUMNS_CONFIG[col]
    print(f"\nКолонка {col}\n")
    print("Доступные виды топлива:")
    fuel_list = list(fuels.keys())
    for i, ft in enumerate(fuel_list, 1):
        tank_name = fuels[ft]
        status = "ACTIVE" if azs.tanks[tank_name]["active"] else "NON ACTIVE"
        print(f"{i}) {ft:<6} (цистерна {tank_name}) {status}")

    choice = input_int("Выберите тип топлива: ", 1, len(fuel_list))
    fuel_type = fuel_list[choice - 1]

    liters = input_float("Введите количество литров: ", 0.1)
    success, msg = azs.serve_client(col, fuel_type, liters)
    print(f"\n{msg}")
    if success:
        price = FUEL_PRICES[fuel_type]
        total = round(liters * price, 2)
        print(f"\nСтоимость:\n{liters} л × {price} ₽ = {total:.2f} ₽")
        confirm = input("\nПодтвердить оплату? (y/n): ").strip().lower()
        if confirm == 'y':
            print("\nОперация выполнена успешно.\nСпасибо за покупку!")
        else:
            # Отмена: вернём топливо и статистику
            tank_name = fuels[fuel_type]
            azs.tanks[tank_name]["current"] += liters
            azs.stats["total_income"] -= total
            azs.stats["cars_served"] -= 1
            azs.stats["fuel_sold"][fuel_type] -= liters
            if azs.history:
                azs.history.pop()  # удалим последнюю запись
            print("Операция отменена.")
    input("\nНажмите Enter для возврата...")

def menu_tank_status(azs):
    print("--- Состояние цистерн ---\n")
    for name, tank in azs.tanks.items():
        status = "ВКЛ" if tank["active"] else "ВЫКЛ"
        warning = ""
        if tank["current"] < 2000:
            warning = " (ниже порога)"
        print(f"{name:<10} | {tank['current']:>6} / {tank['max_volume']} л | {status}{warning}")
    input("\nНажмите Enter...")

def menu_refill(azs):
    print("--- Оформить пополнение топлива ---\n")
    tanks = list(azs.tanks.keys())
    for i, name in enumerate(tanks, 1):
        ft = azs.tanks[name]["fuel_type"]
        print(f"{i}) {name} ({ft})")
    choice = input_int("Выберите цистерну: ", 1, len(tanks))
    tank_name = tanks[choice - 1]
    liters = input_float("Укажите количество литров: ", 1)
    success, msg = azs.refill_tank(tank_name, liters)
    print(f"\n{msg}")
    input("\nНажмите Enter...")

def menu_stats(azs):
    print("--- Баланс и статистика ---\n")
    print(f"Обслужено автомобилей: {azs.stats['cars_served']}")
    print(f"Общий доход: {azs.stats['total_income']:,.2f} ₽\n")
    print("Продано топлива:")
    for ft, liters in azs.stats["fuel_sold"].items():
        income = liters * FUEL_PRICES[ft]
        print(f"{ft:<6} - {liters} л ({income:,.2f} ₽)")
    input("\nНажмите Enter...")

def menu_history(azs):
    print("--- История операций ---\n")
    if not azs.history:
        print("История пуста.")
    else:
        for i, event in enumerate(reversed(azs.history[-10:]), 1):
            print(f"{i}) {event}")
    input("\nНажмите Enter...")

def menu_transfer(azs):
    print("--- Перекачка топлива ---\n")
    tanks = list(azs.tanks.keys())
    print("Источник:")
    for i, name in enumerate(tanks, 1):
        print(f"{i}) {name}")
    src_i = input_int("Выберите источник: ", 1, len(tanks))
    src = tanks[src_i - 1]

    print("\nПриёмник (только того же типа):")
    src_type = azs.tanks[src]["fuel_type"]
    compatible = [name for name in tanks if azs.tanks[name]["fuel_type"] == src_type and name != src]
    if not compatible:
        print("Нет совместимых цистерн.")
        input("\nНажмите Enter...")
        return
    for i, name in enumerate(compatible, 1):
        print(f"{i}) {name}")
    dst_i = input_int("Выберите приёмник: ", 1, len(compatible))
    dst = compatible[dst_i - 1]

    liters = input_float("Объём для перекачки: ", 1)
    success, msg = azs.transfer_fuel(src, dst, liters)
    print(f"\n{msg}")
    input("\nНажмите Enter...")

def menu_manage_tanks(azs):
    print("--- Управление цистернами ---\n")
    print("Доступные действия:")
    print("1) Включить цистерну")
    print("2) Отключить цистерну")
    action = input_int("> ", 1, 2)

    inactive = [name for name, tank in azs.tanks.items() if not tank["active"]]
    active = [name for name, tank in azs.tanks.items() if tank["active"]]

    if action == 1:
        if not inactive:
            print("Нет отключённых цистерн.")
            input("\nНажмите Enter...")
            return
        print("\nЦистерны, доступные для включения:")
        for i, name in enumerate(inactive, 1):
            tank = azs.tanks[name]
            print(f"{i}) {name} | {tank['current']} / {tank['max_volume']} л")
        choice = input_int("Выберите цистерну: ", 1, len(inactive))
        tank_name = inactive[choice - 1]
        success, msg = azs.toggle_tank(tank_name, True)
        print(f"\n{msg}")
    else:
        if not active:
            print("Нет включённых цистерн.")
            input("\nНажмите Enter...")
            return
        print("\nЦистерны, доступные для отключения:")
        for i, name in enumerate(active, 1):
            print(f"{i}) {name}")
        choice = input_int("Выберите цистерну: ", 1, len(active))
        tank_name = active[choice - 1]
        azs.toggle_tank(tank_name, False)
        print(f"\nЦистерна {tank_name} отключена.")

    input("\nНажмите Enter...")

def menu_columns(azs):
    print("--- Состояние колонок ---\n")
    for col in range(1, 9):
        print(f"Колонка {col}:")
        fuels = COLUMNS_CONFIG[col]
        for ft, tank_name in fuels.items():
            tank = azs.tanks[tank_name]
            status = "ACTIVE" if tank["active"] else "NON ACTIVE"
            print(f"  {ft:<6} → {tank_name} {status}")
        print()
    input("Нажмите Enter...")

def menu_emergency(azs):
    if azs.emergency:
        print("\n Аварийный режим уже активен!")
        confirm = input("Выключить аварийный режим? (y/n): ").strip().lower()
        if confirm == 'y':
            azs.deactivate_emergency()
            print("Аварийный режим отключён.")
        else:
            print("Остаёмся в аварии.")
    else:
        print("\n ВНИМАНИЕ! Активация аварийного режима остановит всю заправку!")
        confirm = input("Подтвердить аварию? (y/n): ").strip().lower()
        if confirm == 'y':
            azs.activate_emergency()
            print("АВАРИЯ! Все цистерны заблокированы. Вызваны службы.")
        else:
            print("Авария отменена.")
    input("\nНажмите Enter...")

def main():
    data = load_data()
    azs = AZS(data)
    # Проверим, не нужно ли отключить цистерны из-за низкого уровня
    azs.check_low_tanks()

    while True:
        show_header(azs)
        print("Выберите действие:")
        print("1) Обслужить клиента (касса)")
        print("2) Проверить состояние цистерн")
        print("3) Оформить пополнение топлива")
        print("4) Баланс и статистика")
        print("5) История операций")
        print("6) Перекачка топлива между цистернами")
        print("7) Включение / отключение цистерн")
        print("8) Состояние колонок")
        print("9) EMERGENCY - аварийная ситуация")
        print("0) Выход")
        choice = input("> ").strip()

        # Блокировка всех действий кроме 0 и 9 в аварии
        if azs.emergency and choice not in ("9", "0"):
            print("<<<<< В аварийном режиме доступны только действия 9 и 0.")
            input("Нажмите Enter для возврата в меню...")
            continue

        if choice == "1":
            menu_serve_client(azs)
        elif choice == "2":
            menu_tank_status(azs)
        elif choice == "3":
            menu_refill(azs)
        elif choice == "4":
            menu_stats(azs)
        elif choice == "5":
            menu_history(azs)
        elif choice == "6":
            menu_transfer(azs)
        elif choice == "7":
            menu_manage_tanks(azs)
        elif choice == "8":
            menu_columns(azs)
        elif choice == "9":
            menu_emergency(azs)
        elif choice == "0":
            save_data(azs.to_dict())
            print("Данные сохранены. До свидания!")
            break
        else:
            print("Неверный выбор.")
            input("Нажмите Enter...")

if __name__ == "__main__":
    main()