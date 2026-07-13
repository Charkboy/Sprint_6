class Urls:
    BASE_URL = "https://qa-scooter.praktikum-services.ru/"
    DZEN_URL = "https://dzen.ru/"

class OrderData:
    DATA_SET_1 = {
        "name": "Иван",
        "surname": "Петров",
        "address": "ул. Ленина, 10",
        "metro": "Черкизовская",
        "phone": "+79001234567",
        "date": "2026-07-10",
        "rental_period": "сутки",
        "color": "чёрный",
        "comment": "Позвоните заранее"
    }
    DATA_SET_2 = {
        "name": "Мария",
        "surname": "Сидорова",
        "address": "пр. Мира, 5",
        "metro": "Преображенская площадь",
        "phone": "+79009876543",
        "date": "2026-07-12",
        "rental_period": "двое суток",
        "color": "серая безысходность",
        "comment": "Без комментариев"
    }
    ALL_DATA = [DATA_SET_1, DATA_SET_2]

class Texts:
    SUCCESS_MESSAGE_PART = "Заказ оформлен"