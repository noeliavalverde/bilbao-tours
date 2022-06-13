<template>
  <div class="login-page">
    
    <form>
    <label for="user-name">Nombre de usuario</label>
    <input type="text" id="user-name" placeholder="username" v-model="user">
    <label for="password">Contraseña</label>
    <input type="password" id="password" placeholder="password" v-model="password">
    <button class="btn" @click.prevent="onButtonClicked">Entrar</button>
    </form>
  </div>
</template>

<script>
import { useStorage } from "@vueuse/core";
import { login } from "@/services/auth.js";

export default {
  data() {
    return {
      user: "",
      password: "",
      auth: useStorage("auth", {}),
    };
  },
  methods: {
    async onButtonClicked() {
    
      const response = await login(this.user, this.password);
      const loginStatus = response.status;
      console.log("response", response);

      if (loginStatus === 401) {
        alert("unauthorized");
      } else {
        const auth = await response.json();
        console.log("auth", auth);

        this.auth = auth;
        this.$router.push('/admin/manage-tours');
      }
    },
  },
};
</script>

<style>
</style>
