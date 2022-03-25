import { createRouter, createWebHistory } from 'vue-router'

const routes = [
  {
    path: '/',
    name: 'Home',
    component: () => import('@/pages/home/HomePage.vue'),
  },
  {
    path: '/tours',
    name: 'ToursListPage',
    component: () => import('@/pages/tours-list/ToursListPage.vue'),
  },
  {
    path: '/tours/:tour_id',
    name: 'TourDetailPage',
    component: () => import('@/pages/tour-detail/TourDetailPage.vue'),
  },
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
})

export default router
