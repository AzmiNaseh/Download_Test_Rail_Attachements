import requests
import os

#Remove T from all the test Ids
#tested with testrail version 7

test_ids = ['441941','441702','441834']

for tids in test_ids:
    endpoint = 'https://something.testrail.com/index.php?/api/v2/get_attachments_for_test/:case_id'

    headers = {'Content-Type': 'application/json'}
    auth = ('some@domain.com', 'Some@123456')

    response = requests.get(endpoint.replace(':case_id', f'{tids}'), headers=headers, auth=auth)

    attachments = response.json()

    for attachment in attachments:
        attachment_id = attachment['id']
        filename = attachment['filename']
        print (attachment_id)
        print(filename)

        headers = {'Content-Type': 'application/json'}
        auth = ('some@domain.com', 'Some@123456')

        endpoint = 'https://something.testrail.com/index.php?/api/v2/get_attachment/:attachment_id'

        response = requests.get(endpoint.replace(':attachment_id', attachment_id), headers=headers, auth=auth)
        file_path = '/home/local/folder/TestRail/{}'.format(tids)
        #print(file_path)
        if not os.path.exists(file_path):
            os.mkdir(file_path)
        with open('{}/{}'.format(file_path,filename), 'wb') as f:
            f.write(response.content)

