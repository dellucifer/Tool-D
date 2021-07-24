import os
print(" ")
print(" ===== ===== ===== =        ====== ")
print("   =   =   = =   = =         =    =")
print("   =   =   = =   = =    ===  =    =")
print("   =   =   = =   = =         =    =")
print("   =   ===== ===== ====     ====== ")
print(" ")

print("[1] TBomb")
print("[2] zphisher")
print("[3] Hidden-Eye")
print("[4] wifite")
print("[5] bopscrk")
print("[6] GHunt")
print("[7] pspy")
print("[8] snitch")
print("[9] seeker")
print(" ")
c=int(input("Enter tool no. you want to install: "))

if c==1:
    os.system('git clone https://github.com/TheSpeedX/TBomb.git')
elif c==2:
    os.system('git clone https://github.com/htr-tech/zphisher.git')
elif c==3:
    os.system('git clone https://github.com/darkmidus/HiddenEye.git')
elif c==4:
    os.system('git clone https://github.com/derv82/wifite.git')
elif c==5:
    os.system('git clone https://github.com/r3nt0n/bopscrk.git')
elif c==6:
    os.system('git clone https://github.com/mxrch/GHunt.git')
elif c==7:
    os.system('git clone https://github.com/DominicBreuker/pspy.git')
elif c==8:
    os.system('git clone https://github.com/Smaash/snitch.git')
elif c==9:
    os.system('git clone https://github.com/thewhiteh4t/seeker.git')

else:
    print("Invalid Choice")

print(" ")
print("Thanks for using Tool-D")
