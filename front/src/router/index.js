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
  {
    path: '/admin',
    name: 'adminLoginPage',
    component: () => import('@/pages/login/adminLoginPage.vue'),
  },
  {
    path: '/admin/manage-tours',
    name: 'adminPage',
    component: () => import('@/pages/admin/adminPage.vue'),
  },
  {
    path: '/admin/manage-tours/:tour_id',
    name: 'AdminDetailPage',
    component: () => import('@/pages/admin-detail/AdminDetailPage.vue'),
  },
  {
    path: '/admin/manage-tours/add-tour',
    name: 'AddTourPage',
    component: () => import('@/pages/add-tour/AddTourPage.vue')
  },
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
})

export default router
