
<h4>Installing prerequisites</h4>

<h5>Automation Hat</h5>
Instructions on how to install can be found <a href="https://learn.pimoroni.com/tutorial/sandyj/getting-started-with-automation-hat-and-phat">here</a>.
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