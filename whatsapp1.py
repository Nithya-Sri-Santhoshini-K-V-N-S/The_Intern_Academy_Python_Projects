import pywhatkit as kit

try:
    kit.sendwhatmsg("+91xxxxxxxxxx","Happy Birthday! I hope you have a great day.",23,27)
    kit.sendwhatmsg("+91xxxxxxxxxx","Happy Diwali!",23,28)
    print("Whatsapp Message sent successfully")

except:
    print("Error! Whatsapp Message not sent")