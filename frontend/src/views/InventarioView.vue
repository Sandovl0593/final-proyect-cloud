<template>
<div class="global">
    <div class="table-container">
      <table class="table">
        <thead>
          <tr>
            <th>Número de compra</th>
            <th>Producto</th>
            <th>Precio</th>
            <th>Vendedor</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="compra of compras" :key="compra.codigo_c">
            <td class="table-data">{{ compra.codigo_c }}</td>
            <td class="table-data">{{ compra.nombre }}</td>
            <td class="table-data">S/ {{ compra.precio }}</td>
            <td class="table-data">{{ compra.usuario_v }}</td>
          </tr>
        </tbody>
      </table>
    </div>
    <nav>
      <router-link to="/home"><button class="button">Casa</button></router-link>
    </nav>
  </div>
  </template>
  
  <script>
  export default {
    name: "InventarioView",
    data(){
      return{
        compras: []
      }
    },
    methods: {
      async obtener_compras(){
        let usuario_c = {usuario: this.$store.state.mi_usuario}
        await fetch(`http://LB-ProyParcial-1528179989.us-east-1.elb.amazonaws.com:8081/utecshop/inventario`, {
          method: 'POST',
          headers: {
            'Content-type': 'application/json'
          },
          body: JSON.stringify(usuario_c)
        }).then((resp)=> resp.json()).then((datos)=> this.compras = datos)
      }
    },
    created(){
      this.obtener_compras()
    }
  }
  </script>
  
  <style scoped>
.global {
  position: relative;
  background-image: url('../assets/fondotablas.jpg');
  opacity: 0.9;
  background-size: cover;
  height: 100vh;
}

.table-container {
  background-color: rgba(255, 255, 255, 0.529);
  padding: 10px;
  border-radius: 10px;
}

.table {
  width: 100%;
  border-collapse: collapse;
  margin-bottom: 20px;
}

.table th,
.table td {
  padding: 20px;
  border-bottom: 1px solid #ddd;
  text-align: left;
  color: #000000;
}

.table th {
  background-color: #f2f2f2;
  font-weight: bold;
}

.table-data {
  color: #fff;
}

.button-container {
  margin-top: 20px;
  text-align: center;
}


nav .button {
  padding: 5px 10px;
  border: none;
  border-radius: 5px;
  background-color: #007bff;
  color: #fff;
  text-decoration: none;
  transition: background-color 0.3s ease;
  font-weight: bold;
}


nav .button {
  padding: 5px 10px;
  border: none;
  font-family: 'BebasNeue-Regular', sans-serif;
  font-size: 18px;
  border-radius: 5px;
  background-color: #007bff;
  color: #fff;
  text-decoration: none;
  transition: background-color 0.3s ease;
}

.button:hover {
  background-color: #0056b3;
}

.button:active {
  background-color: #333;
}
  </style>