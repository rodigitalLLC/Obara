import sys
import pandas

# Obara
#def country_xlate(s):
  # RTA-CM
  #if s =='ON':
    #return 'CA'
  #else:
    #return 'US'

#def work_location_xlate(w):
  #work_locations = {
  #"Location":"State Code"
  #}
  #return work_locations[w]

def set_manager_id(m,l):
  print("Setting manager id")
  print(m)
  # query the dataframe using the manager last name, manager first name
  ml=m['Manager Last']
  mf=m['Manager First']

  mid=m['Manager Employee No']
  rv=""

  try:
   q="`Last Name`=='"+ml+"' and `First Name`=='"+mf.strip()+"'"
  except Exception as e:
    print('Cant build query:')
    print(e)
    rv=""
  else:
    print(q)
    r=l.query(q)
    #print(r['EmployeeID'])
    try:
     rv=r['EmployeeID'].iloc[0]
    except Exception as e:
      print(e)
      rv=""
  
  print("Returning "+rv)
  #print(dir(rv))
  return rv



def set_hire_date(r):
  if r['ReHire Date'] !="":
    if r['ReHire Date']< r['Hire Date']:
      r['Hire Date']=r['ReHire Date']

  return r

def state_xlate(s):
  us_state_to_abbrev = {
    "Alabama": "AL",
    "Alaska": "AK",
    "Arizona": "AZ",
    "Arkansas": "AR",
    "California": "CA",
    "Colorado": "CO",
    "Connecticut": "CT",
    "Delaware": "DE",
    "Florida": "FL",
    "Georgia": "GA",
    "Hawaii": "HI",
    "Idaho": "ID",
    "Illinois": "IL",
    "Indiana": "IN",
    "Iowa": "IA",
    "Kansas": "KS",
    "Kentucky": "KY",
    "Louisiana": "LA",
    "Maine": "ME",
    "Maryland": "MD",
    "Massachusetts": "MA",
    "Michigan": "MI",
    "Minnesota": "MN",
    "Mississippi": "MS",
    "Missouri": "MO",
    "Montana": "MT",
    "Nebraska": "NE",
    "Nevada": "NV",
    "New Hampshire": "NH",
    "New Jersey": "NJ",
    "New Mexico": "NM",
    "New York": "NY",
    "North Carolina": "NC",
    "North Dakota": "ND",
    "Ohio": "OH",
    "Oklahoma": "OK",
    "Oregon": "OR",
    "Pennsylvania": "PA",
    "Rhode Island": "RI",
    "South Carolina": "SC",
    "South Dakota": "SD",
    "Tennessee": "TN",
    "Texas": "TX",
    "Utah": "UT",
    "Vermont": "VT",
    "Virginia": "VA",
    "Washington": "WA",
    "West Virginia": "WV",
    "Wisconsin": "WI",
    "Wyoming": "WY",
    "District of Columbia": "DC",
    "American Samoa": "AS",
    "Guam": "GU",
    "Northern Mariana Islands": "MP",
    "Puerto Rico": "PR",
    "United States Minor Outlying Islands": "UM",
    "U.S. Virgin Islands": "VI",
    "Ontario":"ON"
  }
  return(us_state_to_abbrev[s.strip()])


