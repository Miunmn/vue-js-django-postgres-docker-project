<template>
  <div id="app" class="custom-color pb-5">
    <div class="page" v-if="getSpinnerFunction">
      <b-spinner
        class="spinner"
        :variant="'primary'"
        :key="'primary'"
      ></b-spinner>
    </div>
    <div id="nav">
      <top-header></top-header>
    </div>
    <div v-show="!getSpinnerFunction">
      <router-view />
    </div>
  </div>
</template>

<script>
import Header from "./components/Header.vue";
// import { mapGetters } from "vuex";
// import router from "vue-router"
export default {
  name: "app",
  components: { "top-header": Header },
  computed: {
    getSpinnerFunction() {
      let bool_ = this.$store.getters.getSpinner();

      return bool_;
    }
  },

  beforeMount() {
    this.checkUrl();
  },
  methods: {
    checkUrl() {
      let typeParam = this.$route.params.type;

      let urls = ["drivers", "journeys", "passengers", "buses"];

      if (urls.indexOf(typeParam) === -1) this.$router.push("/journeys");
    }
  }
};
</script>

<style lang="scss">
#app {
  font-family: "Montserrat", sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  min-height: 50rem;
}

#nav {
  padding: 30px;

  a {
    // font-weight: bold;
    color: white;
    font-size: 19px;
    line-height: 44px;

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
.custom-color {
  background-image: linear-gradient(#e25160, #d34f96);
}
#crud-ops-drowpdown ul li a {
  color: black !important;
}
</style>
