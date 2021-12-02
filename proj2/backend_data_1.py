from flask import Flask, render_template, request , flash , Markup , send_file
import flask
import os
import shutil
import csv
from fpdf import FPDF
import datetime
from datetime import datetime
from datetime import date
app = Flask(__name__)

def function_2():
    ZZZZ=os.listdir("files1")
    yyyzzzz=os.listdir("files2")

    e = datetime.now()
    znn= date.today()
    pras= e.day
    prasa= znn.strftime("%B")
    prasan=e.year
    prasant=e.strftime("%H:%M")

    prasanth=""
    prasanth+=str(pras)
    prasanth+=" "
    prasanth+=prasa[:3]
    prasanth+=" "
    prasanth+=str(prasan)
    prasanth+=","
    prasanth+=prasant
    print(prasant)
    prasanth+="."
    with open(f"./files/names-roll.csv" , "r") as f:
        reading = csv.reader(f  , delimiter=',')
        lll=[]
        names=[]
        for o in reading:
            if o[0]== "Roll":
                continue
            lll.append(o[0])
            names.append(o[1])
    with open(f"./files/subjects_master.csv" , "r") as f:
        reading = csv.reader(f , delimiter=',')
        d={}
        for o in reading:
            if o[0]== 'subno':
                continue
            d[o[0]]=[o[1] , o[2] , o[3] ]

    z11=lll.copy()
    l2=[]
    BRAND=z11[-1]

    im_dict={x:[] for x in  z11}

    with open(f"./files/grades.csv" , 'r') as f:
            i=2
            reaaa = csv.reader(f)
            lst=[]
            for o in reaaa:

                if o[0] == 'Roll':
                    continue
                if(os.path.exists(f"./templates/output/{o[0]+o[1]}.csv")):
                        with open(f"./templates/output/{o[0]+o[1]}.csv" , "a" , newline='') as f:
                            fieee = [ 'Subject No' , 'Subject Name' , 'L-T-P' , 'Credit' , 'Grade']
                            writer = csv.DictWriter(f , fieldnames=fieee)
                            writer.writerow({ 'Subject No':o[2]  , 'Subject Name':d[o[2]][0] , 'L-T-P':d[o[2]][1] , 'Credit':o[3]   , 'Grade':o[4]})
                else:
                    lst.append(o[1])
                    im_dict[o[0]].append(o[1])
                    with open(f"./templates/output/{o[0]+o[1]}.csv" , "w" , newline='') as f:
                            fieee = [ 'Subject No' , 'Subject Name' , 'L-T-P' , 'Credit' , 'Grade']
                            writer = csv.DictWriter(f , fieldnames=fieee)
                            writer.writerow({ 'Subject No':o[2]  , 'Subject Name':d[o[2]][0] , 'L-T-P':d[o[2]][1] ,'Credit':o[3]  , 'Grade':o[4]})









    lst111=lst.copy()
    dict={}
    lll=True
    loge=z11.copy()
    while(len(loge)>0 ):
        z11[0]= FPDF("L" , "mm" ,"A3")
        z11[0].add_page() 
        z11[0].image('./templates/Picture.png' , 9,5,30,25)
        z11[0].image('./templates/Picture.png',375,5,30,25 , title="INTERIM TRANSCRIPT")
        z11[0].image("./templates/Picture3.png",48,7,300,20 , title='transcript')
        z11[0].set_font('times' ,'u',10)
        z11[0].cell(-5.5)
        z11[0].cell(70,45,"INTERIM TRANSCRIPT" )
        z11[0].cell(-66)
        z11[0].set_font('times' ,'',27)
        z11[0].cell(370,38,"Transcript ", align="C" )
        z11[0].cell(-7.5)
        z11[0].set_font('times' ,'u',10)
        z11[0].cell(80,45,"INTERIM TRANSCRIPT")
        z11[0].set_y(-281)
        z11[0].set_x(110)
        z11[0].rect(5.0, 5.0,405.0,285.0)
        z11[0].rect(5.0, 5.0, 405.0,30.0)
        z11[0].rect(5.0, 5.0, 40.0,30.0)
        z11[0].rect(370.0, 5.0, 40.0,30.0)
        z11[0].rect(105.0, 37, 200.0,13.0)
        z11[0].set_font('times' ,'B',12)
        z11[0].cell(160,48,"Roll No:")
        z11[0].rect(130.0, 39, 25.0,4.0)
        z11[0].cell(-110)
        z11[0].set_font('times' ,'B',12)
        z11[0].cell(90,48,"Name:")
        z11[0].rect(180.0, 39, 44.0,4.0)
        z11[0].cell(-20)
        z11[0].cell(90,48,"Year of Admission:")
        z11[0].rect(270.0, 39 , 20.0 ,4.0 )
        z11[0].cell(-210)
        z11[0].cell(90,60,"Programme: ")
        z11[0].set_font('times' ,'',12)
        z11[0].cell(-60)
        z11[0].cell(0,61,"Bachelor of Technology")
        z11[0].cell(-220)
        z11[0].set_font('times' ,'B',12)
        z11[0].cell(0,60,"Course:")
        z11[0].cell(-200)
        z11[0].set_font('times' ,'',12)
        z11[0].cell(0,62,"hh")
        z11[0].line(5, 110, 410,110)
        z11[0].line(5, 170, 410,170)
        z11[0].line(5, 231, 410,231)
        z11[0].cell(-280)
        z11[0].cell(40,50,f"{loge[0]}")
        z11[0].cell(18)
        z11[0].cell(100,50,f"{names[0]}")
        z11[0].cell(-12)
        z11[0].cell(10,50,"2019")


        zuxxy=0
        luxxy=0
        total_credits=0

        joel=True
        while(True):
            Grades_convert={'AA':10 , 'AB':9 , 'BB':8 ,'BC':7 , 'CC':6 , 'CD':5 , 'DD':4 , 'F':0 , 'I':0  , 'I*':0 , "F*":0 , 'DD*':0}
            xll=3
            while(xll>0):



                if len(lst111) >0 and len(loge)>0:
                    if( not os.path.exists(f"./templates/output/{loge[0]+(lst111[0])}.csv")):
                        joel=False
                        break
                else:
                    break
                z11[0].set_x(30)
                z11[0].set_y(60)
                lo=[]
                z11[0].set_font("times","B",10)
                if(len(im_dict[loge[0]])>0 and xll==3):
                    z11[0].cell(-1)

                    z11[0].cell(9.8,-5,f"semester {im_dict[loge[0]][0]}")
                    z11[0].rect(10,98,100,7)
                    im_dict[loge[0]].pop(0)
                elif ( len(im_dict[loge[0]])>0 and xll==2):
                    z11[0].cell(130)
                    z11[0].cell(140.9,-5,f"semester {im_dict[loge[0]][0]}")
                    z11[0].rect(141,98,100,7)
                    im_dict[loge[0]].pop(0)
                elif( len(im_dict[loge[0]]) >0 and xll==1):
                    z11[0].cell(270)
                    z11[0].cell(340,-5,f"semester {im_dict[loge[0]][0]}")
                    z11[0].rect(280,98,100,7)
                    im_dict[loge[0]].pop(0)


                header=['Subject No' , 'Subject Name' , 'L-T-P' , 'Credit' , 'Grade']
                with open(f"./templates/output/{loge[0] + lst111[0]}.csv" , "r") as f:
                    o= csv.reader(f)
                    current_sem_credits=0
                    luxxy1=0
                    for x in o:
                        lo.append(x)
                        total_credits+=int(x[3])
                        current_sem_credits+=int(x[3])
                        luxxy1+=(int(x[3])*Grades_convert[x[4]])
                    luxxy1/=current_sem_credits
                    zz=round(luxxy1,2)
                    luxxy+=(luxxy1*current_sem_credits)

                    zuxxy=luxxy/total_credits
                    az=round(zuxxy,2)
                    z11[0].cell(-12)  
                    if xll==3:
                        z11[0].cell(4)
                        z11[0].cell(4,82,f"Credits taken:{current_sem_credits}     Credits cleared: {current_sem_credits}    SPI: {zz}    CPI: {az}")
                    elif xll==2:
                        z11[0].cell(-126)
                        z11[0].cell(60,82,f"Credits taken:{current_sem_credits}     Credits cleared: {current_sem_credits}    SPI: {zz}    CPI: {az}")
                    elif xll==1:
                        z11[0].cell(-326)
                        z11[0].cell(200,82,f"Credits taken:{current_sem_credits}     Credits cleared: {current_sem_credits}    SPI: {zz}    CPI: {az}")








                col_width = 'even'
                if(xll==3):
                    z11[0].set_x(9.8)
                elif(xll==2):
                    z11[0].set_x(140.9)
                elif(xll==1):
                    z11[0].set_x(280)
                width_col=[20.0,55.0,15.0,15.0,15.0]
                x_start=z11[0].get_x()
                line_height=4
                y1=z11[0].get_y()
                x_left=z11[0].get_x()
                data=lo
                align_header='L'

                for i in range(len(header)):
                            datum = header[i]
                            z11[0].set_font("times",'B',7)
                            z11[0].multi_cell(width_col[i], line_height, datum, border=1, align="C", ln=3, max_line_height=z11[0].font_size)
                            x_right = z11[0].get_x()
                z11[0].ln(line_height)
                y2 = z11[0].get_y()
                z11[0].line(x_left,y1,x_right,y1)
                z11[0].line(x_left,y2,x_right,y2)
                for i in range(len(data)):
                
                    if(xll==3):
                        z11[0].set_x(9.8)
                    elif(xll==2):
                        z11[0].set_x(140.9)
                    elif(xll==1):
                        z11[0].set_x(280)
                    row = data[i]
                    for i in range(0,len(row)):
                        datum = row[i]
                        z11[0].set_font("times",'',7)
                        z11[0].multi_cell(width_col[i], line_height, datum, border=1, align="C", ln=3, max_line_height=z11[0].font_size)
                    z11[0].ln(line_height)
                    y3 = z11[0].get_y()
                    z11[0].line(x_left,y3,x_right,y3)
                os.remove(f"./templates/output/{loge[0]+lst111[0]}.csv")
                lst111.pop(0)
                xll-=1


            xll=3
            while(xll>0):
                if len(lst111) >0 and len(loge)>0:
                    if( not os.path.exists(f"./templates/output/{loge[0]+(lst111[0])}.csv")):
                        joel=False
                        break
                else:
                    break
                lo=[]
                z11[0].set_x(30)
                z11[0].set_y(120)
                header=['Subject No' , 'Subject Name' , 'L-T-P' , 'Credit' , 'Grade']
                with open(f"./templates/output/{loge[0] + lst111[0]}.csv" , "r") as f:
                    o= csv.reader(f)
                    current_sem_credits=0
                    luxxy1=0
                    for x in o:
                        lo.append(x)
                        total_credits+=int(x[3])
                        current_sem_credits+=int(x[3])
                        luxxy1+=(int(x[3])*Grades_convert[x[4]])
                    luxxy1/=current_sem_credits
                    zz=round(luxxy1,2)
                    luxxy+=(luxxy1*current_sem_credits)

                    zuxxy=luxxy/total_credits
                    az=round(zuxxy,2)
                    z11[0].set_font("times","B",10)
                    if xll==3:

                        z11[0].cell(4,90,f"Credits taken:{current_sem_credits}     Credits cleared: {current_sem_credits}    SPI: {zz}    CPI: {az}")
                    elif xll==2:
                        z11[0].cell(132)
                        z11[0].cell(20,90,f"Credits taken:{current_sem_credits}     Credits cleared: {current_sem_credits}    SPI: {zz}    CPI: {az}")
                    elif xll==1:
                        z11[0].cell(272)
                        z11[0].cell(20,90,f"Credits taken:{current_sem_credits}     Credits cleared: {current_sem_credits}    SPI: {zz}    CPI: {az}")
                col_width = 'even'
                z11[0].set_font("times","B",10)
                if(len(im_dict[loge[0]])>0 and xll==3):
                    z11[0].cell(-4)
                    z11[0].rect(10,161,100,7)
                    z11[0].cell(9.8,-5,f"semester {im_dict[loge[0]][0]}")
                    im_dict[loge[0]].pop(0)
                elif ( len(im_dict[loge[0]])>0 and xll==2):
                    z11[0].cell(-20)
                    z11[0].rect(141,161,100,7)
                    z11[0].cell(140.9,-5,f"semester {im_dict[loge[0]][0]}")
                    im_dict[loge[0]].pop(0)
                elif( len(im_dict[loge[0]]) >0 and xll==1):
                    z11[0].cell(-23)
                    z11[0].rect(280,161,100,7)
                    z11[0].cell(340,-5,f"semester {im_dict[loge[0]][0]}")
                    im_dict[loge[0]].pop(0)



                if(xll==3):
                    z11[0].set_x(9.8)
                elif(xll==2):
                    z11[0].set_x(140.9)
                elif(xll==1):
                    z11[0].set_x(280)
                width_col=[20.0,55.0,15.0,15.0,15.0]
                x_start=z11[0].get_x()
                line_height=4
                y1=z11[0].get_y()
                x_left=z11[0].get_x()
                data=lo
                align_header='C'
                for i in range(len(header)):
                            datum = header[i]
                            z11[0].set_font("times",'B',7)
                            z11[0].multi_cell(width_col[i], line_height, datum, border=1, align="C", ln=3, max_line_height=z11[0].font_size)
                            x_right = z11[0].get_x()
                z11[0].ln(line_height)
                y2 = z11[0].get_y()
                z11[0].line(x_left,y1,x_right,y1)
                z11[0].line(x_left,y2,x_right,y2)
                for i in range(len(data)):
                
                    if(xll==3):
                        z11[0].set_x(9.8)
                    elif(xll==2):
                        z11[0].set_x(140.9)
                    elif(xll==1):
                        z11[0].set_x(280)
                    row = data[i]
                    for i in range(0,len(row)):
                        datum = row[i]
                        z11[0].set_font("times",'',7)
                        z11[0].multi_cell(width_col[i], line_height, datum, border=1, align="C", ln=3, max_line_height=z11[0].font_size)
                    z11[0].ln(line_height)
                    y3 = z11[0].get_y()
                    z11[0].line(x_left,y3,x_right,y3)
                os.remove(f"./templates/output/{loge[0]+lst111[0]}.csv")
                lst111.pop(0)
                xll-=1




            x12=2
            while(x12>0):
                if len(lst111) >0 and len(loge)>0:
                    if( not os.path.exists(f"./templates/output/{loge[0]+(lst111[0])}.csv")):
                        joel=False
                        break
                    else:
                        pass
                elif len(lst111)==0 or len(loge)==0:
                    break
                else:
                    pass
                lo=[]
                z11[0].set_x(30)
                z11[0].set_y(180)
                header=['Subject No' , 'Subject Name' , 'L-T-P' , 'Credit' , 'Grade']
                with open(f"./templates/output/{loge[0] + lst111[0]}.csv" , "r") as f:

                    o= csv.reader(f)
                    current_sem_credits=0
                    luxxy1=0
                    for x in o:
                        lo.append(x)
                        total_credits+=int(x[3])
                        current_sem_credits+=int(x[3])
                        luxxy1+=(int(x[3])*Grades_convert[x[4].strip()])
                    luxxy1/=current_sem_credits
                    zz=round(luxxy1,2)
                    luxxy+=(luxxy1*current_sem_credits)

                    zuxxy=luxxy/total_credits
                    az=round(zuxxy,2)
                    z11[0].set_font("times","B",10)
                    if x12==2:

                        z11[0].cell(4,90,f"Credits taken:{current_sem_credits}     Credits cleared: {current_sem_credits}    SPI: {zz}    CPI: {az}")
                    elif x12==1:
                        z11[0].cell(132)
                        z11[0].cell(20,90,f"Credits taken:{current_sem_credits}     Credits cleared: {current_sem_credits}    SPI: {zz}    CPI: {az}")
                col_width = 'even'
                z11[0].set_font("times","B",10)
                if(len(im_dict[loge[0]])>0 and x12==2):
                        z11[0].cell(-4)
                        z11[0].rect(10,221.5,100,7)
                        z11[0].cell(9.8,-5,f"semester {im_dict[loge[0]][0]}")
                        im_dict[loge[0]].pop(0)
                elif ( len(im_dict[loge[0]])>0 and x12==1):
                        z11[0].cell(130)
                        z11[0].rect(141,221.5,100,7)
                        z11[0].cell(-153)
                        z11[0].cell(100.9,-5,f"semester {im_dict[loge[0]][0]}")
                        im_dict[loge[0]].pop(0)
                if(x12==2):
                    z11[0].set_x(9.8)
                elif(x12==1):
                    z11[0].set_x(140.9)
                width_col=[20.0,55.0,15.0,15.0,15.0]
                x_start=z11[0].get_x()
                line_height=4
                y1=z11[0].get_y()
                x_left=z11[0].get_x()
                data=lo
                align_header='L'
                for i in range(len(header)):
                            datum = header[i]
                            z11[0].set_font("times",'B',7)
                            z11[0].multi_cell(width_col[i], line_height, datum, border=1, align="C", ln=3, max_line_height=z11[0].font_size)
                            x_right = z11[0].get_x()
                z11[0].ln(line_height)
                y2 = z11[0].get_y()
                z11[0].line(x_left,y1,x_right,y1)
                z11[0].line(x_left,y2,x_right,y2)
                for i in range(len(data)):
                
                    if(x12==2):
                        z11[0].set_x(9.8)
                    elif(x12==1):
                        z11[0].set_x(140.9)
                    row = data[i]
                    for i in range(0,len(row)):
                        datum = row[i]
                        z11[0].set_font("times",'',7)
                        z11[0].multi_cell(width_col[i], line_height, datum, border=1, align="C", ln=3, max_line_height=z11[0].font_size)
                    z11[0].ln(line_height)
                    y3 = z11[0].get_y()
                    z11[0].line(x_left,y3,x_right,y3)
                os.remove(f"./templates/output/{loge[0]+lst111[0]}.csv")
                lst111.pop(0)
                x12-=1


            if loge[0]==BRAND:
                hh=loge[0]
                z11[0].set_y(-30)
                z11[0].cell(300)
                z11[0].set_font('times','',15)
                z11[0].cell(200,10,"Assistant Registar" , ln=0)
                z11[0].cell(-500)
                z11[0].cell(20,10,"Date of issue:")
                z11[0].cell(150)
                z11[0].cell(20,10,'stamp')
                z11[0].image(f"./storage1/{ZZZZ[0]}",178,250,18,18 , title='trscript')
                z11[0].image(f"./storage2/{yyyzzzz[0]}",328,250,18,18 , title='trnscript')
                z11[0].cell(-158)
                z11[0].cell(200,10, prasanth)
                z11[0].output(f"./generated/{hh}.pdf")



            if(len(lst111)==0):
                lll= False
                break

            if( not os.path.exists(f"./templates/output/{loge[0]+lst111[0]}.csv")):
                hh=loge[0]
                z11[0].set_y(-30)
                z11[0].cell(300)
                z11[0].set_font('times','',15)
                z11[0].cell(200,10,"Assistant Registar" , ln=0)
                z11[0].cell(-500)
                z11[0].cell(20,10,"Date of issue:")
                z11[0].cell(150)
                z11[0].cell(20,10,'stamp')
                z11[0].image(f"./storage1/{ZZZZ[0]}",178,250,18,18 , title='trscript')
                z11[0].image(f"./storage2/{yyyzzzz[0]}",328,250,18,18 , title='trnscript')
                z11[0].cell(-158)
                z11[0].cell(200,10, prasanth)
                z11[0].output(f"./generated/{hh}.pdf")
                loge.pop(0)
                break
        names.pop(0)
        if lll == False:
            break


