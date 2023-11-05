import { createRouter, createWebHashHistory } from 'vue-router'
import RegistrationView from "./components/pages/RegistrationView.vue"
import HomePage from "./components/pages/HomePage.vue"

export default createRouter({
    history: createWebHashHistory(),
    routes: [
        { path: "/", component: HomePage },
        { path: "/sign_in", component: RegistrationView,
            props: { sign_in: true }},
        { path: "/sign_up", component: RegistrationView,
            props: { sign_in: false }},
    ]
})