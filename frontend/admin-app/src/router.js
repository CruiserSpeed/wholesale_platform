import { createRouter, createWebHashHistory } from 'vue-router'
import RegistrationPageSignIn from "./components/pages/RegistrationPageSignIn.vue"
import RegistrationPageSignUp from "./components/pages/RegistrationPageSignUp.vue"
import HomePage from "./components/pages/HomePage.vue"

export default createRouter({
    history: createWebHashHistory(),
    routes: [
        { path: "/", component: HomePage },
        { path: "/sign_in", component: RegistrationPageSignIn },
        { path: "/sign_up", component: RegistrationPageSignUp }
    ]
})