def function():
        grade = request.files["grades"]
        name = request.files["names_roll"]
        subject=request.files['subject_master']
        stamps=request.files['stamp']
        signature=request.files['signature']
        grade.save(os.path.join("files", (grade.filename)))
        name.save(os.path.join("files",(name.filename)))
        subject.save(os.path.join("files",(subject.filename)))
        stamps.save(os.path.join("files1",(stamps.filename)))
        signature.save(os.path.join("files2",(signature.filename)))
         #flash("Uploaded  successfully :)"  , "info")
        print(stamps.filename)
        return render_template("index.html" )

def storer():
    if(os.path.exists("files")):
        shutil.rmtree("files")
    else:
        pass
    os.mkdir("files")
    if(os.path.exists("files1")):
        shutil.rmtree("files1")
    else:
        pass
    os.mkdir("files1")
    if(os.path.exists("files2")):
        shutil.rmtree("files2")
    else:
        pass
    os.mkdir("files2")
    if(os.path.exists("./templates/output")):
        shutil.rmtree("./templates/output")
    else:
        pass
    os.mkdir("./templates/output")
    if(os.path.exists("generated")):
        shutil.rmtree("generated")
    else:
        pass
    os.mkdir("generated")

def storer_1():
        if(os.path.exists("./templates/output")):
            shutil.rmtree("./templates/output")
        else:
            pass
        os.mkdir("./templates/output")
        if(os.path.exists("generated")):
            shutil.rmtree("generated")
        else:
            pass
        os.mkdir("generated")

