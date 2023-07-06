import { createStore } from 'vuex'

export default createStore({
  state: {
    mi_usuario: "",
    mi_contrasenha: ""
  },
  mutations: {
    actualizar_usuario(state, valor){
      state.mi_usuario = valor
    },
    actualizar_contrasenha(state, valor){
      state.mi_contrasenha = valor
    }
  },
  getters: {
  },
  actions: {
      accion_act_usuario(contexto, act){
          contexto.commit("actualizar_usuario", act)
      },
      accion_act_contra(contexto, act){
          contexto.commit("actualizar_contrasenha", act)
      }
  },
  modules: {
  }
})
