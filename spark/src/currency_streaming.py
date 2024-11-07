from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from pyspark.sql.types import StructType, StructField, StringType, DoubleType
import requests
import json
from datetime import datetime
import time
import logging
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def create_spark_session():
    """Create Spark session with Docker configuration"""
    return SparkSession.builder \
        .appName("CurrencyExchangeStreaming") \
        .config("spark.sql.streaming.checkpointLocation", "./checkpoint") \
        .getOrCreate()
def fetch_currency_data():
    """Fetch exchange rates from API"""
    url = "https://v6.exchangerate-api.com/v6/d859a94bdc40c124d4842d22/latest/USD"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            current_timestamp = datetime.now().isoformat()
            
            rates = {
                'timestamp': current_timestamp,
                'base_currency': 'USD'
            }
            rates.update(data['rates'])
            
            logging.info(f"Data fetched successfully at {current_timestamp}")
            return rates
        else:
            logging.error(f"API request failed: {response.status_code}")
            return None
    except Exception as e:
        logging.error(f"Error fetching data: {str(e)}")
        return None

def process_batch(df, epoch_id):
    """Process each batch of data"""
    try:
        # Add processing timestamp
        df_with_timestamp = df.withColumn("processing_time", current_timestamp())
        
        # Show some statistics
        df_with_timestamp.select("value", "timestamp") \
            .show(5)
            
        logging.info(f"Batch {epoch_id} processed successfully")
    except Exception as e:
        logging.error(f"Error processing batch {epoch_id}: {str(e)}")

def main():
    # Create Spark session
    spark = create_spark_session()
    logging.info("Spark session created")

    try:
        # Create streaming DataFrame
        streaming_df = spark \
            .readStream \
            .format("rate") \
            .option("rowsPerSecond", 1) \
            .load()
        
        # Process the stream
        query = streaming_df \
            .writeStream \
            .foreachBatch(process_batch) \
            .start()

        logging.info("Streaming started")
        query.awaitTermination()

    except Exception as e:
        logging.error(f"Error in main: {str(e)}")
    finally:
        spark.stop()
        logging.info("Spark session stopped")

if __name__ == "__main__":
    main()