from fastapi import Query, Body, APIRouter


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
def hotel_delete(
        hotel_id: int
):
    global hotels
    hotels = [hotel for hotel in hotels if hotel["id"] != hotel_id]
    return {"status": "OK"}


@router.post("", summary="Добавление отеля")
def add_hotel(
        title: str,
        name: str
):
    global hotels
    hotels.append(
        {
        "id": hotels[-1]["id"] + 1,
        "title": title,
        "name": name
        }
    )
    return {"status": "OK"}


@router.patch("/{hotel_id}", summary="Частичное изменение отеля")
def patch_hotel(
        hotel_id: int,
        title: str | None = Body(None),
        name: str | None = Body(None)
):
    global hotels
    hotel_ = [hotel for hotel in hotels if hotel_id == hotel["id"]][0]
    if title != "string" and title:
        hotel_["title"] = title
    if name != "string" and name:
        hotel_["name"] = name
    return {"status": "OK"}


@router.put("/{hotel_id}", summary="Изменение отеля")
def put_hotel(
        hotel_id: int,
        title: str = Body(),
        name: str = Body()
):
    global hotels
    if title == "string" or name == "string":
        return {"status": "ОШИБКА: Оба поля обязательны для заполнения"}
    hotel_ = [hotel for hotel in hotels if hotel_id == hotel["id"]]
    hotel_[0]["title"] = title
    hotel_[0]["name"] = name
    return {"status": "OK"}