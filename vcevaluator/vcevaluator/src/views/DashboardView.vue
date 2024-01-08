<template>
<!--  dialogue box pop-up code-->
  <v-dialog v-model="dialog" max-width="800px">
    <v-card >
      <v-card-title>
        {{ teamName }}
        <v-spacer></v-spacer>
      </v-card-title>
      <v-card-actions>
        <v-btn position="relative" icon @click="closeDialog">
          <v-icon>mdi-close</v-icon>
        </v-btn>
      </v-card-actions>

      <v-card-text class="overflow-y-auto" style="max-height: 800px;">
        <div v-for="(value, key) in pitchData" :key="key">
          <v-divider v-if="shouldShowDivider(key)"></v-divider>
          <h3 v-if="!isSectionRating(key)">{{ formatKey(key) }}</h3>
          <v-chip v-if="isSectionRating(key)" class="ma-2" color="primary" text-color="white">
            {{ value.Rating }}
          </v-chip>
          <p v-if="!isSectionRating(key)">{{ value }}</p>
        </div>
      </v-card-text>
    </v-card>
  </v-dialog>

<!--  this is main display page code-->
  <v-container fluid>
    <v-row>
      <v-col cols="12" md="3">
        <!-- Left Navigation Drawer Content -->
        <v-list density="compact">
          <v-list-item color="primary" variant="outlined" @click="fetchRecentDocument">
            <v-list-item-title>Recent     <v-icon>mdi-refresh</v-icon></v-list-item-title>
          </v-list-item>
          <br>
          <v-list-item color="primary" variant="outlined" link :to="{ name: 'home' }">
            <v-list-item-title>Upload New Venture <v-icon> mdi-upload</v-icon></v-list-item-title>
          </v-list-item>
          <br>
          <v-list-item color="primary" variant="outlined" @click="fetchAllDocument">
            <v-list-item-title>All Uploads <v-icon>mdi-repeat</v-icon></v-list-item-title>
          </v-list-item>
        </v-list>
      </v-col>

      <v-col cols="12" md="9">
        <!-- Top Right Search Button -->
        <v-row justify="end">
          <v-btn icon>
            <v-icon>mdi-magnify</v-icon>
          </v-btn>
        </v-row>

        <!-- Display Section -->
<!--        <v-row justify="center">-->
<!--          <v-col cols="12" class="text-center">-->
<!--&lt;!&ndash;            this is the section of the display section&ndash;&gt;-->
<!--            <v-container>-->
<!--              <v-card outlined>-->
<!--                <v-row>-->
<!--                  &lt;!&ndash; Weekly Overview Card &ndash;&gt;-->
<!--                  <v-col cols="12" md="4">-->
<!--                    <v-card class="pa-3" outlined>-->
<!--                      <v-card-title class="subtitle-1">-->
<!--                        Weekly Overview-->
<!--                      </v-card-title>-->
<!--                      <v-spacer></v-spacer>-->
<!--                      &lt;!&ndash; Insert your chart component here &ndash;&gt;-->
<!--                      <v-card-text>-->
<!--                        <div class="text-center">-->
<!--                          45% Your sales performance is 45% better compared to last month-->
<!--                        </div>-->
<!--                      </v-card-text>-->
<!--                      <v-card-actions>-->
<!--                        <v-btn text color="primary">Details</v-btn>-->
<!--                      </v-card-actions>-->
<!--                    </v-card>-->
<!--                  </v-col>-->

<!--                  &lt;!&ndash; Total Earning Card &ndash;&gt;-->
<!--                  <v-col cols="12" md="4">-->
<!--                    <v-card class="pa-3" outlined>-->
<!--                      <v-card-title class="subtitle-1">-->
<!--                        Total Earning-->
<!--                      </v-card-title>-->
<!--                      <v-spacer></v-spacer>-->
<!--                      <v-card-text>-->
<!--                        <div>-->
<!--                          <h3>$24,895 <span class="green&#45;&#45;text">↑ 10%</span></h3>-->
<!--                          Compared to $84,325 last year-->
<!--                        </div>-->
<!--                      </v-card-text>-->
<!--                      &lt;!&ndash; Add list of items here &ndash;&gt;-->
<!--                    </v-card>-->
<!--                  </v-col>-->

