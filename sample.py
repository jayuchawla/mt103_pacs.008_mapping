#https://en.wikipedia.org/wiki/MT103

import re
from mt103 import MT103

def getTransactions(report):
    transactions = report.split("$")
    return transactions

def getMTMessages(transactions):
    mt_messages = []
    for transaction in transactions:
        mt_messages.append(MT103(transaction))

    return mt_messages

def getCodesValues(transactions):
    
    for transaction in transactions:
        lis = re.findall("{(.*?)}",transaction)
        print(lis)

with open("mt_sample.txt") as f:
    report = f.read().replace('\n','')


MT_messages = getMTMessages(getTransactions(report))

for mtm in MT_messages:
    print("BASIC HEADER: " + mtm.basic_header)
    print("APPLICATION HEADER: " + mtm.application_header)
    print("USER HEADER: " + str(mtm.user_header))
    print("TRANSACTION REFERENCE: " + mtm.text.transaction_reference)
    print("TRAILER: " + str(mtm.trailer))
    print("BANK OPERATION CODE: "+ str(mtm.text.bank_operation_code))
    print("INTERBANK SETTLED CURRENCY: " + str(mtm.text.interbank_settled_currency))
    print("INTERBANK SETTLED AMOUNT: " + str(mtm.text.interbank_settled_amount))
    print("ORIGINAL ORDERED CURRENCY: " + str(mtm.text.original_ordered_currency))
    print("ORIGINAL ORDERED AMOUNT: " + str(mtm.text.original_ordered_amount))
    print("ORDERING CUSTOMER: " + str(mtm.text.ordering_customer))    
    print("ORDERING INSTITUTION: " + str(mtm.text.ordering_institution))
    print("SENDER CORRESPONDENT: " + str(mtm.text.sender_correspondent))
    print("RECEIVER CORRESPONDENT: " + str(mtm.text.receiver_correspondent))
    print("INTERMEDIARY: " + str(mtm.text.intermediary))
    print("ACCOUNT WITH INSTITUTION: " + str(mtm.text.account_with_institution))
    print("BENEFICIARY: " + str(mtm.text.beneficiary))
    print("REMITTANCE INFORMATION: " + str(mtm.text.remittance_information))
    print("DETAILS OF CHARGES: " + str(mtm.text.details_of_charges))
    print("SENDER TO RECEIVER INFORMATION: " + str(mtm.text.sender_to_receiver_information))
    print("REGULATORY REPORTING: " + str(mtm.text.regulatory_reporting))
    print("DATE: " + str(mtm.text.date))
    print("-"*20)