<template>
  <div class="add-tours-page container">
    <section class="add-tour-form">
      <h1>Añadir nueva visita</h1>
      <form>
      <label for="stop-name">Nombre de la vista</label>
      <input type="text" id="stop-name" v-model="stop.stop_name">
      <br />
      <label for="stop-description">Descripción</label>
      <textarea id="stop-description" v-model="stop.stop_description">Escriba aquí la descripción de la visita</textarea>
      <br />
      <label for="before-image">Foto antigua</label>
      <input type="text" v-model="stop.before_picture" id="before-image">
      <br />
      <label for="before-figcaption">Leyenda foto antigua</label>
      <input type="text" id="before-figcaption" v-model="stop.before_figcaption">
      <br />
      <label for="before-alt-text">Breve descripción de la foto antigua</label>
      <input type="text" id="before-alt-text" v-model="stop.before_alt_text">
      <br />
      <label for="after-image">Foto actual</label>
      <input type="text" v-model="stop.after_picture" id="after-image">
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

    
    isValidTourData() {
      if (
        this.stop.stop_name === "" ||
        this.stop.stop_description === "" ||
        this.stop.before_picture === "" ||
        this.stop.after_picture === ""
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

      this.$router.push("/admin/manage-tours");
    },
  },



  
}

</script>