<template>
    <div class="container">
      <router-link to="/admin/manage-tours" class="back-link"> ⇐ Volver a lista de tours</router-link>
    <section class="modify-form">
      <h1>Modificar tour</h1>
      <form>
      <label for="tour-name">Nombre del tour</label>
      <input type="text" id="tour-name" v-model="tour.tour_name">
      <br />
      <label for="tour-description">Descripción</label>
      <textarea id="tour-description" v-model="tour.tour_desc">Escriba aquí la descripción del tour</textarea>
      
      <br />
      <label for="front-image">Foto de portada</label>
      <input type="text" v-model="tour.tour_front_image" id="front-image">
      <br />
      <div class="filters-box">
        <p>Filtros: </p>
        
        <label for="arquitecture">Arquitectura</label>
        <input type="checkbox" value="arquitecture" id="arquitecture" v-model="tour.filters">
        <label for="history">Historia</label>
        <input type="checkbox" value="history" id="history" v-model="tour.filters">
        <label for="nature">Naturaleza</label>
        <input type="checkbox" value="nature" id="nature" v-model="tour.filters">
      </div>
      </form>
      <button @click.prevent="onModifyTourClicked(tour)" class="btn">Modificar</button>
    </section>
 </div>
</template>

<script>

import { getTourDetail, modifyTour } from "@/services/api.js";


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

    isValidTourData() {
      if (
        this.tour.tour_name === "" ||
        this.tour.tour_desc === "" ||
        
        this.tour.filters === ""
      ) {
        return false;
      } else {
        return true;
      }
    },

    async onModifyTourClicked() {
      if (!this.isValidTourData()) {
        alert("datos incompletos");
        return;
      }

      await modifyTour(this.tour);

      alert("Tour modificado con éxito");

      this.$router.push("/admin/manage-tours");
    },

  },
}
</script>

<style scoped>
.back-link{
  text-decoration: underline;
  text-align: right;
  font-weight: 500;
  margin: 1em;
}
.modify-form{
  background-color: lightgrey;
  display: flex;
  flex-direction: column;
  padding: 1em;
  width: 85%;
  margin: 0 auto;
  
 
}
.modify-form form{
  display: flex;
  flex-direction: column;
  
}
.modify-form .filters-box{
  display: flex;
  flex-wrap: wrap;
  align-items: center;
}
.modify-form .filters-box p{
  width: 100%;
  margin-bottom: 0.4em;
}
.modify-form .filters-box input{
  margin: 0 0.8em 0 0.2em;
  
}
.modify-form .btn{
  margin-top: 2em;
  align-self: center;
  background-color: rgba(32,12,70);
  color: rgb(192, 197, 208);
  font-weight: bold;
  border: 1px solid rgba(32,12,70);
  padding: 0.4em 0.6em;
}
.modify-form .btn:hover{
  background-color: rgb(192, 197, 208);
  color: rgba(32,12,70);
}
.modify-form input, textarea{
  padding: 0.6em;
  
}
.modify-form textarea{
  min-height: 10em;
  
}

@media (min-width:800px){

 .modify-form{
   max-width: 750px;
 }

}


</style>