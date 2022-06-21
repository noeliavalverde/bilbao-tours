<template>
  <div class="tour-detail-page container">

  
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
.container{
  background-color: rgb(181, 178, 178);
  

}
.stop-wrapper{
  margin-bottom: 2em;
}
.detail-header h2{
  font-weight: 400;
  text-transform: uppercase;
  font-size: 1.6em;
  text-align: center;
  padding: 1em 0;
  background-color: rgb(6, 2, 46);
  color: rgb(181, 178, 178);
}
.detail-header h3{
  padding: 2em;
  font-weight: normal;
  font-style: italic;
}

.detail-main{
  padding: 2em;
}

</style>