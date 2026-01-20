@echo off
cd /d "E:\TODO-FULL_STACK"

REM Create the frontend directory with Next.js
echo n | npx create-next-app@latest frontend --ts --eslint --tailwind --src-dir --app --import-alias "@/*" --turbopack=false

REM Install additional required packages
cd frontend
npm install better-auth lucide-react
npm install --save-dev @types/node @types/react @types/react-dom typescript