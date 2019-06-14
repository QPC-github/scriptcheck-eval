import time
import subprocess 
import os
import time
import signal
from threading import Timer

_dir = os.path.dirname(__file__)
_top_site_dir = os.path.join(_dir, "top-sites")
_final_url_filename = os.path.join(_top_site_dir, "final_url")

# execute a shell command and block!
def execute(cmd):
	(status, output) = subprocess.getstatusoutput(cmd)
	if status != 0:
		raise Exception("[ERROR] failed to execute " + cmd + " . The status is " + str(status))
	return output

def executeWithoutCheckStatus(cmd):
	(status, output) = subprocess.getstatusoutput(cmd)
	return output

# get the timestamp
def getTime():
	return time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))

class TimTest(object):
	def __init__(self):
		# get the home directory
		self._home_dir = execute("echo $HOME")
		# get the chrome binary
		self._chrome_binary = self._home_dir + "/chromium/tick/src/out/Default/chrome"
		print(self._chrome_binary)
		# get the node binary
		self._node_binary = "node"
		# get the nodejs script
		self._node_filename = "Hello.js"

		self._results_dir = self._home_dir + "/workspace/tim-results"

		# for each web page, we run 3 rounds
		self._round = 3
		self._timeout = 60

		# create an EMPTY directory to save results
		execute("rm -rf " + self._results_dir + " || true")
		execute("mkdir -p " + self._results_dir + " || true")

	def timeoutCallback(self, process_node):
		print("\t\tEnter timeoutCallback")
		try:
			os.killpg(process_node.pid, signal.SIGKILL)
		except Exception as error:
			print(error)

	def runPerUrl(self, url, ret_filename):
		ret_fd = open(ret_filename, 'w')

		process_chrome = subprocess.Popen([self._chrome_binary, '--remote-debugging-port=9222'], stderr=ret_fd, stdout=ret_fd)
		print('>>> START ' + url)
		
		time.sleep(2)

		process_node = subprocess.Popen([self._node_binary, self._node_filename, url], stdout=subprocess.PIPE, stderr=subprocess.PIPE, preexec_fn=os.setsid)
		# create a timer
		my_timer = Timer(self._timeout, self.timeoutCallback, [process_node])
		my_timer.start()

		stdout, _ = process_node.communicate()
		if '''result: { type: 'string', value: 'complete' }''' in str(stdout):
			print("\t\tweb page [%s] is completed!" % url)
		else:
			print(stdout)
			print("\t\tweb page [%s] is TIMEOUT!" % url)
		print('>>> FINISH ' + url)

		my_timer.cancel()

		time.sleep(5)
		# kill chrome
		try:
			print("\t>>> kill Chrome [%d]" % process_chrome.pid)
			os.kill(process_chrome.pid, signal.SIGKILL)
			# os.killpg(process_chrome.pid, signal.SIGTERM)
		except Exception as error:
			print(error)

		ret_fd.close()

	def run(self):
		with open(_final_url_filename, 'r') as f:
			lines = f.readlines()
			for line in lines:
				if line[0] == '#':
					continue
				log = line.strip("\n").split('\t')
				rank, url = log[0], log[1]
				domain = url[url.index("://") + 3 : ]
				print("\n\n\t\t[RANK, URL, DOMAIN] = [%s, %s, %s]\n" % (rank, url, domain))

				# create the directory for results
				ret_dir = self._results_dir + "/" + domain
				execute("mkdir -p " + ret_dir)

				# run that url
				for i in range(0, self._round):
					self.runPerUrl(url, ret_dir + "/" + getTime())
			f.close()

if __name__ == '__main__':
	TimTest().run()
