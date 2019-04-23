import os
print("""
             ..,,;;;;;;,,,,
       .,;'';;,..,;;;,,,,,.''';;,..
    ,,''                    '';;;;,;''
   ;'    ,;@@;'  ,@@;, @@, ';;;@@;,;';.
  ''  ,;@@@@@'  ;@@@@; ''    ;;@@@@@;;;;
     ;;@@@@@;    '''     .,,;;;@@@@@@@;;;
    ;;@@@@@@;           , ';;;@@@@@@@@;;;.
     '';@@@@@,.  ,   .   ',;;;@@@@@@;;;;;;
        .   '';;;;;;;;;,;;;;@@@@@;;' ,.:;'
          ''..,,     ''''    '  .,;'
               ''''''::''''''''
                                   ,;
                                  .;;
                                 ,;;;
                               ,;;;;:
                            ,;@@   .;
                           ;;@@'  ,;
                           ';;, ,;'
Dear Die-ary, I've been to Heaven and Hell...
And I still don't know if there is a God or a Devil.
Still...it's something to write about.
-Nny
""")
print("-----------------------------")
print("Nmap Scans")
print("[1] Nmap All Scan")
print("[2] Eternal Blue Vuln. Scan")
print("[3] Nmap Heartbleed Vuln Scan")
print("[4] Nmap Subnet Scan")
print("[5] Nmap Top Ports Scan")
print("[6] Nmap FTP brute-force")
print("[7] Nmap SMB brute-force")
print("[8] Nmap SSH brute-force")
print("[9] Nmap HTTP-Enumeration")
print("[10] Nmap HTTP Web Server Spider")

option = int(input("Enter number : \n"))


if option == 1:
    os.system("""echo -n " Target : "
read Ip
echo -n " Scan Name :"
read Name
sudo -S nmap -A -v -O -T4 $Ip -oN ~/D3admapReports/$Name
echo "[+] Scan Complete [+]
[*] Check Reports Dir. for Results [*]"
""")

elif option == 2:
    os.system("""echo -n " Target : "
read Ip
echo -n " Name for Scan : "
read Name
sudo -S nmap -Pn -p445 --script smb-vuln-ms17-010 $Ip >> ~/D3admapReports/$Name.txt
echo "[+] Scan Complete [+]
[*] Check Reports Dir. for Results [*]"
""")

elif option == 3:
    os.system("""echo -n " Target : "
read Ip
echo -n " Name for Scan : "
read Name
sudo -S nmap -Pn -p 443 --script ssl-heartbleed $Ip >> ~/D3admapReports/$Name.txt
echo "[+] Scan Complete [+]
[*] Check Reports Dir. for Results [*]"
""")

elif option == 4:
    os.system("""echo -n " Target with subnet (example <IP>/24) : "
read Ip
echo -n " Name for Scan : "
read Name
sudo -S nmap -v $Ip -oN ~/D3admapReports/$Name
echo "[+] Scan Complete [+]
[*] Check Reports Dir. for Results [*]"
""")


if option == 5:
    os.system("""echo -n " Target : "
read Ip
echo -n " Name for Scan : "
read Name
sudo -S nmap -F $Ip -oN ~/D3admapReports/$Name
echo "[+] Scan Complete [+]
[*] Check Reports Dir. for Results [*]""")

elif option == 6:
    os.system("""echo -n " Target : "
read Ip
echo -n " Name for Scan : "
read Name
sudo -S nmap --script ftp-brute -p 21 $Ip -oN ~/D3admapReports/$Name
echo "[+] Scan Complete [+]
[*] Check Reports Dir. for Results [*]"
""")

elif option == 7:
    os.system("""echo -n " Target : "
read Ip
echo -n " Name for Scan : "
read Name
sudo -S nmap -p445 --script smb-brute --script-args userdb=users.txt,passdb=passwords.txt $Ip -oN ~/D3admapReports/$Name
echo "[+] Scan Complete [+]
[*] Check Reports Dir. for Results [*]"
""")

elif option == 8:
    os.system("""echo -n " Target : "
read Ip
echo -n " Name for Scan : "
read Name
sudo -S nmap -p 22 --script ssh-brute --script-args userdb=users.lst,passdb=pass.lst \
  --script-args ssh-brute.timeout=4s $Ip -oN ~/D3admapReports/$Name
echo "[+] Scan Complete [+]
[*] Check Reports Dir. for Results [*]"
""")

elif option == 9:
    os.system("""echo -n " Target : "
read Ip
echo -n " Name for Scan : "
read Name
sudo -S nmap -script http-enum $Ip -oN ~/D3admapReports/$Name
echo "[+] Scan Complete [+]
[*] Check Reports Dir. for Results [*]"
""")

elif option == 10:
    os.system("""echo -n " Target : "
read Ip
echo -n " Name for Scan : "
read Name
sudo -S nmap –script http-sitemap-generator $Ip -oN ~/D3admapReports/$Name
echo "[+] Scan Complete [+]
[*] Check Reports Dir. for Results [*]"
""")
