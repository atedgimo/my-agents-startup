#!/bin/bash
# -----------------------------------------------------------
# Habit Tracker Deployment Script (run.sh)
# Usage: ./run.sh [docker-compose | docker]
# -----------------------------------------------------------

set -e # Exit immediately if a command exits with a non-zero status.

echo "=============================================="
echo "🚀 Starting Habit Tracker Backend Service"
echo "=============================================="

if [ "$1" == "docker-compose" ]; then
    echo "✅ Using Docker Compose for orchestration..."
    # Build and run the services defined in docker-compose.yml
    docker compose up --build -d backend
    echo ""
    echo "✨ Backend service started successfully via Docker Compose."
    echo "   Access API at: http://localhost:8000/api/v1"
elif [ "$1" == "docker" ]; then
    echo "⚠️ Using raw 'docker run' command (Less robust than compose)."
    # This is a simplified single-container run for basic testing
    docker run -d \
        --name habit_tracker_backend \
        -p 8000:8000 \
        -v $(pwd)/data/local_tracker.db:/app/src/backend/local_tracker.db \
        your_image_name # NOTE: Replace 'your_image_name' with the actual image name built by Dockerfile

    echo ""
    echo "✨ Backend service started successfully via raw Docker run."
else
    echo "❌ Error: Please specify a deployment method."
    echo "Usage: $0 [docker-compose | docker]"
fi

echo "=============================================="
echo "Deployment complete. Check logs for details."