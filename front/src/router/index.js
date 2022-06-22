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
    name: 'AdminLoginPage',
    component: () => import('@/pages/login/AdminLoginPage.vue'),
  },
  {
    path: '/admin/manage-tours',
    name: 'AdminPage',
    component: () => import('@/pages/admin/AdminPage.vue'),
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
  {
    path: '/admin/manage-tours/modify-tour/:tour_id',
    name: 'ModifyTourPage',
    component: () => import('@/pages/modify-tour/ModifyTourPage.vue')
  },
  {
    path: '/admin/manage-tours/add-tour-stops/:tour_id',
    name: 'AddTourStopsPage',
    component: () => import('@/pages/add-stops/AddTourStopsPage.vue')
  },
  {
    path: '/admin/manage-tours/create-stops',
    name: 'CreateStopsPage',
    component: () => import('@/pages/create-stops/CreateStopsPage.vue')
  },
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
})

export default router
