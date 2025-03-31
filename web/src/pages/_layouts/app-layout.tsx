import { SideBar } from "@/components/sider-bar";
import { ThemeToggle } from "@/components/theme/theme-toggle";

import { Separator } from "@/components/ui/separator";
import { Outlet } from "react-router-dom";

export function AppLayout() {
    return (
        <>
            <div className="flex flex-1 w-full h-full bg-card gap-4">
                <SideBar />
                <div className="flex flex-col w-full">
                    <div className="text-right mb-2 p-2">
                        <ThemeToggle />
                        <Separator orientation="horizontal" />
                    </div>
                    <Outlet />
                </div>
            </div>
        </>
    )
}