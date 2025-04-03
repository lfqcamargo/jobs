import { zodResolver } from '@hookform/resolvers/zod'
import { useMutation } from '@tanstack/react-query'
import axios from 'axios'
import { useState } from 'react'
import { useForm } from 'react-hook-form'
import { toast } from 'sonner'
import * as z from 'zod'
import { parse, isValid } from 'date-fns'
import { ptBR } from 'date-fns/locale'
import { editUser } from '@/api/edit-user'
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

interface PropsEditUser {
  id: number
  name: string
  email: string
  birthdayDate: string
  curriculum: string
  refetch: any
}

const editUserFormSchema = z
  .object({
    name: z
      .string()
      .max(50, { message: 'Usuário deve conter no máximo 40 caracters.' })
      .optional(),

    email: z.string().email({
        message: 'Email inválido.',
      }).optional(),
    password: z
      .string()
      .max(20, {
        message: 'Senha deve conter no máximo 20 caracters',
      }).optional(),

    repeatPassword: z
      .string()
      .max(20, { message: 'Senha deve conter no máximo 20 caracteres.' }),

      birthdayDate: z
        .string()
        .optional()
        .refine((date) => {
          if (!date) return true 
          const parsedDate = parse(date, 'dd/MM/yyyy', new Date(), { locale: ptBR })
          return isValid(parsedDate)
        }, { message: 'Data inválida' }),

        curriculum: z
        .any()
        .optional()
        .refine((fileList) => {
          if (!fileList || !(fileList instanceof FileList) || fileList.length === 0) {
            return true 
          }
          return fileList[0] instanceof File
        }, {
          message: 'Currículo deve ser um arquivo.',
        })
        .refine((fileList: FileList) => {
          if (!fileList || fileList.length === 0) return true 
          return fileList[0].size <= 2 * 1024 * 1024
        }, { 
          message: 'O arquivo deve ter no máximo 2MB',
        })
        .refine((fileList: FileList) => {
          if (!fileList || fileList.length === 0) return true 
          return fileList[0].type === 'application/pdf'
        }, {
          message: 'O arquivo deve estar no formato PDF',
        }),
  })
  .refine((data) => data.password === data.repeatPassword, {
    message: 'As senhas devem ser iguais.',
    path: ['repeatPassword'],
  })

export type EditUserForm = z.infer<typeof editUserFormSchema>

export function EditUser({
  id,
  name,
  email,
  birthdayDate,
  curriculum,
  refetch,
}: PropsEditUser) {
  const [isDialogOpen, setDialogOpen] = useState(false)

  const editUserFn = useMutation({
    mutationFn: editUser,
  })

  const {
    register,
    handleSubmit,
    reset,
    formState: { errors, isSubmitting },
  } = useForm<EditUserForm>({
    resolver: zodResolver(editUserFormSchema),
    mode: 'onChange',
    defaultValues: {   
      name: name,
      email: email,
      birthdayDate: birthdayDate,
      curriculum: curriculum,
    }
  })

  async function handleEditUser(data: EditUserForm) {
    try {
      await editUserFn.mutateAsync({
        id: id,
        name: data.name,
        email: data.email,
        password: data.password,
        birthdayDate: data.birthdayDate,
        curriculum: data.curriculum
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
    <Dialog open={isDialogOpen} onOpenChange={setDialogOpen}>
      <DialogTrigger asChild>
        <Button> Editar </Button>
      </DialogTrigger>
      <DialogContent className="sm:max-w-[425px]">
        <DialogHeader>
          <DialogTitle>Editar</DialogTitle>
          <DialogDescription>Edição do Usuário {name}</DialogDescription>
        </DialogHeader>
        <form
            onSubmit={handleSubmit(handleEditUser)}
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
                {...register('curriculum')} />
                {errors.curriculum && typeof errors.curriculum.message === 'string' && (
                  <div className='text-destructive'>{errors.curriculum.message}</div>
                )}
            </div>
          <div className="flex flex-col items-center gap-4 w-full">
            <DialogFooter className="w-full flex flex-row flex-1 gap-2">
              <Button
                className="w-full"
                disabled={isSubmitting}
              >
                Editar
              </Button>
            </DialogFooter>
          </div>
        </form>
      </DialogContent>
    </Dialog>
  )
}
