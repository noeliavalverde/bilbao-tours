<template>
  <div class="tours-list-page container">
    <article class="tour-index-box" v-for="tour in tours" :key="tour.tour_id">
        <h3>{{tour.tour_name}}</h3>
        <figure class="front-img-wrapper"><img :src="tour.tour_front_image" alt=""></figure>
        <section class="tour-card-text">
          <p>{{tour.tour_desc}}</p>
          <router-link :to="`/tours/${tour.tour_id}`" class="btn tour-detail-btn">Ver ruta</router-link>
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
.container{
  background-color: rgb(181, 178, 178);
  min-height: 100vh;
}
img{
  display: block;
  width: 100%;
  height: 100%;
  object-fit: cover;
}
.front-img-wrapper{
  width: 100%;
  padding-top: 100%;
  position: relative;
  overflow: hidden;
}

.front-img-wrapper img{
  position: absolute;
  top: 0;
  left: 0;
  z-index: 10;
}

.tour-index-box{
  position: relative;
  height: 100%;
  
}

.tour-card-text{
  position: absolute;
  bottom: 0;
  left: 0;
  background-color: rgba(17, 2, 100, 0.644);
  color: lightblue;
  font-size: 0.9rem;
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  justify-content: space-between;
  z-index: 30;
  width: 100%;
  padding: 0.6em 1.2em;
  box-shadow: 0px 0px 31px 3px rgba(10,3,46,0.75) inset;
}
.tour-index-box h3{
  width: 100%;
  position: absolute;
  top: 0;
  left: 0;
  z-index: 50;
  font-weight: 500;
  font-size: 1.5em;
  background-color: rgba(239, 235, 230, 0.361);
  padding: 0.5em 0.8em;
  box-shadow: 0px 0px 31px 3px rgba(152, 150, 167, 0.75) inset;
  text-align: center;
  text-transform: uppercase;
  color:rgb(2, 2, 22);
  text-shadow: 5px 5px 10px rgba(2,2,22,0.6);
}
.tour-card-text p{
  text-align: justify;
  width: 75%;
}

.tour-detail-btn{
  border: 1px solid lightblue;
  color: rgb(2, 2, 22);
  background-color: lightblue;
  padding: 0.4em 0.5em;
  border: 1px solid lightblue; 
  font-weight: bold;
  font-size: 1.2em;
}
.tour-detail-btn:hover{
  color: lightblue;
  background-color: rgb(2, 2, 22);
}

@media (min-width:550px){

.container{
 
  padding: 2em 0;
}

.tour-index-box{
  width:85%;
  margin: 0 auto 2em;
  box-shadow: 0px 0px 18px 5px rgba(0,0,0,0.75);
  max-width: 600px;
  
}

}
@media (min-width:850px){
 
 
 .tour-index-box{
   width: 48%;
  }

 .tours-list-page{
   display: flex;
   flex-wrap: wrap;
 }
}

@media (min-width:1550px){
 
 
 .tour-index-box{
   width: 32%;
 }
}
</style>