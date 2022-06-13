<template>
  <div class="tours-list-page">
    <h1>Gestionar los tours</h1>
    
    <button>Añadir nuevo tour</button>
    
    <article class="tour-index-box" v-for="tour in tours" :key="tour.tour_id">
        
        <section class="tour-card-text">
          <h3>Nombre del tour: {{tour.tour_name}}</h3>
          <p>Descripción del tour: {{tour.tour_desc}}</p>
          <button class="btn">Modificar</button>
          <button class="btn">Eliminar</button>
          <router-link :to="`/admin/manage-tours/${tour.tour_id}`" class="btn">Ver detalle</router-link>

        </section>
    </article>

  </div>
</template>

<script>
import { getTours } from "@/services/api.js";

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
    }
  
    
  },
}
</script>

<style scoped>


</style>