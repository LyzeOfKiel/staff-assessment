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
            v-for="course of stats"
            :key="course.name"
            link
            :to="courseLink(course.name)"
          >
            {{course['name']}} : {{course['rate']}}
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
            Prof Id: {{prof['id']}}
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
    },
    methods: {

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
            console.log(this.answers)
          });
      }
    }
  };
</script>

<style scoped>

</style>