import { createRouter, createWebHistory } from 'vue-router'
import LoginView from '../views/LoginView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'login',
      component: LoginView
    },
    {
      path: '/home',
      name: 'home',
      component: () => import('../views/HomeView.vue')
    },
    {
      path: '/registrar',
      name: 'registrar',
      component: () => import('../views/RegisterView.vue')
    },
    {
      path: '/productos',
      name: 'productos',
      component: () => import('../views/VentasView.vue')
    },
    {
      path: '/registrar_producto',
      name: 'registrar_producto',
      component: () => import('../views/RegistrarProductoView.vue')
    },
    {
      path: '/comprar',
      name: 'comprar',
      component: () => import('../views/ComprasView.vue')
    },
    {
      path: '/inventario',
      name: 'inventario',
      component: () => import('../views/InventarioView.vue')
    }
  ]
})

export default router;
