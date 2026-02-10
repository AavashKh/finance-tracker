import { useState } from 'react'
import { DashboardLayout } from './layouts/DashboardLayout'
import './App.css'

function App() {
  const [count, setCount] = useState(0)

  return (
    <DashboardLayout>

      <div className='space-y-6'>
        <h1 className='text-2xl font-bold text-white'>Financial Dashboard</h1>

        <div className='p-6 bg-app-surface border border-app-muted/20 rounded-xl shadow-fin'>
          <p className='text-app-muted mb-4'>Metric Tracking Engine</p>

          <button
            onClick={() => setCount((count) => count + 1)}
            className='px-4 py-2 bg-gain text-app-bg font-bold rounded-lg transition-transform active:scale-95'
          > 
            Incremental Gains: {count}
            </button>
        </div>

        <p className='text-app-muted text-sm'>
          System status: <span className='text-gain'>Operational</span>
        </p>
      </div>

    </DashboardLayout>
  )
}

export default App
