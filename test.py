import sys






class configure(object):

    def __init__(self):
	return;

    #adds a topic as a subscription.
    def add_topic_for_subscription(self):
		bool_val=1
		while bool_val == 1:
			new_topic = raw_input("Add a topic for chat to subscribe to.")
			write_to = open("C:/Users/kmanasvi/Desktop/topic_database_log.txt", "a+")
			write_to.write(new_topic + "|\n")
			bool_val = raw_input("Press 1 to add more strings and 0 to quit")
		write_to.close()
		return;

	 
    #adds any of the words which belongs to a particular topic.
	def add_subscription_word(self):
	 get_data = open("C:\Users\kmanasvi\Desktop\topic_database_log.txt", "r")
	 var bool_val=1
	 var seq=0
	 lines = get_data.readlines()
	 for topics in lines:
	  print(seq + ". " + topics)
	  ++seq
	 get_data.close()
	 if topics is None {
	 print("Please assign a topic first")
	 return;
	 }
	 topic_number = raw_input("Please enter a number to choose a topic according to their sequential order")
	 while bool_val==1:
	  topic_string = raw_input("Add a string for this topic to subscribe to.")
	  write_to = open("C:\Users\kmanasvi\Desktop\topic_database_log.txt", "a+")
	  var count=0
	  while(count < topic_number):
	   write_to.write("")
	   ++count 
	  write_to.write("," + topic_string )
	  bool_val = raw_input("Press 1 to add more strings and 0 to quit")
	 write_to.close()
     return; 
	 
	 
	 
	 
	 
 
print("Has started")
config = configure()
print config.add_topic_for_subscription()
 