<template>
  <div class="stops-list container">
    <header>
      <img src="@/assets/img/logo-b-tours.png" alt="logo b-tours app">
     
      
      <nav>
        <router-link to="/admin/manage-tours" class="btn">Gestionar tours</router-link>
        <router-link to="/admin/manage-tours/create-stops" class="btn">Crear nueva visita</router-link>
      </nav>
       <h2>Gestionar visitas</h2>
    </header>
    <article class="stop-index-box" v-for="stop in tour_stops" :key="stop.stop_id">
      <section class="stop-card-text">

        <div class="stop-header">
          <h3>{{stop.stop_name}}</h3>
          <button class="btn remove-btn" @click="removeStop(stop)">Eliminar</button>
        </div>

        <p>{{stop.stop_description}}</p>
        <p>Imágenes:</p>
        <div class="images-wrapper">
          <figure>
            <img :src="stop.before_picture" :alt="stop.before_alt_text">
            <figcaption>{{stop.before_figcaption}}</figcaption>
          </figure>
          <figure>
            <img :src="stop.after_picture" :alt="stop.after_alt_text">
            <figcaption>{{stop.after_figcaption}}</figcaption>
          </figure>
        </div> 

      </section>
    </article>

  </div>
    
    <pre>{{tour_stops}}</pre>
    <h1>HOLA</h1>
    
</template>

<script>
import { getTourStops, deleteStop } from "@/services/api.js";


export default {
  name: 'AdminStopsPage',
  data() {
    return {
      tour_stops: []
    }
  },
  mounted() {
    this.loadData()
  },
  methods: {

    async loadData(){

        this.tour_stops = await getTourStops();
    },

    async removeStop(stop) {
      
      this.stop = await deleteStop(stop);
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
.stops-list nav{
  display: flex;
  flex-direction: column;
  
}
.stops-list nav .btn{
  width: 100%;
  margin-bottom: 0.6em;
  text-align: center;
  
}
.stops-list nav a{
  padding: 0.2em 0.4em;
  font-weight: normal;
  
}

.stops-list header{
  display: flex;
  flex-direction: row;
  flex-wrap: wrap;
  justify-content: space-between;
  align-items: flex-start;
  max-width: 1100px;
  margin: 0 auto;
  
}
.stops-list header h2{
  width: 100%;
  margin: 2em 0 1em;
  font-weight: normal;
  color:rgba(32,12,70);
}
.stops-list img{
 width: 20%;
 min-width: 100px;  
}

.stop-header{
  display: flex;
  justify-content: space-between;
  align-items: center;
}
.stop-index-box{
  box-shadow: 0px 0px 14px 3px rgba(187, 194, 211, 0.75);
  padding: 1.5em 1.5em 3em;
  background-color: rgb(243, 245, 249);
  margin-bottom: 1.5em;
  max-width: 950px;
  margin: 1.5em auto;
  text-align: justify;
}

.images-wrapper{
  display: flex;
  flex-direction: row;
  justify-content:space-around;
   
}

.images-wrapper img{
  width:100%;
  height: 100%;
  display: block;
  object-fit: cover;
  position: absolute;
  top: 0;
  left: 0;

  }

.images-wrapper figure{
  width: 40%;
  padding-top: 40%;
  position: relative;
  overflow: hidden;
  
}
.images-wrapper figcaption{
  position: absolute;
  top: 90%;
  left: 0;
  z-index: 30;
  background-color: rgb(37, 26, 26);
  padding: 0.3em;
  color: white;
  font-weight: bold;
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
.stop-header{
  padding: 1em 0;
}
.stop-card-text .stop-header .remove-btn{
  padding: 0.5em 0.7em;
  margin: 0;
}

.stop-card-text img{
  display: block;
}
.stop-card-text li{
  list-style:inside;
}
.stop-card-text p{
  margin: 0.6em 0;
}
</style>