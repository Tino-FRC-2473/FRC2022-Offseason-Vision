from Circle import Circle

def sendData(circles):
    toSend = "\n[Open]\n"
    for i in circles:
         toSend += "[Circle " + str(i.x) + " " + str(i.y) + " " + str(i.r) + "]\n"
    toSend += "[Close]\n"
    return toSend

circles = [Circle(0, 0, 10), Circle(50, 50, 5)]
print(sendData(circles))
