new Vue({
    el: '#app',
    data:{
        icons: [
            'mdi-facebook',
            'mdi-twitter',
            'mdi-linkedin',
            'mdi-instagram',
          ],
    },
    vuetify: new Vuetify({
        icons:{
            iconfont:'md'
        },
        theme:{
            light:true,
            themes:{
                light:{
    primary: '#ffc107',
    secondary:'#ff5722',
    accent: '#009688',
    error: '#f44336',
    warning: '#ff9800',
    info: '#cddc39',
    success: '#4caf50'
    }
            }
        }
    }),
  })