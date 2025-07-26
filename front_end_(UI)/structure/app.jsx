// JSX is XML that looks like HTML, 
// and is written in Javascript
import { Routes, Route } from "react-router";

import homestead_homepage from "./main_layout";

function App() {


    return (
        <>
        <Routes>
            <Route element={< homestead_homepage />}>
        </Routes>
        </>
    );
}

{/* Need a route for each page in the website */}