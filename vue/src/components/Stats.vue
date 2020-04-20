<template>
  <v-row align="center">
    <v-card
      class="mx-auto"
      max-width="800"
      tile
    >
      <v-list
      >
        <v-subheader>Stats</v-subheader>
        <v-list-item-group color="primary">
          <v-list-item
            v-for="(rate, course_name) of stats"
            :key="course_name"
          >
            {{course_name}}: {{rate}}
          </v-list-item>
        </v-list-item-group>
      </v-list>
    </v-card>
  </v-row>

</template>

<script>
  export default {
    name: "Stats",
    data: () => ({
      stats: null
    }),
    created() {
      this.getStats()
    },
    methods: {
      getStats() {
        this.axiosInstance.get('models/stats/')
          .then(({data}) => {
            this.stats = data
          })
      }
    }
  }
</script>

<style scoped>

</style>