import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import { createPinia } from 'pinia'
import { useUserInfoStore } from '@/stores/UserInfoStore.js';


const pinia = createPinia()
const app = createApp(App)
app.use(router)
app.use(pinia)
app.mount('#app')

router.beforeEach((to, from) => {
    const user_info_store = useUserInfoStore();
    console.log(to.name)
    console.log(user_info_store.is_auntificated)
    if (!user_info_store.is_auntificated && to.name !== 'sign_in' && to.name !== "sign_up") {
        return { name: 'sign_in' }
    }
})


