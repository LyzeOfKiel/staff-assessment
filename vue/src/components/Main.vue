<template>
  <div>
    <v-navigation-drawer
      v-model="drawer"
      app
      temporary
    >
      <Courses/>
    </v-navigation-drawer>
    <v-app-bar
      app
      dense
    >
      <v-app-bar-nav-icon @click.stop="drawer = !drawer"></v-app-bar-nav-icon>

      <v-toolbar-title>Staff assessment</v-toolbar-title>

      <v-spacer></v-spacer>

      <v-menu
        left
        bottom
      >
        <template v-slot:activator="{ on }">
          <v-btn icon v-on="on">
            <v-icon>mdi-dots-vertical</v-icon>
          </v-btn>
        </template>

        <v-list>
          <v-list-item
            v-for="n in 5"
            :key="n"
            @click="() => {}"
          >
            <v-list-item-title>Option {{ n }}</v-list-item-title>
          </v-list-item>
        </v-list>
      </v-menu>
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

            </v-row>
          </v-col>
        </v-row>
      </v-container>
    </v-content>
  </div>
</template>

<script>
  import Courses from "@/components/Courses"

  export default {
    name: "Main",
    components: {Courses},
    data: () => ({
      drawer: null
    })
  }
</script>

<style scoped>

</style>