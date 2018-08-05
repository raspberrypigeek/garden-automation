
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

>{'four': 0.58, 'three': 0.03, 'two': 0.03, 'one': 0.03}
>{'four': 0.55, 'three': 0.03, 'two': 0.03, 'one': 0.03}
>{'four': 0.54, 'three': 0.03, 'two': 0.03, 'one': 0.03}
>...
<h3>Setting up the client</h3>