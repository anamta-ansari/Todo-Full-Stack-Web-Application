// app/api/register/route.ts
import { NextRequest } from 'next/server';
import { NextResponse } from 'next/server';

export async function POST(req: NextRequest) {
  try {
    const body = await req.json();
    const { email, password } = body;

    // Basic validation
    if (!email || !password) {
      return NextResponse.json(
        { error: 'Email and password are required' },
        { status: 400 }
      );
    }

    // In a real app, you would create a user in the database
    // For this demo, we'll just accept any non-empty email/password
    if (email && password) {
      // Create a mock user object
      const user = {
        id: 1,
        email,
        name: email.split('@')[0], // Use part of email as name
      };

      // Create a mock JWT token (in a real app, you'd generate a real JWT)
      const token = `mock-jwt-token-${Date.now()}-${Math.random().toString(36).substr(2, 9)}`;
      
      return NextResponse.json({ 
        user,
        token,
        message: 'Registration successful'
      });
    } else {
      return NextResponse.json(
        { error: 'Invalid registration data' },
        { status: 400 }
      );
    }
  } catch (error) {
    console.error('Registration error:', error);
    return NextResponse.json(
      { error: 'Internal server error' },
      { status: 500 }
    );
  }
}