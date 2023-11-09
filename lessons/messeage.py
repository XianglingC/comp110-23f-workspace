"""Class to store a message (operator overload, default parameters)"""

class Message:

    # attribute
    to: str
    content: str
    important: bool

    def __init__(self, recipient: str|int, message_content: str = "", importance_flag: bool = False):
        """Construct a message"""
        self.to = recipient
        self.content = message_content
        self.important = importance_flag
    

    def __str__(self) -> str:
        output: str = f"Message to {self.to:} \n" #\n: new line
        output += f"Important? {self.important}\n"
        output += f'"{self.content}"'
        return output
    
    #Operator overload
    def __mul__(self, factor: int): # self --corresponding to the message part printed above| __mul__ = * that's why we can use * to call the function
        """Multiplication operator overload"""
        copy_val: str = self.content
        for loop_number in range(0, factor):
            self.content += "" + copy_val

######!!!!! what the self refers to

        

msg: Message = Message("erin","Great job!", False)
# msg * 100 you can't do this, because it's str & int
msg_to_myself: Message = Message("me", "Do your 110 homework!", True)
#msg * 100 
print(msg)
msg_to_camilla: Message = Message("carmilla", "You inspire the students!")# the importance is default
msg_to_bear: Message = Message("bear")
print(msg_to_bear) # the content and importance is default
msg_to_bear.content = "Good by!"
msg_to_bear.important = False
print(msg_to_bear)
