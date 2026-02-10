# Apple Music Local V1

A local music player with FastAPI backend and React frontend.

## Prerequisites

- Python 3.9+
- Node.js & npm
- PostgreSQL (optional, defaults to SQLite)

## Setup


1. Create and activate a Conda environment (recommended):
   conda create -n fk python=3.10
   conda activate fk
2. Install dependencies:
   pip install -r requirements.txt
3. Run the backend:
   uvicorn app.main:app --reload


4. Install dependencies:
   npm install
5. Run the frontend:
   npm run dev

## Music Library

Place your MP3 files in the `music_library/` directory. Each subfolder will be treated as an album.
Example:

music_library/
  Pink Floyd - The Dark Side of the Moon/
    01 - Speak to Me.mp3
    cover.jpg

The app will scan the library on startup and extract metadata.

## Instructions to Play MP3 Tracks

1. Start both backend and frontend.
2. Open the browser at the address provided by Vite (usually `http://localhost:5173`).
3. Your music will appear in the "Listen Now" or "Library" views.
4. Click on an album to see its tracks.
5. Click "Play" on a track to start playback.



