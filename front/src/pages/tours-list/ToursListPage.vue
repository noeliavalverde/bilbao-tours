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
          {"tour_name":"Ruta 1",
          "tour_id":"tour001",
          "tour_description":"Breve explicacion ruta 1",
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