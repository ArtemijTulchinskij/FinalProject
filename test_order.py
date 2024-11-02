from sender_stand_request import create_order, get_order_by_track
def test_create_and_get_order():
    # Создаем заказ
    response = create_order()
    assert response.status_code == 201, f"Ожидался код 201, получен {response.status_code}"

    # Получаем номер трека из ответа
    track = response.json()["track"]
    print("Заказ создан. Номер трека:", track)

    # Получаем заказ по номеру трека
    response = get_order_by_track(track)
    assert response.status_code == 200, f"Ожидался код 200, получен {response.status_code}"

    # Проверяем, что номер трека совпадает
    order_data = response.json()
    assert order_data["order"]["track"] == track, "Номер трека не совпадает"
    print("Тест успешно пройден.")

# Запуск теста
if __name__ == "__main__":
    test_create_and_get_order()
#Тульчинский Артем 23-я когорта QA расширенный