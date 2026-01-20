'use client';

import { useState, useEffect } from 'react';
import { useRouter } from 'next/navigation';
import Link from 'next/link';
import { useAuth } from '@/contexts/AuthContext';
import {
  getUserTasks,
  createUserTask,
  updateUserTask,
  deleteUserTask,
  toggleTaskCompletion
} from '@/utils/api';

// Define the Task type
type Task = {
  id: number;
  title: string;
  description: string;
  completed: boolean;
};

export default function DashboardPage() {
  const [tasks, setTasks] = useState<Task[]>([]);
  const [title, setTitle] = useState('');
  const [description, setDescription] = useState('');
  const [editingTask, setEditingTask] = useState<Task | null>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);
  const [success, setSuccess] = useState<string | null>(null);
  const [actionLoading, setActionLoading] = useState<number | null>(null); // Track loading state for individual actions
  const router = useRouter();
  const { user, signOut, isLoading } = useAuth();

  // Protect the route - redirect to signin if not authenticated
  useEffect(() => {
    if (!isLoading && !user) {
      router.push('/signin');
    }
  }, [user, isLoading, router]);

  // Load tasks on component mount
  useEffect(() => {
    if (!user && !isLoading) {
      router.push('/signin');
      return;
    }

    if (user) {
      const fetchTasks = async () => {
        try {
          setLoading(true);
          const tasksFromApi = await getUserTasks(user.id);
          setTasks(tasksFromApi);
        } catch (err) {
          setError('Failed to load tasks');
          console.error('Error loading tasks:', err);
        } finally {
          setLoading(false);
        }
      };

      fetchTasks();
    }
  }, [user, isLoading, router]);

  // Clear success message after 3 seconds
  useEffect(() => {
    if (success) {
      const timer = setTimeout(() => {
        setSuccess(null);
      }, 3000);
      return () => clearTimeout(timer);
    }
  }, [success]);

  // Handle logout
  const handleLogout = () => {
    signOut();
  };

  // Create a new task
  const handleCreateTask = async (e: React.FormEvent) => {
    e.preventDefault();

    if (!title.trim() || !user) return;

    try {
      const newTask = await createUserTask(user.id, { title, description });
      setTasks([...tasks, newTask]);
      setTitle('');
      setDescription('');
      setSuccess('Task added successfully!');
      setError(null);
    } catch (err: any) {
      setError(err.message || 'Failed to create task');
      console.error('Error creating task:', err);
      setSuccess(null);
    }
  };

  // Update an existing task
  const handleUpdateTask = async (e: React.FormEvent) => {
    e.preventDefault();

    if (!editingTask || !title.trim() || !user) return;

    try {
      setActionLoading(editingTask.id);
      const updatedTask = await updateUserTask(user.id, editingTask.id, {
        title: title,
        description: description
      });

      setTasks(tasks.map(task =>
        task.id === editingTask.id ? updatedTask : task
      ));

      setEditingTask(null);
      setTitle('');
      setDescription('');
      setSuccess('Task updated successfully!');
      setError(null);
    } catch (err: any) {
      setError(err.message || 'Failed to update task');
      console.error('Error updating task:', err);
      setSuccess(null);
    } finally {
      setActionLoading(null);
    }
  };

  // Delete a task
  const handleDeleteTask = async (id: number) => {
    if (!user) return;

    if (window.confirm('Are you sure you want to delete this task?')) {
      try {
        setActionLoading(id);
        await deleteUserTask(user.id, id);
        setTasks(tasks.filter(task => task.id !== id));
        setSuccess('Task deleted successfully!');
        setError(null);
      } catch (err: any) {
        setError(err.message || 'Failed to delete task');
        console.error('Error deleting task:', err);
        setSuccess(null);
      } finally {
        setActionLoading(null);
      }
    }
  };

  // Toggle task completion status
  const toggleComplete = async (id: number) => {
    if (!user) return;

    try {
      setActionLoading(id);
      const updatedTask = await toggleTaskCompletion(user.id, id);
      setTasks(tasks.map(task =>
        task.id === id ? updatedTask : task
      ));
      setSuccess(updatedTask.completed ? 'Task marked as complete!' : 'Task marked as incomplete!');
      setError(null);
    } catch (err: any) {
      setError(err.message || 'Failed to update task status');
      console.error('Error toggling task completion:', err);
      setSuccess(null);
    } finally {
      setActionLoading(null);
    }
  };

  // Prepare for editing a task
  const startEditing = (task: Task) => {
    setEditingTask(task);
    setTitle(task.title);
    setDescription(task.description || '');
  };

  // Cancel editing
  const cancelEditing = () => {
    setEditingTask(null);
    setTitle('');
    setDescription('');
  };

  // Show loading state if auth is still loading
  if (isLoading) {
    return (
      <div className="min-h-screen flex items-center justify-center bg-gradient-to-br from-pink-50 to-purple-100">
        <p className="text-xl">Loading...</p>
      </div>
    );
  }

  // Show nothing if not authenticated (will redirect)
  if (!user && !isLoading) {
    return null;
  }

  return (
    <div className="min-h-screen bg-gradient-to-br from-pink-50 to-purple-100 p-4">
      <div className="max-w-6xl mx-auto">
        {/* Header */}
        <header className="py-6 flex justify-between items-center">
          <h1 className="text-3xl font-bold bg-clip-text text-transparent bg-gradient-to-r from-pink-500 to-purple-600">
            TodoHub Dashboard
          </h1>
          <button
            onClick={handleLogout}
            className="px-4 py-2 bg-pink-500 text-white rounded-lg hover:bg-pink-600 transition-colors"
          >
            Logout
          </button>
        </header>

        <main className="mt-8">
          {/* Success message */}
          {success && (
            <div className="mb-4 p-3 bg-green-100 text-green-700 rounded-lg">
              {success}
            </div>
          )}

          {/* Error message */}
          {error && (
            <div className="mb-4 p-3 bg-red-100 text-red-700 rounded-lg">
              {error}
            </div>
          )}

          {/* Add Task Form */}
          <div className="bg-white p-6 rounded-xl shadow-lg mb-8">
            <h2 className="text-2xl font-semibold mb-4">
              {editingTask ? 'Edit Task' : 'Add New Task'}
            </h2>

            <form onSubmit={editingTask ? handleUpdateTask : handleCreateTask}>
              <div className="mb-4">
                <label htmlFor="title" className="block text-gray-700 mb-2">Title *</label>
                <input
                  id="title"
                  type="text"
                  value={title}
                  onChange={(e) => setTitle(e.target.value)}
                  className="w-full px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-pink-500"
                  placeholder="Task title"
                  required
                />
              </div>

              <div className="mb-6">
                <label htmlFor="description" className="block text-gray-700 mb-2">Description</label>
                <textarea
                  id="description"
                  value={description}
                  onChange={(e) => setDescription(e.target.value)}
                  className="w-full px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-pink-500"
                  placeholder="Task description"
                  rows={3}
                />
              </div>

              <div className="flex gap-3">
                <button
                  type="submit"
                  disabled={actionLoading !== null}
                  className={`px-6 py-3 bg-pink-500 text-white rounded-lg hover:bg-pink-600 transition-colors ${
                    actionLoading !== null ? 'opacity-50 cursor-not-allowed' : ''
                  }`}
                >
                  {actionLoading !== null ? (
                    <span className="flex items-center">
                      <svg className="animate-spin -ml-1 mr-2 h-4 w-4 text-white" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24">
                        <circle className="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" strokeWidth="4"></circle>
                        <path className="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path>
                      </svg>
                      Processing...
                    </span>
                  ) : (
                    editingTask ? 'Update Task' : 'Add Task'
                  )}
                </button>

                {editingTask && (
                  <button
                    type="button"
                    onClick={cancelEditing}
                    className="px-6 py-3 bg-gray-300 text-gray-700 rounded-lg hover:bg-gray-400 transition-colors"
                  >
                    Cancel
                  </button>
                )}
              </div>
            </form>
          </div>

          {/* Tasks List */}
          <div className="bg-white p-6 rounded-xl shadow-lg">
            <h2 className="text-2xl font-semibold mb-6">Your Tasks</h2>

            {loading ? (
              <div className="flex justify-center items-center py-8">
                <div className="animate-spin rounded-full h-12 w-12 border-t-2 border-b-2 border-pink-500"></div>
              </div>
            ) : tasks.length === 0 ? (
              <p className="text-gray-500 text-center py-8">No tasks yet. Add your first task!</p>
            ) : (
              <div className="space-y-4">
                {tasks.map((task) => (
                  <div
                    key={task.id}
                    className={`p-4 border rounded-lg flex justify-between items-start ${
                      task.completed ? 'bg-green-50 border-green-200' : 'bg-white border-gray-200'
                    }`}
                  >
                    <div>
                      <h3 className={`text-lg font-medium ${task.completed ? 'line-through text-gray-500' : ''}`}>
                        {task.title}
                      </h3>
                      <p className={`${task.completed ? 'line-through text-gray-500' : 'text-gray-600'} mt-1`}>
                        {task.description}
                      </p>
                    </div>

                    <div className="flex space-x-2">
                      <button
                        onClick={() => toggleComplete(task.id)}
                        disabled={actionLoading === task.id}
                        className={`p-2 rounded-full ${
                          task.completed
                            ? 'bg-green-100 text-green-600'
                            : 'bg-gray-100 text-gray-400'
                        } ${actionLoading === task.id ? 'opacity-50 cursor-not-allowed' : 'hover:opacity-80'}`}
                        aria-label={task.completed ? "Mark as incomplete" : "Mark as complete"}
                      >
                        {actionLoading === task.id ? (
                          <svg className="animate-spin h-5 w-5 text-current" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24">
                            <circle className="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" strokeWidth="4"></circle>
                            <path className="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path>
                          </svg>
                        ) : task.completed ? (
                          <svg xmlns="http://www.w3.org/2000/svg" className="h-5 w-5" viewBox="0 0 20 20" fill="currentColor">
                            <path fillRule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clipRule="evenodd" />
                          </svg>
                        ) : (
                          <svg xmlns="http://www.w3.org/2000/svg" className="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                            <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M6 18L18 6M6 6l12 12" />
                          </svg>
                        )}
                      </button>

                      <button
                        onClick={() => startEditing(task)}
                        disabled={actionLoading === task.id}
                        className="px-3 py-1 bg-blue-100 text-blue-800 rounded hover:bg-blue-200 disabled:opacity-50 disabled:cursor-not-allowed"
                      >
                        Edit
                      </button>

                      <button
                        onClick={() => handleDeleteTask(task.id)}
                        disabled={actionLoading === task.id}
                        className="px-3 py-1 bg-red-100 text-red-800 rounded hover:bg-red-200 disabled:opacity-50 disabled:cursor-not-allowed"
                      >
                        Delete
                      </button>
                    </div>
                  </div>
                ))}
              </div>
            )}
          </div>
        </main>

        <footer className="py-8 text-center text-gray-600 mt-12">
          <p>© 2026 TodoHub. All rights reserved.</p>
        </footer>
      </div>
    </div>
  );
}