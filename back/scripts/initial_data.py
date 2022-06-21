def main():
    import sys

    sys.path.insert(0, "")

    from src.domain.tour import Tour, TourRepository, TourStop
    from src.domain.user import User, UserRepository

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
        tour_name="Tour de los puentes",
        tour_desc="La Ría atraviesa Bilbao y deja de ser río para mezclarse con el mar. Es su arteria principal y su última razón de ser. La villa nace para ser un puerto allí donde la Ría dejaba que la cruzasen. Con el paso del tiempo llegaron los puentes bajo los que la Ría recorre su camino acercándose al Abra, al mar.",
        tour_front_image="https://static.elcorreo.com/www/multimedia/201903/17/media/cortadas/bilbao-ria-U70885953289CFD-U70933389644eaG-624x385@El%20Correo-ElCorreo.jpg",
        favourite_tour=False,
        filters=["nature", "history"],
    )

    tour_stop_example = TourStop(
        stop_id="stop_001",
        stop_name="Plaza Circular",
        stop_description="Don Diego López de Haro, Señor de Bizkaia, funda la villa en 1300, y aún la vigila desde lo alto de su monolito en la Plaza Circular rodeado del centro de negocios de esta pujante ciudad. Los tilos dan sombra y perfume a la Gran Vía invitándonos a pasear, a mirar tiendas y a admirar fachadas.",
        before_picture="https://i.pinimg.com/736x/a0/c6/57/a0c657021b83d2edd1c7c26d59c695a9--basque-country-bilbao.jpg",
        before_figcaption="Plaza circular - antes",
        before_alt_text="Plaza circular",
        after_picture="https://abraseguridad.es/wp-content/uploads/2017/12/Edificio-Plaza-Circular.jpg",
        after_figcaption="Plaza circular - actual",
        after_alt_text="Plaza circular",
    )

    tour_stop_example2 = TourStop(
        stop_id="stop_002",
        stop_name="Alameda Urquijo/Bertendona",
        stop_description="Las sedes del Banco de España y del BBVA nos conducen hacia la Alameda Urquijo y a la Residencia, iglesia neogótica de piedra y ladrillo de los Jesuitas, entre fachadas eclécticas y miradores. Continuamos por Urquijo hasta encontrar a nuestra izquierda Bertendona. En esta calle descubrimos el Teatro Campos que parece tener vergüenza de ser diferente, de ser modernista. Contrasta con la rotunda monumentalidad de su vecino, el edificio de Correos, ejemplo de la arquitectura franquista, que sin complejos mira hacia Urquijo.",
        before_picture="https://scontent.fbio1-1.fna.fbcdn.net/v/t1.18169-9/970471_412930742161727_1705928822_n.jpg?_nc_cat=108&ccb=1-5&_nc_sid=9267fe&_nc_ohc=7Gg1qcGm7c4AX-5nFlS&_nc_ht=scontent.fbio1-1.fna&oh=00_AT-0-6rhE19UyW-tQj750z4aVj3HrIvjVPbUaesbC7vn7Q&oe=626B72EC",
        before_figcaption="Alameda Urquijo - antes",
        before_alt_text="Alameda Urquijo",
        after_picture="https://bilbaoarquitecturayurbanismo2ohome.files.wordpress.com/2019/11/p1080368.jpg",
        after_figcaption="Alameda Urquijo - actual",
        after_alt_text="Alameda Urquijo",
    )

    tour_stop_example3 = TourStop(
        stop_id="stop_003",
        stop_name="Teatro Campos Elíseos",
        stop_description="El Teatro Campos Elíseos forma parte de la vida de Bilbao desde 1902, cuando se inauguró en lo que aquel entonces era el solar de los ‘Jardines de los Campos Elíseos’. Obra del arquitecto Alfredo Acebal y el decorador francés Jean Batiste Darroguy (quien diseñó su característica fachada), el edificio modernista está hoy catalagado como Bien de Interés Cultural. En plena expansión económica, urbanística y cultural de Bilbao, pronto el teatro, conocido ya como ‘la bombonera de Bertendona’, se convirtió en una de las salas de mayor categoría artística, y en la plataforma escénica que impulsó con mayor acierto la pujante ópera vasca, – por aquel entonces recién concebida. Además, cultivaba la programación dramática, cómica, y de cine, una función a la que terminó por dedicarse en exclusividad. Sin embargo, diversos infortunios, como el atentado que sufrió en 1978 llevaron al Teatro Campos Elíseos a su deterioro y al cese de su actividad. En 2010, un minucioso trabajo de rehabilitación consiguió recuperar en la medida de lo posible el diseño original modernista, a la vez que incrementó espacios y volúmenes. Actualmente la superficie del edificio es de 7300m2, donde conviven dos salas de representación y un centro de formación artístico y tecnológico. La modernización de sus instalaciones incluye además las soluciones tecnológicas más avanzadas para la representación de las artes escénicas. Desde 2017 el teatro está gestionado por Klemark Espectáculos Teatrales con un objetivo claro: devolver a la ciudad de Bilbao la riqueza artística y cultural que ha caracterizado durante años al Teatro Campos Elíseos. Un lugar donde las compañías nacionales e internacionales se den la mano con los artistas vascos, atendiendo siempre a la máxima calidad de sus espectáculos.",
        before_picture="https://i.pinimg.com/originals/3a/26/ce/3a26cef27dcea9e511b1ce2533b94529.jpg",
        before_figcaption="Teatro Campos Elíseos - antes",
        before_alt_text="Teatro Campos Elíseos - antes",
        after_picture="https://images.adsttc.com/media/images/5128/a0e8/b3fc/4b11/a700/4a97/large_jpg/1284057850-mg-0006modb.jpg?1414370082",
        after_figcaption="Teatro Campos Elíseos - actual",
        after_alt_text="Teatro Campos Elíseos",
    )

    tour_stop_example4 = TourStop(
        stop_id="stop_004",
        stop_name="Plaza Moyua",
        stop_description="En esta plaza, fuente y jardines son rodeados de ejemplos del eclecticismo, del racionalismo, del fascismo o de las últimas construcciones de la arquitectura moderna. El palacio Chavarri, neoflamenco o el hotel Carlton, segundo imperio francés, visten de solemnidad este centro neurálgico de las compras en Bilbao. Ocho calles que son cuatro, se encuentran aquí; por la Alameda Rekalde, y hacia la Ría, salimos de la plaza.",
        before_picture="https://live.staticflickr.com/65535/51622226022_75dcf748e5_k.jpg",
        before_figcaption="Plaza Moyua - 1960",
        before_alt_text="foto de plaza moyua en 1960",
        after_picture="https://www.destinoseuskadi.com/wp-content/uploads/2016/11/Plaza-Moyua-1200x591.jpg",
        after_figcaption="Plaza Moyua - actual",
        after_alt_text="foto de plaza moyua actual",
    )

    tour_stop_example5 = TourStop(
        stop_id="stop_005",
        stop_name="Puente de San Antón",
        stop_description="Al lado de esta iglesia, aunque no donde estuvo durante siglos, se levanta parte del escudo de Bilbao: iglesia y puente de San Antón, con sus lobos. Por aquí entraban las acémilas de mulas y volvían a Castilla con las mercancías de otras tierras y el hierro vizcaíno. Cruzamos este puente como lo hicieron tantos mercaderes y bajamos hasta el Muelle de Marzana por una escalera lateral.",
        before_picture="https://soka.gitlab.io/bilbi100urte/Callejero/Puente-San-Anton/img/San-Anton-22.jpg",
        before_figcaption="Puente de San Antón - antes",
        before_alt_text="Foto antigua del puente de San Antón",
        after_picture="https://www.xn--cafalasdoce-dbb.com/wp-content/uploads/2017/02/P2118823-01.jpg",
        after_figcaption="Puente de San Antón - actual",
        after_alt_text="Foto actual del puente de San Antón",
    )

    tour_stop_example6 = TourStop(
        stop_id="stop_006",
        stop_name="Puente de la Ribera",
        stop_description="Paseando por el Muelle de Marzana vemos las traseras solemnes de las casas de Bilbao la Vieja, cuyos bajos acogen la cocina hecha arte o parte de la modernidad de la villa. El Mercado de la Ribera, en la otra orilla, como un barco varado en el viejo puerto, esperando a zarpar repleto de puestos y vida. Llegamos ante el heredero del puente de la canción: No hay en el mundo Puente Colgante más elegante que el de Bilbao... Hoy mucho más modesto después de ser destruido y reconstruido en más de una ocasión.",
        before_picture="https://live.staticflickr.com/1749/41840904895_34e0cf38bd_z.jpg",
        before_figcaption="Puente de la Ribera - 1938",
        before_alt_text="Foto antigua puente de la Ribera",
        after_picture="http://fotos.elcorreo.com/200911/_dsc0216_7_8-correo.jpg",
        after_figcaption="Puente de la Ribera - actual",
        after_alt_text="Foto actual puente de la Ribera",
    )
    tour_stop_example7 = TourStop(
        stop_id="stop_007",
        stop_name="Puente de Deusto",
        stop_description="La universidad de Deusto, literaria junto a la Ría y comercial en un jardín, llega hasta el puente, que aún espera ser abierto para dejar pasar los barcos, camino de los viejos amarraderos o la gabarra cargada de la ilusión de un pueblo que siente deboción por el Athletic de Bilbao. La Torre Iberdrola, sobre nosotros, señala el cielo de Bilbao",
        before_picture="https://fotos01.deia.eus/2020/02/02/690x278/fotos-3.jpg",
        before_figcaption="Puente de Deusto- antes",
        before_alt_text="Foto antigua puente de Deusto",
        after_picture="https://i.pinimg.com/originals/c0/f7/97/c0f797b33d5b803a44480f799e77aaca.jpg",
        after_figcaption="Puente de Deusto - actual",
        after_alt_text="Foto actual puente de Deusto",
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
    tour_repository.save_tour_stop(tour_stop_example7)

    tour_repository.save_tour_stops_to_tour(
        "tour_001", ["stop_001", "stop_002", "stop_003", "stop_004"]
    )
    tour_repository.save_tour_stops_to_tour(
        "tour_002", ["stop_005", "stop_006", "stop_007"]
    )

    user_repository = UserRepository(database_path)

    user_repository.save(User(id="user-1", name="admin-1", password="12345"))
    user_repository.save(User(id="user-2", name="admin-2", password="54321"))


if __name__ == "__main__":
    main()
