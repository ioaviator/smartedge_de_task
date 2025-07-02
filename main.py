import logging

# configure logging 
logging.basicConfig(
    filename='data_quality_logs.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def main():
  ...
  

if __name__ == "__main__":
  main()