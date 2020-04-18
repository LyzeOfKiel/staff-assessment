<template>
  <v-app-bar
    app
    color="cyan"
    dark
  >

    <v-app-bar-nav-icon @click.stop="drawer = !drawer"/>
    <v-toolbar-title>Courses</v-toolbar-title>
  </v-app-bar>

  <v-navigation-drawer
    v-model="drawer"
    app
    left
  >
    <v-list shaped>
      <v-list-item
        v-for="course in available_courses"
        v-bind:key="course.id"
        class="link"
        :to="{ name: 'dff', params: { course_id: course.id } }">

        {{course.name}}

      </v-list-item>

      <v-list-item
        class="link"
        :to="{name: 'stats'}">
        Stats
      </v-list-item>
    </v-list>
  </v-navigation-drawer>
</template>

<script>
  import axios from 'axios'

  export default {
    name: "Nav",
    data: () => ({
      drawer: null,
      available_courses: [],
      endpoint: 'http://localhost:8080/api/courses',
    }),
    created() {
      this.getAllCourses()
    },
    methods: {
      // getAllCourses() {
      //   axios.get(this.endpoint)
      //     .then(response => {
      //       this.available_courses = response.data;
      //       console.log(this.available_courses)
      //     })
      //     .catch(error => {
      //       console.log('-----error-------');
      //       console.log(error);
      //     })
      // }
    }
  }
</script>

<style scoped>

</style>