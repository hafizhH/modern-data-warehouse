# config.py

# API Configuration
API_KEY = "d859a94bdc40c124d4842d22"  # Ganti dengan API key Anda
API_BASE_URL = "https://v6.exchangerate-api.com/v6/d859a94bdc40c124d4842d22/latest/USD"

# Spark Configuration
SPARK_APP_NAME = "CurrencyExchangeStreaming"
CHECKPOINT_LOCATION = "./checkpoint"
BATCH_INTERVAL = 60  # seconds

# HDFS Configuration
HDFS_OUTPUT_PATH = "./data/currency_rates"

# Logging Configuration
LOG_FILE = "logs/currency_streaming.log"

# Currency pairs to monitor
CURRENCY_PAIRS = [
    "EUR",
    "GBP",
    "JPY",
    "AUD",
    "CAD",
    "IDR",  # Indonesian Rupiah
    "SGD",  # Singapore Dollar
    "MYR"   # Malaysian Ringgit
]

# Spark Streaming Configuration
STREAMING_CONFIG = {
    "rowsPerSecond": 1,
    "format": "rate"
}

# Docker Environment
SPARK_MASTER_URL = "local[*]"  # Untuk local development
# SPARK_MASTER_URL = "spark://spark-master:7077"  # Untuk Docker

# Data Processing
BATCH_SIZE = 100
MAX_OFFSETS_PER_TRIGGER = 200

# Error Handling
MAX_RETRIES = 3
RETRY_DELAY = 5  # seconds