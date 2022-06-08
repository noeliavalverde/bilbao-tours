def main():
    import sys

    sys.path.insert(0, "")

    from src.domain.tour import Tour, TourRepository, TourStop

    database_path = "data/database.db"

    tour_example = Tour(
        tour_id="tour_001",
        tour_name="Primer ensanche",
        tour_desc="A principios del siglo XIX la Villa de Bilbao salta la Ría. Las estrechas calles del Casco Viejo se han quedado pequeñas y se diseña una nueva ciudad moderna y luminosa. La burguesía quiere reflejarse en Europa y los modelos a seguir son París y Londres.",
        tour_front_image="https://www.vigoe.es/wp-content/uploads/2021/11/bilbao.jpg",
        favourite_tour=False,
        filters=["arquitecture", "history", "monuments"],
    )
    tour_example2 = Tour(
        tour_id="tour_002",
        tour_name="Segundo tour",
        tour_desc="Tour de ejemplo 2",
        tour_front_image="https://www.bilbao.bi/wp-content/uploads/2021/11/que-ver-en-bilbao-2.jpg",
        favourite_tour=False,
        filters=["nature", "history"],
    )

    tour_stop_example = TourStop(
        stop_id="stop_001",
        stop_name="Ejemplo de primera parada",
        stop_description="Esta es un ejemplo de descripción de la primera parada",
        before_picture="esto debe ser una url con imagen pasado",
        after_picture="esto debe ser una url con imagen presente",
    )

    tour_stop_example2 = TourStop(
        stop_id="stop_002",
        stop_name="Ejemplo de segunda parada",
        stop_description="Esta es un ejemplo de descripción de la segunda parada",
        before_picture="esto debe ser una url con imagen pasado",
        after_picture="esto debe ser una url con imagen presente",
    )

    tour_stop_example3 = TourStop(
        stop_id="stop_003",
        stop_name="Ejemplo de tercera parada",
        stop_description="Esta es un ejemplo de descripción de la tercera parada",
        before_picture="esto debe ser una url con imagen pasado",
        after_picture="esto debe ser una url con imagen presente",
    )

    tour_stop_example4 = TourStop(
        stop_id="stop_004",
        stop_name="Ejemplo de cuarta parada",
        stop_description="Esta es un ejemplo de descripción de la cuarta parada",
        before_picture="esto debe ser una url con imagen pasado",
        after_picture="esto debe ser una url con imagen presente",
    )

    tour_stop_example5 = TourStop(
        stop_id="stop_005",
        stop_name="Ejemplo de quinta parada",
        stop_description="Esta es un ejemplo de descripción de la quinta parada",
        before_picture="esto debe ser una url con imagen pasado",
        after_picture="esto debe ser una url con imagen presente",
    )

    tour_stop_example6 = TourStop(
        stop_id="stop_006",
        stop_name="Ejemplo de sexta parada",
        stop_description="Esta es un ejemplo de descripción de la sexta parada",
        before_picture="esto debe ser una url con imagen pasado",
        after_picture="esto debe ser una url con imagen presente",
    )

    tour_repository = TourRepository(database_path)

    tour_repository.save_tour(tour_example)
    tour_repository.save_tour(tour_example2)
    tour_repository.save_tour_stop(tour_stop_example)
    tour_repository.save_tour_stop(tour_stop_example2)
    tour_repository.save_tour_stop(tour_stop_example3)
    tour_repository.save_tour_stop(tour_stop_example4)
    tour_repository.save_tour_stop(tour_stop_example5)
    tour_repository.save_tour_stop(tour_stop_example6)
    tour_repository.save_tour_stops_to_tour("tour_001", ["stop_006", "stop_002"])


if __name__ == "__main__":
    main()
