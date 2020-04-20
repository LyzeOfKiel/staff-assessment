<template>
  <v-app>
    <router-view/>
  </v-app>
</template>

<script>
  export default {
    name: 'App',
    props: {
      source: String,
    },
    created() {
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
        },
      )
    },
  }
</script>
