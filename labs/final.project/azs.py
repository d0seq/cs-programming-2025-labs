from config import FUEL_PRICES, MIN_FUEL_LEVEL, COLUMNS_CONFIG


class AZS:
    def __init__(self, data):
        self.emergency = data["emergency"]
        self.tanks = data["tanks"]  # dict: имя -> параметры
        self.stats = data["stats"]
        self.history = data["history"]

    def add_to_history(self, event):
        self.history.append(event)
        if len(self.history) > 50:  # ограничим историю
            self.history.pop(0)

    def get_tank_by_name(self, name):
        return self.tanks.get(name)

    def get_tanks_by_fuel(self, fuel_type):
        return {name: tank for name, tank in self.tanks.items() if tank["fuel_type"] == fuel_type}

    def check_low_tanks(self):
        """Отключает цистерны с уровнем топлива ниже MIN_FUEL_LEVEL"""
        low = []
        for name, tank in self.tanks.items():
            if tank["current"] < MIN_FUEL_LEVEL and tank["active"]:
                tank["active"] = False
                self.add_to_history(f"Цистерна {name} отключена: уровень ниже {MIN_FUEL_LEVEL} л")
                low.append(name)
        return low

    def get_inactive_tanks(self):
        return [name for name, tank in self.tanks.items() if not tank["active"]]

    def serve_client(self, column, fuel_type, liters):
        if self.emergency:
            return False, "АЗС в аварийном режиме. Заправка невозможна."

        if column not in COLUMNS_CONFIG:
            return False, "Неверный номер колонки."

        col_config = COLUMNS_CONFIG[column]
        if fuel_type not in col_config:
            return False, f"Колонка {column} не поддерживает топливо '{fuel_type}'."

        tank_name = col_config[fuel_type]
        tank = self.tanks[tank_name]

        if not tank["active"]:
            return False, f"Цистерна {tank_name} отключена. Отпуск топлива невозможен."

        if tank["current"] < liters:
            return False, f"Недостаточно топлива в цистерне {tank_name}. Доступно: {tank['current']} л."

        price = FUEL_PRICES[fuel_type]
        total = round(liters * price, 2)

        # Выполняем продажу
        tank["current"] -= liters
        self.stats["total_income"] += total
        self.stats["cars_served"] += 1
        self.stats["fuel_sold"][fuel_type] += liters

        self.add_to_history(f"Продажа: колонка {column}, {fuel_type}, {liters} л, {total} ₽")

        return True, f"Операция выполнена успешно.\nСпасибо за покупку!"

    def refill_tank(self, tank_name, liters):
        tank = self.tanks[tank_name]
        new_level = tank["current"] + liters
        if new_level > tank["max_volume"]:
            return False, f"Превышение объёма! Максимум: {tank['max_volume']} л."
        tank["current"] = new_level
        self.add_to_history(f"Пополнение: цистерна {tank_name}, +{liters} л")
        return True, "Пополнение успешно."

    def transfer_fuel(self, src, dst, liters):
        if self.tanks[src]["fuel_type"] != self.tanks[dst]["fuel_type"]:
            return False, "Перекачка возможна только между цистернами одного типа топлива."

        if not self.tanks[src]["active"]:
            return False, "Источник отключён."

        if self.tanks[src]["current"] < liters:
            return False, "Недостаточно топлива в источнике."

        if self.tanks[dst]["current"] + liters > self.tanks[dst]["max_volume"]:
            return False, "Недостаточно места в приёмнике."

        self.tanks[src]["current"] -= liters
        self.tanks[dst]["current"] += liters
        self.add_to_history(f"Перекачка: {src} → {dst}, {liters} л")
        return True, "Перекачка выполнена."

    def toggle_tank(self, tank_name, active):
        tank = self.tanks[tank_name]
        if active and tank["current"] < MIN_FUEL_LEVEL:
            return False, f"Уровень топлива ({tank['current']} л) ниже минимального ({MIN_FUEL_LEVEL} л). Включение невозможно."
        tank["active"] = active
        status = "включена" if active else "отключена"
        self.add_to_history(f"Цистерна {tank_name} {status}")
        return True, f"Цистерна {tank_name} {status}."

    def activate_emergency(self):
        self.emergency = True
        for tank in self.tanks.values():
            tank["active"] = False
        self.add_to_history("АВАРИЯ: все цистерны заблокированы")

    def deactivate_emergency(self):
        self.emergency = False
        self.add_to_history("Выход из аварийного режима")

    def to_dict(self):
        return {
            "emergency": self.emergency,
            "tanks": self.tanks,
            "stats": self.stats,
            "history": self.history
        }