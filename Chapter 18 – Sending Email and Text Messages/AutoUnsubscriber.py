import imapclient, bs4, pyzmail, webbrowser

imapObj = imapclient.IMAPClient('imap.gmail.com', ssl=True)
email = input("Enter email adress")
password = input("Enter password")

imapObj.login(email, password)
imapObj.select_folder("INBOX")
UIDs = imapObj.search(['BODY', 'unsubscribe'])

for uid in UIDs:
    rawMassages = imapObj.fetch(UIDs, [b'BODY[]'])
    message = pyzmail.PyzMessage.factory(rawMassages[uid][b'BODY[]'])
    new_message = message.html_part.get_payload().decode(message.html_part.charset)
    soup = bs4.BeautifulSoup(new_message, 'lxml')
    linkEl = soup.select('a')
    print("Unsubscribing at: {} ...".format(linkEl[0].get('href')))
    print()
    webbrowser.open(linkEl[0].get('href'))