<template>
  <v-row align="center">
    <v-card
      class="mx-auto"
      max-width="800"
      tile
    >
      <v-list
      >
        <v-subheader>Professors Stats</v-subheader>
        <v-list-item-group color="primary">
          <v-list-item :to="{name: 'stats'}">
            Courses
          </v-list-item>

          <v-list-item
            v-for="prof of stats"
            :key="prof.id"
            link
            :to="profLink(prof.id)"
          >
            Prof {{profName[prof.id]}} : {{prof['rate']}}
          </v-list-item>
        </v-list-item-group>
      </v-list>
      <v-list-item
        v-for="(prof, i) of answers"
        :key="prof.id"
      >
        <v-container>
          <v-row
            justify="center"
          >
            Prof {{profName[prof.id]}}
          </v-row>
          <v-row>
            <div id="chart">
              <apexchart
                type="pie"
                width="380"
                :options="chartOptions"
                :series="prof['series']"
              >
              </apexchart>
            </div>
          </v-row>
        </v-container>
      </v-list-item>

    </v-card>
  </v-row>

</template>

<script>
  export default {
    name: "Stats_Profs",
    data: () => ({
      answers: [],
      stats: [],
      profName: {},
      chartOptions: {
        chart: {
          width: 380,
          type: 'pie',
        },
        labels: ['1', '2', '3', '4', '5'],
        responsive: [{
          breakpoint: 480,
          options: {
            chart: {

              width: 200
            },
            legend: {
              position: 'bottom'
            }
          }
        }],
      }
    }),
    created() {
      this.getChart();
      this.getStats();
      this.getProfIdToName();
    },
    methods: {
     getProfIdToName() {
        this.axiosInstance.get('models/profs/')
          .then(({data}) => {
            this.profName = {}
            for (const prof of data) {
              console.log(prof)
              this.profName[prof.id] = prof.username;
            }
            console.log(this.profName)
          });
      },
      profLink(id){
        return {name: 'prof_stats', params: {prof_id: parseInt(id, 10), prof_name: this.profName[id]}}
      },
      getStats() {
        this.axiosInstance.get('models/stats-profs/')
          .then(({data}) => {
            const profRate = Object.keys(data)
              .map(key => ({id: parseInt(key, 10), rate: data[key]}));
            this.stats = profRate.sort((a, b) => {
              return b['rate'] - a['rate'];
            });
            console.log(this.stats)
          });
      },

      getFormattedChartData(feedbacks) {
        let profStat = {};
        for (const fb of feedbacks) {
          const rate = fb['rate'];
          if (!(fb.prof in profStat)) {
            profStat[fb.prof] = [0, 0, 0, 0, 0];
          }
          profStat[fb.prof][rate - 1]++;
        }

        const formattedData = [];
        for (const profId in profStat) {
          formattedData.push({
            'id': profId,
            'series': profStat[profId]
          });
        }
        return formattedData;
      },
      getChart() {
        this.axiosInstance.get('models/feedback_prof/')
          .then(({data}) => {
            /*
            [
              {
                id: "1",
                series: [1,2,3,4,5]
              }
            ]
             */
            this.answers = this.getFormattedChartData(data);
          });
      }
    }
  };
</script>

<style scoped>

</style>