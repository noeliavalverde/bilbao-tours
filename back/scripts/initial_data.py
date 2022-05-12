def main():
    import sys

    sys.path.insert(0, "")

    from src.domain.info import Info, InfoRepository
    from src.domain.tour import Tour, TourRepository

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

    tour_repository = TourRepository(database_path)
    tour_repository.save_tour(tour_example)


if __name__ == "__main__":
    main()
