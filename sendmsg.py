#Impport pywhatkit library for sending whatsapp text
import pywhatkit as kit

#sendwhatmsg() takes receiver phone number, text to be sent, also the hour and minute when it should be sent. 
kit.sendwhatmsg("+91**********", "Hi, This message is sent via automated script written in python.", 20, 20)

#Change +91********** to +91receiver's_mobile_number

#Requirements for this code to woek:
# 1. Google chrome browser
# 2. Web.whatsapp logged in to Google chrome browser
# 3. Delivery time should be always set minimum 4-5 minutes more than the current time.
   
