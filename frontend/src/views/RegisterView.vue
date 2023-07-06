<template>
  <div class="global">
  <div class="register-container">
    <h2>Registro</h2>
    <div class="form-group">
      <label>Nombre</label>
      <input type="text" v-model="nombre" v-on:input="registrar_nombre" class="form-control">
    </div>
    <div class="form-group">
      <label>Teléfono</label>
      <input type="text" v-model="telefono" v-on:input="registrar_telefono" lass="form-control">
    </div>
    <div class="form-group">
      <label>Dirección</label>
      <input type="text" v-model="direccion" v-on:input="registrar_direccion" class="form-control">
    </div>
    <div class="form-group">
      <label>Usuario</label>
      <input type="text" v-model="nombre_usuario" v-on:input="registrar_nusuario" class="form-control">
    </div>
    <div class="form-group">
      <label>Email</label>
      <input type="text" v-model="email" v-on:input="registrar_email" class="form-control">
    </div>
    <div class="form-group">
      <label>Contraseña</label>
      <input type="password" v-model="contrasenha" v-on:input="registrar_contrasenha" class="form-control">
    </div>
    <button v-on:click="registrar_usuario" class="btn btn-primary">Registrar</button>
  </div>
  </div>
</template>

<script>
export default {
  name: "RegisterView",
  data() {
    return {
      nombre: "",
      telefono: "",
      direccion: "",
      nombre_usuario: "",
      email: "",
      contrasenha: ""
    }
  },
  methods: {
    casa(){
        this.$store.dispatch("accion_act_usuario", this.nombre_usuario)
        this.$store.dispatch("accion_act_contra", this.contrasenha)
        this.$router.push('/home')
      },
      registrar_nombre(e){
        this.nombre = e.target.value
      },
      registrar_telefono(e){
        this.telefono = e.target.value
      },
      registrar_direccion(e){
        this.direccion = e.target.value
      },
      registrar_nusuario(e){
        this.nombre_usuario = e.target.value
      },
      registrar_email(e){
        this.email = e.target.value
      },
      registrar_contrasenha(e){
        this.contrasenha = e.target.value
      },
      async registrar_usuario(){
        let n_usuario =  {nombre: this.nombre, telefono: this.telefono, direccion: this.direccion,
          nombre_usuario: this.nombre_usuario, email: this.email, contrasenha: this.contrasenha}
        await fetch('http://LB-ProyParcial-1528179989.us-east-1.elb.amazonaws.com:8000/utecshop/register', {
          method: 'POST',
          headers: {
            'Content-type': 'application/json'
          },
          body: JSON.stringify(n_usuario)
        }).then(this.casa)
      }
  }
}
</script>

<style scoped>

.global {
  background-image: url('../assets/foto2.jpg');
  background-size: cover;
  height: 100vh;
  display: flex;
  justify-content: center;
  align-items: center;
}

.register-container {
  width: 25%;
  max-width: 800px;
  margin: 0 auto;
  padding: 100px;
  border-radius: 15px;
  background-color: rgba(255, 255, 255, 0.1);
  backdrop-filter: blur(6px);
}

h2 {
  text-align: center;
  margin-bottom: 20px;
  color: #EFEFEF;
}

.form-group {
  margin-bottom: 15px;
}

label {
  display: block;
  font-weight: bold;
  margin-bottom: 5px;
  color: #EFEFEF;
}

.form-control {
  width: 100%;
  padding: 10px;
  border: 1px solid #ccc;
  border-radius: 4px;
}

.form-control:focus {
  outline: none;
}

.btn {
  padding: 10px 20px;
  border: none;
  border-radius: 19px;
  cursor: pointer;
  font-size: 18px;
}

.btn-primary {
  background-color: #007bff;
  color: #fff;
}

.btn-primary:hover {
  background-color: #0056b3;
}

</style>
