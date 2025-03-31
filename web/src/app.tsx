import { RouterProvider } from 'react-router-dom'

import { router } from './router'
import { ThemeProvider } from './components/theme/theme-provider'

export function App() {
  return (
    <ThemeProvider defaultTheme='system' storageKey='jobs001'>

      <RouterProvider router={router} />
    </ThemeProvider>
  )
}
