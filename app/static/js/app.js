
const Home = Vue.component('home', {
    template: `
    <div class="home">
    <a href="https://www.freeforexapi.com">
    <img alt="Free Forex API" src="https://www.freeforexapi.com/Images/link.png" height="20">
    https://www.freeforexapi.com/api/live?pairs=EURGBP,USDJPY

    </a>
    </div>
   
    `,
    created: function() {
      let self = this;
    fetch('https://www.freeforexapi.com/api/live?pairs=EURGBP,USDJPY').then(function(response) {
    return response.json();
    }).then(function(data) {
      console.log(data);
      });}
  }
    );
  
     

    Vue.component('app-header', {
        template: `
            <header>
                <nav class="navbar navbar-expand-lg navbar-dark bg-primary fixed-top">
                  <a class="navbar-brand" href="#">Abritrage</a>
                  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
                    <span class="navbar-toggler-icon"></span>
                  </button>
      
                  <div class="collapse navbar-collapse" id="navbarSupportedContent">

                  </div>
                </nav>
            </header>    
        `,
        data: function() {
          return {};
        }
      });
      Vue.component('app-footer', {
        template: `
            <footer>
                <div class="container">
                    <p>Copyright &copy {{ year }} Flask Inc.</p>
                </div>
            </footer>
        `,
        data: function() {
            return {
                year: (new Date).getFullYear()
            };
        }
      });

const router = new VueRouter({
    mode: 'history',
    routes: [
    { path: '/', component: Home }
    ]
    });
  
    
  
  const app = new Vue({
    el: '#app',
    router
    });
  
  