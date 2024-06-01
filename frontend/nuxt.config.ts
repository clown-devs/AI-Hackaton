// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  devtools: { enabled: true },

  modules: [
    'nuxt-svgo',
    [
      '@nuxtjs/google-fonts',
      {
        families: {
          'Open Sans': [400, 700],
          Montserrat: true,
        },
      },
    ],
  ],
});
