FROM apache/spark:3.5.0

# Set working directory
WORKDIR /app

# Install Python dependencies
COPY spark/requirements.txt .
RUN pip install -r requirements.txt

# Copy the application code
COPY spark/src /app/src/

# Create data directory
RUN mkdir -p /app/data

# Set environment variables
ENV SPARK_MASTER_HOST=spark-master
ENV SPARK_MASTER_PORT=7077
ENV PYTHONPATH=/app

# Default command
CMD ["bash"]