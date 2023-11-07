import { createRouter, createWebHashHistory } from 'vue-router'
import RegistrationView from "./components/pages/RegistrationView.vue"
import HomePage from "./components/pages/HomePage.vue"

export default createRouter({
    history: createWebHashHistory(),
    routes: [
        { path: "/home", component: HomePage, name: "home" },
        { path: "/sign_in", component: RegistrationView, name: "sign_in",
            props: { sign_in: true }},
        { path: "/sign_up", component: RegistrationView, name: "sign_up",
            props: { sign_in: false }},
    ],
})