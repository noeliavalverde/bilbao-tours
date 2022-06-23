<template>
  <div class="tour-detail-page container">
   
    <header class="detail-header">
      <nav><router-link to="/tours" class="btn">⇐ Volver a lista de tours</router-link></nav>
      <h2> {{tour.tour_name}}</h2>
      <h3>{{tour.tour_desc}}</h3>
   
      
    </header>

    <main class="detail-main">
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
    </main>

  </div>

</template>


<script>

import { getTourDetail } from "@/services/api.js";

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
     async loadData(){ 
       let tourId = this.$route.params.tour_id;
       this.tour = await getTourDetail(tourId)
    
     },

  },
}
</script>

<style scoped>
.container{
  background-color: rgb(242, 233, 233);
  text-align: justify;
  
}
.tour-detail-page nav a{
  display: block;
  margin-left: auto;
  text-decoration: underline;
  font-weight: 600;
  font-size: 1.2em;
}

.tour-detail-page nav{
  background-color: rgb(181, 178, 178);
}
figure{
  margin: 1.6em 0;
}
figcaption{
  padding: 1em;
  background-color:rgb(6, 2, 46);
  color: rgb(242, 233, 233);
  font-weight: 500;
}

.detail-header h2{
  font-weight: 500;
  text-transform: uppercase;
  font-size: 1.6em;
  text-align: center;
  padding: 1em 0;
  background-color: rgb(6, 2, 46);
  color: rgb(242, 233, 233)
}
.detail-header h3{
  padding: 2em;
  font-weight: normal;
  font-style: italic;
  margin: 0 auto;
  max-width: 1000px;
  
}

.stop-wrapper{
  padding: 2em;
  width: 95%;
  max-width: 800px;
  margin: 0 auto;
  box-shadow: 6px 6px 18px 3px rgba(40,40,41,0.61);
  margin-bottom: 1em;
}
.stop-wrapper:nth-child(odd){
  background-color: rgb(175, 184, 232);
}
.stop-wrapper:nth-child(even){
  background-color: rgb(217, 221, 243);
}
.stop-wrapper h4{
  margin-bottom: 1em;
  text-align: center;  
}

</style>