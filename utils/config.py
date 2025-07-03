import logging

# configure logging 
logging.basicConfig(
    filename='data_quality_logs.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

logger = logging.getLogger(__name__)
