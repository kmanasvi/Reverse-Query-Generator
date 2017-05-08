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




















# adds any of the words which belongs to a particular topic.
    @staticmethod
    def add_subscription_word():
	    get_data = open("/Users/kumarmanasvi/Desktop/topic_database_log.txt", "r")
	    bool_val=1
	    seq=0
	    lines = get_data.readlines()
	    for topics in lines:
	        print(seq + "." + topics)
	        seq += 1
	    get_data.close()
	    if topics is None:
                print("Please assign a topic first")
	    topic_number = raw_input("Please enter a number to choose a topic according to their sequential order")
	    while(bool_val!=0):
	        topic_string = raw_input("Add a string for this topic to subscribe to.")
	        write_to = open("/Users/kumarmanasvi/Desktop/topic_database_log.txt", "a+")
	        count=0
	    while(count < topic_number):
	        write_to.write("")
	        ++count 
	        write_to.write("," + topic_string )
	        bool_val = raw_input("Press 1 to add more strings and 0 to quit")
	        write_to.close()
    return 1
	


	#adds any string that is required.
	def add_random_string():
	    bool_val=1
	    while(bool_val!=0):
	       string_of_interest = raw_input("Add a string which you think may be included in the discussion.")
	       write_to = open("/Users/kumarmanasvi/Desktop/words_database_log.txt", "a+")
	       write_to.write(string_of_interest)
	       bool_val = raw_input("Press 1 to add more strings and 0 to quit")
	       write_to.close()
	return 1
	 
	#++++++++++++++++++++++++++++++++++++++Deleting Items Functions+++++++++++++++++++++++++++++++++++++++++++++++++++++++
	
	
	
	
	#deletes any of the words that were put in the input.
	def delete_random_string(database):
	   bool_val=1
	   list_of_words=databasase.list_of_words
	   seq=0
	   topic_number = raw_input("Please enter a number to choose a word according to their sequential order")
	 
	   get_data = open("/Users/kumarmanasvi/Desktop/topic_database_log.txt", "r")
	   lines = get_data.readlines()
	 
	   for topics in lines:
	       print(seq + ". " + topics)
	       ++seq
	   get_data.close()
	   if topics is None :
	       print("Please assign a topic first")
	   return 1
	   while(bool_val!=0):
	       count=0
	       write_to = open("/Users/kumarmanasvi/Desktop/topic_database_log.txt", "a+")
	       for line in lines:
               if count!=topic_number:
                   write_to.write(line)
	       ++count 
	       write_to.write("," + topic_string )
	   bool_val = raw_input("Press 1 to delete more strings and 0 to quit") 
	 
	
    # Deletes a particular word from a subscribed topic from the database
    def delete_words_from_subscribtion(database):
	    bool_val=1
	    seq=0
	    list_of_topics=databasase.list_of_subscription
	    topic_number = raw_input("Please enter a number to choose a topic according to their sequential order")
	    for topics in list_of_topics:
	        print(seq + ". " + topics)
	        ++seq
	    while(bool_val!=0):
	        topic_number = raw_input("Please enter a number to choose a word according to their sequential order")
	        for words in list_of_words:
	        print(seq + ". " + topics)
	        ++seq
	    bool_val = raw_input("Press 1 to delete more strings and 0 to quit")

	 
	# Deletes a particular topic that has been subscribed to from the database.
	def delete_topic(database):
	    bool_val=1
	    seq=0
	    list_of_topics=databasase.list_of_subscription
	    while(bool_val!=0):
	        topic_number = raw_input("Please enter a number to choose a topic according to their sequential order”)
	        for topics in list_of_topics:
	        print(seq + ". " + topics)
	        ++seq
	    bool_val = raw_input("Press 1 to delete more and 0 to quit")
	 





	 def delete_words_from_subscribtion(database):
        with open('/Users/kumarmanasvi/Desktop/topic_database_log.json', 'r+') as read_now:
            data = json.load(read_now)
            bool_val=1
            if data[0] == {}:
                print("Please assign a topic first")
                return 1
            while(bool_val!=0):
                print(data[0])
                topic_number = raw_input("Please enter a number to choose a topic according to their sequential order")
                print(data[0][topic_number])
                topic_string = raw_input("Select a string according to their order of sequence to delete that string from the topic")
                bool_val = int(raw_input("Press 1 to add more strings or 0 to quit"))
            with open('/Users/kumarmanasvi/Desktop/topic_database_log.json', 'w') as output:        
                json.dump(data, output)   
        return 1


	 
	 

	

	
	 

 