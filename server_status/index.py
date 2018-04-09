#<meta http-equiv="refresh" content="1">
import os,psutil,thread
def start_http():
	os.system("xterm -e 'sudo python -m SimpleHTTPServer 12345'")
thread.start_new_thread(start_http,())
flag=True
c1=[]
c2=[]
c3=[]
c4=[]
for i in range(1,41):
	c1.append(0)
	c2.append(0)
	c3.append(0)
	c4.append(0)
cnt=0
initial_down = psutil.net_io_counters().bytes_recv
initial_up = psutil.net_io_counters().bytes_sent
while flag:
	"""now_down = psutil.net_io_counters().bytes_recv
	now_up = psutil.net_io_counters().bytes_sent
	download_speed = (now_down - initial_down)/1000
	upload_speed = (now_up - initial_up)/1000
	speed=str(download_speed)+"kb/"+str(upload_speed)+"kb"
	initial_down = now_down
	initial_up = now_up"""
	try:
		try:
			s=psutil.cpu_percent(interval=1,percpu=True)
		except:
			s=[0,0,0,0]
			flag=False
		c1.append((s[0]))
		c2.append((s[1]))
		c3.append((s[2]))
		c4.append((s[3]))
		""""if cnt%60==0:
				mem =str(psutil.virtual_memory()).split("=")[3].split(",")[0]
				#btry_status=os.popen("cat /sys/class/power_supply/BAT0/uevent").read().split("POWER_SUPPLY_CAPACITY=")[1].split("\n")[0]
			cnt+=1"""
		print c1
		print c2
		print c3
		print c4
		html="""
<!DOCTYPE HTML>
<html>
<head>  
<meta http-equiv="refresh" content="2">
<script>
window.onload = function () {

var chart = new CanvasJS.Chart("chartContainer", {
	animationEnabled: false,
	title:{
		text: "Server-Suite"
	},
	axisX: {
		ValueFormatString: "DD MMM hh:mm TT"
	},
	axisY: {
		title: "CPU Percentage",
		includeZero: false,
		suffix: " %"
	},
	legend:{
		cursor: "pointer",
		fontSize: 16,
		itemclick: toggleDataSeries
	},
	toolTip:{
		shared: true
	},
	data: [{
		name: "Core 1",
		type: "spline",
		yValueFormatString: "#0.## '%'",
		showInLegend: true,
		dataPoints: [
			{ x: 1, y: """+str(c1[0])+""" },
			{ x: 2, y: """+str(c1[1])+""" },
			{ x: 3, y: """+str(c1[2])+""" },
			{ x: 4, y: """+str(c1[3])+""" },
			{ x: 5, y: """+str(c1[4])+""" },
			{ x: 6, y: """+str(c1[5])+""" },
			{ x: 7, y: """+str(c1[6])+""" },
			{ x: 8, y: """+str(c1[7])+""" },
			{ x: 9, y: """+str(c1[8])+""" },
			{ x: 10, y: """+str(c1[9])+""" },
			{ x: 11, y: """+str(c1[10])+""" },
			{ x: 12, y: """+str(c1[11])+""" },
			{ x: 13, y: """+str(c1[12])+""" },
			{ x: 14, y: """+str(c1[13])+""" },
			{ x: 15, y: """+str(c1[14])+""" },
			{ x: 16, y: """+str(c1[15])+""" },
			{ x: 17, y: """+str(c1[16])+""" },
			{ x: 18, y: """+str(c1[17])+""" },
			{ x: 19, y: """+str(c1[18])+""" },
			{ x: 20, y: """+str(c1[19])+""" },
			{ x: 21, y: """+str(c1[20])+""" },
			{ x: 22, y: """+str(c1[21])+""" },
			{ x: 23, y: """+str(c1[22])+""" },
			{ x: 24, y: """+str(c1[23])+""" },
			{ x: 25, y: """+str(c1[24])+""" },
			{ x: 26, y: """+str(c1[25])+""" },
			{ x: 27, y: """+str(c1[26])+""" },
			{ x: 28, y: """+str(c1[27])+""" },
			{ x: 29, y: """+str(c1[28])+""" },
			{ x: 30, y: """+str(c1[29])+""" },
			{ x: 31, y: """+str(c1[30])+""" },
			{ x: 32, y: """+str(c1[31])+""" },
			{ x: 33, y: """+str(c1[32])+""" },
			{ x: 34, y: """+str(c1[33])+""" },
			{ x: 35, y: """+str(c1[34])+""" },
			{ x: 36, y: """+str(c1[35])+""" },
			{ x: 37, y: """+str(c1[36])+""" },
			{ x: 38, y: """+str(c1[37])+""" },
			{ x: 39, y: """+str(c1[38])+""" },
			{ x: 40, y: """+str(c1[39])+""" }
		]
	},
	{
		name: "Core 2",
		type: "spline",
		yValueFormatString: "#0.## '%'",
		showInLegend: true,
		dataPoints: [
			{ x: 1, y: """+str(c2[0])+""" },
			{ x: 2, y: """+str(c2[1])+""" },
			{ x: 3, y: """+str(c2[2])+""" },
			{ x: 4, y: """+str(c2[3])+""" },
			{ x: 5, y: """+str(c2[4])+""" },
			{ x: 6, y: """+str(c2[5])+""" },
			{ x: 7, y: """+str(c2[6])+""" },
			{ x: 8, y: """+str(c2[7])+""" },
			{ x: 9, y: """+str(c2[8])+""" },
			{ x: 10, y: """+str(c2[9])+""" },
			{ x: 11, y: """+str(c2[10])+""" },
			{ x: 12, y: """+str(c2[11])+""" },
			{ x: 13, y: """+str(c2[12])+""" },
			{ x: 14, y: """+str(c2[13])+""" },
			{ x: 15, y: """+str(c2[14])+""" },
			{ x: 16, y: """+str(c2[15])+""" },
			{ x: 17, y: """+str(c2[16])+""" },
			{ x: 18, y: """+str(c2[17])+""" },
			{ x: 19, y: """+str(c2[18])+""" },
			{ x: 20, y: """+str(c2[19])+""" },
			{ x: 21, y: """+str(c2[20])+""" },
			{ x: 22, y: """+str(c2[21])+""" },
			{ x: 23, y: """+str(c2[22])+""" },
			{ x: 24, y: """+str(c2[23])+""" },
			{ x: 25, y: """+str(c2[24])+""" },
			{ x: 26, y: """+str(c2[25])+""" },
			{ x: 27, y: """+str(c2[26])+""" },
			{ x: 28, y: """+str(c2[27])+""" },
			{ x: 29, y: """+str(c2[28])+""" },
			{ x: 30, y: """+str(c2[29])+""" },
			{ x: 31, y: """+str(c2[30])+""" },
			{ x: 32, y: """+str(c2[31])+""" },
			{ x: 33, y: """+str(c2[32])+""" },
			{ x: 34, y: """+str(c2[33])+""" },
			{ x: 35, y: """+str(c2[34])+""" },
			{ x: 36, y: """+str(c2[35])+""" },
			{ x: 37, y: """+str(c2[36])+""" },
			{ x: 38, y: """+str(c2[37])+""" },
			{ x: 39, y: """+str(c2[38])+""" },
			{ x: 40, y: """+str(c2[39])+""" }
		]
	},
	{
		name: "Core 3",
		type: "spline",
		yValueFormatString: "#0.## '%'",
		showInLegend: true,
		dataPoints: [
			{ x: 1, y: """+str(c3[0])+""" },
			{ x: 2, y: """+str(c3[1])+""" },
			{ x: 3, y: """+str(c3[2])+""" },
			{ x: 4, y: """+str(c3[3])+""" },
			{ x: 5, y: """+str(c3[4])+""" },
			{ x: 6, y: """+str(c3[5])+""" },
			{ x: 7, y: """+str(c3[6])+""" },
			{ x: 8, y: """+str(c3[7])+""" },
			{ x: 9, y: """+str(c3[8])+""" },
			{ x: 10, y: """+str(c3[9])+""" },
			{ x: 11, y: """+str(c3[10])+""" },
			{ x: 12, y: """+str(c3[11])+""" },
			{ x: 13, y: """+str(c3[12])+""" },
			{ x: 14, y: """+str(c3[13])+""" },
			{ x: 15, y: """+str(c3[14])+""" },
			{ x: 16, y: """+str(c3[15])+""" },
			{ x: 17, y: """+str(c3[16])+""" },
			{ x: 18, y: """+str(c3[17])+""" },
			{ x: 19, y: """+str(c3[18])+""" },
			{ x: 20, y: """+str(c3[19])+""" },
			{ x: 21, y: """+str(c3[20])+""" },
			{ x: 22, y: """+str(c3[21])+""" },
			{ x: 23, y: """+str(c3[22])+""" },
			{ x: 24, y: """+str(c3[23])+""" },
			{ x: 25, y: """+str(c3[24])+""" },
			{ x: 26, y: """+str(c3[25])+""" },
			{ x: 27, y: """+str(c3[26])+""" },
			{ x: 28, y: """+str(c3[27])+""" },
			{ x: 29, y: """+str(c3[28])+""" },
			{ x: 30, y: """+str(c3[29])+""" },
			{ x: 31, y: """+str(c3[30])+""" },
			{ x: 32, y: """+str(c3[31])+""" },
			{ x: 33, y: """+str(c3[32])+""" },
			{ x: 34, y: """+str(c3[33])+""" },
			{ x: 35, y: """+str(c3[34])+""" },
			{ x: 36, y: """+str(c3[35])+""" },
			{ x: 37, y: """+str(c3[36])+""" },
			{ x: 38, y: """+str(c3[37])+""" },
			{ x: 39, y: """+str(c3[38])+""" },
			{ x: 40, y: """+str(c3[39])+""" }
		]
	},
	{
		name: "Core 4",
		type: "spline",
		yValueFormatString: "#0.## '%'",
		showInLegend: true,
		dataPoints: [
			{ x: 1, y: """+str(c4[0])+""" },
			{ x: 2, y: """+str(c4[1])+""" },
			{ x: 3, y: """+str(c4[2])+""" },
			{ x: 4, y: """+str(c4[3])+""" },
			{ x: 5, y: """+str(c4[4])+""" },
			{ x: 6, y: """+str(c4[5])+""" },
			{ x: 7, y: """+str(c4[6])+""" },
			{ x: 8, y: """+str(c4[7])+""" },
			{ x: 9, y: """+str(c4[8])+""" },
			{ x: 10, y: """+str(c4[9])+""" },
			{ x: 11, y: """+str(c4[10])+""" },
			{ x: 12, y: """+str(c4[11])+""" },
			{ x: 13, y: """+str(c4[12])+""" },
			{ x: 14, y: """+str(c4[13])+""" },
			{ x: 15, y: """+str(c4[14])+""" },
			{ x: 16, y: """+str(c4[15])+""" },
			{ x: 17, y: """+str(c4[16])+""" },
			{ x: 18, y: """+str(c4[17])+""" },
			{ x: 19, y: """+str(c4[18])+""" },
			{ x: 20, y: """+str(c4[19])+""" },
			{ x: 21, y: """+str(c4[20])+""" },
			{ x: 22, y: """+str(c4[21])+""" },
			{ x: 23, y: """+str(c4[22])+""" },
			{ x: 24, y: """+str(c4[23])+""" },
			{ x: 25, y: """+str(c4[24])+""" },
			{ x: 26, y: """+str(c4[25])+""" },
			{ x: 27, y: """+str(c4[26])+""" },
			{ x: 28, y: """+str(c4[27])+""" },
			{ x: 29, y: """+str(c4[28])+""" },
			{ x: 30, y: """+str(c4[29])+""" },
			{ x: 31, y: """+str(c4[30])+""" },
			{ x: 32, y: """+str(c4[31])+""" },
			{ x: 33, y: """+str(c4[32])+""" },
			{ x: 34, y: """+str(c4[33])+""" },
			{ x: 35, y: """+str(c4[34])+""" },
			{ x: 36, y: """+str(c4[35])+""" },
			{ x: 37, y: """+str(c4[36])+""" },
			{ x: 38, y: """+str(c4[37])+""" },
			{ x: 39, y: """+str(c4[38])+""" },
			{ x: 40, y: """+str(c4[39])+""" }
		]
	}]
});
chart.render();

function toggleDataSeries(e){
	if (typeof(e.dataSeries.visible) === "undefined" || e.dataSeries.visible) {
		e.dataSeries.visible = false;
	}
	else{
		e.dataSeries.visible = true;
	}
	chart.render();
}

}
</script>
</head>
<body>
<center><div id="chartContainer" style="height: 300px; width: 100%;"></div></center>
<script src="https://canvasjs.com/assets/script/canvasjs.min.js"></script>
</body>
</html>
"""
		with open("index_2.html","w") as f:
			f.write(html)
		if len(c1)>=40:
			c1.pop(0)
			c2.pop(0)
			c3.pop(0)
			c4.pop(0)
	except Exception,e:
		flag=False
	if flag==False:
		print "\nbye saurabh"

