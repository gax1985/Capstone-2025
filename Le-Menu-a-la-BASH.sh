
# Let us start by greeting, and add a command prompting the user to enter their choice :

echo "Good Day! I am a helpful Cybersecurity guide, and I am here to check up on your nice computer that you have there. "
echo "May I ask you to choose one of the following options, to determine our course of action:"

cat << 'EOF' 

1. Network Scans (with nmap)
2. Web Application Scans (with wapiti and nikto)
3. File Scanning (with ClamAV)

EOF

# Now, we can turn the user's choice into reality : 

print -p "Please Enter your Selection ( please enter 1,2,3 or type the letter 'q' to exit ) : " CHOICE

case CHOICE in 1

    bla
    bla
    bla command 
    ;;

case CHOICE in 2

    bla
    bla
    bla

    ;;

case CHOICE in 3 

    bla
    bla
    bla

    ;;

case CHOICE in q

    break

    ;;

esac








                



