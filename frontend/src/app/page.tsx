'use client';

import Link from 'next/link';
import { useState } from 'react';

export default function HomePage() {
  const [darkMode, setDarkMode] = useState(false);

  return (
    <div className={`min-h-screen ${darkMode ? 'bg-gray-900 text-white' : 'bg-gradient-to-br from-pink-50 to-purple-100 text-gray-900'}`}>
      {/* Header */}
      <header className="py-6 px-4 sm:px-6 lg:px-8">
        <div className="flex justify-between items-center">
          <h1 className="text-2xl font-bold bg-clip-text text-transparent bg-gradient-to-r from-pink-500 to-purple-600">
            TodoHub
          </h1>
          <nav className="hidden md:flex space-x-8">
            <Link href="/" className="hover:text-pink-500 transition-colors">Home</Link>
            <Link href="/signin" className="hover:text-pink-500 transition-colors">Sign In</Link>
            <Link href="/signup" className="hover:text-pink-500 transition-colors">Sign Up</Link>
          </nav>
          <button 
            onClick={() => setDarkMode(!darkMode)}
            className="p-2 rounded-full hover:bg-gray-200 dark:hover:bg-gray-700"
          >
            {darkMode ? '☀️' : '🌙'}
          </button>
        </div>
      </header>

      {/* Hero Section */}
      <section className="py-20 px-4 text-center">
        <h1 className="text-4xl md:text-6xl font-bold mb-6">
          Organize Your Life with <span className="bg-clip-text text-transparent bg-gradient-to-r from-pink-500 to-purple-600">TodoHub</span>
        </h1>
        <p className="text-xl max-w-2xl mx-auto mb-10">
          The most intuitive and beautiful task management app to boost your productivity.
        </p>
        <div className="space-x-4">
          <Link 
            href="/signin" 
            className="px-6 py-3 bg-pink-500 text-white rounded-lg hover:bg-pink-600 transition-colors shadow-lg"
          >
            Sign In
          </Link>
          <Link 
            href="/signup" 
            className="px-6 py-3 bg-white text-pink-500 border border-pink-500 rounded-lg hover:bg-pink-50 transition-colors shadow-lg"
          >
            Sign Up
          </Link>
        </div>
      </section>

      {/* Features Section */}
      <section className="py-16 px-4 max-w-6xl mx-auto">
        <h2 className="text-3xl font-bold text-center mb-12">Powerful Features</h2>
        <div className="grid grid-cols-1 md:grid-cols-3 gap-8">
          <div className={`p-6 rounded-xl shadow-lg ${darkMode ? 'bg-gray-800' : 'bg-white'}`}>
            <h3 className="text-xl font-semibold mb-3">Easy Organization</h3>
            <p>Create, categorize, and prioritize your tasks effortlessly.</p>
          </div>
          <div className={`p-6 rounded-xl shadow-lg ${darkMode ? 'bg-gray-800' : 'bg-white'}`}>
            <h3 className="text-xl font-semibold mb-3">Smart Reminders</h3>
            <p>Never miss a deadline with intelligent notifications.</p>
          </div>
          <div className={`p-6 rounded-xl shadow-lg ${darkMode ? 'bg-gray-800' : 'bg-white'}`}>
            <h3 className="text-xl font-semibold mb-3">Cross Platform</h3>
            <p>Access your tasks anywhere, anytime on any device.</p>
          </div>
        </div>
      </section>

      {/* Testimonials */}
      <section className="py-16 px-4 max-w-4xl mx-auto">
        <h2 className="text-3xl font-bold text-center mb-12">What Our Users Say</h2>
        <div className={`p-6 rounded-xl shadow-lg ${darkMode ? 'bg-gray-800' : 'bg-white'}`}>
          <p className="italic mb-4">"TodoHub transformed how I manage my daily tasks. Highly recommended!"</p>
          <p className="font-semibold">- Alex Johnson</p>
        </div>
      </section>

      {/* Footer */}
      <footer className="py-8 text-center border-t mt-12">
        <p>© 2026 TodoHub. All rights reserved.</p>
      </footer>
    </div>
  );
}