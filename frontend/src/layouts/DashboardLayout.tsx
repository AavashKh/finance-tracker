/**
 * /src/layouts/DashboardLayout.tsx
 *
 * This is the layout for the dashboard pages. It includes the sidebar and the main content area.
 * The sidebar is a separate component that can be reused across different pages.
 */

import React from 'react';

// I can just write the Sidebar code once with this snippet
interface Props {
    children: React.ReactNode;
}

export const DashboardLayout = ({ children }: Props) => {
    return (
        // Hides horizontal overflow and sets height to the viewport
        <div className="flex h-screen overflow-hidden bg-app-bg">
            {/* Sidebar : Fixed wideth on large screen, hidden on small */}
            <aside className='w-64 shrink-0 border-r border-app-muted/10 bg-app-surface/50'>
                <div className='p-6'>
                    <h2 className='text-xl font-bold text-white tracking-tight'>
                        CASH<span className='text-gain'>RIVER</span>
                    </h2>
                </div>
                <nav className='mt-4 px-4 space-y-2'>
                    {/* Navigation links */}
                    <div className='p-3 rounded-md bg-app-muted/10 text-white cursor-pointer'>Dashboard</div>
                    <div className='p-3 rounded-md text-app-muted hover:bg-app-muted/5 cursor-pointer'>Portfolio</div> 
                    <div className='p-3 rounded-md text-app-muted hover:bg-app-muted/5 cursor-pointer'>Markets</div> 
                </nav>
            </aside>

            {/* Main content area */}
            <main className='flex-1 flex flex-col min-w-0 overflow-hidden'>

                {/* Top header / Search Bar */}
                <header className='h-16 border-b border-app-muted/10 flex items-center justify-between px-8 bg-app-bg/80 backdrop-blur-md'>
                    <div className='text-app-muted text-sm font-medium'>Market Overview</div>
                    <div className='flex items-center gap-4'>
                        <div className='h-8 w-8 rounded-full bg-app-muted/20 border border-app-muted/30'></div>
                    </div>
                </header>

                {/* Viewport : Where the page renders */}
                <section className='flex-1 overflow-y-auto p-8 custom-scrollbar'>
                    <div className='max-w-7xl mx-auto'>
                    {children}
                    </div>
                </section>
            </main>
        </div>
    );
};