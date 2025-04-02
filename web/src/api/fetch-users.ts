import { api } from '@/lib/axios'

export interface FetchUsersResponse {
  users: [
    {
      id: number
      name: string
      email: string
      birthday_date: string
      curriculum: string
    },
  ]
}

export async function fetchUsers(): Promise<FetchUsersResponse> {
  const response = await api.get<FetchUsersResponse>(`/users`)
  
  return response.data
}
