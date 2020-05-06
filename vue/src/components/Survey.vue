<template>
  <v-container fluid>
    <v-row
      justify="center"
      no-gutters
    >
      <v-col
        :cols="8"
      >
        <p v-if="type === 'Prof'"></p>

        <v-form @submit.prevent="submit" ref="form">
          <v-select
            v-model="fields.form.rate"
            :items="grade_options"
            label="How do you like it?"
          >
            <template v-slot:selection="{ item, index }">
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
            v-model="fields.form.feedback"
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


          <v-row>
            <v-col>
              <v-dialog v-model="showDialog" max-width="290">
                <v-card>
                  <v-card-title class="headline">Success!</v-card-title>
                  <v-card-text>Feedback sent</v-card-text>
                  <v-card-actions>
                    <v-spacer></v-spacer>
                    <v-btn color="green darken-1" text @click="showDialog = false">Ok</v-btn>
                  </v-card-actions>
                </v-card>
              </v-dialog>
            </v-col>
          </v-row>
        </v-form>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
  export default {
    name: "Survey",
    props: ['course', 'type'],
    data: () => ({
      fields: {form: {}},
      grade_options: [1, 2, 3, 4, 5],
      showDialog: false
    }),
    methods: {
      submit() {
        this.fields.form.course = this.course
        this.axiosInstance.post(`models/feedback_${this.type.toLowerCase()}/`, this.fields.form, {
          headers: {
            'Content-Type': 'application/json',
          }
        }).then(() => {
          this.showDialog = true
        })
      }
    }
  }

</script>

<style scoped>

</style>