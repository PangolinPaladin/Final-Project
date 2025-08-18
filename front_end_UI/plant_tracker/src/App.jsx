import { useState } from 'react'
import ClerkProviderWithRoutes from "./auth/ClerkProviderWithRoutes.jsx"
import {Routes, Route} from "react-router-dom"

import {Layout} from "./layout/Layout.jsx"
import {ChallengeGenerator} from ".plants.challenge/ChallengeGenerator.jsx";
import {HistoryPanel} from "./history/HistoryPanel.jsx";
import {AuthenticationPage} from "./auth/AuthenticationPage.jsx"

// import reactLogo from './assets/react.svg'
// import viteLogo from '/vite.svg'
import './App.css'

function App() {
  return 
    <ClerkProviderWithRoutes>
      <Routes>
        <Route path="/sign-in/*" element={<AuthenticationPage />} />
        <Route path="/sign-up" element={<AuthenticationPage />} />
        <Route element={<Layout />}>
          <Route path="/" element={ChallengeGenerator } />
          {/* Doesn't like these nested fragments, */}
          <Route path="/maintenance.history" element={<HistoryPanel />} />
        </Route>
      </Routes> 
  </ClerkProviderWithRoutes>
}
export default App
