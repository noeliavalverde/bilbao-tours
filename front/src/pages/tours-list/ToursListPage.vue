<template>
  <div class="tours-list-page">
    <h1>Todos los tours</h1>
    <article class="tour-index-box" v-for="tour in tours" :key="tour.tour_id">
        
        <h3>Nombre del tour: {{tour.tour_name}}</h3>
        <p>Descripción del tour: {{tour.tour_description}}</p>
        <router-link :to="`/tours/${tour.tour_id}`">Ir a la ruta</router-link>
    </article>

    <pre>{{$data}}</pre>
  </div>
</template>

<script>

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

    loadData(){
        this.tours = [
          {"tour_name":"Primer ensanche",
          "tour_id":"tour001",
          "tour_description":"A principios del siglo XIX la Villa de Bilbao salta la Ría. Las estrechas calles del Casco Viejo se han quedado pequeñas y se diseña una nueva ciudad moderna y luminosa. La burguesía quiere reflejarse en Europa y los modelos a seguir son París y Londres.",
          "favorite_tour":true,
          "completed":false,
          "filters":["arquitecture", "industrial"],
          "quarter":["Abando"],
          "tour_stops":[{"stop_id": "stop001",
                         "stop_name":"Plaza Circular",
                         "stop_description":"Don Diego López de Haro, Señor de Bizkaia, funda la villa en 1300, y aún la vigila desde lo alto de su monolito en la Plaza Circular rodeado del centro de negocios de esta pujante ciudad. Los tilos dan sombra y perfume a la Gran Vía invitándonos a pasear, a mirar tiendas y a admirar fachadas.",
                         "before_picture":"https://i.pinimg.com/736x/a0/c6/57/a0c657021b83d2edd1c7c26d59c695a9--basque-country-bilbao.jpg",
                         "after_picture":"https://abraseguridad.es/wp-content/uploads/2017/12/Edificio-Plaza-Circular.jpg",
                         },
                       {"stop_id": "stop002",
                        "stop_name":"punto 2",
                        "stop_description":"explicación del punto",
                        "before_picture":"url",
                        "after_picture":"url",
                                       },
                        ]
                },
          {"tour_name":"Ruta 2",
           "tour_id":"tour002",
          "tour_description":"Breve explicacion ruta 2",
          "favorite_tour":true,
          "completed":false,
          "filters":["arquitecture", "industrial"],
          "quarter":["abando", "casco", "deusto", "uribarri"],
          "tour_stops":[{"stop_id": "stop001",
                         "stop_name":"punto 1",
                         "stop_description":"explicación del punto",
                         "before_picture":"url",
                         "after_picture":"url",
                       },
                       {"stop_id": "stop002",
                        "stop_name":"punto 2",
                        "stop_description":"explicación del punto",
                        "before_picture":"url",
                        "after_picture":"url",
                       },
                      ]
          },
               ]
    }
  
    
  },
}
</script>

<style scoped>

</style>