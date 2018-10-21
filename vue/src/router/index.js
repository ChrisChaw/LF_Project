import Vue from 'vue'
import Router from 'vue-router'
import Course from '@/components/Course'


Vue.use(Router);

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Course',
      component: Course
    },

  ]
})
