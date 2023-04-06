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

- Raw Packet return IP alterration sending back any hacked packets or AI packets that are sent your way so you both get the same results.

- Packet capture that puts a link to one of my songs with an AI in it for scare tactics. Psyops are not illegal.

in order to use this correctly implement this code into your .bashrc and run "a" in terminal:

function lose(){

  nohup python3 glitch.py &

  nohup python3 SKHD.py &

  nohup python3 loopback.py &

  nohup python3 blanket &

  nohup python3 SECRET.py &

  nohup python3 cascade.py &

  nohup python3 def.py &
  
  nohup python3 udploop.py &
  
  nohup python3 raw.py &
  
  nohup python3 packet.py &

}

alias a = lose
