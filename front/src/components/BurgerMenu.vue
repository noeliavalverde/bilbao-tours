<template>
  <div id="burger-menu" v-bind:class="isOpenMenu">
    <button id="open-menu-btn" class="btn">
            
            
                <span class="bar"></span>
                <span class="bar"></span>
                <span class="bar"></span>

           

    </button>
    <nav id="main-nav">
        <router-link to="/">Home</router-link>
        <router-link to="/tours">Tours</router-link>
    </nav>
  </div>
  
</template>

<script>
export default {
    name:"BurgerMenu",
    data() {
        return{
        isOpenMenu: true,
        }
    }

}
</script>

<style scoped>
#burger-menu{
background-color: rgb(19, 19, 65);
color: white;
}
#main-nav{
    display: flex;
    flex-direction: column;
    text-align: center;
    padding: 5em 0;
    font-size: 1.5em;
    min-height: 100vh;
    justify-content: center;
    
}

#open-menu-btn{
    width: 34px;
    height: 34px;
    background-color: transparent;
    border: none;
    display: flex;
    flex-direction: column;
    justify-content: space-evenly;
    margin: 0 .8em 0 auto;
    padding-top:4em ;
    position: relative;
}

#open-menu-btn .bar{
    width: 100%;
    height: 2px;
    background-color: white;
    display: block;
}

/*Estilo menu abierto*/
#burger-menu.isOpenMenu #open-menu-btn{
    
}
#burger-menu.isOpenMenu #open-menu-btn .bar:nth-child(2){
    visibility: hidden;
}
#burger-menu.isOpenMenu #open-menu-btn .bar:nth-child(1){
    transform-origin: 50%;
    transform: translateY(-50%) rotate(45deg);
    position: absolute;
    top: 50%;
    left: 0;
}

#burger-menu.isOpenMenu #open-menu-btn .bar:nth-child(3){
    transform-origin: 50%;
    transform: translateY(-50%) rotate(-45deg);
    position: absolute;
    top: 50%;
    left: 0;
}

</style>