def main():
    import sys

    sys.path.insert(0, "")

    from src.domain.info import Info, InfoRepository
    from src.domain.tour import Tour, TourRepository
    from src.domain.stops import TourStop, TourStopRepository

    database_path = "data/database.db"

    info_repository = InfoRepository(database_path)

    info_repository.save(Info(app_name="f5-seed-app"))

    tour_example = Tour(
        tour_id="tour_001",
        tour_name="Primer ensanche",
        tour_desc="A principios del siglo XIX la Villa de Bilbao salta la Ría. Las estrechas calles del Casco Viejo se han quedado pequeñas y se diseña una nueva ciudad moderna y luminosa. La burguesía quiere reflejarse en Europa y los modelos a seguir son París y Londres.",
        tour_front_image="https://www.vigoe.es/wp-content/uploads/2021/11/bilbao.jpg",
        favourite_tour=False,
        completed=False,
        filters=["arquitecture", "history", "monuments"],
    )
    tour_example2 = Tour(
        tour_id="tour_002",
        tour_name="Segundo tour",
        tour_desc="Tour de ejemplo 2",
        tour_front_image="https://www.bilbao.bi/wp-content/uploads/2021/11/que-ver-en-bilbao-2.jpg",
        favourite_tour=False,
        completed=False,
        filters=["nature", "history"],
    )

    tour_stop_example = TourStop(
        stop_id="001",
        stop_name="Ejemplo de primera parada",
        stop_description="Esta es un ejemplo de descripción de la primera parada",
        before_picture="esto debe ser una url con imagen pasado",
        after_picture="esto debe ser una url con imagen presente",
    )

    tour_stop_example2 = TourStop(
        stop_id="002",
        stop_name="Ejemplo de segunda parada",
        stop_description="Esta es un ejemplo de descripción de la segunda parada",
        before_picture="esto debe ser una url con imagen pasado",
        after_picture="esto debe ser una url con imagen presente",
    )

    tour_repository = TourRepository(database_path)
    stop_repository = TourStopRepository(database_path)
    tour_repository.save_tour(tour_example)
    tour_repository.save_tour(tour_example2)
    stop_repository.save_tour_stop(tour_stop_example)
    stop_repository.save_tour_stop(tour_stop_example2)


if __name__ == "__main__":
    main()
