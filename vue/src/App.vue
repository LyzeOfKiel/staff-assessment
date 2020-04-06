<template>
  <v-app id="inspire">
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

    <v-app-bar
      app
      color="cyan"
      dark
    >

      <v-app-bar-nav-icon @click.stop="drawer = !drawer"/>
      <v-toolbar-title>Courses</v-toolbar-title>
    </v-app-bar>

    <v-content>
      <v-container fluid>
        <v-row>
          <v-col cols="12">
            <v-row
              align="center"
              justify="center"
              style="height: auto;"
            >
              <router-view/>
            </v-row>
          </v-col>
        </v-row>
      </v-container>
    </v-content>

    <v-footer
      color="cyan"
      app
    >
      <v-spacer/>

      <span class="white--text">&copy; 2019</span>
    </v-footer>
  </v-app>
</template>

<script>
  import axios from 'axios'

  export default {
    name: 'LayoutsDemosBaselineFlipped',
    props: {
      source: String,
    },
    created() {
      this.getAllCourses();
    },
    data: () => ({
      drawer: null,
      available_courses: [],
      endpoint: 'http://localhost:8080/api/get_courses',
    }),
    methods: {
      getAllCourses() {
        axios.get(this.endpoint)
          .then(response => {
            this.available_courses = response.data;
            console.log(this.available_courses)
          })
          .catch(error => {
            console.log('-----error-------');
            console.log(error);
          })
      }
    }
  }
</script>

<style>
  .tile {
    margin: 5px;
    border-radius: 4px;
  }

  .tile:hover {
    background: green;
  }

  .tile:active {
    background: yellow;
  }
</style>