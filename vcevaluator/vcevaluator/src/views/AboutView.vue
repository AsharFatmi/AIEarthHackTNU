<template>
  <v-container>
    <v-card>
      <v-card-title bold> Team TNU</v-card-title>
    </v-card>
    <br>
    <br>
    <br>
    <br>
    <br>
    <br>
    <v-row justify="center">
      <v-col cols="12" sm="6" md="3" v-for="member in teamMembers" :key="member.name">
        <v-card>
          <v-img height="300px" aspect-ratio="1" style="display:flex" :src=member.image></v-img>
          <v-card-title>{{ member.name }}</v-card-title>
          <v-card-subtitle>
            {{ member.subtitle1 }}<br>
            {{ member.subtitle2 }}
          </v-card-subtitle>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
export default {
  // name: 'About',
  data() {
    return {
      teamMembers: [
        { name: 'Ashwani Chaurasia', subtitle1: 'Team member', subtitle2: 'Retail-Ecommerce|Product Manager', image:require("../assets/ashwani.jpg") },
        { name: 'Ashar F', subtitle1: 'Team member', subtitle2: 'AI | Computer Research',image:require("../assets/ashar.jpg") },
        { name: 'Mustufa G. Sodagar', subtitle1: 'Team member', subtitle2: 'Tech & Sustainable Housing',image:require("../assets/soda.jpg") },
        { name: 'Anusha R', subtitle1: 'Team member', subtitle2: 'Software Engineer',image:require("../assets/anusha.jpg") }
      ]
    };
  }
};
</script>
