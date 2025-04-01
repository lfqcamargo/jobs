import { RouterProvider } from 'react-router-dom'

import { router } from './router'
import { QueryClientProvider } from '@tanstack/react-query'
import { ThemeProvider } from './components/theme/theme-provider'
import { Helmet, HelmetProvider } from 'react-helmet-async'
import { queryClient } from './lib/react-query'
import { Toaster } from 'sonner'

export function App() {
  return (
    <HelmetProvider>
      <ThemeProvider defaultTheme='system' storageKey='jobs001'>
        <Helmet titleTemplate="%s | pizza.shop" />

        <Toaster richColors />
        <QueryClientProvider client={queryClient}>
          <RouterProvider router={router} />
        </QueryClientProvider>
      </ThemeProvider>
    </HelmetProvider>
  )
}
