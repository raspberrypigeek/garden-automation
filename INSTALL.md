
<h3>Setting up the server</h3>
<h4>Installing prerequisites</h4>

<h5>Automation Hat</h5>
Instructions on how to install can be found <a href="https://learn.pimoroni.com/tutorial/sandyj/getting-started-with-automation-hat-and-phat">here</a>.
But in summary, you need to do the following:
<ul>
<li>sudo apt-get update</li>
<li>sudo apt-get upgrade</li>
<li>curl https://get.pimoroni.com/automationhat | bash</li>
<li>Press 'y'</li>
<li>sudo reboot'</li>
</ul>
<p>That didn't work as it turns out... by default it seems to favour python3 but I wanted to use 2.7. So  I then...</p>
<ul>
<li>sudo pip2.7 install automationhat</li>
<li>python ~/Pimoroni/automationhat/examples/output.py</li>
</ul>
If all is working, you should see something like:

>{'four': 0.58, 'three': 0.03, 'two': 0.03, 'one': 0.03}<br>
>{'four': 0.55, 'three': 0.03, 'two': 0.03, 'one': 0.03}<br>
>{'four': 0.54, 'three': 0.03, 'two': 0.03, 'one': 0.03}<br>
>...
<h5>The stack...</h5>
sudo pip install flask
sudo pip install flasgger

To store the configuration of your system we need somewhere to persist the configuration, obviously configuration files are an option but given that I want this to scale out then Zookeeper would seem to be the sensible choice.


>sudo apt-get install zookeeper
That didn't work so... Plan B:
cd /opt
sudo mkdir zookeeper
cd zookeeper
sudo wget http://www.mirrorservice.org/sites/ftp.apache.org/zookeeper/zookeeper-3.4.13/zookeeper-3.4.13.tar.gz
sudo tar -zxvf zookeeper-3.4.13.tar.gz
cd zookeeper-3.4.13/
sudo cp conf/zoo_sample.cfg conf/zoo.cfg
sudo bin/zkServer.sh start

bin/zkCli.sh -server 127.0.0.1:2181

<h3>Setting up the client</h3>