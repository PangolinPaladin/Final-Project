import { Outlet } from "react-router";


const main_layout = () => {
    return (
        <>
            < Header />
            < Outlet />
            < Footer />

        </>
    )
}

export default main_layout;