<!--                  &lt;!&ndash; Total Profit Card &ndash;&gt;-->
<!--                  <v-col cols="12" md="4">-->
<!--                    <v-card class="pa-3" outlined>-->
<!--                      <v-card-title class="subtitle-1">-->
<!--                        Total Profit-->
<!--                      </v-card-title>-->
<!--                      <v-spacer></v-spacer>-->
<!--                      <v-card-text>-->
<!--                        <div>-->
<!--                          <h3>$86.4k <span class="green&#45;&#45;text">↑ 42%</span></h3>-->
<!--                          Weekly Project-->
<!--                        </div>-->
<!--                      </v-card-text>-->
<!--                    </v-card>-->
<!--                  </v-col>-->

<!--                  &lt;!&ndash; Sessions Card &ndash;&gt;-->
<!--                  <v-col cols="12" md="4">-->
<!--                    <v-card class="pa-3" outlined>-->
<!--                      <v-card-title class="subtitle-1">-->
<!--                        Sessions-->
<!--                      </v-card-title>-->
<!--                      <v-spacer></v-spacer>-->
<!--                      &lt;!&ndash; Insert your sessions graph here &ndash;&gt;-->
<!--                      <v-card-text>-->
<!--                        2,856-->
<!--                      </v-card-text>-->
<!--                    </v-card>-->
<!--                  </v-col>-->
<!--                </v-row>-->
<!--              </v-card>-->
<!--            </v-container>-->
<!--          </v-col>-->
<!--        </v-row>-->

<!--        this part is for the display content information-->
          <v-container>
            <v-progress-linear disabled="load_flag" stream color="green"></v-progress-linear>
            <v-card>
              <v-card-title class="text-h5 mb-4">{{Title}}</v-card-title>
                <v-container class="overflow-y-auto">
                    <v-row v-for="(item, index) in pitches" :key="index">
                      <v-card hover outlined class="d-flex  flex-grow-1 pa-4 mb-2">
                        <!-- Company Name and Industry -->
                        <v-col align-self="start" class="grow" size="86">
                          <v-card-title left class="text-subtitle-1">{{ item.teamName }}</v-card-title>
                          <v-card-subtitle class="text-caption">Industry: {{ item.industry }}</v-card-subtitle>
                        </v-col>

                        <!-- Numeric Indicator -->
                        <v-col align-self="center" onresize="this">
                          <v-chip variant="flat" :color="colourDecider(item.score)" color-text="Black" bold size="x-large" class="ma-0">
                            {{ item.score }}
                          </v-chip>
                          <v-icon>circle</v-icon>
                        </v-col>

                        <v-col class="v-data-table-group-header-row__column">
                          <v-btn elevation="0" variant="text" @click="displayInformation(item.teamName)" > More </v-btn>
                        </v-col>
                      </v-card>
                    </v-row>
                </v-container>
            </v-card>
          </v-container>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import axios from 'axios';
