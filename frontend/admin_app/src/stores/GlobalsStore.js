// stores/counter.js
import { defineStore } from 'pinia'

export const useGlobalsStore = defineStore('globalsStore', {
  state: () => {
    return {
      JV_EMAIL_NOT_CONFIRMED: "email_not_confirmed",
      JV_ADMIN_NOT_CONFIRMED: "admin_not_confirmed",
      JV_ADMIN_REFUSED: "admin_refused",
      JV_INVALID_CREDENTIALS: "invalid_credentials",
      JV_SUCCESS: "success",
      JV_ERROR: "error",
      JV_ALREADY_EXISTS: "already_exists",
      JF_RESULT: "result",
      JF_EMAIL: "email",
      JF_PASSWORD: "password",
      registration_sign_in_url: "http://127.0.0.1:5000/registration/sign_in",
      registration_sign_up_url: "http://127.0.0.1:5000/registration/sign_up",
    }
  },
})