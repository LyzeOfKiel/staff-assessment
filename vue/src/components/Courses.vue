<template>
  <v-card
      height="400"
      width="256"
      class="mx-auto"
  >
    <div class="courses">
      <v-list shaped>
        <v-list-item
            v-for="course in courses"
            v-bind:key="course.name">
          <v-list-item-content>
            <v-list-item-title class="title">
              <b>{{course.name}}</b>
            </v-list-item-title>
            <v-list-item
                class="link"
                :to="{name: 'survey', params:{'course': course.name, 'type':
                'TA'
                }}">
              TA
            </v-list-item>
            <v-list-item
                class="link"
                :to="{name: 'survey', params:{'course': course.name, 'type':
                'Prof'
                }}">
              Prof
            </v-list-item>
            <v-list-item
                class="link"
                :to="{name: 'survey', params:{'course': course.name,
                'type':'Course'}}">
              Course
            </v-list-item>
          </v-list-item-content>
        </v-list-item>

        <v-list-item
          class="link"
          :to="{name: 'stats'}"
        >
          Stats
        </v-list-item>
      </v-list>
    </div>
  </v-card>
</template>

<script>
  export default {
    name: "Courses",
    data: () => ({
      courses: []
    }),
    created() {
      this.getCourses()
    },
    methods: {
      getCourses() {
        return this.axiosInstance.get('models/courses/')
          .then(({data}) => {
            this.courses = data
            console.log(data)
          })
      }
    }
  }
</script>
