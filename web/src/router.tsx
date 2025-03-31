import { createBrowserRouter } from 'react-router-dom'

import { AppLayout } from '@/pages/_layouts/app-layout'
import { Home } from './pages/home'
import { Users } from './pages/users'
import { Settings } from './pages/settings'

export const router = createBrowserRouter([
  {
    path: '/',
    element: <AppLayout />,
    children: [
      {
        index: true,
        element: <Home />,
      }, 
      {
        path: '/users',
        element: <Users />
      },
      {
        path: '/settings',
        element: <Settings />
      }
    ]
  },
])
