<template>
<div>
  {{info}}
</div>
</template>

<script>
  import axios from 'axios';

  export default {
    name: "FeedbackStatistics",
    data() {
      return {
        info: null,
        endpoint: 'http://localhost:8080/api',
      }
    },
    created() {
      this.get_stats()
    },
    methods: {
      get_stats() {
        axios.get(`${this.endpoint}/get_all_feedbacks`)
          .then(response => {
            console.log(response.data)
            this.info = response.data
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