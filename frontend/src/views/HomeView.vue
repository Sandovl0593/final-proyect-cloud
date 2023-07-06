 <template>
  <div class="global">
    <div class="container">
      <div class="home">
        <h1 class="logo-text">Utec Shop</h1>
        <div v-for="usuario of usuarios" :key="usuario.id">
          <h2 v-if="usuario.nombre_usuario === $store.state.mi_usuario">Usuario: {{ usuario.nombre_usuario }}</h2>
          <h2 v-if="usuario.contrasenha === $store.state.mi_contrasenha">Contraseña: {{ usuario.contrasenha }}</h2>
        </div>
        <div class="button-container">
          <router-link to="/comprar" class="button">Comprar</router-link>
          <router-link to="/productos" class="button">Mis productos</router-link>
          <router-link to="/inventario" class="button">Mis compras</router-link>
          <router-link to="/" class="button">Logout</router-link>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
.container {
  display: flex;
  align-items: center;
  justify-content: center;
  height: 85vh;
}

.home {
  text-align: center;
}

.logo-text {
  font-family: 'BebasNeue-Regular', sans-serif;
  font-size: 145px;
  color: #E7E7E7;
  letter-spacing: -2px;
  margin-bottom: 20px;
  user-select: none;
}

h2 {
  font-size: 20px;
  margin-bottom: 10px;
}

.button-container {
  margin-top: 0px;
}

.button {
  display: inline-block;
  margin: 10px;
  padding: 14px 30px;
  background-color: #000000;
  color: #FFFFFF;
  text-decoration: none;
  border-radius: 15px;
  font-family: 'BebasNeue-Regular', sans-serif;
  font-size: 18px;
  transition: background-color 0.3s ease;
}


.global {
  position: relative;
  background-image: url('../assets/foto 2.jpg');
  background-size: cover;
  height: 100vh;
 /* Ajusta el valor de opacidad según tu preferencia */
}

.button:hover {
  background-color: #7F7F7F;
}
</style>

<script>
export default {
  name: 'HomeView',
  data() {
    return {
      usuarios: []
    };
  },
  methods: {
    async obtenerUsuarios() {
      await fetch(`http://LB-ProyParcial-1528179989.us-east-1.elb.amazonaws.com:8000/utecshop/usuarios`)
        .then((resp) => resp.json())
        .then((datos) => (this.usuarios = datos));
    }
  },
  created() {
    this.obtenerUsuarios();
  }
};
</script>