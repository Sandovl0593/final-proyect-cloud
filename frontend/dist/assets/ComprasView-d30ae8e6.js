import{_ as d,r as p,o as r,c as n,a as t,F as _,b as h,d as m,w as b,t as s,f as y,p as g,g as C}from"./index-a7d8e155.js";const f={name:"ComprasView",data(){return{productos:[]}},methods:{async obtener_productos(){let e={usuario:this.$store.state.mi_usuario};await fetch("http://LB-ProyParcial-1528179989.us-east-1.elb.amazonaws.com:8001/utecshop/tienda",{method:"POST",headers:{"Content-type":"application/json"},body:JSON.stringify(e)}).then(a=>a.json()).then(a=>this.productos=a)},async comprar(e,a){let l={codigo_producto:e,usuario_comprador:this.$store.state.mi_usuario,usuario_vendedor:a};await fetch("http://LB-ProyParcial-1528179989.us-east-1.elb.amazonaws.com:8001/utecshop/registrar_compra",{method:"POST",headers:{"Content-type":"application/json"},body:JSON.stringify(l)}),alert("Producto comprado"),this.$router.push("/productos")}},created(){this.obtener_productos()}},v=e=>(g("data-v-28703839"),e=e(),C(),e),w={class:"global"},k={class:"compras"},P=v(()=>t("thead",null,[t("tr",null,[t("th",null,"Código"),t("th",null,"Vendedor"),t("th",null,"Nombre"),t("th",null,"Precio"),t("th",null,"Marca"),t("th",null,"Categoría"),t("th")])],-1)),S=["onClick"];function V(e,a,l,x,c,i){const u=p("router-link");return r(),n("div",w,[t("div",k,[t("table",null,[P,t("tbody",null,[(r(!0),n(_,null,h(c.productos,o=>(r(),n("tr",{key:o.codigo},[t("td",null,s(o.codigo),1),t("td",null,s(o.usuario_nombre),1),t("td",null,s(o.nombre),1),t("td",null,s(o.precio),1),t("td",null,s(o.marca),1),t("td",null,s(o.tipo),1),t("td",null,[t("button",{class:"comprar-button",onClick:N=>i.comprar(o.codigo,o.usuario_nombre)},"Comprar",8,S)])]))),128))])])]),t("nav",null,[m(u,{to:"/home",class:"casa-link"},{default:b(()=>[y("Casa")]),_:1})])])}const B=d(f,[["render",V],["__scopeId","data-v-28703839"]]);export{B as default};