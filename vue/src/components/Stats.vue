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
              v-for="course of stats"
              :key="course.name"
          >
            {{course['name']}} : {{course['rate']}}
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
      stats: []
    }),
    created() {
      this.getStats()
    },
    methods: {
      getStats() {
        this.axiosInstance.get('models/stats/')
          .then(({data}) => {
            const courseRate = Object.keys(data)
              .map(key => ({name: key, rate: data[key]}));
            this.stats = courseRate.sort((a, b) => {
              return b['rate'] - a['rate']
            });
          })

      }
    }
  }
</script>

<style scoped>

</style>