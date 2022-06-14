<template>
  <div class="add-tours-page">
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
    <p>Filtros</p>
    
    <label for="arquitechture">Arquitectura</label>
    <input type="checkbox" value="arquitechture" id="arquitechture" v-model="tour.filters">
    <label for="history">Historia</label>
    <input type="checkbox" value="history" id="history" v-model="tour.filters">
    <label for="nature">Naturaleza</label>
    <input type="checkbox" value="nature" id="nature" v-model="tour.filters">


    </form>
    <button @click.prevent="onSaveTourClicked">Guardar e ir a añadir stops</button>

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

      this.$router.push("/");
    },
  },



  
}
  
  
</script>

<style scoped>


</style>