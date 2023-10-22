import { createRouter, createWebHashHistory } from 'vue-router'
import RegistrationPage from "./components/pages/RegistrationPage.vue"
import HomePage from "./components/pages/HomePage.vue"
import App from './App.vue'

export default createRouter({
    history: createWebHashHistory(),
    routes: [
        { path: "/", component: HomePage },
        { path: "/sign_in", component: RegistrationPage },
        { path: "/sign_up", component: RegistrationPage }
    ]
})