def function_1():
    start_range=request.form.get("from_range")
    end_range=request.form.get("to_range")
    start_RANGE=start_range.upper()
    end_RANGE=end_range.upper()
    h1=int(end_RANGE[-2:])
    ze=start_RANGE[:-2]
    zem=int(start_RANGE[-2:])
    print(zem , type(zem))
    print(ze, type(ze))
    print(h1, type(h1))
    range_1=[]
    range_2=[]


    zz = os.listdir("files1")
    zy = os.listdir("files2")

    e = datetime.now()
    from datetime import date
    xnn= date.today()
    pras= e.day
    prasa= xnn.strftime("%B")
    prasan=e.year
    prasant=e.strftime("%H:%M")

    prasanth=""
    prasanth+=str(pras)
    prasanth+=" "
    prasanth+=prasa[:3]
    prasanth+=" "
    prasanth+=str(prasan)
    prasanth+=","
    prasanth+=prasant
    print(prasant)
    prasanth+="."
    with open(f"./storage/names-roll.csv" , "r") as f:
        reader = csv.reader(f  , delimiter=',')
        l=[]
        name=[]
        for o in reader:
            if o[0]== "Roll":
                continue
            l.append(o[0])
            name.append(o[1])
    for x in range(zem , h1+1):
        jj=0
        
        for y in range(0, len(l)):
            if( x >=10):
                if ze + str(x) ==l[y]:
                    range_1.append(l[y])
                    jj=1
                    break
            elif x < 10:
                if ze + "0"+ str(x) ==l[y]:
                    range_1.append(l[y])
                    jj=1
                    break
        if(jj==0):
            if x <10:
                range_2.append(ze+"0"+ str(x))
            else:
                range_2.append(ze + str(x))

    print(range_1)
    print(range_2)

    with open(f"./files/subjects_master.csv" , "r") as f:
        reader = csv.reader(f , delimiter=',')
        d={}
        for o in reader:
            if o[0]== 'subno':
                continue
            d[o[0]]=[o[1] , o[2] , o[3] ]

    lst11=range_1.copy()
    im_dict={x:[] for x in  lst11}
    lis=[]
    while(len(lst11)>0):
        with open(f"./files/grades.csv" , 'r') as f:
            i=2
            reaaa = csv.reader(f)
            for o in reaaa:

                if o[0] == lst11[0]:
                    if(os.path.exists(f"./templates/output/{o[0]+o[1]}.csv")):
                            with open(f"./templates/output/{o[0]+o[1]}.csv" , "a" , newline='') as f:
                                fie = [ 'Subject No' , 'Subject Name' , 'L-T-P' , 'Credit' , 'Grade']
                                writer = csv.DictWriter(f , fieldnames=fie)
                                writer.writerow({ 'Subject No':o[2]  , 'Subject Name':d[o[2]][0] , 'L-T-P':d[o[2]][1] , 'Credit':o[3]   , 'Grade':o[4]})
                    else:
                        lis.append(o[1])
                        im_dict[o[0]].append(o[1])
                        with open(f"./templates/output/{o[0]+o[1]}.csv" , "w" , newline='') as f:
                                fie = [ 'Subject No' , 'Subject Name' , 'L-T-P' , 'Credit' , 'Grade']
                                writer = csv.DictWriter(f , fieldnames=fie)
                                writer.writerow({ 'Subject No':o[2]  , 'Subject Name':d[o[2]][0] , 'L-T-P':d[o[2]][1] ,'Credit':o[3]  , 'Grade':o[4]})

        lst11.pop(0)

    lst111=lis.copy()
    l=True
    BRAND=range_1[-1]
    z11=range_1.copy()
    loge=range_1.copy()
    while(len(loge)>0 ):
        z11[0]= FPDF("L" , "mm" ,"A3")
        z11[0].add_page() 
        z11[0].image('./templates/Picture.png' , 9,5,30,25  )
        z11[0].image('./templates/Picture.png',375,5,30,25 )
        z11[0].image("./templates/Picture3.png",48,7,300,20 )
        z11[0].set_font('times' ,'u',10)
        z11[0].cell(-5.5)
        z11[0].cell(70,45,"INTERIM TRANSCRIPT" )
        z11[0].cell(-66)
        z11[0].set_font('times' ,'',27)
        z11[0].cell(370,38,"Transcript ", align="C" )
        z11[0].cell(-7.5)
        z11[0].set_font('times' ,'u',10)
        z11[0].cell(80,45,"INTERIM TRANSCRIPT")
        z11[0].set_y(-281)
        z11[0].set_x(110)
        z11[0].rect(5.0, 5.0,405.0,285.0)
        z11[0].rect(5.0, 5.0, 405.0,30.0)
        z11[0].rect(5.0, 5.0, 40.0,30.0)
        z11[0].rect(370.0, 5.0, 40.0,30.0)
        z11[0].rect(105.0, 37, 200.0,13.0)
        z11[0].set_font('times' ,'B',12)
        z11[0].cell(160,48,"Roll No:")
        z11[0].rect(130.0, 39, 25.0,4.0)
        z11[0].cell(-110)
        z11[0].set_font('times' ,'B',12)
        z11[0].cell(90,48,"Name:")
        z11[0].rect(180.0, 39, 44.0,4.0)
        z11[0].cell(-20)
        z11[0].cell(90,48,"Year of Admission:")
        z11[0].rect(270.0, 39 , 20.0 ,4.0 )
        z11[0].cell(-210)
        z11[0].cell(90,60,"Programme: ")
        z11[0].set_font('times' ,'',12)
        z11[0].cell(-60)
        z11[0].cell(0,61,"Bachelor of Technology")
        z11[0].cell(-220)
        z11[0].set_font('times' ,'B',12)
        z11[0].cell(0,60,"Course:")
        z11[0].cell(-200)
        z11[0].set_font('times' ,'',12)
        z11[0].cell(0,62,"hh")
        z11[0].line(5, 110, 410,110)
        z11[0].line(5, 170, 410,170)
        z11[0].line(5, 231, 410,231)
        z11[0].cell(-280)
        z11[0].cell(40,50,f"{loge[0]}")
        z11[0].cell(18)
        z11[0].cell(100,50,f"{name[0]}")
        z11[0].cell(-12)
        z11[0].cell(10,50,"2019")


        zuxxy=0
        luxxy=0
        credits_total=0

        pra=True
        while(True):
            Grades_map={'AA':10 , 'AB':9 , 'BB':8 ,'BC':7 , 'CC':6 , 'CD':5 , 'DD':4 , 'F':0 , 'I':0  , 'I*':0 , "F*":0 , 'DD*':0}
            xll=3
            while(xll>0):



                if len(lst111) >0 and len(loge)>0:
                    if( not os.path.exists(f"./templates/output/{loge[0]+(lst111[0])}.csv")):
                        pra=False
                        break
                else:
                    break
                z11[0].set_x(30)
                z11[0].set_y(60)
                lo=[]
                z11[0].set_font("times","B",10)
                if(len(im_dict[loge[0]])>0 and xll==3):
                    z11[0].cell(-1)

                    z11[0].cell(9.8,-5,f"semester {im_dict[loge[0]][0]}")
                    z11[0].rect(10,98,100,7)
                    im_dict[loge[0]].pop(0)
                elif ( len(im_dict[loge[0]])>0 and xll==2):
                    z11[0].cell(130)
                    z11[0].cell(140.9,-5,f"semester {im_dict[loge[0]][0]}")
                    z11[0].rect(141,98,100,7)
                    im_dict[loge[0]].pop(0)
                elif( len(im_dict[loge[0]]) >0 and xll==1):
                    z11[0].cell(270)
                    z11[0].cell(340,-5,f"semester {im_dict[loge[0]][0]}")
                    z11[0].rect(280,98,100,7)
                    im_dict[loge[0]].pop(0)


                header=['Subject No' , 'Subject Name' , 'L-T-P' , 'Credit' , 'Grade']
                with open(f"./templates/output/{loge[0] + lst111[0]}.csv" , "r") as f:
                    o= csv.reader(f)
                    current_sem_credits=0
                    luxxy1=0
                    for x in o:
                        lo.append(x)
                        credits_total+=int(x[3])
                        current_sem_credits+=int(x[3])
                        luxxy1+=(int(x[3])*Grades_map[x[4]])
                    luxxy1/=current_sem_credits
                    zz=round(luxxy1,2)
                    luxxy+=(luxxy1*current_sem_credits)

                    zuxxy=luxxy/credits_total
                    az=round(zuxxy,2)
                    z11[0].cell(-12)  
                    if xll==3:
                        z11[0].cell(4)
                        z11[0].cell(4,82,f"Credits taken:{current_sem_credits}     Credits cleared: {current_sem_credits}    SPI: {zz}    CPI: {az}")
                    elif xll==2:
                        z11[0].cell(-126)
                        z11[0].cell(60,82,f"Credits taken:{current_sem_credits}     Credits cleared: {current_sem_credits}    SPI: {zz}    CPI: {az}")
                    elif xll==1:
                        z11[0].cell(-326)
                        z11[0].cell(200,82,f"Credits taken:{current_sem_credits}     Credits cleared: {current_sem_credits}    SPI: {zz}    CPI: {az}")








                col_width = 'even'
                if(xll==3):
                    z11[0].set_x(9.8)
                elif(xll==2):
                    z11[0].set_x(140.9)
                elif(xll==1):
                    z11[0].set_x(280)
                widths_col=[20.0,55.0,15.0,15.0,15.0]
                x_start=z11[0].get_x()
                line_height=4
                y1=z11[0].get_y()
                x_left=z11[0].get_x()
                data=lo
                align_header='L'

                for i in range(len(header)):
                            datum = header[i]
                            z11[0].set_font("times",'B',7)
                            z11[0].multi_cell(widths_col[i], line_height, datum, border=1, align="C", ln=3, max_line_height=z11[0].font_size)
                            x_right = z11[0].get_x()
                z11[0].ln(line_height)
                y2 = z11[0].get_y()
                z11[0].line(x_left,y1,x_right,y1)
                z11[0].line(x_left,y2,x_right,y2)
                for i in range(len(data)):
                
                    if(xll==3):
                        z11[0].set_x(9.8)
                    elif(xll==2):
                        z11[0].set_x(140.9)
                    elif(xll==1):
                        z11[0].set_x(280)
                    row = data[i]
                    for i in range(0,len(row)):
                        datum = row[i]
                        z11[0].set_font("times",'',7)
                        z11[0].multi_cell(widths_col[i], line_height, datum, border=1, align="C", ln=3, max_line_height=z11[0].font_size)
                    z11[0].ln(line_height)
                    y3 = z11[0].get_y()
                    z11[0].line(x_left,y3,x_right,y3)
                os.remove(f"./templates/output/{loge[0]+lst111[0]}.csv")
                lst111.pop(0)
                xll-=1





            xll=3
            while(xll>0):
                if len(lst111) >0 and len(loge)>0:
                    if( not os.path.exists(f"./templates/output/{loge[0]+(lst111[0])}.csv")):
                        pra=False
                        break
                else:
                    break
                lo=[]
                z11[0].set_x(30)
                z11[0].set_y(120)
                header=['Subject No' , 'Subject Name' , 'L-T-P' , 'Credit' , 'Grade']
                with open(f"./templates/output/{loge[0] + lst111[0]}.csv" , "r") as f:
                    o= csv.reader(f)
                    current_sem_credits=0
                    luxxy1=0
                    for x in o:
                        lo.append(x)
                        credits_total+=int(x[3])
                        current_sem_credits+=int(x[3])
                        luxxy1+=(int(x[3])*Grades_map[x[4]])
                    luxxy1/=current_sem_credits
                    zz=round(luxxy1,2)
                    luxxy+=(luxxy1*current_sem_credits)

                    zuxxy=luxxy/credits_total
                    az=round(zuxxy,2)
                    z11[0].set_font("times","B",10)
                    if xll==3:

                        z11[0].cell(4,90,f"Credits taken:{current_sem_credits}     Credits cleared: {current_sem_credits}    SPI: {zz}    CPI: {az}")
                    elif xll==2:
                        z11[0].cell(132)
                        z11[0].cell(20,90,f"Credits taken:{current_sem_credits}     Credits cleared: {current_sem_credits}    SPI: {zz}    CPI: {az}")
                    elif xll==1:
                        z11[0].cell(272)
                        z11[0].cell(20,90,f"Credits taken:{current_sem_credits}     Credits cleared: {current_sem_credits}    SPI: {zz}    CPI: {az}")
                col_width = 'even'
                z11[0].set_font("times","B",10)
                if(len(im_dict[loge[0]])>0 and xll==3):
                    z11[0].cell(-4)
                    z11[0].rect(10,161,100,7)
                    z11[0].cell(9.8,-5,f"semester {im_dict[loge[0]][0]}")
                    im_dict[loge[0]].pop(0)
                elif ( len(im_dict[loge[0]])>0 and xll==2):
                    z11[0].cell(-20)
                    z11[0].rect(141,161,100,7)
                    z11[0].cell(140.9,-5,f"semester {im_dict[loge[0]][0]}")
                    im_dict[loge[0]].pop(0)
                elif( len(im_dict[loge[0]]) >0 and xll==1):
                    z11[0].cell(-23)
                    z11[0].rect(280,161,100,7)
                    z11[0].cell(340,-5,f"semester {im_dict[loge[0]][0]}")
                    im_dict[loge[0]].pop(0)



                if(xll==3):
                    z11[0].set_x(9.8)
                elif(xll==2):
                    z11[0].set_x(140.9)
                elif(xll==1):
                    z11[0].set_x(280)
                widths_col=[20.0,55.0,15.0,15.0,15.0]
                x_start=z11[0].get_x()
                line_height=4
                y1=z11[0].get_y()
                x_left=z11[0].get_x()
                data=lo
                align_header='C'
                for i in range(len(header)):
                            datum = header[i]
                            z11[0].set_font("times",'B',7)
                            z11[0].multi_cell(widths_col[i], line_height, datum, border=1, align="C", ln=3, max_line_height=z11[0].font_size)
                            x_right = z11[0].get_x()
                z11[0].ln(line_height)
                y2 = z11[0].get_y()
                z11[0].line(x_left,y1,x_right,y1)
                z11[0].line(x_left,y2,x_right,y2)
                for i in range(len(data)):
                
                    if(xll==3):
                        z11[0].set_x(9.8)
                    elif(xll==2):
                        z11[0].set_x(140.9)
                    elif(xll==1):
                        z11[0].set_x(280)
                    row = data[i]
                    for i in range(0,len(row)):
                        datum = row[i]
                        z11[0].set_font("times",'',7)
                        z11[0].multi_cell(widths_col[i], line_height, datum, border=1, align="C", ln=3, max_line_height=z11[0].font_size)
                    z11[0].ln(line_height)
                    y3 = z11[0].get_y()
                    z11[0].line(x_left,y3,x_right,y3)
                os.remove(f"./templates/output/{loge[0]+lst111[0]}.csv")
                lst111.pop(0)
                xll-=1




            x12=2
            while(x12>0):
                if len(lst111) >0 and len(loge)>0:
                    if( not os.path.exists(f"./templates/output/{loge[0]+(lst111[0])}.csv")):
                        pra=False
                        break
                    else:
                        pass
                elif len(lst111)==0 or len(loge)==0:
                    break
                else:
                    pass
                lo=[]
                z11[0].set_x(30)
                z11[0].set_y(180)
                header=['Subject No' , 'Subject Name' , 'L-T-P' , 'Credit' , 'Grade']
                with open(f"./templates/output/{loge[0] + lst111[0]}.csv" , "r") as f:

                    o= csv.reader(f)
                    current_sem_credits=0
                    luxxy1=0
                    for x in o:
                        lo.append(x)
                        credits_total+=int(x[3])
                        current_sem_credits+=int(x[3])
                        luxxy1+=(int(x[3])*Grades_map[x[4].strip()])
                    luxxy1/=current_sem_credits
                    zz=round(luxxy1,2)
                    luxxy+=(luxxy1*current_sem_credits)

                    zuxxy=luxxy/credits_total
                    az=round(zuxxy,2)
                    z11[0].set_font("times","B",10)
                    if x12==2:

                        z11[0].cell(4,90,f"Credits taken:{current_sem_credits}     Credits cleared: {current_sem_credits}    SPI: {zz}    CPI: {az}")
                    elif x12==1:
                        z11[0].cell(132)
                        z11[0].cell(20,90,f"Credits taken:{current_sem_credits}     Credits cleared: {current_sem_credits}    SPI: {zz}    CPI: {az}")
                col_width = 'even'
                z11[0].set_font("times","B",10)
                if(len(im_dict[loge[0]])>0 and x12==2):
                        z11[0].cell(-4)
                        z11[0].rect(10,221.5,100,7)
                        z11[0].cell(9.8,-5,f"semester {im_dict[loge[0]][0]}")
                        im_dict[loge[0]].pop(0)
                elif ( len(im_dict[loge[0]])>0 and x12==1):
                        z11[0].cell(130)
                        z11[0].rect(141,221.5,100,7)
                        z11[0].cell(-150)
                        z11[0].cell(100.9,-5,f"semester {im_dict[loge[0]][0]}")
                        im_dict[loge[0]].pop(0)
                if(x12==2):
                    z11[0].set_x(9.8)
                elif(x12==1):
                    z11[0].set_x(140.9)
                widths_col=[20.0,55.0,15.0,15.0,15.0]
                x_start=z11[0].get_x()
                line_height=4
                y1=z11[0].get_y()
                x_left=z11[0].get_x()
                data=lo
                align_header='L'
                for i in range(len(header)):
                            datum = header[i]
                            z11[0].set_font("times",'B',7)
                            z11[0].multi_cell(widths_col[i], line_height, datum, border=1, align="C", ln=3, max_line_height=z11[0].font_size)
                            x_right = z11[0].get_x()
                z11[0].ln(line_height)
                y2 = z11[0].get_y()
                z11[0].line(x_left,y1,x_right,y1)
                z11[0].line(x_left,y2,x_right,y2)
                for i in range(len(data)):
                
                    if(x12==2):
                        z11[0].set_x(9.8)
                    elif(x12==1):
                        z11[0].set_x(140.9)
                    row = data[i]
                    for i in range(0,len(row)):
                        datum = row[i]
                        z11[0].set_font("times",'',7)
                        z11[0].multi_cell(widths_col[i], line_height, datum, border=1, align="C", ln=3, max_line_height=z11[0].font_size)
                    z11[0].ln(line_height)
                    y3 = z11[0].get_y()
                    z11[0].line(x_left,y3,x_right,y3)
                os.remove(f"./templates/output/{loge[0]+lst111[0]}.csv")
                lst111.pop(0)
                x12-=1


            if loge[0]==BRAND:
                hh=loge[0]
                z11[0].set_y(-30)
                z11[0].cell(300)
                z11[0].set_font('times','',15)
                z11[0].cell(200,10,"Assistant Registar" , ln=0)
                z11[0].cell(-500)
                z11[0].cell(20,10,"Date of issue:")
                z11[0].cell(150)
                z11[0].cell(20,10,'stamp')
                z11[0].image(f"./storage1/{zz[0]}",178,250,18,18 , title='transcript')
                z11[0].image(f"./storage2/{zy[0]}",328,250,18,18 , title='transc]]ript')
                z11[0].cell(-158)
                z11[0].cell(200,10, prasanth)
                z11[0].output(f"./generated/{hh}.pdf")



            if(len(lst111)==0):
                l= False
                break

            if( not os.path.exists(f"./templates/output/{loge[0]+lst111[0]}.csv")):
                hh=loge[0]
                z11[0].set_y(-30)
                z11[0].cell(300)
                z11[0].set_font('times','',15)
                z11[0].cell(200,10,"Assistant Registar" , ln=0)
                z11[0].cell(-500)
                z11[0].cell(20,10,"Date of issue:")
                z11[0].cell(150)
                z11[0].cell(20,10,'stamp')
                z11[0].image(f"./files1/{zz[0]}",178,250,18,18 , title='transcript')
                z11[0].image(f"./files2/{zy[0]}",328,250,18,18 , title='transc]]ript')
                z11[0].cell(-158)
                z11[0].cell(200,10, prasanth)
                z11[0].output(f"./generated/{hh}.pdf")
                loge.pop(0)
                break
        name.pop(0)
        if l == False:
            break
    while(len(range_2)>0):
        flash(f"{range_2[0]}" )
        range_2.pop(0)
    return render_template("index.html" )
