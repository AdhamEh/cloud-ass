# Use an official Python runtime as a parent image
FROM python:3.9

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app
COPY . .

# Copy the Python script from the 'src' directory into the container at /app
COPY src/script.py /app/

# Install any needed dependencies specified in requirements.txt
RUN pip install nltk

# Download NLTK stopwords
RUN python -m nltk.downloader stopwords

# Expose port 5000 (example port number)
EXPOSE 5000

# Run the Python script
CMD ["python", "script.py"]


