<template>
  <v-row align="center">
    <v-card
      class="mx-auto"
      max-width="800"
      tile
    >
      <v-list
      >
        <v-subheader>Stats Of Prof {{prof_name}}</v-subheader>
        <v-list-item-group color="primary">

          <v-list-item
            v-for="course of stats"
            :key="course.name"
          >
          <v-container>{{course['name']}} : {{course['rate']}} </v-container>
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
            {{course['name']}}
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
    name: "ProfStats",
    props: ['prof_id', 'prof_name'],
    data: () => ({
      courseId: {},
      courseProf: {},
      stats: [],
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
      this.getCourseIdRelation();
      this.getCourseProfRelation();
    },
    methods: {
      courseLink(name){
        return {name: 'course_stats', params: {course_id: this.courseId[name]}}
      },
      getStats() {
        this.axiosInstance.get('models/stats/')
          .then(({data}) => {
            let proc_data = {};
            let keys = Object.keys(data)
            for(let i = 0; i < keys.length; i++){
              if (this.$props.prof_id == this.courseProf[keys[i]]){
                proc_data[keys[i]] = data[keys[i]]
              }
            }
            const courseRate = Object.keys(proc_data)
              .map(key => ({name: key, rate: proc_data[key]}));
            this.stats = courseRate.sort((a, b) => {
              return b['rate'] - a['rate'];
            });
          });
      },

      getFormattedChartData(feedbacks) {
        let courseStat = {};
        for (const fb of feedbacks) {
          if (this.$props.prof_id != this.courseProf[fb.course]){
            continue;
          }
          const rate = fb['rate'];
          if (!(fb.course in courseStat)) {
            courseStat[fb.course] = [0, 0, 0, 0, 0];
          }
          courseStat[fb.course][rate - 1]++;
        }

        const formattedData = [];
        for (const courseName in courseStat) {
          formattedData.push({
            'name': courseName,
            'series': courseStat[courseName]
          });
        }
        return formattedData;
      },
      getChart() {
        this.axiosInstance.get('models/feedback_course/')
          .then(({data}) => {
            /*
            [
              {
                name: "math",
                series: [1,2,3,4,5]
              }
            ]
             */
            this.answers = this.getFormattedChartData(data);
          });
      },
      getCourseIdRelation() {
        this.axiosInstance.get('models/courses/')
          .then(({data}) => {
            this.courseId = {}
            for (const course of data) {
              this.courseId[course.name] = course.id;
            }
          });
      },
      getCourseProfRelation(){
         this.axiosInstance.get('models/courses/')
          .then(({data}) => {
            this.courseProf = {}
            for (const course of data) {
              this.courseProf[course.name] = course.prof;
            }

            this.getStats();
            this.getChart();
          });
      }

    }
  };
</script>

<style scoped>

</style>