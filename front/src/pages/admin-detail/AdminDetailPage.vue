<template>
  <div class="tour-detail-page container">
  <header class="detail-header">
    <router-link to="/admin/manage-tours" class="btn backlink">⇐ Volver a lista de tours</router-link>
    
    <h2>{{tour.tour_name}}</h2>
    <h3>{{tour.tour_desc}}</h3>
    <div class="filters-box">
      <p>Filtros: </p>
      <ul>
        <li v-for="filter in tour.filters" :key="filter">{{filter}} </li>
      </ul>
    </div>
  </header>
  

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
   <nav>
  <button class="btn">
            <router-link :to="`/admin/manage-tours/modify-tour/${tour.tour_id}`">Modificar</router-link>
          </button>
          <button class="btn"><router-link :to="`/admin/manage-tours/add-tour-stops/${tour.tour_id}`">Añadir visitas</router-link></button>
          <button class="btn remove-btn" @click="removeTour(tour)">Eliminar</button>
          
</nav>
  </div>

</template>


<script>

import { getTourDetail } from "@/services/api.js";
import { deleteTour } from "@/services/api.js";

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
     async removeTour(tour) {
      
      this.tour = await deleteTour(tour);
      this.$router.push("/admin/manage-tours");
  
  },

  },
}
</script>

<style scoped>
.container{
  background-color: rgb(242, 233, 233);
  text-align: justify;
  
}
.tour-detail-page .backlink{
  display: block;
  margin-left: auto;
  margin-bottom: 0.8em;
  text-decoration: underline;
  font-weight: 600;
  font-size: 1.2em;
  background-color: rgb(192, 197, 208);
  color: rgba(32,12,70);
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

.filters-box{
  max-width: 1000px;
  margin: 0 auto 2em;
  padding: 0 3em;
}
.filters-box ul{
  display: flex;
}
.filters-box ul li{
  margin-right: 1em;
  padding-right: 1em;
  border-right: 1px solid black;
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

nav{
  padding: 2em 0 3em;
  text-align: center;
}
nav *{
  margin-right: 0.5em;
}
nav:last-child a{
  margin-right: 0;
}
.remove-btn{
  padding: 0.5em 0.7em;
}
.btn{
  background-color: rgba(32,12,70);
  color: rgb(192, 197, 208);
  border: 1px solid rgba(32,12,70);
  font-weight: bold;
  
}

.btn:hover{
  
  background-color: rgb(192, 197, 208);
  color: rgba(32,12,70);
 
}


</style>