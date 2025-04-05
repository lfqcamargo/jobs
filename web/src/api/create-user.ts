import { api } from '@/lib/axios'

export interface CreateUserRequest {
  name: string
  email: string
  password: string
  birthdayDate: string
  curriculum: File
}

export async function createUser({
    name,
    email,
    password,
    birthdayDate,
    curriculum,
}: CreateUserRequest): Promise<void> {   
    const formData = new FormData()

    formData.append('json_data', JSON.stringify({
        name: name,
        email: email,
        password: password,
        birthday_date: birthdayDate,
      }))

    formData.append('curriculum', curriculum[0])
    
    await api.post('/users', formData, {
        headers: {'Content-Type': 'multipart/form-data',},
        },
    )
}
