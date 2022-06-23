<template>
  <div class="add-tour-stops-page container">
    <router-link to="/admin/manage-tours" class="back-link"> ⇐ Volver a lista de tours</router-link>
    <header>
      <h2>{{tour.tour_name}}</h2>
      <p>{{tour.tour_desc}}</p>
      
    </header>

    <main>
      <section class="stops-selector">
        <p>Visitas disponibles</p>
        <select v-model="selectedStop">
          <option disabled selected value="">Elija una visita</option>
          <option id="available-stops" v-for="stop in tour_stops" :key="stop.stop_id">{{stop.stop_name}}</option>
        </select>
        <button @click.prevent="addObjects" class="btn">Añadir al tour</button>
      </section>
      <section class="added-stops">
        <p>Visitas añadidas</p>
        <dl v-for="stop in stops_list" :key="stop.stop_id">
          <dt>{{stop.stop_name}} <button class="btn" @click="deleteStops(stops_list, stop)">X</button></dt>
          <dd>{{stop.stop_description}}</dd>
        </dl>
         <button class="btn confirm-stops" @click.prevent="onSaveStopsClicked">Confirmar cambios</button>
      </section>
    </main>

 

  </div>
</template>

<script>
import { getTourDetail, getTourStops, addTourStops } from "@/services/api.js"


export default {
  name: 'AddTourPage',
  data() {
    return {
        tour: {},
        tour_stops:[],
        stops_list:[],
        selectedStop:"",
        data_to_send:[]

    }
  },
  mounted() {
    this.loadData()
  
  },

  computed: {
    

  },

  methods: {

    async loadData(){
        let tourId = this.$route.params.tour_id;
        this.tour = await getTourDetail(tourId);
        this.tour_stops = await getTourStops();
    },

    addObjects(){
        for (let item of this.tour_stops){
            
            if (item.stop_name === this.selectedStop){
              this.stops_list.push(item)
              this.data_to_send.push(item.stop_id)
              
            }
      }
    
        
    },
    deleteStops(object, item){
      
      let indice = object.indexOf(item)
      object.splice(indice,1)
      
      this.data_to_send.splice(indice, 1)
      
    },
 

    async onSaveStopsClicked() {
        
        
        await addTourStops(this.$route.params.tour_id, this.data_to_send);

        alert("Tour guardado exitosamente");

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
  margin-bottom: 0.8em;
}

.add-tour-stops-page{
  background-color: rgb(192, 197, 208);
  padding: 2em;
  width: 95%;
  max-width: 1150px;
  margin: 3em auto;
  
}
.add-tour-stops-page header h2{
  font-size: 1.5em;
  font-weight: 500;
  text-align: center;
  background-color: rgb(2, 2, 22);
  color: lightblue; 
  padding: 0.6em 0;
  margin-bottom: 0.5em;
}
.add-tour-stops-page header{
  border: 1px solid rgb(2, 2, 22);
  background-color: rgb(243, 245, 249);
  margin-bottom: 0.8em;
}
.add-tour-stops-page header p{
  padding: 1.5em 0.6em;
}

.stops-selector {
  background-color: rgb(243, 245, 249);
  border: 1px solid rgb(2, 2, 22);
  padding: 1.5em 0.6em;
  display: flex;
  flex-direction: column;
  font-weight: bold;
  font-size: 1.1em;
  margin-bottom: 1.5em;
}
.stops-selector select{
  padding: 0.3em;
  margin: 1em 0 1em;
}

.btn{
  border: 1px solid lightblue;
  color: rgb(243, 245, 249);
  background-color: rgb(2, 2, 22);
  padding: 0.4em 0.5em;
  border: 1px solid rgb(2, 2, 22);; 
  font-weight: normal;
  font-size: 0.8em;
}
.btn:hover{
  color: rgb(2, 2, 22);
  background-color: rgb(243, 245, 249);
}

.added-stops{
  background-color: rgb(243, 245, 249);
  border: 1px solid rgb(2, 2, 22);
  padding: 1.5em 0.6em;
}
.added-stops p{
  font-weight: bold;
  font-size: 1.1em;
  margin-bottom: 1em;
}

.added-stops dt{
 padding: 0.3em;
 background-color: rgb(184, 182, 182);
 display: flex;
 justify-content: space-between;
 align-items: center;
 font-weight: 500;
}
.added-stops dd{
 font-weight: 500;
 max-height: 150px;
 border:1px solid rgb(2, 2, 22);
 overflow-y: scroll;
 background-color: rgb(243, 245, 249);
 margin-bottom: 1em;
 padding: 0.3em;
}
.added-stops .confirm-stops{
  font-weight: bold;
  margin: 0 auto;
  display: block;
  font-size: 1em;
}

</style>