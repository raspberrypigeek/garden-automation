<h3>Introduction</h3>
The aim of this repo is to provide a simple platform for watering the garden. So the intent is to build something that could just work on a single
Raspberry Pi but if you have a big garden (front and back? :-) ) and want to use more than one Raspberry then the intent of this project is to buid something that scales out.
As part of this project the intent is also to design that is robust and manageable. Therefore my hope is to build something that can reliably look after your garden or just your loved Bonsai tree.
<h3>Project</h3>

<h4>Phase 0: Prototype</h4>
<h4>Phase 1: Watering Pots</h4>
<h4>Phase 2: Sprinklers + Pots</h4>
<h4>Phase 3: Alexa integration</h4>

<h3>Geting Started</h3>
The kit list below is intended to support all four phases of the project - if you want to scale down then you can swap the Raspberry Pi for a Pi Zero and the Automation Hat for the Automation Phat. The key difference between
the hat and the phat is that hat has three relays and the phat only one. For the purposes of this work I am limiting one relay to one valve but it is entirely possible to drive more than one valve off more than one relay, you just need to think about the
electronics a bit more.
<ul>
<li><a href="https://www.raspberrypi.org/">Raspberry Pi</a></li>
<li><a href="https://shop.pimoroni.com/products/automation-hat">Automation Hat</a></li>
<li>Temperature sensors</li>
<li>Capacitive soil moisture sensor</li>
</ul>
Details on installing the prerequistes, can be found <a href="INSTALL.md">here</a>


<h4>Deployment</h4>
If you want to use this project, you need to install the following: 
>git clone https://github.com/raspberrypigeek/garden-automation.git
>cd server/bin

<h3>Architecture</h3>
So the initial assumption is that I want to build something that can run on a single Raspberry Pi but if desired be deployed across multiple Raspberry Pis.


<h4>Client</h4>

<h4>Server</h4>
