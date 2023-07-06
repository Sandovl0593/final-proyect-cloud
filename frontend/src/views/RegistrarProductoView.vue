<template>
  <div class="global">
  <div class="filtro">
  </div>
    <div class="register-container">
      <h2>Registro</h2>
      <div class="form-group">
        <label>Nombre</label>
        <input type="text" v-model="nombre" class="form-control">
      </div>
      <div class="form-group">
        <label>Precio</label>
        <input type="text" v-model="precio" class="form-control">
      </div>
      <div class="form-group">
        <label>Marca</label>
        <input type="text" v-model="marca" class="form-control">
      </div>
      <div class="form-group">
        <label>Categoria</label>
        <input type="text" v-model="categoria" class="form-control">
      </div>
      <button v-on:click="registrar_producto" class="btn btn-primary">Registrar producto</button>
    </div>
  </div>
</template>

<script>
export default {
  name: "RegistrarProductoView",
  data() {
    return {
      codigo: "",
      usuario_nombre: this.$store.state.mi_usuario,
      nombre: "",
      precio: "",
      categoria: "",
      marca: ""
    };
  },
  methods: {
    productos() {
      this.$router.push('/productos');
    },
    registrar_producto() {
      let n_producto = {
        usuario: this.usuario_nombre,
        nombre: this.nombre,
        precio: this.precio,
        marca: this.marca,
        categoria: this.categoria
      };
      fetch(`http://LB-ProyParcial-1528179989.us-east-1.elb.amazonaws.com:8001/utecshop/registrar_producto`, {
        method: 'POST',
        headers: {
          'Content-type': 'application/json'
        },
        body: JSON.stringify(n_producto)
      })
      .then(this.productos);
    }
  }
};
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
.filtro{
  width :100%;
  height: 100%;
  position: absolute;
  top: 0;
  left: 0;
  z-index:1;
   background-color: rgba(0,0,0,0.1);
}

.register-container {
  width: 25%;
  max-width: 800px;
  margin: 0 auto;
  padding: 100px;
  border-radius: 15px;
  background-color: rgba(255, 255, 255, 0.1);
  backdrop-filter: blur(5px);
  z-index:2;
  
  
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
  background-color: #000000;
  color: #fff;
}

.btn-primary:hover {
  background-color: #7F7F7F;
}
</style>
