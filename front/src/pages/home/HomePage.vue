<template>
  <div class="home-page container">
    
    <div class="background-cover">
      <main>
        <img src="@/assets/img/logo-white.png" alt="logo B Tours">
        <h1>Visita el pasado y el presente de Bilbao</h1>
        <p>Lorem ipsum, dolor sit amet consectetur adipisicing elit. 
          Repellat maxime nam similique explicabo sint quidem, est rem 
          ut iusto quod harum neque. Totam perferendis provident tempora 
          sint. Saepe, molestiae incidunt!</p>
        <router-link to="/tours"><button class="btn home-btn">Ver rutas</button></router-link>
      </main>
    </div>
    
  </div>
</template>

<script>

export default {
  name: 'Home',
  data() {
    return {
      
    }
  },
  mounted() {
   
  },
  methods: {
    
  }


}
</script>

<style scoped>
.container{
  background-image: url(~@/assets/img/bilbao.jpg);
  background-position: center;
  background-size: cover;

}

.home-page .background-cover{
  width: 100%;
  min-height: 100vh;
  background-color: rgba(250, 235, 215, 0.394);
  position: relative;
}
.home-page main{
  background-color: rgba(2, 2, 127, 0.508);
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 2.3em 1em;
  width: 100%;
  color:antiquewhite;
  max-width: 500px; 

}
.home-page img{
  width: 40%;
}
.home-page h1{
  font-size: 1.4em;
  font-weight: 500;
  font-style: italic;
  text-align: center;
  margin: 0.6em 0;
}
.home-page p{
  text-align: center;
}
.home-page .home-btn{
  border: 1px solid antiquewhite;
  background-color: rgb(250, 235, 215);
  text-transform: uppercase;
  color: rgb(4, 4, 76);
  margin-top: 1.8em;
  font-weight: bold;
  padding: 0.7em 0.9em;

}
.home-page .home-btn:hover{
  
  background-color: rgb(4, 4, 76);
  color: antiquewhite;

}




</style>
