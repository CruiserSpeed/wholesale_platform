import { defineStore } from 'pinia'

export const useUserInfoStore = defineStore('userInfoStore', {
  state: () => {
    return {
        is_auntificated: false
    }
  },
})