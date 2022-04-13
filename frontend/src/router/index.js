import Vue from "vue";
import VueRouter from "vue-router";
import Editor from "../components/Editor.vue";

Vue.use(VueRouter);

const routes = [
  {
    path: "/:type?",
    name: "editor",
    component: Editor
  }
];

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes
});

export default router;
