<template>
    <div class="container">
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
.modify-form{
  background-color: lightgrey;
  display: flex;
  flex-direction: column;
  padding: 1em;
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  width: 85%;
  
 
}
.modify-form form{
  display: flex;
  flex-direction: column;
  
}
.modify-form .filters-box{
  display: flex;
  flex-wrap: wrap;
}
.modify-form .filters-box p{
  width: 100%;
  margin-bottom: 0.4em;
}
.modify-form .filters-box input{
  margin: 0 0.8em 0 0.2em;
  
}
.modify-form .btn{
  align-self: center;
  margin-top: 2em;
}
.modify-form input, textarea{
  padding: 0.6em;
  
}

@media (min-width:800px){

 .modify-form{
   max-width: 750px;
 }

}


</style>