import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView
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
    }
  ]
})

export default router;
