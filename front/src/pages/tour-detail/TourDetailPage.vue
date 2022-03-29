<template>
  <div class="tour-detail-page">

  <h2>Nombre ruta: {{tour.tour_name}}</h2>
  <h3>Descripción ruta: {{tour.tour_description}}</h3>
  <ul v-for="(filter, index) in tour.filters" :key="index">
    <li>filtros: {{filter}}</li>
  </ul>
  <p>barrio: {{tour.quarter}}</p>

  <section v-for="(stop, index) in tour.tour_stops" :key="index">

    
    <h4>{{stop.stop_name}}</h4>
    <p>{{stop.stop_description}}</p>
    <img :src="stop.before_picture" alt="">
    <img :src="stop.after_picture" alt="">
  </section>

  </div>

  <pre>{{$data}}</pre>
</template>

<script>

export default {
  name: 'TourDetailPage',
  data() {
    return {
        tour: {},
        
    }
  },
  mounted() {
    this.loadData()
    
  },
  methods: {
     loadData(){
       this.tour = {
       tour_name:"Ruta 1",
       tour_id:"tour001",
       tour_description:"Breve explicacion ruta 1",
       favorite_tour:true,
       completed:false,
       filters:["arquitecture", "industrial"],
       quarter:["abando", "casco", "deusto", "uribarri"],
       tour_stops:[{"stop_id": "stop001",
                    "stop_name":"punto 1",
                    "stop_description":"explicación del punto",
                    "before_picture":"http://especial.elcorreo.com/2017/fotos-ria-bilbao/img/puente-bn.jpg",
                    "after_picture":"http://especial.elcorreo.com/2017/fotos-ria-bilbao/img/puente-color.jpg",
                     },
                    {"stop_id": "stop002",
                     "stop_name":"punto 2",
                     "stop_description":"explicación del punto",
                     "before_picture":"http://especial.elcorreo.com/2017/fotos-ria-bilbao/img/puente-ayuntamiento-bn.jpg",
                     "after_picture":"http://especial.elcorreo.com/2017/fotos-ria-bilbao/img/puente-ayuntamiento-color.jpg",
                     },
                ]
          
       
    }
     },

  },
}
</script>

<style scoped>

</style>