<template>
  <div class="tour-detail-page">

  
  <h2>Nombre ruta: {{tour.tour_name}}</h2>
  <h3>Descripción ruta: {{tour.tour_desc}}</h3>
  <ul v-for="filter in tour.filters" :key="filter">
    <li>filtros: {{filter}}</li>
  </ul>
  

  <section v-for="stop in tour.stops" :key="stop.stop_id" class="stop-wrapper">

    
    <h4>{{stop.stop_name}}</h4>
    <p>{{stop.stop_description}}</p>
    <figure class="image-wrapper"><img :src="stop.before_picture" :alt="stop.before_alt_text">
    <figcaption>{{stop.before_figcaption}}</figcaption>
    </figure>
    <figure class="image-wrapper"><img :src="stop.after_picture" :alt="stop.after_alt_text">
    <figcaption>{{stop.after_figcaption}}</figcaption>
    </figure>
    
  </section>
    <button>Modificar tour</button>
  </div>

</template>


<script>

import { getTourDetail } from "@/services/api.js";

export default {

  name: 'AdminDetailPage',
  data() {
    return {
        tour: {},
        
    }
  },
  mounted() {
    this.loadData()
    
  },
  methods: {
     async loadData(){ 
       let tourId = this.$route.params.tour_id;
       this.tour = await getTourDetail(tourId)

     },

  },
}
</script>

<style scoped>

.stop-wrapper{
  margin-bottom: 2em;
}

</style>