import{_,r as p,o as n,c as r,a as t,F as h,b as m,d as u,w as i,f as c,t as a,p as b,g as f}from"./index-df8ef575.js";const g={name:"VentasView",data(){return{productos:[]}},methods:{async obtener_productos(){let e={usuario:this.$store.state.mi_usuario};await fetch("https://n9h5lbsqu4.execute-api.us-east-1.amazonaws.com/prod/productos",{method:"POST",headers:{"Content-type":"application/json"},body:JSON.stringify(e)}).then(s=>s.json()).then(s=>this.productos=s),this.productos.filter(s=>s.username==this.$store.state.mi_usuario)}},created(){this.obtener_productos()}},v=e=>(b("data-v-96718ecc"),e=e(),f(),e),y={class:"page-background"},V={class:"ventas"},w={class:"table"},x=v(()=>t("thead",null,[t("tr",null,[t("th",null,"Nombre"),t("th",null,"Precio"),t("th",null,"Marca"),t("th",null,"Categoría")])],-1));function S(e,s,k,C,d,N){const l=p("router-link");return n(),r("div",y,[t("div",V,[t("table",w,[x,t("tbody",null,[(n(!0),r(h,null,m(d.productos,o=>(n(),r("tr",{key:o.codigo},[t("td",null,a(o.nombre),1),t("td",null,"S/ "+a(o.precio),1),t("td",null,a(o.marca),1),t("td",null,a(o.categoria),1)]))),128))])])]),t("nav",null,[u(l,{to:"/registrar_producto",class:"button"},{default:i(()=>[c("Registrar producto")]),_:1}),c(" | "),u(l,{to:"/home",class:"button"},{default:i(()=>[c("Casa")]),_:1})])])}const I=_(g,[["render",S],["__scopeId","data-v-96718ecc"]]);export{I as default};