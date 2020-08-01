var component=document.getElementById("component");
var style=component.content.querySelector('style');
if(style){
  document.getElementsByTagName('head')[0].appendChild(style);
}
var script=component.content.querySelector("script");
var m={};
if(script){
   try{
    Function('module','exports',script.innerText ).call({},m);
   }catch(ex){
     console.error(ex);
   }
}

if(!m.exports){
  m.exports={};
}
m.exports.template=component.content.querySelector('template').content.firstElementChild.outerHTML;
Vue.component(component.attributes.name.value,m.exports);

new Vue({
    el: '#app',
    data:{
      tab:component.attributes.name.value,
      cart_drawer:false,
      menu_drawer:false,
      emailRules: [
        v => !!v || 'Ingrese su email',
        v => /^\w+([.-]?\w+)*@\w+([.-]?\w+)*(\.\w{2,3})+$/.test(v) || 'El email debe ser válido'
      ],
      newsletter:'',
    },
    methods:{
      subscribe(){
        if(this.$refs.newsletter.validate()){
          
        }
      }
    },
    vuetify: new Vuetify({
        icons:{
            iconfont:'md'
        },
        theme:{
            dark:false,
            themes:{
                light:{
    primary: '#42a5f6',
    toolbar: '#1b2530',
    secondary:'#232f3e',
    accent: '#ff5722',
    error: '#f44336',
    warning: '#ff9800',
    info: '#cddc39',
    success: '#4caf50'
    },
    dark:{
      primary: '#42a5f6',
      toolbar: '#1b2530',
      secondary:'#232f3e',
      accent: '#ff5722',
      error: '#f44336',
      warning: '#ff9800',
      info: '#cddc39',
      success: '#4caf50'
      }
            }
        }
    }),
  });
  const $api = axios.create({
    baseURL: 'http://localhost:5000/api/',
    transformRequest: [function (args, headers) {
      const data=new FormData();
      for(let arg in args){
        data.append(arg,args[arg]);
      }
      return data;
    }],
  });