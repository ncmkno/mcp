import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'

import { StytchProvider } from '@stytch/react';
import { createStytchUIClient } from '@stytch/react/ui';

import './index.css'
import App from './App.jsx'

const stytch = createStytchUIClient('public-token-test-aad0d6b0-58b6-4d75-9768-479becc11e43');

createRoot(document.getElementById('root')).render(
  <StrictMode>
    <StytchProvider stytch={stytch}>
      <App />
    </StytchProvider>
  </StrictMode>,
)
