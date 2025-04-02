import { format } from 'date-fns'
import { ptBR } from 'date-fns/locale'
import { useMutation, useQuery } from '@tanstack/react-query'
import {
    Table,
    TableBody,
    TableCell,
    TableHead,
    TableHeader,
    TableRow,
  } from '@/components/ui/table'
import { fetchUsers } from '@/api/fetch-users'
import { Button } from '@/components/ui/button'
import { CreateUserForm } from './components/create-user-form'
import { deleteUser } from '@/api/delete-user'
import axios from 'axios'
import { toast } from 'sonner'

export function Users() {
    const { data: users, refetch } = useQuery({
        queryKey: ['users'],
        queryFn: () => fetchUsers(),
        staleTime: Infinity,
      })

    const { mutateAsync: deleteUserFn, isPending: isDeletingUser } =
      useMutation({
        mutationFn: deleteUser,
      })


    function handleDownloadPDF(byteArray: string, name: string) {
        const byteCharacters = atob(byteArray) 
        const byteNumbers = new Uint8Array(byteCharacters.length)
        
        for (let i = 0; i < byteCharacters.length; i++) {
            byteNumbers[i] = byteCharacters.charCodeAt(i)
        }
        
        const blob = new Blob([byteNumbers], { type: 'application/pdf' })
        const blobUrl = URL.createObjectURL(blob)
        
        const link = document.createElement('a')
        link.href = blobUrl
        link.download = name
        document.body.appendChild(link)
        link.click()
        
        document.body.removeChild(link)
        URL.revokeObjectURL(blobUrl)
    }

    async function handleDeleteUser(identifier: number) {
        try {
            await deleteUserFn({identifier})
            await refetch()
            toast.success('Usuário deletado com sucesso.')
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
            <Table>
                <TableHeader>
                <TableRow>
                    <TableHead>Nome</TableHead>
                    <TableHead>Email</TableHead>
                    <TableHead>Nascimento</TableHead>
                    <TableHead>Curriculo</TableHead>
                    <TableHead></TableHead>
                    <TableHead>
                        <CreateUserForm refetch={refetch} />
                    </TableHead>
                </TableRow>
                </TableHeader>
                <TableBody>
                {users?.users.map((user) => (
                    <TableRow key={user.id}>
                        <TableCell>{user.name}</TableCell>
                        <TableCell>{user.email}</TableCell>              
                        <TableCell>
                            {user.birthday_date
                                ? format(new Date(user.birthday_date), 'dd/MM/yyyy', { locale: ptBR })
                                : 'Data não informada'}
                        </TableCell>
                        <TableCell>
                            {user.curriculum ? (
                                <Button
                                onClick={() => handleDownloadPDF(user.curriculum, user.name)}
                                variant="link"
                                className='-ml-4'
                            >
                                Baixar PDF
                            </Button>
                            ) : (
                                'Nenhum arquivo'
                            )}
                        </TableCell>
                        <TableCell><Button variant={'default'}>Editar</Button></TableCell>
                        <TableCell>
                            <Button 
                                onClick={() => handleDeleteUser(user.id)} 
                                variant={'destructive'}
                                disabled={isDeletingUser}>
                                Excluir
                            </Button>
                        </TableCell>
                    </TableRow>
                ))}
                </TableBody>
            </Table>
        </>
    )
}