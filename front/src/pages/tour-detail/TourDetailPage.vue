<template>
  <div class="tour-detail-page">

  <h3>{{tours.tour_name}}</h3>
  
  <pre>{{$data}}</pre>
    
  </div>
</template>

<script>

export default {
  name: 'TourDetailPage',
  data() {
    return {
       tours: {"tour_name":"Ruta 1",
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
                }
               
    }
  },
  mounted() {
    
  },
  methods: {
    

  },
}
</script>

<style scoped>

</style>