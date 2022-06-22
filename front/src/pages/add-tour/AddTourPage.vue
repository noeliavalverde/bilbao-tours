<template>
  <div class="add-tours-page container">
    <section class="add-tour-form">
      <h1>Añadir nuevo tour</h1>
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
      <button @click.prevent="onSaveTourClicked" class="btn">Guardar tour</button>
    </section>

  </div>
</template>

<script>
import { addTour } from "@/services/api.js"

export default {
  name: 'AddTourPage',
  data() {
    return {
        tour: { tour_name: "",
            tour_desc: "",
            tour_front_image: "",
            filters:[],}

    }
  },
 
  methods: {

    
    
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

    async onSaveTourClicked() {
      if (!this.isValidTourData()) {
        alert("datos incompletos");
        return;
      }

      await addTour(this.tour);

      alert("Tour guardado exitosamente");

      this.$router.push("/admin/manage-tours");
    },
  },



  
}
  
  
</script>

<style scoped>
.add-tour-form{
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
.add-tour-form form{
  display: flex;
  flex-direction: column;
  
}
.add-tour-form .filters-box{
  display: flex;
  flex-wrap: wrap;
  align-items: center;
}
.add-tour-form .filters-box p{
  width: 100%;
  margin-bottom: 0.4em;
}
.add-tour-form .filters-box input{
  margin: 0 0.8em 0 0.2em;
}
.add-tour-form .btn{
  align-self: center;
  margin-top: 2em;
  color: rgb(243, 245, 249);
  background-color: rgb(2, 2, 22);
  padding: 0.6em 0.7em;
  border: 1px solid rgb(2, 2, 22);; 
  font-weight: bold;
  font-size: 0.8em;
}
.add-tour-form .btn:hover{
  color: rgb(2, 2, 22);
  background-color: rgb(243, 245, 249);
}

.add-tour-form input, textarea{
  padding: 0.6em;
}

@media (min-width:800px){

 .add-tour-form{
   max-width: 750px;
 }

}


</style>