def output_to_at_csv(df):
  template=[
    'Type', #A
    'EmployeeID', #B
    'Last Name', #C
    'First Name',#D
    'Middle Name', #E
    'Title', #F
    'Location', #G
    'Work State', #H
    'Work Country', #I
    'Home Phone', #J
    'Work Phone', #K
    'Mobile Phone', #L
    'Employee Phone Alt', #M
    'Business Email', #N
    'Personal Email', #O
    'Address',#P
    'Address Line 2',#Q
    'City', #R
    'State', #S
    'Zip', #T
    'Country',#U
    'PT/FT', #V
    'Manager Employee No', #W
    'Manager Last', #X
    'Manager First', #Y
    'Manager Phone', #Z
    'Manager Email', #AA
    'HR Contact Emp No', #AB
    'HR Contact Last', #AC
    'HR Contact First', #AD
    'HR Contact Phone', #AE
    'HR Contact Email', #AF
    'Spouse Emp No', #AG
    'DOB', #AH
    'Gender', #AI
    'Exempt-NonExempt', #AJ
    '50/75', #AK
    'Key Employee', #AL
    'Military Status',#AM
    'Employment Status',#AN
    'Term Date',#AO
    'Pay Rate',#AP
    'Pay Type',#AQ
    'Hire Date',#AR
    'ReHire Date',#AS
    'Service Date',#AT
    'Minutes Per Week',#AU
    'Hrs worked past 12 mos',#AV
    'Sunday',#AW
    'Monday',#AX
    'Tuesday',#AY
    'Wednesday',#AZ
    'Thursday',#BA
    'Friday',#BB
    'Saturday',#BC
    'Variable Flag', #BD
    'Effective Date',#BE 
    'Job Classification',#BF
    'Department',#BG
    'Cost Center',#BH
    'Schedule Effective Date',#BI
    'Employee Reference Code',#BJ
    'SSN',#BK
    'Pay Schedule',#BL
    'Start Date of Week',#BM
    'Average Weekly Minutes',#BN
    'Work County',#BO
    'Residence County',#BP
    'Work City',#BQ
    'Airline Flight Crew',#BQ
    ]
  df.to_csv('obara.csv',index=False,columns=template)

def rename_cols(df):
 return df.rename(columns={
    "EMPLOYEE NUMBER":"EmployeeID",
    "EMPLOYEE LAST NAME":"Last Name",
    "EMPLOYEE FIRST NAME":"First Name",
    "EMPLOYEE MIDDLE NAME":"Middle Name",
    "JOB TITLE":"Title",
    "WORK LOCATION":"Location",
    "WORK STATE":"Work State",
    "DATE OF BIRTH":"DOB",
    "GENDER":"Gender",
    "HIRE DATE":"Hire Date",
    "EMPLOYEE PHONE HOME":"Home Phone",
    "EMPLOYEE PHONE WORK":"Work Phone",
    "EMPLOYEE PH MOBILE":"Mobile Phone",
    "EMPLOYEE PHONE ALT":"Employee Phone Alt",
    "EMPLOYEE WORK EMAIL":"Business Email",
    "EMPLOYEE PERSONAL EMAIL":"Personal Email",
    "MAILING ADDRESS":"Address",
    "MAILING ADDRESS 2":"Address Line 2",
    "MAILING CITY":"City",
    "MAILING STATE":"State",
    "MAILING POSTAL CODE":"Zip",
    "MAILING COUNTRY":"Country",
    "ADJ HIRE DATE":"ReHireDate",
    "HOURS WORKED 12 MO":"Hrs worked past 12 mos",
    "TERM DATE":"Term Date",
  })

