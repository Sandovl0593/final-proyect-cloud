<template>
  <div class="global">
  <div class="login-container">
    <div class="form-group">
      <label for="usuario">Usuario</label>
      <input id="usuario" type="text" v-bind:value="nombre_usuario" v-on:input="verificar_nombre" class="form-control">
    </div>
    <div class="form-group">
      <label for="contrasenha">Contraseña</label>
      <input id="contrasenha" type="password" v-bind:value="contrasenha" v-on:input="verificar_contrasenha" class="form-control">
    </div>
    <button v-on:click="casa" class="btn btn-primary">Iniciar sesión</button>
  </div>
  <nav>
    <router-link to="/registrar">Registrarse</router-link>
  </nav>
  </div>
</template>

<script>
export default {
  name: "LoginView",
  data() {
    return {
      nombre_usuario: "",
      contrasenha: ""
    };
  },
  methods: {
    casa() {
      this.$store.dispatch("accion_act_usuario", this.nombre_usuario);
      this.$store.dispatch("accion_act_contra", this.contrasenha);
      this.$router.push("/home");
    },
    verificar_nombre(e) {
      this.nombre_usuario = e.target.value;
    },
    verificar_contrasenha(e) {
      this.contrasenha = e.target.value;
    },
    async verificar_usuario() {
      let v_usuario = { nombre_usuario: this.nombre_usuario, contrasenha: this.contrasenha };
      await fetch(`http://LB-ProyParcial-1528179989.us-east-1.elb.amazonaws.com:8000/utecshop/login`, {
        method: "POST",
        headers: {
          "Content-type": "application/json"
        },
        body: JSON.stringify(v_usuario)
      })
        .then((resp) => resp.json())
        .then((datos) => {
          if (datos.nombre_usuario === this.nombre_usuario && datos.contrasenha === this.contrasenha) {
            this.casa();
          }
        });
    }
  }
}
</script>
  
<style scoped>

.global{
  background-image: url('../assets/foto1.jpg');
  background-size: cover;
  height: 100vh;
 
}


.login-container {
  max-width: 400px;
  margin: 0 auto;
  padding: 20px;
  border-radius: 5px;
  background-size: cover;
  background-position: center;
 
}

.form-group {
  margin-bottom: 15px;
}

label {
  display: block;
  font-weight: bold;
  margin-bottom: 5px;
  color:#EFEFEF;
}

.form-control {
  width: 100%;
  padding: 10px;
  border: 1px solid #EFEFEF;
  border-radius: 4px;
}

.btn {
  padding: 10px 20px;
  border: none;
  border-radius: 19px;
  cursor: pointer;
  font-size: 18px;
  background-color: #000000;
  color:#fff;
  transition: background-color 0.3s ease;
}

.btn-primary:hover {
  background-color: #7F7F7F;
}

nav a {
  padding: 10px 20px;
  border: none;
  border-radius: 19px;
  cursor: pointer;
  font-size: 18px;
  background-color: #000000;
  color: #fff; /* Cambia el color del enlace "Registrarse" a blanco */
}
</style>