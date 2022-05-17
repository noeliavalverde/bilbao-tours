<template>
  <div class="tours-list-page">
    <h1>Todos los tours</h1>
    <article class="tour-index-box" v-for="tour in tours" :key="tour.tour_id">
        
        <figure class="front-img-wrapper"><img :src="tour.tour_front_image" alt=""></figure>
        <section class="tour-card-text">
          <h3>Nombre del tour: {{tour.tour_name}}</h3>
          <p>Descripción del tour: {{tour.tour_desc}}</p>
          <font-awesome-icon icon="fa-solid fa-circle-heart" />
          <router-link :to="`/tours/${tour.tour_id}`" class="btn tour-detail-btn">Ir a la ruta</router-link>
        </section>
    </article>

    <pre>{{$data}}</pre>
  </div>
</template>

<script>
import { getTours } from "@/services/api.js";

export default {
  name: 'ToursListPage',
  data() {
    return {
      tours: []
    }
  },
  mounted() {
    this.loadData()
  },
  methods: {

    async loadData(){
        // this.tours = [
        //   {"tour_name":"Primer ensanche",
        //   "tour_id":"tour001",
        //   "tour_description":"A principios del siglo XIX la Villa de Bilbao salta la Ría. Las estrechas calles del Casco Viejo se han quedado pequeñas y se diseña una nueva ciudad moderna y luminosa. La burguesía quiere reflejarse en Europa y los modelos a seguir son París y Londres.",
        //   "favorite_tour":true,
        //   "completed":false,
        //   "tour_front_image": "https://www.vigoe.es/wp-content/uploads/2021/11/bilbao.jpg",
        //   "filters":["arquitecture", "industrial"],
        //   "quarter":["Abando"],
        //   "tour_stops":[{"stop_id": "stop001",
        //                  "stop_name":"Plaza Circular",
        //                  "stop_description":"Don Diego López de Haro, Señor de Bizkaia, funda la villa en 1300, y aún la vigila desde lo alto de su monolito en la Plaza Circular rodeado del centro de negocios de esta pujante ciudad. Los tilos dan sombra y perfume a la Gran Vía invitándonos a pasear, a mirar tiendas y a admirar fachadas.",
        //                  "before_picture":"https://i.pinimg.com/736x/a0/c6/57/a0c657021b83d2edd1c7c26d59c695a9--basque-country-bilbao.jpg",
        //                  "after_picture":"https://abraseguridad.es/wp-content/uploads/2017/12/Edificio-Plaza-Circular.jpg",
        //                  },
        //                {"stop_id": "stop002",
        //                 "stop_name":"punto 2",
        //                 "stop_description":"explicación del punto",
        //                 "before_picture":"url",
        //                 "after_picture":"url",
        //                                },
        //                 ]
        //         },
        //   {"tour_name":"Ruta 2",
        //    "tour_id":"tour002",
        //   "tour_description":"Breve explicacion ruta 2",
        //   "favorite_tour":true,
        //   "completed":false,
        //   "tour_front_image":"https://www.65ymas.com/uploads/s1/27/29/61/bigstock-bilbao-spain-may-v-316213297.jpeg",
        //   "filters":["arquitecture", "industrial"],
        //   "quarter":["abando", "casco", "deusto", "uribarri"],
        //   "tour_stops":[{"stop_id": "stop001",
        //                  "stop_name":"punto 1",
        //                  "stop_description":"explicación del punto",
        //                  "before_picture":"url",
        //                  "after_picture":"url",
        //                },
        //                {"stop_id": "stop002",
        //                 "stop_name":"punto 2",
        //                 "stop_description":"explicación del punto",
        //                 "before_picture":"url",
        //                 "after_picture":"url",
        //                },
        //               ]
        //   },
        //        ]

        this.tours = await getTours();
    }
  
    
  },
}
</script>

<style scoped>

img{
  display: block;
}
.front-img-wrapper{
  width: 100%;
  padding-top: 75%;
  position: relative;
  overflow: hidden;
}

.front-img-wrapper img{
  position: absolute;
  top: 0;
  left: 0;
}

.tour-index-box{
  position: relative;
}

.tour-card-text{
  position: absolute;
  bottom: 0;
  left: 0;
  background-color: rgba(17, 2, 100, 0.644);
  color: lightblue;
  font-size: 0.8rem;
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  justify-content: space-between;
  padding: 1em 0.8em;

}
.tour-card-text h3{
  width: 100%;
}
.tour-card-text p{
  text-align: justify;
  width: 75%;
}

.tour-detail-btn{
  border: 1px solid lightblue;
  color: rgb(2, 2, 22);
  background-color: lightblue;
  padding: 0.4em 0.5em;
  border-radius: 6px;
  font-weight: bold;
}

</style>