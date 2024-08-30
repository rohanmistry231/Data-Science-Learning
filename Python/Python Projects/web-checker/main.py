import requests
import csv 
from fake_useragent import UserAgent
from http import HTTPStatus

# Website checker read file with websites and check if a website is in running considiton or not. and deliver a message as per the information received through server. Few functions to deleope for the project:
# T read a csv file 
# Get user agent firefox 
# Check for status code 
# check if website found  and running 
# main function 


def read_websites_file(file_path):
    websites = []
    with open(file_path, 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            if "https://" not in row[0] and "http://" not in row[0]:
                websites.append(f"https://{row[0]}")
            else:
                websites.append(row[0])

        return websites


# print(read_websites_file('websites.csv'))

def get_user_agent():
    user_agent = UserAgent()
    return user_agent.firefox



def check_website_status_code(status_code):
    for value in HTTPStatus:
        if value == status_code:
            website_description = f"{value.name} - {value.description}"

            return website_description
    return "UNKOWN STATUS CODE.. NO DETAILS"


def check_website(website, user_agent):
    try:
        code = requests.get(website, headers={'User-Agent': user_agent}).status_code
        print(website, check_website_status_code(code))
    except Exception:
        print(f"NO INFORMATION FOUND FOR - {website}")




def main():
    websites = read_websites_file('websites.csv')
    user_agent = get_user_agent()

    for web in websites:
        check_website(web, user_agent)


if __name__ =="__main__":
    main()