# middle-square-method

This is a repository of  that middle-square method have been converted to ROS.

# DEMO
![image](https://user-images.githubusercontent.com/66021066/103771582-5607b300-506b-11eb-9dab-7a3d909c44f7.png)

https://www.youtube.com/watch?v=T2Y9UUCg_V8&feature=youtu.be

# Usage

*copy the repository  
`git clone https://github.com/yanamaki0208/myled.git`  

*move directory  
`cd myled`  

*compile "myled.c"  
`make`  

*install the module  
`sudo insmod myled.ko`  

*change permissions  
`sudo chmod 666 /dev/myled0`    


*turn off the red LED  
`echo 0 < /dev/myled0`  

*turn off the yellow LED  
`echo 1 < /dev/myled0`

*turn off the blue LED  
`echo 2 < /dev/myled0`  

*turn off all LEDs  
`echo 012 < /dev/myled0`    


*turn on the red LED  
`echo 3 < /dev/myled0`  

*turn on the yellow LED  
`echo 4 < /dev/myled0`  

*turn on the blue LED  
`echo 5 < /dev/myled0`

*turn on all LEDs  
`echo 345 < /dev/myled0`  

*uninstall the module   
`sudo rmmod meled.ko`  

# Note

The smaller the initial value s1 is, the faster the random number converges to zero.

# Author

* Masaki Yara and Ryuichi Ueda  
* Chiba Institute of Technology  
* masaki.yara@gmail.com  

# License

"middle-square-method" is under [GNU General Public License v3.0](https://ja.wikipedia.org/wiki/GNU_General_Public_License#%E3%83%90%E3%83%BC%E3%82%B8%E3%83%A7%E3%83%B33).
