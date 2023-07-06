<template>
  <div class = "global">
  <div class="compras">
    <table>
      <thead>
        <tr>
          <th>Código</th>
          <th>Vendedor</th>
          <th>Nombre</th>
          <th>Precio</th>
          <th>Marca</th>
          <th>Categoría</th>
          <th></th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="producto in productos" :key="producto.codigo">
          <td>{{ producto.codigo }}</td>
          <td>{{ producto.usuario_nombre }}</td>
          <td>{{ producto.nombre }}</td>
          <td>{{ producto.precio }}</td>
          <td>{{ producto.marca }}</td>
          <td>{{ producto.tipo }}</td>
          <td><button class="comprar-button" @click="comprar(producto.codigo, producto.usuario_nombre)">Comprar</button></td>
        </tr>
      </tbody>
    </table>
  </div>
  <nav>
    <router-link to="/home" class="casa-link">Casa</router-link>
  </nav>
  </div>
</template>

<script>
export default {
  name: "ComprasView",
  data() {
    return {
      productos: []
    };
  },
  methods: {
    async obtener_productos() {
      let usuario_p = {
        usuario: this.$store.state.mi_usuario
      };
      await fetch(`http://LB-ProyParcial-1528179989.us-east-1.elb.amazonaws.com:8001/utecshop/tienda`, {
        method: "POST",
        headers: {
          "Content-type": "application/json"
        },
        body: JSON.stringify(usuario_p)
      })
        .then((resp) => resp.json())
        .then((datos) => (this.productos = datos));
    },
    async comprar(codigo_p, usuario_v) {
      let n_compra = {
        codigo_producto: codigo_p,
        usuario_comprador: this.$store.state.mi_usuario,
        usuario_vendedor: usuario_v
      };
      await fetch(`http://LB-ProyParcial-1528179989.us-east-1.elb.amazonaws.com:8001/utecshop/registrar_compra`, {
        method: "POST",
        headers: {
          "Content-type": "application/json"
        },
        body: JSON.stringify(n_compra)
      });
      alert("Producto comprado");
      this.$router.push("/productos");
    }
  },
  created() {
    this.obtener_productos();
  }
};
</script>

<style scoped>
.compras {
  margin-top: 20px;
}

table {
  width: 100%;
  border-collapse: collapse;
}

th,
td {
  padding: 10px;
  text-align: left;
  border-bottom: 1px solid #ddd;
}

th {
  background-color: #f2f2f2;
}

nav {
  margin-top: 20px;
}

nav a.casa-link {
  padding: 5px 10px;
  border: none;
  border-radius: 5px;
  background-color: #007bff;
  color: #fff;
  text-decoration: none;
  transition: background-color 0.3s ease;
}

nav a.casa-link:hover {
  background-color: #0056b3;
}

.global {
  position: relative;
  background-image: url('../assets/fondotablas.jpg');
  background-size: cover;
  opacity: 0.9;
  height: 100vh;
}

.compras {
  margin-top: 20px;
  background-color: rgba(255, 255, 255, 0.7);
  padding: 10px;
  border-radius: 10px;
}

table {
  width: 100%;
  border-collapse: collapse;
  margin-bottom: 20px;
}

th,
td {
  padding: 20px;
  border-bottom: 1px solid #ddd;
  text-align: left;
  color: #000000;
}

th {
  background-color: #f2f2f2;
  font-weight: bold;
}

button.comprar-button {
  padding: 10px 20px;
  background-color: #000;
  color: #fff;
  text-decoration: none;
  border-radius: 4px;
  font-family: 'BebasNeue-Regular', sans-serif;
  font-size: 18px;
  border: none;
  transition: background-color 0.3s ease;
}

button.comprar-button:hover {
  background-color: #555;
}

button.comprar-button:active {
  background-color: #333;
}
</style>