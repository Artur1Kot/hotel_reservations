from fastapi import Query, Body, APIRouter
from schemas.hotels import Hotel, HotelPATCH

router = APIRouter(prefix="/hotels", tags=["Отели"])


hotels = [
    {"id": 1, "title": "Сочи", "name": "sochi"},
    {"id": 2, "title": "Дубай", "name": "dubai"}
]


@router.get("", summary="Получение отеля")
def get_hotels(
        title: str | None = Query(None, description="Название отеля"),
        id: int | None = Query(None, description="id отеля")
):
    hotels_ =[]
    for hotel in hotels:
        if id and hotel["id"] != id:
            continue
        elif title and hotel["title"] != title:
            continue
        hotels_.append(hotel)
    return hotels_


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