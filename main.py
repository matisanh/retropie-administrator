import SimpleHTTPServer
import SocketServer
import subprocess
import signal
import os


PORT = 8080
def killapp(name):
	p = subprocess.Popen(['ps', '-A'], stdout=subprocess.PIPE)
	out, err = p.communicate()
	for line in out.splitlines():
		if name in line:
			pid = int(line.split(None, 1)[0])
			os.kill(pid, signal.SIGKILL)
			
class action(SimpleHTTPServer.SimpleHTTPRequestHandler):
	def do_GET(self):
		if self.path == '/':
			print 'Index'
			self.path = '/'
		elif self.path == '/kill_atari?':
			# Termino proceso del emulador de Atari
			killapp('retroarch')
			self.path = '/'
		elif self.path == '/kill_snes?':
			# Termino proceso del emulador de Super Nintendo
			killapp('snes9x')
			self.path = '/'
		elif self.path == '/kill_nes?':
			# Termino proceso del emulador de Nintendo
			killapp('retroarch')
			self.path = '/'
		elif self.path == '/restart_retropie?':
			# Termino proceso de RetroPie (vuelve a la consola) y lo inicio nuevamente
			command = "killall emulationstation"
			process = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
			self.path = '/'
		elif self.path == '/rpi_shutdown?':
			# Apago la RPI
			command = "sudo init 0"
			process = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
			self.path = '/'
		elif self.path == '/rpi_reboot?':
			# Reinicio la RPI
			command = "/usr/bin/sudo /sbin/shutdown -r now"
			process = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
			self.path = '/'
			
		return SimpleHTTPServer.SimpleHTTPRequestHandler.do_GET(self)

Handler = action

httpd = SocketServer.TCPServer(("", PORT), Handler)

print "serving at port", PORT

	
httpd.serve_forever()