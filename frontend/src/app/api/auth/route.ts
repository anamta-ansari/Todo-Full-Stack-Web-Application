// app/api/auth/[...nextauth]/route.ts
import { NextRequest } from 'next/server';
import { NextResponse } from 'next/server';

export async function POST(req: NextRequest) {
  const { pathname } = req.nextUrl;
  const action = pathname.split('/').pop();

  try {
    if (action === 'login') {
      // Mock login
      const body = await req.json();
      const { email, password } = body;

      // In a real app, you would validate credentials against a database
      // For this demo, we'll just accept any non-empty email/password
      if (email && password) {
        // Create a mock JWT token
        const token = `mock-jwt-token-${Date.now()}`;
        
        return NextResponse.json({ 
          user: { id: 1, email, name: email.split('@')[0] },
          token 
        });
      } else {
        return NextResponse.json({ error: 'Invalid credentials' }, { status: 401 });
      }
    } else if (action === 'register') {
      // Mock registration
      const body = await req.json();
      const { email, password } = body;

      // In a real app, you would create a user in the database
      // For this demo, we'll just accept any non-empty email/password
      if (email && password) {
        // Create a mock JWT token
        const token = `mock-jwt-token-${Date.now()}`;
        
        return NextResponse.json({ 
          user: { id: 1, email, name: email.split('@')[0] },
          token 
        });
      } else {
        return NextResponse.json({ error: 'Invalid registration data' }, { status: 400 });
      }
    } else if (action === 'logout') {
      // Mock logout
      return NextResponse.json({ message: 'Logged out successfully' });
    } else {
      return NextResponse.json({ error: 'Unknown action' }, { status: 400 });
    }
  } catch (error) {
    return NextResponse.json({ error: 'Internal server error' }, { status: 500 });
  }
}