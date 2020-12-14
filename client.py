import socket

def main():
  print("**********APPLE REQUEST PROGRAM***********")
  print("Welcome to the Apple Request Program. This program communicates with a fully functioning server to help you learn about the product released by apple each year.")
  print()
  ip_address = input("Enter Server IP Address: ")

  # Addresses are a two part tuple including ip/hostname and port
  server_address = (ip_address, 5000)

  playAgain = True
  while playAgain:
    request = input("Which year would you like to see? ")
    getStuff(server_address, request)
    playAgain = input("Would you like to enter another Year? (y/n)\n >")
    if playAgain == 'n' or playAgain == 'N':
      playAgain = False

def getStuff(server_address, request):
  with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
    sock.sendto(bytes(request,"UTF-8"), server_address)

    result = str(sock.recv(1024), "UTF-8")
    print("Results: ")
    print(format(result))
  pass

main()
