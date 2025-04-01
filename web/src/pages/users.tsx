import { format } from 'date-fns'
import { ptBR } from 'date-fns/locale'
import { useQuery } from '@tanstack/react-query'
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

export function Users() {
    const { data: users, refetch } = useQuery({
        queryKey: ['users'],
        queryFn: () => fetchUsers(),
        staleTime: Infinity,
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
                    <TableCell><Button variant={'destructive'}>Excluir</Button></TableCell>
                    </TableRow>
                ))}
                </TableBody>
            </Table>
        </>
    )
}