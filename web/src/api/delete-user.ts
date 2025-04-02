import { api } from '@/lib/axios'

export interface DeleteUserParam {
    identifier: number
}

export async function deleteUser({identifier}: DeleteUserParam): Promise<void> {
  await api.delete(`/users/${identifier}`)
}
