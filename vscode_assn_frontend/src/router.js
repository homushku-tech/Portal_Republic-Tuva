import { createMemoryHistory, createRouter } from 'vue-router'

import Republic from './components/top_navbar/Republic.vue'
import Main from './components/top_navbar/Main.vue'
import Investpasport from './components/top_navbar/Investpasport.vue'
import Internetpriem from  './components/top_navbar/Internetpriem.vue'
import Officialdocument from './components/top_navbar/Officialdocument.vue'
import Contacts from  './components/top_navbar/Contacts.vue'

const routes = [
  { path: '/', component: Main },
  { path: '/republic', component: Republic },
  { path: '/investpasport', component: Investpasport},
  { path: '/internetpriem', component: Internetpriem },
  { path: '/officialdocument', component: Officialdocument },
  { path: '/contacts', component: Contacts },
]

const router = createRouter({
  history: createMemoryHistory(),
  routes,
})

export default router