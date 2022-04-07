<template>
  <div id="app" class="custom-color pb-5">
    <div class="page" v-if="getSpinner">
      <b-spinner class="spinner" :variant="'primary'" :key="'primary'"></b-spinner>
    </div>
    <div id="nav" >
      <top-header></top-header>
    </div>
    <router-view />
  </div>
</template>

<script>
import Header from "./components/Header.vue"
import { mapGetters } from "vuex";
// import router from "vue-router"
export default {
  name: 'app',
  components: { "top-header": Header },
    computed: {
    ...mapGetters(["getSpinner"])
  },
  
  data() {
    return {
      msg: 'Welcome to Your Vue.js App'
    }
  },
  beforeMount(){
    this.checkUrl();
  },
  methods:{
    checkUrl(){
      let typeParam = this.$route.params.type

      let urls = ['drivers', 'journeys', 'passengers', 'buses']
      
      if (urls.indexOf(typeParam) === -1)
        this.$router.push('/journeys')

    }
  }
  } 
</script>

<style lang="scss">
#app {
  font-family: "Avenir", Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  min-height: 50rem;
}

#nav {
  padding: 30px;

  a {
    font-weight: bold;
    color: white;

    &.router-link-exact-active {
      color: #42b983;
    }
  }
}
.page {
  position: absolute;
  background: rgba(0, 0, 0, 0.3);
  z-index: 25;
  width: 100%;
  height: 100%;
}
.spinner {
  z-index: 26;
  position: relative;
  top: 50%;
}
.custom-color{
  background-image: linear-gradient(#e25160, #d34f96);
}
#crud-ops-drowpdown ul li a{
  color: black !important
}
</style>
