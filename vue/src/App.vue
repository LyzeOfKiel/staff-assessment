<template>
  <div id="app">
    <header>
      <h1>Leave your feedback below</h1>
    </header>
    <main>
      <aside class="sidebar">
        <router-link
            v-for="course in available_courses"
            v-bind:key="course.id"
            active-class="is-active"
            class="link"
            :to="{ name: 'dff', params: { course_id: course.id } }">
          {{course.name}}
        </router-link>
        <router-link
          class="link"
          :to="{name: 'stats'}">
          Stats
        </router-link>
      </aside>
      <div class="content">
        <router-view></router-view>
      </div>
    </main>
  </div>
</template>

<script>
  import axios from 'axios'
  export default {
    data () {
      return {
        available_courses: [],
        endpoint: 'http://localhost:8080/api/get_courses',
      }
    },
    created() {
      this.getAllCourses();
    },
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

<style lang="scss">
  body {
    margin: 0;
    padding: 0;
  }
  #app {
    font-family: 'Avenir', Helvetica, Arial, sans-serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    color: #2c3e50;
  }
  h1, h2 {
    font-weight: normal;
  }
  ul {
    list-style-type: none;
    padding: 0;
  }
  li {
    display: inline-block;
    margin: 0 10px;
  }
  header {
    position: fixed;
    top: 0;
    width: 100%;
    min-height: 90px;
    border-bottom: 1px solid #42b983;
    text-align: center;
    background: #ffffff;
  }
  main {
    display: flex;
    height: calc(100vh - 90px);
    max-width: 1200px;
    margin-top: 90px;
    margin-left: auto;
    margin-right: auto;
    overflow: hidden;
  }
  aside {
    flex: 1 0 30%;
    height: 100%;
    overflow-y: auto;
    width: 30%;
    padding: 50px 30px;
    box-sizing: border-box;
    border-right: 1px solid #42b983;
  }
  .content {
    flex: 1 1 70%;
    display: flex;
    align-items: center;
    justify-content: center;
  }
  .link {
    display: block;
    text-decoration: none;
    margin-bottom: 10px;
    color: #2c3e50;
    &--home {
      text-transform: uppercase;
      margin-bottom: 30px;
    }
    &.is-active {
      color: #42b983;
    }
  }
</style>