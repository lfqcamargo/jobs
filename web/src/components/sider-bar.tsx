import { Button } from "@/components/ui/button"
import { Separator } from "@/components/ui/separator"
import { Link } from 'react-router-dom'

export function SideBar() {
    return (
        <>
            <div className="w-[250px]">
                <nav>
                    <ul className="flex flex-col gap-2">
                        <li className="flex flex-col">
                            <Button variant={'outline'} asChild className="justify-start">
                                <Link to={'/'}>Início</Link>
                                </Button>
                            <Separator orientation="horizontal" />
                        </li>

                        <li className="flex flex-col">
                            <Button variant={'outline'} asChild className="justify-start">
                                <Link to={'/users'}>Usuários</Link>
                                </Button>
                            <Separator orientation="horizontal" />
                        </li>

                        <li className="flex flex-col">
                            <Button variant={'outline'} asChild className="justify-start">
                                <Link to={'/settings'}>Configurações</Link>
                                </Button>
                            <Separator orientation="horizontal" />
                        </li>

                    </ul>
                </nav>
            </div>
        </>
    )
}