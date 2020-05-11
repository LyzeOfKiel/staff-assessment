<template>
  <v-row align="center">
    <v-card
      class="mx-auto"
      max-width="800"
      tile
    >
      <v-list-item class="justify-center">
        Professor: {{prof.username}}
      </v-list-item>
      <v-container>
        <v-row>
          <div id="chart">
            <apexchart
              type="pie"
              width="380"
              :options="chartOptions"
              :series="stats['series']"
            >
            </apexchart>
          </div>
        </v-row>
      </v-container>
      <v-list-item class="justify-center"
        v-for="ta in tas"
        :key="ta.id"
      >
        {{ta.username}}: {{taScore[ta.id]}}
      </v-list-item>

    </v-card>
  </v-row>
</template>

<script>
  export default {
    name: "Stats",
    props: ['course_id'],
    data: () => ({
      tas: [],
      taScore: {},
      course: {tas: null},
      prof: {username: null, id: null},
      stats: {series: [0, 0, 0, 0, 0]},
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
      this.getCourse()
        .then(() => {
          this.getTAs();
          return this.getProf();
        })
        .then(() => {
          this.getChart();
        });
    },
    methods: {
      getCourse() {
        return this.axiosInstance.get(`models/courses/${this.course_id}/`)
          .then(({data}) => {
            this.course = data;
          });
      },
      getProf() {
        return this.axiosInstance.get(`auth/users/${this.course.prof}/`)
          .then(({data}) => {
            this.prof = data;
          });
      },

      async getTAs() {
        this.tas = []
        const tmpTaScore = {}
        for (const ta_id of this.course.tas) {
          await this.axiosInstance.get(`auth/users/${ta_id}/`)
            .then(({data}) => {
              this.tas.push(data);
              return data.id
            })
            .then(id => {
              return this.axiosInstance.get(`models/tas/${id}/all/`) 
                .then(({data}) => {
                  const total = data.reduce((acc, c) => acc + c.rate, 0) 
                  tmpTaScore[id] = data.length > 0 ? total / data.length : 0
                })
            })
        }
        this.taScore = tmpTaScore
      },
      getFormattedChartData(feedbacks) {
        const stat = {'series': [0, 0, 0, 0, 0]};
        for (const fb of feedbacks) {
          const rate = fb['rate'];
          stat['series'][rate - 1]++;
        }
        stat.name = 'Professor stats';

        return stat;
      },
      getChart() {
        this.axiosInstance.get(`models/profs/${this.prof.id}/all/`)
          .then(({data}) => {
            /*
            [
              {
                name: "math",
                series: [1,2,3,4,5]
              }
            ]
             */
            this.stats = this.getFormattedChartData(data);
          });
      },
    }
  }
  ;
</script>
