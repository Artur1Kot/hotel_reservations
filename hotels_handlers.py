from fastapi import Query, Body, APIRouter
from schemas.hotels import Hotel, HotelPATCH

router = APIRouter(prefix="/hotels", tags=["Отели"])


hotels = [
    {"id": 1, "title": "Сочи", "name": "sochi"},
    {"id": 2, "title": "Дубай", "name": "dubai"},
    {"id": 3, "title": "Москва", "name": "moscow"},
    {"id": 4, "title": "Санкт-Петербург", "name": "spb"},
    {"id": 5, "title": "Казань", "name": "kazan"},
    {"id": 6, "title": "Екатеринбург", "name": "ekb"},
    {"id": 7, "title": "Новосибирск", "name": "novosibirsk"},
    {"id": 8, "title": "Краснодар", "name": "krasnodar"},
    {"id": 9, "title": "Калининград", "name": "kaliningrad"},
    {"id": 10, "title": "Владивосток", "name": "vladivostok"},
    {"id": 11, "title": "Париж", "name": "paris"},
    {"id": 12, "title": "Лондон", "name": "london"},
    {"id": 13, "title": "Нью-Йорк", "name": "newyork"},
    {"id": 14, "title": "Токио", "name": "tokyo"},
    {"id": 15, "title": "Барселона", "name": "barcelona"},
    {"id": 16, "title": "Рим", "name": "rome"},
    {"id": 17, "title": "Берлин", "name": "berlin"},
    {"id": 18, "title": "Амстердам", "name": "amsterdam"},
    {"id": 19, "title": "Стамбул", "name": "istanbul"},
    {"id": 20, "title": "Дубай Марина", "name": "dubai_marina"},
]


@router.get("", summary="Получение отеля")
def get_hotels(
        title: str | None = Query(None, description="Название отеля"),
        id: int | None = Query(None, description="id отеля"),
        page: int | None = Query(default=1, description="номер страницы"),
        per_page: int | None = Query(default=4, description="количество отелей на странице")
):
    hotels_ =[]
    for hotel in hotels:
        if id and hotel["id"] != id:
            continue
        elif title and hotel["title"] != title:
            continue
        hotels_.append(hotel)
    start = (page - 1) * per_page
    end = start + per_page
    return hotels_[start:end]


@router.delete("/{hotel_id}", summary="Удаление отеля")
def hotel_delete(hotel_id: int):
    global hotels
    hotels = [hotel for hotel in hotels if hotel["id"] != hotel_id]
    return {"status": "OK"}


@router.post("", summary="Добавление отеля")
def add_hotel(hotel_data: Hotel):
    global hotels
    hotels.append(
        {
        "id": hotels[-1]["id"] + 1,
        "title": hotel_data.title,
        "name": hotel_data.name
        }
    )
    return {"status": "OK"}


@router.patch("/{hotel_id}", summary="Частичное изменение отеля")
def patch_hotel(
        hotel_id: int,
        hotel_data: HotelPATCH
):
    global hotels
    hotel_ = [hotel for hotel in hotels if hotel_id == hotel["id"]][0]
    if hotel_data.title != "string" and hotel_data.title:
        hotel_["title"] = hotel_data.title
    if hotel_data.name != "string" and hotel_data.name:
        hotel_["name"] = hotel_data.name
    return {"status": "OK"}


@router.put("/{hotel_id}", summary="Изменение отеля")
def put_hotel(
        hotel_id: int,
        hotel_data: Hotel
):
    global hotels
    if hotel_data.title == "string" or hotel_data.name == "string":
        return {"status": "ОШИБКА: Оба поля обязательны для заполнения"}
    hotel_ = [hotel for hotel in hotels if hotel_id == hotel["id"]]
    hotel_[0]["title"] = hotel_data.title
    hotel_[0]["name"] = hotel_data.name
    return {"status": "OK"}