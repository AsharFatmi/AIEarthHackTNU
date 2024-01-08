<template>
  <v-container>
    <!-- Use a single v-row and justify-center to align items in the center -->
    <v-row justify="center" height>
      <v-col cols="12" sm="8" md="6" lg="4">
        <!-- Wrap your form elements in a v-card -->
        <v-card class="pa-5" outlined>
          <!-- Text Input -->
          <v-text-field
              label="Team Name"
              v-model="team_name"
              outlined
              class="mb-4"
          ></v-text-field>

          <v-text-field
              label="Problem Statement"
              v-model="problem_statement"
              outlined
              class="mb-4"
          ></v-text-field>

          <v-text-field
              label="Solution"
              v-model="solution_statement"
              outlined
              class="mb-4"
          ></v-text-field>

          <!-- Submit Button -->
          <v-btn
              color="green"
              @click="submitForm"
              :disabled="!canSubmit"
              block
          >
            Submit
          </v-btn>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import axios from 'axios';
export default {
  data() {
    return {
      team_name:'',
      problem_statement:'',
      solution_statement:'',
      file: null,
      flag:'false',
    };
  },
  computed: {
    canSubmit() {
      return this.team_name !== '' && this.problem_statement !== '' && this.solution_statement !== '';
    },
  },
  methods: {
    submitForm() {
      let urlMongo="http://localhost:1324/update/venturelist/";
      // let url="http://10.0.0.38:4000/analyse"
      let jsonDataMongo = {
        'vProblem': this.problem_statement,
        'vSolution': this.solution_statement,
        'teamName': this.team_name,
        'collectionName': 'ventureData',
        'db': 'VentureEvaluator'
      }
      // let jsonData = {
      //   'problem': this.problem_statement,
      //   'solution': this.solution_statement,
      //   'teamName':this.team_name
      // }
      axios.post(urlMongo,jsonDataMongo)
          .then(response=>{
            console.log("Sent to Mongo",response.status)
            setTimeout(3000)
            this.flag='false'
          })
          .catch(error=>{
            console.error(error)
          })
      // axios.post(url,jsonData) // sending data to genAI
      //     .then(response=>{
      //       if (response.status === 200 || response.status ===202){
      //         this.flag='true'
      //         console.log("Sent to GenAI")
      //         axios.post(urlMongo,jsonDataMongo)
      //             .then(response=>{
      //               console.log("Sent to Mongo",response.status)
      //               setTimeout(3000)
      //               this.flag='false'
      //               // location.reload()
      //             })
      //             .catch(error=>{
      //               console.error(error)
      //               // location.reload()
      //             })
      //       }
      //     })
      //     .catch(error=>{
      //       console.error(error)
      //       // location.reload()
      //     })
      location.reload()
    },
  },
};
</script>
