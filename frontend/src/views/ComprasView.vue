<template>
  <div class = "global">
  <div class="compras">
    <table>
      <thead>
        <tr>
          <th>Vendedor</th>
          <th>Nombre</th>
          <th>Precio</th>
          <th>Marca</th>
          <th>Categoría</th>
          <th></th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="producto in productos" :key="producto.codigo_p">
          <td>{{ producto.username }}</td>
          <td>{{ producto.nombre }}</td>
          <td>S/ {{ producto.precio }}</td>
          <td>{{ producto.marca }}</td>
          <td>{{ producto.categoria }}</td>
          <td><button class="comprar-button" @click="comprar(producto.codigo_p, producto.username)">Comprar</button></td>
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
      await fetch(`https://n9h5lbsqu4.execute-api.us-east-1.amazonaws.com/prod/productos`, {
        method: "POST",
        headers: {
          "Content-type": "application/json"
        },
        body: JSON.stringify(usuario_p)
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
          if (elemento.username !== nombreUsuarioEspecifico) {
            resultado.push(elemento);
          }
          return resultado;
        }, []);
    },

    async comprar(codigo_p, usuario_v) {
      let n_compra = {
        tenant_id: "UTEC_SHOP",
        codigo_producto: codigo_p,
        usuario_comprador: this.$store.state.mi_usuario,
        usuario_vendedor: usuario_v
      };
      await fetch(`https://n9h5lbsqu4.execute-api.us-east-1.amazonaws.com/prod/register_compra`, {
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
.global {
  position: relative;
  background-image: url('../assets/fondorojotablas.jpg');
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

nav {
  margin-top: 20px;
}

nav a.casa-link {
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

nav a.casa-link:hover {
  background-color: #0056b3;
  transform: scale(1.1);

}
</style>
