import SendNoti as SN
import Scraper as SC
from UserInfo import UserInfo

def main():
    crns = UserInfo.keys()
    for crn in crns:
        if(SC.check_available(crn)):
            for email in UserInfo[crn]:
                content = "Seats open in CRN: " + crn
                SN.send_email("Course Available", content, email)


if __name__ == "__main__":
   main()