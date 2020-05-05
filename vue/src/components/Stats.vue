<template>
  <v-row align="center">
    <v-card
      class="mx-auto"
      max-width="800"
      tile
    >
      <v-list
      >
        <v-subheader>Stats</v-subheader>
        <v-list-item-group color="primary">
          <v-list-item
            v-for="course of stats"
            :key="course.name"
          >
            {{course['name']}} : {{course['rate']}}
          </v-list-item>
        </v-list-item-group>
      </v-list>
      <v-list-item
        v-for="(course, i) of answers"
        :key="course.name"
      >
        <v-container>
          <v-row
            justify="center"
          >
            {{course['course']}}
          </v-row>
          <v-row>
            <div id="chart">
              <apexchart
                type="pie"
                width="380"
                :options="chartOptions"
                :series="course['series']"
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
    name: "Stats",
    data: () => ({
      stats: [],
      answers: [],
      series: [],
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
      this.getStats();
      this.getChart();
    },
    methods: {
      getStats() {
        this.axiosInstance.get('models/stats/')
          .then(({data}) => {
            const courseRate = Object.keys(data)
              .map(key => ({name: key, rate: data[key]}));
            this.stats = courseRate.sort((a, b) => {
              return b['rate'] - a['rate'];
            });
          });
      },

      getFormattedChartData(feedbacks) {
        let courseStat = {};
        for (const fb of feedbacks) {
          const rate = fb['rate']
          if (!(fb.name in courseStat)) {
            courseStat[fb.name] = [0, 0, 0, 0, 0];
          }
          courseStat[fb.name][rate-1]++;
        }

        const formattedData = []
        for (const courseName in courseStat){
          formattedData.push({
            'name': courseName,
            'series': courseStat[courseName]
          })
        }
        return formattedData
      },
      getChart() {
        this.axiosInstance.get('models/feedback/')
          .then(({data}) => {
            /*
            [
              {
                name: "math",
                series: [1,2,3,4,5]
              }
            ]
             */
            this.answers = this.getFormattedChartData(data)
          })
          .then(async () => {
            const id_name = await this.getRelIdName();
            for (let c of this.answers) {
              c['course'] = id_name[c['course']];
            }
          });
      },
      getRelIdName() {
        return this.axiosInstance.get('models/courses/')
          .then(({data}) => {
            const id_name = {};
            for (let c of data) {
              id_name[c['id']] = c['name'];
            }
            return id_name;
          });
      }
    }
  };
</script>

<style scoped>

</style>