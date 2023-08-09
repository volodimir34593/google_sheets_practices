import gspread
from oauth2client.service_account import ServiceAccountCredentials


url = 'https://docs.google.com/spreadsheets/d/10U6xJMMKPye4At5fPARUn_UTCj88CNyNqOaA1fVYkCo/edit#gid=0'
scopes = [
    'https://www.googleapis.com/auth/spreadsheets',
    'https://www.googleapis.com/auth/drive',
]

creds = ServiceAccountCredentials.from_json_keyfile_name('secrets.json', scopes=scopes)
client = gspread.authorize(credentials=creds)


data = client.open_by_url(url)
print(data.fetch_sheet_metadata().get('sheets'))
student = data.sheet1
print(student.get_all_values())