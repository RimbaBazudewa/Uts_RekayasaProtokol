import socket
import psutil

s= socket.socket()
host = ""
port=12345
s.bind((host,port))
s.listen(5)
mem_use = psutil.virtual_memory()
print "Waiting For  Connetion..."
while True:
	c, addr= s.accept()
	printah = str(c.recv(1024))
	print ('diperintahkan untuk') ,printah
	print ('oleh') , addr

	if printah == 'mem':
		message_str = 'total memory :' + str(mem_use.total) \
		+' bytes\nTersedia :' + str(mem_use.available) \
		+ ' bytes\nPesent :' + str(mem_use.percent) +'%' \
		+ '\nused memory :' + str(mem_use.used) \
		+ ' bytes\nfree memory :' + str(mem_use.free)+' bytes' 
		c.send(message_str)
	
	#c.send('thank')
	
	c.close()
