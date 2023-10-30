import pytesseract
import cv2
import numpy as np
import os
import spacy
import re
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"


def front_data(img):
    regex_name = None
    regex_gender = None
    regex_dob = None
    regex_aadhaar_number = None
    #Name Entity Recognition function
    NER = spacy.load("en_core_web_sm")
    #thresh = image_processing(img)
    img2str_config_name = "--psm 4 --oem 3"
    res_string_name = pytesseract.image_to_string(img,lang='eng',config=img2str_config_name)
    name=NER(res_string_name)
    #extracting name
    for word in name.ents:
        if word.label_ == "PERSON":
            regex_name  = re.findall("[A-Z][a-z]+", word.text)
    if not regex_name:
        regex_name = re.findall("[A-Z][a-z]+", res_string_name)
    # print(regex_name)

    #extracting information other than name
    img2str_config_else = "--psm 3 --oem 3"
    res_string_else = pytesseract.image_to_string(img,lang='eng',config=img2str_config_else)


    if not regex_name:
        regex_name = re.findall("[A-Z][a-z]+", res_string_else)
    #extracting gender
    regex_gender = re.findall("MALE|FEMALE|male|female|Male|Female", res_string_else)
    if regex_gender:
        regex_gender = regex_gender[0]
    # print(regex_gender)

    dob = res_string_else.find('DOB')
    year= res_string_else.find('Year')

    #extracting date of birth
    regex_dob = re.findall("\d\d/\d\d/\d\d\d\d", res_string_else[dob+4:])

    if regex_dob:
        regex_dob = regex_dob[0]
    if not regex_dob:
        regex_dob = re.findall("(\d\d\d\d){1}", res_string_else[year+5:])[0]
    # print(regex_dob)

    #extracting aadhaar number
    regex_aadhaar_number = re.findall("\d\d\d\d \d\d\d\d \d\d\d\d",res_string_else)
    if regex_aadhaar_number:
        regex_aadhaar_number = regex_aadhaar_number[0]
    # print(regex_aadhaar_number)

    return (regex_name, regex_gender, regex_dob, regex_aadhaar_number)



def back_data(img):

    ocr_text = pytesseract.image_to_string(img, config=f'-l eng --psm 11 --oem 3 ')

    try:
        address_start = ocr_text.find('Address')
        if address_start==-1:
            address_start = ocr_text.find('To\n')
        address = ocr_text[address_start+8:]
        pinpatn = r'[0-9]{6}'
        address_end = 0
        pinloc = re.search(pinpatn, address)
        if pinloc:
            address_end = pinloc.end() 
        else:
            print('Pin code not found in address')
            address = re.sub('\n', ' ', address[:address_end])
        address = address[:address_end]
    except:
        address = re.sub('\n', ' ', ocr_text)
        pinpatn = re.compile(r'[0-9]{6}')
        pincode = re.search(pinpatn, address)
    return address.replace("\n","")