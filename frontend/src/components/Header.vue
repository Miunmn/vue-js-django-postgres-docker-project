<template>
  <div>
    <b-navbar id="nav-bar" toggleable="lg">
      <!-- <img style="width: '20%'" src='../../public/logo.png'/> -->
      <b-navbar-brand href="#">Buses</b-navbar-brand>

      <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>

      <b-collapse id="nav-collapse" is-nav>
        <b-navbar-nav>
          <b-nav-item to="/">Home</b-nav-item>
          <b-nav-item to="/about">Acerca de nosotros</b-nav-item>
        </b-navbar-nav>

        <!-- Right aligned nav items -->
      </b-collapse>
    </b-navbar>
  </div>
</template>

<script>
export default {
  methods: {
    // search() {
    //   // console.log(this.searchText);
    //   this.$store.dispatch("search", { text: this.searchText });
    // }
  },
  data() {
    return {
      // searchText: ""
    };
  }
};
</script>

<style lang="scss" scoped>
#nav a.router-link-exact-active {
  color: white;
}
</style>
