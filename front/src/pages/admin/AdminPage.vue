<template>
  <div class="tours-list-page container">
    <header>
      <img src="@/assets/img/logo-b-tours.png" alt="logo b-tours app">
     
      
      <nav>
        <router-link to="/admin/manage-stops" class="btn">Gestionar visitas</router-link>
        <router-link to="/admin/manage-tours/add-tour" class="btn">Añadir nuevo tour</router-link>
        
      </nav>
       <h2>Gestionar tours</h2>
    </header>
    
    <article class="tour-index-box" v-for="tour in tours" :key="tour.tour_id">
        
        <section class="tour-card-text">
          <h3>{{tour.tour_name}}</h3>
          <p>{{tour.tour_desc}}</p>
          <p>Imagen de portada:</p>
          <img :src="tour.tour_front_image" alt="imagen de portada">
          <p>Visitas añadidas al tour: </p>
          <p v-if="tour.stops.length === 0 ">No hay ninguna visita añadida</p>
          <ul v-if="tour.stops.length > 0"><li v-for="stop in tour.stops" :key="stop.stop_id">{{stop.stop_name}}</li></ul>
          <button class="btn">
            <router-link :to="`/admin/manage-tours/modify-tour/${tour.tour_id}`">Modificar</router-link>
          </button>
          <button class="btn"><router-link :to="`/admin/manage-tours/add-tour-stops/${tour.tour_id}`">Añadir visitas</router-link></button>
          <button class="btn remove-btn" @click="removeTour(tour)">Eliminar</button>
          <button class="btn">
            <router-link :to="`/admin/manage-tours/${tour.tour_id}`" >Ver detalle</router-link>
          </button>

        </section>
       
    </article>
   

  </div>
</template>

<script>
import { getTours } from "@/services/api.js";
import { deleteTour } from "@/services/api.js";

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

        this.tours = await getTours();
    },

    async removeTour(tour) {
      
      this.tour = await deleteTour(tour);
      location.reload(true);
  
  },
  
    
  },
}
</script>

<style scoped>
.container{
  background-color:rgb(192, 197, 208);
  padding: 3em;

}
.tours-list-page nav{
  display: flex;
  flex-direction: column;
  
}
.tours-list-page nav .btn{
  width: 100%;
  margin-bottom: 0.6em;
  text-align: center;
  
}
.tours-list-page nav a{
  padding: 0.2em 0.4em;
  font-weight: normal;
  
}

.tours-list-page header{
  display: flex;
  flex-direction: row;
  flex-wrap: wrap;
  justify-content: space-between;
  align-items: flex-start;
  
}
.tours-list-page header h2{
  width: 100%;
  margin: 2em 0 1em;
  font-weight: normal;
  color:rgba(32,12,70);
}
.tours-list-page img{
 width: 20%;
 min-width: 100px;  
}

.tour-index-box{
  box-shadow: 0px 0px 14px 3px rgba(187, 194, 211, 0.75);
  padding: 1.5em;
  background-color: rgb(243, 245, 249);
  margin-bottom: 1.5em;
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
.tour-card-text h3{
 
  margin-bottom: 1em;
}
.tour-card-text .btn{
  margin-right: 0.5em;
  margin-top: 1em;
}
.tour-card-text img{
  display: block;
}
.tour-card-text li{
  list-style:inside;
}
.tour-card-text p{
  margin: 0.6em 0;
}
</style>