<template>
  <div class="post">
    <!--    action="http://localhost:8080/api/set_dfeedback_course" method="post"-->
    <form @submit.prevent="submit">
      <label for="general">How do you like it?</label>
      <select id="general" name="grade" v-model="fields.form.general">
        <option value="1">Very good</option>
        <option value="2">Good</option>
        <option value="3">Not good</option>
        <option value="4">Bad</option>
      </select>

      <p>
        <label for="feedbackText">Other feedback?</label>
        <input name="age" id="feedbackText" v-model="fields.form.feedbackText">
      </p>


      <p>
        <input type="submit" value="Submit">
      </p>

    </form>
  </div>
</template>

<script>
  import axios from 'axios';

  export default {
    props: ['course_id'],
    metaInfo() {
      return {
        title: this.post && this.post.title,
      };
    },
    data() {
      return {
        fields: {form: {}},
        errors: {},
        endpoint: 'http://localhost:8080/api',
      }
    },
    methods: {
      submit() {
        this.errors = {};
        this.fields.course_id = this.course_id
        console.log(this.fields)
        axios.post(`${this.endpoint}/set_dfeedback_course`, this.fields, {
          headers: {
            'Content-Type': 'application/json',
          }
        }).then(response => {
          console.log(response.data)
        }).catch(error => {
          if (error.response.status === 422) {
            this.errors = error.response.data.errors || {};
          }
        });
      }
    }
  }
</script>

<style scoped>

</style>