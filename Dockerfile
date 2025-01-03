FROM python:3.12-slim

# Set the working directory
WORKDIR /app

COPY . .

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port
EXPOSE 8501

# Run the application
CMD ["streamlit", "run", "main.py"]