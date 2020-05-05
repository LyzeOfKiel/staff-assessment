<template>
  <div>
    <v-card width="400" class="mx-auto mt-5">
      <v-card-title class="pb-0">
        <h1>Sign up</h1>
      </v-card-title>
      <v-card-text>
        <v-form>
          <v-text-field
            v-model="username"
            label="Username"
            prepend-icon="mdi-account-circle">

          </v-text-field>
          <v-text-field
            v-model="password"
            :type="showPassword ? 'text' : 'password'"
            label="Password"
            prepend-icon="mdi-lock"
            :append-icon="showPassword ? 'mdi-eye' : 'mdi-eye-off'"
            @click:append="showPassword = !showPassword">

          </v-text-field>

          <v-radio-group v-model="userType" label="Select user type">
            <v-radio
              label="Student"
              value="Student">
            </v-radio>
            <v-radio
              label="TA"
              value="TA">
            </v-radio>
            <v-radio
              label="Prof"
              value="Prof">
            </v-radio>
          </v-radio-group>
        </v-form>
      </v-card-text>
      <v-card-actions>
        <v-btn @click="registerUser" color="yellow" test-id="btn-register">Register</v-btn>
      </v-card-actions>
    </v-card>
  </div>
</template>

<script>
  import axios from 'axios'

  export default {
    name: "Auth",
    data: () => ({
      username: null,
      password: null,
      showPassword: false,
      userType: null,
    }),
    created() {
    },
    methods: {
      registerUser() {
        return this.axiosInstance.post('auth/users/',
          {
            'username': this.username,
            'password': this.password,
            'email': '',
            'user_type': this.userType,
          }).then(({data}) => {
          localStorage.setItem('tokens', JSON.stringify(data))
          this.axiosInstance.defaults.headers['Authorization'] = `Bearer ${
            data.access
          }`;
          this.$router.push({name: 'main'})
        })
      }
    }
  }
</script>
