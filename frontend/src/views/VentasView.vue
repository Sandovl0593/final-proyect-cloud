<template>
  <div class="page-background">
  <div class="ventas">
    <table class="table">
      <thead>
        <tr>
          <th>Nombre</th>
          <th>Precio</th>
          <th>Marca</th>
          <th>Categoría</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="producto of productos" :key="producto.codigo_p">
          <td>{{ producto.nombre }}</td>
          <td>S/ {{ producto.precio }}</td>
          <td>{{ producto.marca }}</td>
          <td>{{ producto.categoria }}</td>
        </tr>
      </tbody>
    </table>
  </div>
  <nav>
    <router-link to="/registrar_producto" class="button">Registrar producto</router-link> |
    <router-link to="/home" class="button">Casa</router-link>
  </nav>
  </div>
</template>

<script>
export default {
  name: "VentasView",
  data() {
    return {
      productos: [],
    };
  },
  methods: {
    async obtener_productos() {
      let usuario_p = { usuario: this.$store.state.mi_usuario };
      await fetch(`https://n9h5lbsqu4.execute-api.us-east-1.amazonaws.com/prod/productos`, {
        method: "POST",
        headers: {
          "Content-type": "application/json",
        },
        body: JSON.stringify(usuario_p),
      })
        .then((resp) => resp.json())
        .then(data => {
          this.productos = JSON.parse(data);
          this.filtrarProductos();
      });
    },
    filtrarProductos() {
      const nombreUsuarioEspecifico = this.$store.state.mi_usuario;
        this.productos = this.productos.reduce((resultado, elemento) => {
          if (elemento.username === nombreUsuarioEspecifico) {
            resultado.push(elemento);
          }
          return resultado;
        }, []);
    },
  },
  created() {
    this.obtener_productos();
  },
};
</script>

<style scoped>
/* Clase global para el fondo de la página */
.page-background {
  background-image: url('../assets/fondorojotablas.jpg');
  background-size: cover;
  opacity: 0.9;
  background-position: center;
  height: 100vh;
}

.ventas {
  margin-top: 20px;
}

.table {
  width: 100%;
  border-collapse: collapse;
  margin-bottom: 20px;
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


tbody {
  background: rgba(255, 233, 233, 0.829);
}

nav a.button {
  padding: 12px 24px;
  background-color: #000;
  color: #fff;
  text-decoration: none;
  border-radius: 50px;
  font-family: 'BebasNeue-Regular', sans-serif;
  font-size: 18px;
  border: none;
  transition: background-color 0.3s ease;
  width: 150px;
}

.button:hover {
  background-color: #0056b3;
  transform: scale(1.1);
}

.button:active {
  background-color: #555;
}
</style>