def customize(xls):
  xls['Type']='E'
  xls['Country']=xls['Country'].apply(lambda x: x[:2] if x=='USA' else x)
  xls['DOB']="01/01/1900"
  xls['First Name']=xls['First Name'].apply(lambda x: x.title())
  xls['Last Name']=xls['Last Name'].apply(lambda x: x.title())
  xls['Middle Name']=xls['Middle Name'].apply(lambda x: x[:1])
  xls['Work Country']=xls['Country']
  #xls['ReHire Date']=pandas.to_datetime(xls['ReHire Date'])
  xls['Hire Date']=pandas.to_datetime(xls['Hire Date'])

  #xls['Employment Status']=xls['Employment Status'].apply(lambda x: x[:1])
  xls['Employment Status']='A'
  #xls=xls.apply(set_hire_date, axis=1)
  xls['Exempt-NonExempt']=xls['EXEMPT/NONEXEMPT STS'].apply(lambda x: x[:1])
  xls['Gender']=xls['Gender'].apply(lambda x: 'U' if 'N' in x else x[:1])
  xls['Service Date']=xls['Hire Date']
  xls['Schedule Effective Date']=xls['Hire Date']


  #xls['ReHire Date']=xls['ReHire Date'].dt.strftime('%m/%d/%y')

  xls['Home Phone']=xls['Home Phone'].apply(lambda x: x.replace('-',''))
  xls['Work Phone']=xls['Work Phone'].apply(lambda x: x.replace('-',''))
  xls['Mobile Phone']=xls['Mobile Phone'].apply(lambda x: x.replace('-',''))
  xls['Employee Phone Alt']=xls['Employee Phone Alt'].apply(lambda x: x.replace('-',''))

  # define to '' those elements that are not present
  xls = xls.assign(**{'Manager Phone': '', 
                    'PT/FT':'',
                    'HR Contact Emp No':'', 
                    'Key Employee':'',
                    'HR Contact Last':'',
                    'HR Contact First':'',
                    'HR Contact Phone':'', 
                    'HR Contact Email':'', 
                    'Department':'',
                    'Cost Center':'',
                    'Work State':'',
                    'Pay Type':'',
                    'Spouse Emp No':'', 
                    'Manager First':'',
                    'Manager Last':'',
                    'Manager Employee No':'',
                    'Manager Email':'',
                    '50/75':'', 
                    'Military Status':'', 
                    'ReHire Date':'',
                    'Minutes Per Week':'', 
                    'Sunday':'', 
                    'Monday':'', 
                    'Tuesday':'', 
                    'Wednesday':'', 
                    'Thursday':'', 
                    'Friday':'', 
                    'Saturday':'',
                    'Variable Flag':'',
                    'Effective Date':'', 
                    'Case Status':'', 
                    #'Schedule Effective Date':'', 
                    'SSN':'', 
                    'Pay Schedule':'', 
                    'Start Date of Week':'', 
                    'Average Weekly Minutes':'', 
                    'Work County':'', 
                    'Residence County':'', 
                    'Work City':'', 
                    'Pay Rate':'', 
                    'Job Classification':'',
                    'Employee Reference Code':'',
                    'Airline Flight Crew':'',
                    })
  
  #xls['Home Phone']=xls['Home Phone'].apply(lambda x: '' if x=='0' else x)
  #xls['Mobile Phone']=xls['Mobile Phone'].apply(lambda x: '' if x=='0' else x)
  #xls['Work Phone']=xls['Work Phone'].apply(lambda x: '' if x=='0' else x)
  #xls['Employee Phone Alt']=xls['Employee Phone Alt'].apply(lambda x: '' if x=='0' else x)

  xls['Home Phone']=xls['Home Phone'].apply(lambda x: '{ignore}' if x=='' else x)
  xls['Mobile Phone']=xls['Mobile Phone'].apply(lambda x: '{ignore}' if x=='' else x)
  xls['Work Phone']=xls['Work Phone'].apply(lambda x: '{ignore}' if x=='' else x)
  xls['Employee Phone Alt']=xls['Employee Phone Alt'].apply(lambda x: '{ignore}' if x=='' else x)
  return xls
# main

# database

# required columns: Type,EmployeeID,Last Name,First Name,Title,Work State,PT/FT,DOB,Gender,Exemption Status,Employment Status,Hire Date,Service Date
#if len(sys.argv)!=3:
  #print ("Usage: {} {} {}".format(sys.argv[0],"<input xlsx sheet>"))
  #sys.exit()

xl=pandas.read_csv(sys.argv[1],na_filter=False,dtype={'EMPLOYEE NUMBER':'string'})
xls=xl.astype('string')
# 
# debug out
xls=rename_cols(xls)
xls=customize(xls)
#print(xls)
output_to_at_csv(xls)