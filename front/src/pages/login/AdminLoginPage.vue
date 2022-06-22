<template>
  <div class="login-page container">
    <main class="login-main">
      <img src="@/assets/img/logo-b-tours.png" alt="logo b-tours app">
      <form>
      <label for="user-name">Usuario</label>
      <input type="text" id="user-name" placeholder="username" v-model="user">
      <label for="password">Contraseña</label>
      <input type="password" id="password" placeholder="password" v-model="password">
      <button class="btn" @click.prevent="onButtonClicked">Entrar</button>
      </form>
    </main>
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

<style scoped>
.container{
  position: relative;
}

.login-main{
  background-color: rgb(192, 197, 208);
  width:80%;
  margin: auto;
  padding: 2em 0;
  position: absolute;
  top: 50%;
  left:50%;
  transform: translate(-50%, -50%);
  box-shadow: 0px 0px 14px 3px rgba(32,12,70,0.75);

}
.login-main label{
  margin-bottom: 0.6em;
}
.login-main input{
  margin-bottom: 1em;
}
.login-main img{
  width: 25%;
  display: block;
  margin: 0 auto 2em;
}

.login-page form{
  display: flex;
  flex-direction: column;
  width: 80%;
  margin: auto;
 
}
.login-page input{
  border: none;
  padding: 0.4em;
}
.login-page label{
  font-weight: bold;
}
.login-page .btn{
  align-self: center;
  background-color: rgba(32,12,70);
  color: rgb(192, 197, 208);
  font-weight: bold;
  border: 1px solid rgba(32,12,70);
  padding: 0.4em 0.6em;
}
.login-page .btn:hover{
  
  background-color: rgb(192, 197, 208);
  color: rgba(32,12,70);
 
}

@media (min-width:550px){

.login-main{
  max-width: 350px;
}

}


</style>
