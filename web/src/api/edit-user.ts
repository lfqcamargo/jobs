import { api } from '@/lib/axios'

export interface EditUserRequest {
  id: number
  name: string | undefined
  email: string | undefined
  password: string | undefined
  birthdayDate: string | undefined
  curriculum: File | string  | undefined
}

export async function editUser({
    id,
    name,
    email,
    password,
    birthdayDate,
    curriculum,
}: EditUserRequest): Promise<void> {   
    const formData = new FormData()

    formData.append('json_data', JSON.stringify({
        id: id,
        name: name,
        email: email,
        password: password,
        birthday_date: birthdayDate,
      }))

    if (curriculum) {
      formData.append('curriculum', curriculum[0])
    }
    
    
    await api.patch('/users', formData, {
        headers: {'Content-Type': 'multipart/form-data',},
        },
    )
}
