import requests
import json
import bcolors
import sys, argparse


def banner():
    print("""
                 
            ░██╗░░░░░░░██╗██████╗░░░░░░░░█████╗░███╗░░██╗░█████╗░██╗░░░░░██╗░░░██╗███████╗███████╗██████╗░
            ░██║░░██╗░░██║██╔══██╗░░░░░░██╔══██╗████╗░██║██╔══██╗██║░░░░░╚██╗░██╔╝╚════██║██╔════╝██╔══██╗
            ░╚██╗████╗██╔╝██████╔╝█████╗███████║██╔██╗██║███████║██║░░░░░░╚████╔╝░░░███╔═╝█████╗░░██████╔╝
            ░░████╔═████║░██╔═══╝░╚════╝██╔══██║██║╚████║██╔══██║██║░░░░░░░╚██╔╝░░██╔══╝░░██╔══╝░░██╔══██╗
            ░░╚██╔╝░╚██╔╝░██║░░░░░░░░░░░██║░░██║██║░╚███║██║░░██║███████╗░░░██║░░░███████╗███████╗██║░░██║
            ░░░╚═╝░░░╚═╝░░╚═╝░░░░░░░░░░░╚═╝░░╚═╝╚═╝░░╚══╝╚═╝░░╚═╝╚══════╝░░░╚═╝░░░╚══════╝╚══════╝╚═╝░░╚═╝
                                                                                                Code by NG          
          """)

if len(sys.argv) > 1:
    banner()
    if (sys.argv[1] == '-u') :
        try:
            input_url = sys.argv[2]

            input_header = requests.get(input_url)
            parser = argparse.ArgumentParser()
            parser.add_argument("-u", required=True)
            args = parser.parse_args()

            append_url = '/wp-json/wp/v2/users/'

            full_input_url = input_url + append_url
            print(bcolors.BOLD + full_input_url)

            UrlCode = requests.get(full_input_url)

            if(UrlCode.status_code ==200):
                  try:
                        json_input = json.loads(UrlCode.text)
                        i=0
                        jsonInput_length = len(json_input)
                        for i in range(jsonInput_length):
                              print(bcolors.OK + json_input[i]['name'], '(' +json_input[i]['link'] + ')')
                              i +=1
                  except:
                        print(bcolors.OKMSG +  "User not found")
            else:
                  print(bcolors.OKMSG +  "No User Found")
        except:
            print(bcolors.BOLD +  'Please enter python wpanalyzer.py -u <valid URL with http:// or https://> ')

    elif ((sys.argv[1] == '-h') | (sys.argv[1] == '--help')):
        print(bcolors.BOLD + 'usage: wpanalyzer.py [-h] -u URL' '\n' 'OPTIONS:' '\n' 'h,--help    '
                             'show this help message and exit' '\n''-u URL of wordpress website,   --url Url')
else:
      banner()
      print(bcolors.ERR + 'Please select at least 1 option from -u or -h, with a valid url')
