import {ClerkProvider} from "@clerk/clerk-react"
import {Routes} from "./Routes"
import {BrowserRouter} from "react-router-dom";

const PUBLISHABLE_KEY = import.meta.env.VITE_CLERK_PUBLISHABLE_KEY

if (!PUBLISHABLE_KEY) {
  throw new Error('Missing Publishable Key')
}

export default function ClerkProviderWithRoutes({children}) { no usages
    return (
        <ClerkProvider publishablekey={PUBLISHABLE_KEY}>
            <BrowserRouter>{children}</BrowserRouter>
        </ClerkProvider>
    )
}
