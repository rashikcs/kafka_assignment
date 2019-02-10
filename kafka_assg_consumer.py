from kafka import KafkaConsumer
from json import loads


def main():
	consumer = KafkaConsumer(
		'numtest',
		 bootstrap_servers=['localhost:9092'],
		 auto_offset_reset='earliest',
		 api_version=(0, 10),
		 enable_auto_commit=True,
		 group_id='my-group')
		 
	for msg in consumer:
		message = str(msg.value,'utf-8')
		producer_name = str(msg.key,'utf-8')
		print('{} message recieved from {} .'.format(message,producer_name))
		#print('{}{}'.format(message,producer_name))
    
if __name__ == '__main__':
	print("Okay so far!!")
	main()