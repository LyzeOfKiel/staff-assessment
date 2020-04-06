<template>
  <!--    action="http://localhost:8080/api/set_dfeedback_course" method="post"-->
  <v-form @submit.prevent="submit" ref="form">
      <v-select
        v-model="fields.form.general"
        :items="grade_options"
        :disabled="disabled"
        label="How do you like it?"
      >
        <template v-if="selectSlot" v-slot:selection="{ item, index }">
          <v-chip v-if="index === 0">
            <span>{{ item }}</span>
          </v-chip>
          <span
            v-if="index === 1"
            class="grey--text caption"
          >(+{{ model.length - 1 }} others)</span>
        </template>
      </v-select>

    <v-text-field
      v-model="fields.form.feedbackText"
      label="Other feedback"
      required
    ></v-text-field>


    <v-btn
      color="success"
      class="mr-4"
      @click="submit"
    >
      Submit
    </v-btn>


  </v-form>
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
        grade_options: ['Very good', 'Good', 'Not good', 'Bad'],
        fields: {form: {}},
        errors: {},
        endpoint: 'http://localhost:8080/api',
      }
    },
    created() {
      console.log(2378)
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