class Vehicle:

    swet = {"дальний": "Включен дальний свет",
            "ближний": "Включен ближний свет"}



    def __init__(self, model_name, engine_power, color, manufacture_year,
                 manufacture_country, doors_count, hijacked_status):
        self.__model_name = model_name
        self.__engine_power = engine_power
        self.__color = color
        self.__manufacture_year = manufacture_year
        self.__manufacture_country = manufacture_country
        self.__doors_count = doors_count
        self.__hijacked_status = hijacked_status
        self.__engine_status = False
        self.__headlights_status = False


    @property
    def model_name(self):
        return self.__model_name

    @property
    def engine_power(self):
        return int(self.__engine_power)

    @property
    def color(self):
        return self.__color

    @property
    def manufacture_year(self):
        return int(self.__manufacture_year)

    @property
    def manufacture_country(self):
        return self.__manufacture_country

    @property
    def doors_count(self):
        return int(self.__doors_count)

    @property
    def hijacked_status(self):
        if self.__hijacked_status == True:
            return "Данное т/с в угоне!"
        else:
            return "Данное т/с не имеет криминальной истории"

    @property
    def engine_status(self):
        if self.__engine_status == True:
            return "Двигатель запущен"
        else:
            return "Автомобиль не заведен"

    @property
    def headlights_status(self):
        if self.__headlights_status == True:
            return "Фары включены"
        else:
            return "Фары отключены"


    def start_engine(self):
        self.__engine_status = True


    def stop_engine(self):
        self.__engine_status = False


    def switch_on_headlights(self, light_type):
        for key, value in Vehicle.swet.items():
            if light_type.lower() == key:
                print(value)
                self.__headlights_status = True
                break

            elif light_type.lower() == key:
                print(value)
                self.__headlights_status = True
                break

            elif light_type not in Vehicle.swet:
                print("Вы выбрали неверный режим освещения."
                        "Возможны режимы: 'ближний' и 'дальний' ")
                break


    def switch_off_headlights(self):
        self.__headlights_status = False



