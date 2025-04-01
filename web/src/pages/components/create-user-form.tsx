import { zodResolver } from '@hookform/resolvers/zod'
import { RefetchOptions, useMutation } from '@tanstack/react-query'
import axios from 'axios'
import { useState } from 'react'
import { useForm } from 'react-hook-form'
import { toast } from 'sonner'
import * as z from 'zod'
import { parse, isValid } from 'date-fns'
import { ptBR } from 'date-fns/locale'

import { createUser } from '@/api/create-user'
import { Button } from '@/components/ui/button'
import {
  Dialog,
  DialogContent,
  DialogDescription,
  DialogFooter,
  DialogHeader,
  DialogTitle,
  DialogTrigger,
} from '@/components/ui/dialog'
import { Label } from '@/components/ui/label'
import { Input } from '@/components/ui/input'

interface CreateUserFormProps {
  refetch: (options?: RefetchOptions) => Promise<any>
}

const createUserFormSchema = z
  .object({
    name: z
      .string()
      .min(4, { message: 'Usuário deve conter pelo menos 4 caracters' })
      .max(50, { message: 'Usuário deve conter no máximo 40 caracters.' }),

    email: z.string().email({
        message: 'Email inválido.',
      }),
    password: z
      .string()
      .min(6, { message: 'Senha deve conter no mínimo 6 caracters' })
      .max(20, {
        message: 'Senha deve conter no máximo 20 caracters',
      }),

    repeatPassword: z
      .string()
      .min(6, { message: 'Senha deve conter no mínimo 6 caracteres.' })
      .max(20, { message: 'Senha deve conter no máximo 20 caracteres.' }),

      birthdayDate: z.string().refine((date) => {
        const parsedDate = parse(date, 'dd/MM/yyyy', new Date(), { locale: ptBR })
        return isValid(parsedDate)
      }, { message: 'Data inválida' }),

    cirrculum: z
      .any()
      .refine((fileList) => fileList instanceof FileList && fileList.length > 0, {
        message: 'Você deve selecionar um arquivo.',
      })
      .refine((fileList: FileList) => {
        const file = fileList[0]
        return file instanceof File
      }, {
        message: 'Currículo deve ser um arquivo.',
      })
      .refine((fileList: FileList) => {
        const file = fileList[0]
        return file.size <= 2 * 1024 * 1024
      }, { 
        message: 'O arquivo deve ter no máximo 2MB',
      })
      .refine((fileList: FileList) => {
        const file = fileList[0]
        return file.type === 'application/pdf'
      }, {
        message: 'O arquivo deve estar no formato PDF',
      }),
  })
  .refine((data) => data.password === data.repeatPassword, {
    message: 'As senhas devem ser iguais.',
    path: ['repeatPassword'],
  })

export type CreateUserForm = z.infer<typeof createUserFormSchema>

export function CreateUserForm({ refetch }: CreateUserFormProps) {

  const [isDialogOpen, setDialogOpen] = useState(false)

  const createUserFn = useMutation({
    mutationFn: createUser,
  })

  const {
    register,
    handleSubmit,
    watch,
    reset,
    formState: { errors },
  } = useForm<CreateUserForm>({
    resolver: zodResolver(createUserFormSchema),
    mode: 'onChange',
  })

  const nameWatch = watch('name')
  const emailWatch = watch('email')  
  const passwordWatch = watch('password')
  const repeatPasswordWatch = watch('repeatPassword')
  const birthdayDateWatch = watch('birthdayDate')
  const cirrculumWatch = watch('cirrculum')

  const isButtonActived = !!(
    nameWatch &&
    emailWatch &&
    passwordWatch &&
    passwordWatch &&
    repeatPasswordWatch &&
    birthdayDateWatch &&
    cirrculumWatch
  )

  async function handleCreateUser(data: CreateUserForm) {
    try {
      await createUserFn.mutateAsync({
        name: data.name,
        email: data.email,
        password: data.password,
        birthdayDate: data.birthdayDate,
        curriculum: data.cirrculum
      })

      refetch()
      reset()
      toast.success('Cadastro Realizado.')

      setDialogOpen(false)
    } catch (error) {
      if (axios.isAxiosError(error)) {
        console.log(error)
        toast.error(error.message)
      } else {
        toast.error('Ocorreu um erro inesperado.')
      }
    }
  }

  return (
    <>
      <Dialog open={isDialogOpen} onOpenChange={setDialogOpen}>
        <DialogTrigger asChild>
          <Button className='bg-green-600'> + </Button>
        </DialogTrigger>
        <DialogContent className="sm:max-w-[425px]">
          <DialogHeader>
            <DialogTitle>Criar Usuário</DialogTitle>
            <DialogDescription>Preencha os campos abaixo</DialogDescription>
          </DialogHeader>
          <form
            onSubmit={handleSubmit(handleCreateUser)}
            className="flex flex-col items-center py-6 px-4 gap-4"
          >
            <div className='w-[350px]'>
              <Label>Nome Completo:</Label>
              <Input className='w-full' {...register('name')}/>
              {errors.name && <div className='text-destructive'>{errors.name.message}</div>}
            </div>
            <div className='w-[350px]'>
              <Label>Email:</Label>
              <Input className='w-full' {...register('email')} />
              {errors.email && <div className='text-destructive'>{errors.email.message}</div>}
            </div>
            <div className='w-[350px]'>
              <Label>Senha:</Label>
              <Input type='password' className='w-full' {...register('password')} />
              {errors.password && <div className='text-destructive'>{errors.password.message}</div>}
            </div>
            <div className='w-[350px]'>
              <Label>Repita a senha:</Label>
              <Input type='password' className='w-full' {...register('repeatPassword')} />
              {errors.password && <div className='text-destructive'>{errors.password.message}</div>}
            </div>
            <div className='w-[350px]'>
              <Label>Data de Nascimento</Label>
              <Input className='w-full' {...register('birthdayDate')} />
              {errors.birthdayDate && <div className='text-destructive'>{errors.birthdayDate.message}</div>}
            </div>
            <div className='w-[350px]'>
              <Label>Currcículo</Label>
              <Input 
                className='w-full' 
                type="file" 
                accept="application/pdf" 
                {...register('cirrculum')} />
                {errors.cirrculum && typeof errors.cirrculum.message === 'string' && (
                  <div className='text-destructive'>{errors.cirrculum.message}</div>
                )}
            </div>
            <DialogFooter className="pt-4 w-full">
              <Button disabled={!isButtonActived}>Cadastrar</Button>
            </DialogFooter>
          </form>
        </DialogContent>
      </Dialog>
    </>
  )
}
