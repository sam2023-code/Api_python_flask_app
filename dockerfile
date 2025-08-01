# Use the official Python image from the Docker Hub
FROM python:3.9-slim AS flask_app

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
#pip freeze > requirements.txt
COPY requirements.txt .

# Install PostgreSQL development packages
RUN apt-get update && apt-get install -y libpq-dev

# Install the dependencies
RUN pip install --upgrade pip 

# Install psycopg2 or psycopg2-binary
#RUN pip install psycopg2-binary  # Use this line if you want to avoid building from source

# Install requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container
COPY . .

# Expose the port that the app runs on
#EXPOSE 5000

# Command to run the application
CMD ["python", "run.py"]


# Use the official Nginx image from Docker Hub
#FROM nginx:alpine

# Copy the Nginx configuration file
#COPY nginx.conf /etc/nginx/conf.d/default.conf


# Copy the Flask app from the previous stage
#COPY --from=flask_app /app /usr/share/nginx/html

# Expose port 80
#EXPOSE 80

# Start Nginx
#CMD ["nginx", "-g", "daemon off;"]

#docker build -t my_flask_app .
#docker run -d -p 5000:5000 my_flask_app