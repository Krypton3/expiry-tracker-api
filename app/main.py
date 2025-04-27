import uvicorn
from fastapi import FastAPI
from app.api import reminders
from app.logging.logging_mechanism import LoggingTracker
from fastapi.middleware.cors import CORSMiddleware

# Initialize the logger
logger = LoggingTracker()

class ExpiryTrackerApp:
    def __init__(self):
        logger.info("Expiry Tracker App initialized successfully.")
    
    def main(self):
        # Create FastAPI instance
        self.app = FastAPI(title="Expiry Tracker API", version="1.0.0")
        
        # Set up CORS middleware
        self.app.add_middleware(
            CORSMiddleware,
            allow_origins=["*"],  # Allow all origins
            allow_credentials=True,
            allow_methods=["*"],  # Allow all methods
            allow_headers=["*"],  # Allow all headers
        )
        
        # Include the reminders router
        self.app.include_router(reminders.router, prefix="/api/v1/reminders", tags=["reminders"])
        
        # Return the FastAPI instance
        return self.app

# Main function to run the application
tracker_main = ExpiryTrackerApp()
app = tracker_main.main()

# Entry point for the application
if __name__ == "__main__":
    try:
        # Run the FastAPI application
        uvicorn.run(app, host="0.0.0.0", port=5000)
    except KeyboardInterrupt:
        print("Server stopped.")
    except Exception as e:
        print(f"An error occurred: {e}")