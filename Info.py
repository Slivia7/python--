import pickle

class Message():
     image=""
     userFrom=""
     userTo=""
     def __init__(self,imageName,name1,name2):
        self.image = imageName
        self.userFrom = name1
        self.userTo=name2
     def getImage(self):
          return self.image
     def getUserFrom(self):
          return self.userFrom
     def getUserTo(self):
          return self.userTo
     def setImage(self,imageName):
          self.image=imageName
     def setUserFrom(self,name):
          self.userFrom=name
     def setUserTo(self,name):
          self.userTo=name

class user:
     name=""
     password=""
     received=[]
     send=[]
     def __init__(self,name,password):
          self.name=name
          self.password=password


     def getName(self):
          return self.name
     def getPassword(self):
          return self.password
     def addReceived(self,message):
          self.received.append(message)
     def addSend(self,message):
          self.send.append(message)
     def removeReceivedByImage(self,messagefile):
          i=0
          while(i<len(received)):
               if(received[i].getImage==messagefile):
                    self.received.pop([i])
     def removeReceivedByuser(self,user):
          i=0
          while(i<len(received)):
               if(received[i].getUserFrom==user):
                    received.pop([i])
     def removeReceivedAll(self):
          self.received.clear()

     def removeSendByImage(self,messagefile):
          i=0
          while(i<len(send)):
               if(send[i].getImage==messagefile):
                    send.pop([i])
     def removeSendByUser(self,user):
          i=0
          while(i<len(send)):
               if(send[i].getUserTo==user):
                    send.pop([i])
     def removeSendAll(self):
          self.send.clear()



class Service:
     message=""
     usr_name=""
     def __init__(self,message):
          self.message=message
          self.usr_name=self.message.getUserTo()
     def service(self):
          try:
               with open('usr_info.pickle','rb') as usr_file:
                    usrs_info=pickle.load(usr_file)
                    usr_file.close()
          except FileNotFoundError:
               return "服务器异常！"
          if self.usr_name in usrs_info:
               usrs_info[self.usr_name].addReceived(self.message)
               usrs_info[self.message.getUserFrom()].addSend(self.message)
               f=open('usr_info.pickle','wb')
               pickle.dump(usrs_info,f)
               f.close()
               print("目标："+self.usr_name)
               print("发送者："+self.message.getUserFrom())
               print(usrs_info[self.usr_name].received[-1])
               return "发送成功"
          else:
               return "此用户不存在"



#test
#m=new Message("images/test.png",)
