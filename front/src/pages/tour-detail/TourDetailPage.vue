<template>
  <div class="tour-detail-page">

  <h2>Nombre ruta: {{tour_name}}</h2>
  <h3>Descripción ruta: {{tour_description}}</h3>
  <ul>
    <li>filtros: {{filter}}</li>
  </ul>
  </div>

  <pre>{{$data}}</pre>
</template>

<script>

export default {
  name: 'TourDetailPage',
  data() {
    return {
        tour: {}
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
          
       
    }
     }

  },
}
</script>

<style scoped>

</style>