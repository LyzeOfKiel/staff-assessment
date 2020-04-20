<template>
  <div>
    <v-card width="400" class="mx-auto mt-5">
      <v-card-title class="pb-0">
        <h1>Sign in</h1>
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

        </v-form>
      </v-card-text>
      <v-card-actions>
        <v-btn @click="login" color="yellow">Login</v-btn>
        <v-btn @click="login" color="yellow" to="/register">Register here</v-btn>
      </v-card-actions>
    </v-card>
  </div>
</template>

<script>
  import axios from 'axios'

  export default {
    name: "Login",
    data: () => ({
      username: null,
      password: null,
      showPassword: false
    }),
    created() {
    },
    methods: {
      login() {
        return this.axiosInstance.post('token/',
          {
            'username': this.username,
            'password': this.password
          })
          .then(({data}) => {
            localStorage.setItem('tokens', JSON.stringify(data))
            this.axiosInstance.interceptors.request.use(
              config => {
                const tokens = JSON.parse(localStorage.getItem('tokens'));

                if (tokens) {
                  const token = tokens.access

                  if (token) {
                    config.headers.Authorization = `Bearer ${token}`;
                  }
                }
                return config;
              })
            this.$router.push({name: 'main'})
          })
      }
    }
  }
</script>
