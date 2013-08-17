#!/usr/bin/python
#host = "ic.despegar.it.ar"
import smtpd, asyncore
port = 25

# SMTP server class
class CustomSMTPServer(smtpd.SMTPServer):
    
    def process_message(self, peer, mailfrom, rcpttos, data):
        print 'Message from:', mailfrom
        print 'Message to  :', rcpttos
        print 'Message     :', data
	print '-----------------------------------------------'
        return

#server = smtpd.DebuggingServer(('localhost', port), None)
server = CustomSMTPServer(('127.0.0.1', port), None)
print "Listening on port: "+str(port)
asyncore.loop()
