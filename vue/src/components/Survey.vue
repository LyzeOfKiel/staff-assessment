<template>
  <div>
    <h1>Please leave your feedback for {{course}} {{type}}</h1>
    <div v-if="type==='Course'">
      <p> How would you rate the course?</p>
      <p> What materials were useful for understanding the course?</p>
      <p> What improvements would you make to the course? </p>

    </div>
  </div>
</template>

<script>
  export default {
    name: "Survey",
    props: ['course', 'type'],
    data: () => ({
    }),
  }

</script>

<style scoped>

</style>