<template>
  <div class="tours-list-page">
    <h1>Gestionar los tours</h1>
    
    <router-link to="/admin/manage-tours/add-tour">Añadir nuevo tour</router-link>
    
    <article class="tour-index-box" v-for="tour in tours" :key="tour.tour_id">
        
        <section class="tour-card-text">
          <h3>Nombre del tour: {{tour.tour_name}}</h3>
          <p>Descripción del tour: {{tour.tour_desc}}</p>
          <button class="btn">Modificar</button>
          <button class="btn" @click="removeTour(tour)">Eliminar</button>
          <router-link :to="`/admin/manage-tours/${tour.tour_id}`" class="btn">Ver detalle</router-link>

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
      console.log(tour)
      this.tour = await deleteTour(tour);
      location.reload(true);
  
  },
  
    
  },
}
</script>

<style scoped>


</style>