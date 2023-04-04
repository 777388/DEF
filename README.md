# DEF
Defense against stolen Processes, be sure to run in a VM or Chromebook when you're in the thick of it.

***Be sure to set your username on def.py****

**** ONLY RUN IN VM OR CHROMEBOOK THAT DOESNT ACCEPT GRAPHICS FROM LINUX ****

This will do several things

- Nullify all Definitions

- Graphical Errors

- Camera Errors

- Electron Collisions

- Nondeterminism 

- Loopback server that sends hacks back to sender while replacing any IP's in the request with your own

in order to use this correctly implement this code into your .bashrc and run "a" in terminal:

function lose(){

  nohup python3 glitch.py &

  nohup python3 SKHD.py &

  nohup python3 loopback.py &

  nohup python3 blanket &

  nohup python3 SECRET.py &

  nohup python3 cascade.py &

  nohup python3 def.py &
  
  nohup python3 udp.py &

}

alias a = lose
