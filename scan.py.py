#Jangan ganti author , hargai creator cape loh buat nya



b="\033[0;34m"
g="\033[1;32m"
w="\033[1;37m"
r="\033[1;31m"
y="\033[1;33m"
cyan = "\033[0;36m"
lgray = "\033[0;37m"
dgray = "\033[1;30m"
ir = "\033[0;101m"
reset = "\033[0m"



def main():
    print("{}        ____ ").format(r)
    print("   _[]_/____\__n_ ")
    print("  |_____.--.__()_|")
    print("  |I   //# \\\    |")
    print("{}  |P   \\\__//    | ").format(w)
    print("  |CS   '--'     | ")
    print("{}  '--------------'----------{}------------------.  ").format(r,w)
    print("{}  | {}Author  : {}HVmbl3 {}     | {}INDO{}N{}{}ESIA         | ").format(r,w,r,w,r,ir,reset,w)
    print("{}  | {}Youtube : {}Shodiq 2701 {}| {}+62-813-6487-3762 {}|").format(r,w,w,w,lgray,w)
    print("{}  '------------------------------------{}-------'  ").format(r,w)
    print ("  {}[ 1 ] {}Jordan").format(r,w)
    print ("  {}[ 2 ] {}Exit").format(r,w)
    select = input("\033[1;31m[ \033[1;37mSelect@Number \033[1;31m]\033[1;37m> ")
    filtering(select)



def filtering(pilih):
    if pilih == 1:
        Jordan()
    elif pilih == 9:
        print (r+"Exiting ..."+w)
        os.sys.exit()
    else:
        print (r+"Exiting ..."+w)
        os.sys.exit()

if __name__ == '__main__':