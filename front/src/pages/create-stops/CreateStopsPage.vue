<template>
  <div class="add-stop-page container">
    <router-link to="/admin/manage-stops" class="back-link"> ⇐ Volver a lista de visitas</router-link>
    <section class="add-stop-form">
      <h2>Añadir nueva visita</h2>
      <form>
      <label for="stop-name">Nombre de la vista</label>
      <input type="text" id="stop-name" v-model="stop.stop_name">
      <br />
      <label for="stop-description">Descripción</label>
      <textarea id="stop-description" v-model="stop.stop_description">Escriba aquí la descripción de la visita</textarea>
      <br />
      <label for="before-image">Foto antigua</label>
      <input type="file"  @change="setPastImage" accept="image/*" id="before-image">
      <br />
      <label for="before-figcaption">Leyenda foto antigua</label>
      <input type="text" id="before-figcaption" v-model="stop.before_figcaption">
      <br />
      <label for="before-alt-text">Breve descripción de la foto antigua</label>
      <input type="text" id="before-alt-text" v-model="stop.before_alt_text">
      <br />
      <label for="after-image">Foto actual</label>
      <input type="file"  @change="setPresentImage" accept="image/*" id="after-image">
      <br />
      <label for="after-figcaption">Leyenda foto actual</label>
      <input type="text" id="after-figcaption" v-model="stop.after_figcaption">
      <br />
      <label for="after-alt-text">Breve descripción de la foto actual</label>
      <input type="text" id="after-alt-text" v-model="stop.after_alt_text">
      <br />
      
      </form>
      <button @click.prevent="onSaveTourClicked" class="btn">Guardar visita</button>
    </section>

  </div>
</template>

<script>
import { addStop } from "@/services/api.js"

export default {
  name: 'CreateStopsPage',
  data() {
    return {
        stop: { stop_name: "",
                stop_description: "",
                before_picture: "",
                before_figcaption: "",
                before_alt_text: "",
                after_picture: "",
                after_figcaption: "",
                after_alt_text: "",

           }

    }
  },
 
  methods: {

    setPastImage(ev){
      console.log("set image", ev.target.files[0])
      const reader = new FileReader()
      reader.onload = (a) => {this.stop.before_picture = a.target.result}
      reader.readAsDataURL(ev.target.files[0])
    },
    setPresentImage(ev){
      console.log("set image", ev.target.files[0])
      const reader = new FileReader()
      reader.onload = (e) => {this.stop.after_picture = e.target.result}
      reader.readAsDataURL(ev.target.files[0])
    },
    
    isValidTourData() {
      if (
        this.stop.stop_name === "" ||
        this.stop.stop_description === "" 
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

      await addStop(this.stop);

      alert("Visita guardada con éxito");

      this.$router.push("/admin/manage-stops");
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
.add-stop-form{
  background-color: lightgrey;
  display: flex;
  flex-direction: column;
  padding: 1em;
  width: 85%;
  margin: 4em auto;
}

.add-stop-form h2{
  margin-bottom: 0.6em;
}

.add-stop-form form{
  display: flex;
  flex-direction: column;
  
}
.add-stop-form .btn{
  align-self: center;
  margin-top: 2em;
  color: rgb(243, 245, 249);
  background-color: rgb(2, 2, 22);
  padding: 0.6em 0.7em;
  border: 1px solid rgb(2, 2, 22);; 
  font-weight: bold;
  font-size: 0.8em;
}
.add-stop-form .btn:hover{
  color: rgb(2, 2, 22);
  background-color: rgb(243, 245, 249);
}
.add-stop-form input, textarea{
  padding: 0.4em;
}

@media (min-width:800px){

 .add-stop-form{
   max-width: 750px;
 }

}

</style>