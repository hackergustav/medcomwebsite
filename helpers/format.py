import sys,re,time
import os
import glob
import shutil

output= open("output.txt","w+")



f=open("tmpl.txt", "r")
if f.mode == 'r':
  tmpl =f.read()

full_name_re = re.compile(r"\{full_name\}")
title_re = re.compile(r"\{title\}")
image_file_re = re.compile(r"\{image_file\}")

ff=open("member_format.txt", "r")
data =ff.readlines()
for x in data:
  tmpl_tmp = tmpl
  #Adam Gustavsson  adam_gustavsson.jpg Analyst
  member_data = x.split("\t")
  full_name=member_data[0]
  title=member_data[2].replace("\n","")
  image_file=member_data[1]

  tmpl_tmp = full_name_re.sub(full_name, tmpl_tmp)
  tmpl_tmp = title_re.sub(title, tmpl_tmp)
  tmpl_tmp = image_file_re.sub(image_file, tmpl_tmp)

  #shutil.copyfile('place_holder.jpg', image_file)
  #print(tmpl)
  output.write(tmpl_tmp)
