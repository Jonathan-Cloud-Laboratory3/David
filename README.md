What is the framework used? 
For this laboratory, I used flask as the framework. Flask was chosen because it is 
lightweight, easy to set up, and perfect for simple multi-page web applications like this 
one. It also allowed me to easily manage routing between pages like Home, About, and 
Contact while keeping the project simple and organized.

How to run the project?
To run the project, I followed these steps:
- First, I made sure that Flask was installed by running pip install flask.
- Next, I copied the project files into the virtual machine.
- Then, inside the project folder, I opened the terminal and ran the command python3 app.py.
- The Flask server started, and I was able to access the web app by visiting 
http://0.0.0.0:5000 inside the VM, or http://192.168.1.10:5000 from my
main computer after setting up the Bridged Adapter properly.

What are the issues encountered and solutions?
- CSS not loading: At first, the styling didn’t appear because the style.css file
wasn’t properly linked in the HTML. I fixed it by using {{ url_for('static',
filename='style.css') }} inside the HTML templates.
- Accessing from the main computer: I couldn’t access the website from my main PC
at first. I realized it was because my VM was only using NAT. I solved it by enabling
Adapter 2 in VirtualBox and setting it as Bridged Adapter, which gave the VM a
192.168.x.x IP address that my host machine could reach.
- Firewall blocking port 5000: Another issue was that Ubuntu's firewall was blocking
connections to port 5000. I fixed it by running sudo ufw allow 5000 and then
reloading the firewall.
