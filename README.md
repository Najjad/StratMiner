# Stragetic Mining Program (V.1)

## Using NBmining software --> https://github.com/NebuTech/NBMiner
## Using Python 3.7
## Using Gooey python library for GUI --> https://github.com/chriskiehl/Gooey/
## Using Pyinstaller to compile code --> https://pyinstaller.org/en/stable/
## Everything tested on Nvidia 1660 GPU and 3090


###### **WINDOWS ONLY**

This program checks the difficulty of a cryptocurrency every 15 minutes, and determines when or when not to mine the coin



Compatible with (so far):

```
Ravencoin - RVN
```

This program was designed to be aplicable to nearly all cryptocurrencies, the reason it is only compatible with Ravencoin so far is time constraints.

### Branches labeled by Coin letters (BTC, RVN, ETH, etc.)
### Branches contain download for each version of program
### You can find the list of branches at the top left of this repository

###### This software is still in progress


# How To Use

This very simple GUI created with the help of the Gooey library is very straightforward
* click the start button at the bottom right of the window
![image1](https://user-images.githubusercontent.com/80614053/172917020-e7e0cf3a-d02c-4a2f-95f8-3f2e9c7c8805.jpg)
 
 * Once you've clicked start, you'll be greeted by this screen
![image2](https://user-images.githubusercontent.com/80614053/172917081-a9d2974c-4ae0-4601-a246-83db6dd9ed3e.png)

* This screen is where all information will be printed out to, whether difficulty is higher or whether you are currently mining
![image3](https://user-images.githubusercontent.com/80614053/172917202-1c3e1386-8326-4935-a8c1-b26b30f25bc9.png)

* Fear not when a command line window appears! this just means your mining is working exactly as intended
![image4](https://user-images.githubusercontent.com/80614053/172917261-b2f67aa1-bdfb-42bd-8ca7-641466157545.png)

## For download and setting up instructions navigate to the branch labeled with the crypto you'd like to mine



# Customizable options:

* In the programs current form it was not designed to be customizable to the beginner user
* If you have python experience you are more than welcome to copy and alter my program to fit your needs better / fix problems / optimize
* Editing the program will need you to download all files from this GitHub then use pyinstaller (or whatever other compiler you have) to recompile your altered version


# Why use this program?

This program targets moments of a crypto currency’s difficulty going lower than average and then proceeds to mine at these lows

This allows for less power usage, and hardware working less leading to longer longevity of your computer

With my program, your crypto mining will be much more efficient and just as easy to do as normal

# Who is this for?

This program is aimed at all who want to get into mining crypto but don’t have a dedicated mining rig

This helps in preserving hardware allowing for your computer to last longer

# Proof of this working: (Currently tested on Ravencoin mining)


## Test Data: (taken from all log files of mining) 
Log files compared from my program VS. the same base mining software running constantly

## #-------Uptime:-------#

Average uptime on my program:
* 18 minutes 20 seconds~

Average uptime on 24/7 mining: 
* 3 hours~

## #-------CPU Usage:-------#

Average usage on my program:
* 1.3% CPU average usage

Average usage on 24/7 mining:
* 8% CPU average usage

## #-------GPU Temperature:-------#

Average temperature on my program:
* 63°C

Average temperature on 24/7 mining:
* 72°C

## #-------Power Usage:-------#

Average power usage on my program:
* 83 Watt-Hours

Average power usage 24/7 mining:
* 89 Watt-Hours 

## #-------Hash Rate: (the rate at which your computer mines, higher is better)-------#

Average hash rate on my program:
* 10.61 Megahash

Average hash rate 24/7 mining:
* 9.9 Megahash

## Data Conclusions:
```
My program uses 83.75% less CPU power than constantly mining
My program creates 12.5% less heat than constantly mining
My program uses 6.8% less power than constantly mining
My program mines with a 6.7% higher hash rate than constantly mining
My program runs for only 10% of the time in comparison to constantly mining
```
Overall, with the uptime, heat, and power usage being lower, the amount of strain on your computer is lessened therefore preserving your hardware for much longer. The fact that the program also targets times of low difficulty allows you to mine more of the specified Cryptocurrency with less resources

![Test Results Graph](https://user-images.githubusercontent.com/80614053/172891095-08abb8f1-8c45-4189-854d-b83bd382cad1.png)
* Hashrate is better when higher
* everything besides hashrate is better lower


***By: Najjad***
