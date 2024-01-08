<template>
  <v-app>
    <v-container>
    <v-row no-gutters>
        <v-col style="position: left">
            <v-img height="100px" aspect-ratio="1" style="display:flex" :src=logo></v-img>
        </v-col>
        <v-col>
          <nav>
            <router-link to="/">Home</router-link>
          </nav>
        </v-col>
        <v-col>
          <nav>|
          </nav>
        </v-col>
        <v-col>
          <nav>
            <router-link to="/about">About</router-link>
          </nav>
        </v-col>
        <v-col>
          <nav>|
          </nav>
        </v-col>
        <v-col>
          <nav>
            <router-link to="/dashboard">Investor's View</router-link>
          </nav>
        </v-col>
    </v-row>

    <router-view/>

    </v-container>
  </v-app>
</template>
<script>
export default {
  // name: 'About',
  data() {
    return {
      logo:require("./assets/ve.png")
    };
  },
  methods:{
    onclick(){
      this.$router.push('/')
    }
  }
};
</script>
<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

nav {
  padding: 30px;
}

nav a {
  font-weight: bold;
  color: #2c3e50;
}

nav a.router-link-exact-active {
  color: #42b983;
}
</style>
<script setup>
</script>