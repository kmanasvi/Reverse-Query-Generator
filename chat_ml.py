import json


    


class configure(object):





    # adds a topic as a subscription.
    def add_topic_for_subscription(self):
        bool_val = 1
        data="" 
        with open('/Users/kumarmanasvi/Desktop/topic_database_log.json', 'r+') as read_now:
            data = json.load(read_now)

            while bool_val != 0:
                new_topic = raw_input("Add a topic for chat to subscribe to. ")
                counter=len(data[0])
                topic={new_topic :{}}
                data[0][counter]=topic
                bool_val = int(raw_input("Press 1 to add more strings and 0 to quit"))
            with open('/Users/kumarmanasvi/Desktop/topic_database_log.json', 'w') as output:        
                json.dump(data, output)
        return 1




    #adds any of the words which belongs to a particular topic.
    def add_subscription_word(self):
        with open('/Users/kumarmanasvi/Desktop/topic_database_log.json', 'r+') as read_now:
            data = json.load(read_now)
            bool_val=1
            if data[0] == {}:
                print("Please assign a topic first")
                return 1  
            while(bool_val!=0):
                print(data[0])
                topic_number = raw_input("Please enter a number to choose a topic according to their sequential order")
                topic_string = raw_input("Add a string for this topic to subscribe to.")
                topic_name=str(data[0][topic_number])
                print(topic_name)
                #data[0][topic_number][counter]=topic_string
                bool_val = int(raw_input("Press 1 to add more strings or 0 to quit"))
            with open('/Users/kumarmanasvi/Desktop/topic_database_log.json', 'w') as output:        
                json.dump(data, output)   
        return 1






     





y = configure()
#y.add_topic_for_subscription()
y.add_subscription_word()