export default {
  data() {
    return {
      vcDataLis : [],
      teamName:'',
      Title:'Pitches',
      dialog:false,
      pitchData: {},
      load_flag:true,
      // pitches:[
      //   {
      //     "_id": {
      //       "$oid": "659b267b220b37620364cfff"
      //     },
      //     "teamName": "Golf",
      //     "industry": "travel & tourism",
      //     "score": 150,
      //     "created_at": "2024-01-07 22:31:37.362888"
      //   },
      //   {
      //     "_id": {
      //       "$oid": "659b267b220b37620364d000"
      //     },
      //     "teamName": "India",
      //     "industry": "travel & tourism",
      //     "score": 180,
      //     "created_at": "2024-01-07 22:30:37.362911"
      //   },
      //   {
      //     "_id": {
      //       "$oid": "659b267b220b37620364d001"
      //     },
      //     "teamName": "Echo",
      //     "industry": "automotive",
      //     "score": 167,
      //     "created_at": "2024-01-07 22:29:37.362920"
      //   },
      //   {
      //     "_id": {
      //       "$oid": "659b267b220b37620364d002"
      //     },
      //     "teamName": "Hotel",
      //     "industry": "automotive",
      //     "score": 138,
      //     "created_at": "2024-01-07 22:28:37.362928"
      //   },
      //   {
      //     "_id": {
      //       "$oid": "659b267b220b37620364d003"
      //     },
      //     "teamName": "Charlie",
      //     "industry": "automotive",
      //     "score": 184,
      //     "created_at": "2024-01-07 22:27:37.362935"
      //   },
      //   {
      //     "_id": {
      //       "$oid": "659b267b220b37620364d004"
      //     },
      //     "teamName": "Charlie",
      //     "industry": "food & beverage",
      //     "score": 90,
      //     "created_at": "2024-01-07 22:26:37.362942"
      //   },
      //   {
      //     "_id": {
      //       "$oid": "659b267b220b37620364d005"
      //     },
      //     "teamName": "Alpha",
      //     "industry": "food & beverage",
      //     "score": 51,
      //     "created_at": "2024-01-07 22:25:37.362950"
      //   },
      //   {
      //     "_id": {
      //       "$oid": "659b267b220b37620364d006"
      //     },
      //     "teamName": "India",
      //     "industry": "automotive",
      //     "score": 90,
      //     "created_at": "2024-01-07 22:24:37.362956"
      //   },
      //   {
      //     "_id": {
      //       "$oid": "659b267b220b37620364d007"
      //     },
      //     "teamName": "Bravo",
      //     "industry": "construction",
      //     "score": 152,
      //     "created_at": "2024-01-07 22:23:37.362963"
      //   },
      //   {
      //     "_id": {
      //       "$oid": "659b267b220b37620364d008"
      //     },
      //     "teamName": "Hotel",
      //     "industry": "construction",
      //     "score": 150,
      //     "created_at": "2024-01-07 22:22:37.362969"
      //   }
      // ],
      pitches:[],
    };
  },
  name: 'DashboardView',
  mounted() {
    this.fetchRecentDocument()
  },
  methods:{
    formatKey(key) {
      return key.replace(/([A-Z])/g, ' $1').replace(/^./, str => str.toUpperCase());
    },
    isSectionRating(key) {
      return this.pitchData[key] && typeof this.pitchData[key] === 'object' && 'Rating' in this.pitchData[key];
    },
    shouldShowDivider(key) {
      return !this.isSectionRating(key) && !['CreatedAt', 'UpdatedAt', '_id'].includes(key);
    },
    closeDialog(){
      this.dialog=false
    },
    async displayInformation(teamName){
      console.log("display information called",teamName)
      let url="http://localhost:1324/collection/";
      let collectionName = 'dataGenerated'
      await axios.get(url+collectionName+'/'+teamName+'/' )
          .then(response =>{
            if(response.status ===200){
              this.pitchData = response.data['data'][0]
              this.teamName = this.pitchData.teamName
              delete this.pitchData.teamName
              delete this.pitchData._id
              this.dialog=true
            }
          })
          .catch(error=>{
            console.error(error)
          })
    },
    colourDecider(score){
      if(score>200){
        return 'green'
      }
      else if (score > 150 && score < 200){
        return 'yellow'
      }
      else if (score > 100 && score < 150){
        return 'orange'
      }
      else if (score < 100){
        return 'red'
      }
    },
    async fetchRecentDocument(){
      let url="http://localhost:1324/collection/recent/";
      let jsonData= {
        'collectionName': 'ventureDataGenResponse',
        'tag': 'recent'
      }
      await axios.get(url, {params:jsonData})
          .then(response =>{
            if(response.status ===200){
              this.Title = 'Recent Pitches'
              this.pitches = response.data
            }
          })
          .catch(error=>{
            console.error(error)
          })
    },
    async fetchAllDocument(){
      let url="http://localhost:1324/collection/recent/";
      let jsonData= {
        'collectionName': 'ventureDataGenResponse',
        'tag': 'all'
      }
      await axios.get(url,{params:jsonData})
          .then(response =>{
            if(response.status ===200){
              this.Title = 'Pitches'
              this.pitches = response.data
            }
          })
          .catch(error=>{
            console.error(error)
          })
    }
  }
  // Additional component options
};
</script>

<style >
.overflow-y-auto {
  overflow-y: auto;
}
</style>
