from django.http import HttpResponse
from django.shortcuts import render
from graduate.models import Student1


def index(request):
    all_Std = Student1.objects.all()
    return render(request,"index.html",{"all_Std":all_Std})

def chart(request):
    j1 = Student1.objects.filter(Publish_type='การประชุมวิชาการระดับชาติ').count()
    j1 = int(j1)
    print('จำนวนของประเภทการประชุมวิชาการระดับชาติเท่ากับ ',j1)

    j2 = Student1.objects.filter(Publish_type='การประชุมวิชาการระดับนานาชาติ').count()
    j2 = int(j2)
    print('Number of Computer Engineering Student1 Are',j2)

    j3 = Student1.objects.filter(Publish_type='ตีพิมพ์ลักษณะใดลักษณะหนึ่ง').count()
    j3 = int(j3)
    print('Number of Software Engineering Student1 Are',j3)

    j4 = Student1.objects.filter(Journal_db='ฐานข้อมูลระดับนานาชาติอื่น').count()
    j4 = int(j4)
    print('Number of Computer Security Student1 Are',j4)

    j5 = Student1.objects.filter(Journal_db='TCI กลุ่ม 1').count()
    j5 = int(j5)
    print('Number of Computer Security Student1 Are',j5)

    j6 = Student1.objects.filter(Journal_db='Scopus').count()
    j6 = int(j6)
    print('Number of Computer Security Student1 Are',j6)

    j7 = Student1.objects.filter(Journal_db='WoS').count()
    j7 = int(j7)
    print('Number of Computer Security Student1 Are',j7)

    j8 = Student1.objects.filter(Journal_db='TCI กลุ่ม 2').count()
    j8 = int(j8)
    print('Number of Computer Security Student1 Are',j8)

    j9 = Student1.objects.filter(Journal_db='SSRN').count()
    j9 = int(j9)
    print('Number of Computer Security Student1 Are',j9)

    j10 = Student1.objects.filter(Journal_db='EBSCO').count()
    j10 = int(j10)
    print('Number of Computer Security Student1 Are',j10)

    j11 = Student1.objects.filter(Journal_db='ไม่อยู่ในฐานข้อมูล').count()
    j11 = int(j11)
    print('Number of Computer Security Student1 Are',j11)

    y2555 = Student1.objects.filter(Cal_year=2555).count()
    y2555 = int(y2555)
    print('จำนวนปี 2555 มีจำนวน ',y2555)

    y2556 = Student1.objects.filter(Cal_year=2556).count()
    y2556 = int(y2556)
    print('จำนวนปี 2555 มีจำนวน ',y2556)

    y2557 = Student1.objects.filter(Cal_year=2557).count()
    y2557 = int(y2557)
    print('จำนวนปี 2555 มีจำนวน ',y2557)

    y2558 = Student1.objects.filter(Cal_year=2558).count()
    y2558 = int(y2558)
    print('จำนวนปี 2555 มีจำนวน ',y2558)

    y2559 = Student1.objects.filter(Cal_year=2559).count()
    y2559 = int(y2559)
    print('จำนวนปี 2555 มีจำนวน ',y2559)

    y2560 = Student1.objects.filter(Cal_year=2560).count()
    y2560 = int(y2560)
    print('จำนวนปี 2555 มีจำนวน ',y2560)

    y2561 = Student1.objects.filter(Cal_year=2561).count()
    y2561 = int(y2561)
    print('จำนวนปี 2555 มีจำนวน ',y2561)

    y2562 = Student1.objects.filter(Cal_year=2562).count()
    y2562 = int(y2562)
    print('จำนวนปี 2555 มีจำนวน ',y2562)

    y2563 = Student1.objects.filter(Cal_year=2563).count()
    y2563 = int(y2563)
    print('จำนวนปี 2555 มีจำนวน ',y2563)

    y2564 = Student1.objects.filter(Cal_year=2564).count()
    y2564 = int(y2564)
    print('จำนวนปี 2555 มีจำนวน ',y2564)

    Cal_year_list = [2555,2556,2557,2558,2559,2560,2561,2562,2563,2564]
    Cal_year_number = [y2555,y2556,y2557,y2558,y2559,y2560,y2561,y2562,y2563,y2564]
    jlist = [1,2,3,4,5,6,7,8,9,10]
    course_list = ['การประชุมวิชาการระดับชาติ', 'การประชุมวิชาการระดับนานาชาติ', 'ตีพิมพ์ลักษณะใดลักษณะหนึ่ง', 'ฐานข้อมูลระดับนานาชาติอื่น',
                   'TCI กลุ่ม 1','Scopus','WoS','TCI กลุ่ม 2','SSRN','EBSCO','ไม่อยู่ในฐานข้อมูล']
    number_list = [j1, j2, j3,j4,j5,j6,j7,j8,j9,j10,j11]
    context = {'course_list':course_list, 'number_list':number_list
               , 'Cal_year_list':Cal_year_list, 'Cal_year_number':Cal_year_number,'jlist':jlist}
    return render(request,'chart.html',context)

def chartbar2(request):
    j1 = Student1.objects.filter(Publish_type='การประชุมวิชาการระดับชาติ').count()
    j1 = int(j1)
    print('จำนวนของประเภทการประชุมวิชาการระดับชาติเท่ากับ ',j1)

    j2 = Student1.objects.filter(Publish_type='การประชุมวิชาการระดับนานาชาติ').count()
    j2 = int(j2)
    print('Number of Computer Engineering Student1 Are',j2)

    j3 = Student1.objects.filter(Publish_type='ตีพิมพ์ลักษณะใดลักษณะหนึ่ง').count()
    j3 = int(j3)
    print('Number of Software Engineering Student1 Are',j3)

    j4 = Student1.objects.filter(Journal_db='ฐานข้อมูลระดับนานาชาติอื่น').count()
    j4 = int(j4)
    print('Number of Computer Security Student1 Are',j4)

    j5 = Student1.objects.filter(Journal_db='TCI กลุ่ม 1').count()
    j5 = int(j5)
    print('Number of Computer Security Student1 Are',j5)

    j6 = Student1.objects.filter(Journal_db='Scopus').count()
    j6 = int(j6)
    print('Number of Computer Security Student1 Are',j6)

    j7 = Student1.objects.filter(Journal_db='WoS').count()
    j7 = int(j7)
    print('Number of Computer Security Student1 Are',j7)

    j8 = Student1.objects.filter(Journal_db='TCI กลุ่ม 2').count()
    j8 = int(j8)
    print('Number of Computer Security Student1 Are',j8)

    j9 = Student1.objects.filter(Journal_db='SSRN').count()
    j9 = int(j9)
    print('Number of Computer Security Student1 Are',j9)

    j10 = Student1.objects.filter(Journal_db='EBSCO').count()
    j10 = int(j10)
    print('Number of Computer Security Student1 Are',j10)

    j11 = Student1.objects.filter(Journal_db='ไม่อยู่ในฐานข้อมูล').count()
    j11 = int(j11)
    print('Number of Computer Security Student1 Are',j11)

    y2555 = Student1.objects.filter(Cal_year=2555).count()
    y2555 = int(y2555)
    print('จำนวนปี 2555 มีจำนวน ',y2555)

    y2556 = Student1.objects.filter(Cal_year=2556).count()
    y2556 = int(y2556)
    print('จำนวนปี 2555 มีจำนวน ',y2556)

    y2557 = Student1.objects.filter(Cal_year=2557).count()
    y2557 = int(y2557)
    print('จำนวนปี 2555 มีจำนวน ',y2557)

    y2558 = Student1.objects.filter(Cal_year=2558).count()
    y2558 = int(y2558)
    print('จำนวนปี 2555 มีจำนวน ',y2558)

    y2559 = Student1.objects.filter(Cal_year=2559).count()
    y2559 = int(y2559)
    print('จำนวนปี 2555 มีจำนวน ',y2559)

    y2560 = Student1.objects.filter(Cal_year=2560).count()
    y2560 = int(y2560)
    print('จำนวนปี 2555 มีจำนวน ',y2560)

    y2561 = Student1.objects.filter(Cal_year=2561).count()
    y2561 = int(y2561)
    print('จำนวนปี 2555 มีจำนวน ',y2561)

    y2562 = Student1.objects.filter(Cal_year=2562).count()
    y2562 = int(y2562)
    print('จำนวนปี 2555 มีจำนวน ',y2562)

    y2563 = Student1.objects.filter(Cal_year=2563).count()
    y2563 = int(y2563)
    print('จำนวนปี 2555 มีจำนวน ',y2563)

    y2564 = Student1.objects.filter(Cal_year=2564).count()
    y2564 = int(y2564)
    print('จำนวนปี 2555 มีจำนวน ',y2564)

    Cal_year_list = [2555,2556,2557,2558,2559,2560,2561,2562,2563,2564]
    Cal_year_number = [y2555,y2556,y2557,y2558,y2559,y2560,y2561,y2562,y2563,y2564]
    jlist = [1,2,3,4,5,6,7,8,9,10]
    course_list = ['การประชุมวิชาการระดับชาติ', 'การประชุมวิชาการระดับนานาชาติ', 'ตีพิมพ์ลักษณะใดลักษณะหนึ่ง', 'ฐานข้อมูลระดับนานาชาติอื่น',
                   'TCI กลุ่ม 1','Scopus','WoS','TCI กลุ่ม 2','SSRN','EBSCO','ไม่อยู่ในฐานข้อมูล']
    number_list = [j1, j2, j3,j4,j5,j6,j7,j8,j9,j10,j11]
    context = {'course_list':course_list, 'number_list':number_list
               , 'Cal_year_list':Cal_year_list, 'Cal_year_number':Cal_year_number,'jlist':jlist}
    return render(request,'chartbar2.html',context)

def chartdo1(request):
    j1 = Student1.objects.filter(Publish_type='การประชุมวิชาการระดับชาติ').count()
    j1 = int(j1)
    print('จำนวนของประเภทการประชุมวิชาการระดับชาติเท่ากับ ',j1)

    j2 = Student1.objects.filter(Publish_type='การประชุมวิชาการระดับนานาชาติ').count()
    j2 = int(j2)
    print('Number of Computer Engineering Student1 Are',j2)

    j3 = Student1.objects.filter(Publish_type='ตีพิมพ์ลักษณะใดลักษณะหนึ่ง').count()
    j3 = int(j3)
    print('Number of Software Engineering Student1 Are',j3)

    j4 = Student1.objects.filter(Journal_db='ฐานข้อมูลระดับนานาชาติอื่น').count()
    j4 = int(j4)
    print('Number of Computer Security Student1 Are',j4)

    j5 = Student1.objects.filter(Journal_db='TCI กลุ่ม 1').count()
    j5 = int(j5)
    print('Number of Computer Security Student1 Are',j5)

    j6 = Student1.objects.filter(Journal_db='Scopus').count()
    j6 = int(j6)
    print('Number of Computer Security Student1 Are',j6)

    j7 = Student1.objects.filter(Journal_db='WoS').count()
    j7 = int(j7)
    print('Number of Computer Security Student1 Are',j7)

    j8 = Student1.objects.filter(Journal_db='TCI กลุ่ม 2').count()
    j8 = int(j8)
    print('Number of Computer Security Student1 Are',j8)

    j9 = Student1.objects.filter(Journal_db='SSRN').count()
    j9 = int(j9)
    print('Number of Computer Security Student1 Are',j9)

    j10 = Student1.objects.filter(Journal_db='EBSCO').count()
    j10 = int(j10)
    print('Number of Computer Security Student1 Are',j10)

    j11 = Student1.objects.filter(Journal_db='ไม่อยู่ในฐานข้อมูล').count()
    j11 = int(j11)
    print('Number of Computer Security Student1 Are',j11)

    y2555 = Student1.objects.filter(Cal_year=2555).count()
    y2555 = int(y2555)
    print('จำนวนปี 2555 มีจำนวน ',y2555)

    y2556 = Student1.objects.filter(Cal_year=2556).count()
    y2556 = int(y2556)
    print('จำนวนปี 2555 มีจำนวน ',y2556)

    y2557 = Student1.objects.filter(Cal_year=2557).count()
    y2557 = int(y2557)
    print('จำนวนปี 2555 มีจำนวน ',y2557)

    y2558 = Student1.objects.filter(Cal_year=2558).count()
    y2558 = int(y2558)
    print('จำนวนปี 2555 มีจำนวน ',y2558)

    y2559 = Student1.objects.filter(Cal_year=2559).count()
    y2559 = int(y2559)
    print('จำนวนปี 2555 มีจำนวน ',y2559)

    y2560 = Student1.objects.filter(Cal_year=2560).count()
    y2560 = int(y2560)
    print('จำนวนปี 2555 มีจำนวน ',y2560)

    y2561 = Student1.objects.filter(Cal_year=2561).count()
    y2561 = int(y2561)
    print('จำนวนปี 2555 มีจำนวน ',y2561)

    y2562 = Student1.objects.filter(Cal_year=2562).count()
    y2562 = int(y2562)
    print('จำนวนปี 2555 มีจำนวน ',y2562)

    y2563 = Student1.objects.filter(Cal_year=2563).count()
    y2563 = int(y2563)
    print('จำนวนปี 2555 มีจำนวน ',y2563)

    y2564 = Student1.objects.filter(Cal_year=2564).count()
    y2564 = int(y2564)
    print('จำนวนปี 2555 มีจำนวน ',y2564)

    Cal_year_list = [2555,2556,2557,2558,2559,2560,2561,2562,2563,2564]
    Cal_year_number = [y2555,y2556,y2557,y2558,y2559,y2560,y2561,y2562,y2563,y2564]
    jlist = [1,2,3,4,5,6,7,8,9,10]
    course_list = ['การประชุมวิชาการระดับชาติ', 'การประชุมวิชาการระดับนานาชาติ', 'ตีพิมพ์ลักษณะใดลักษณะหนึ่ง', 'วารสาร ฐานข้อมูลระดับนานาชาติอื่น',
                   'วารสาร TCI กลุ่ม 1','วารสาร Scopus','วารสาร WoS','วารสาร TCI กลุ่ม 2','วารสาร SSRN','วารสาร EBSCO','วารสาร ไม่อยู่ในฐานข้อมูล']
    number_list = [j1, j2, j3,j4,j5,j6,j7,j8,j9,j10,j11]
    context = {'course_list':course_list, 'number_list':number_list
               , 'Cal_year_list':Cal_year_list, 'Cal_year_number':Cal_year_number,'jlist':jlist}
    return render(request,'chartdo1.html',context)

def chartdo2(request):
    j1 = Student1.objects.filter(Publish_type='การประชุมวิชาการระดับชาติ').count()
    j1 = int(j1)
    print('จำนวนของประเภทการประชุมวิชาการระดับชาติเท่ากับ ',j1)

    j2 = Student1.objects.filter(Publish_type='การประชุมวิชาการระดับนานาชาติ').count()
    j2 = int(j2)
    print('Number of Computer Engineering Student1 Are',j2)

    j3 = Student1.objects.filter(Publish_type='ตีพิมพ์ลักษณะใดลักษณะหนึ่ง').count()
    j3 = int(j3)
    print('Number of Software Engineering Student1 Are',j3)

    j4 = Student1.objects.filter(Journal_db='ฐานข้อมูลระดับนานาชาติอื่น').count()
    j4 = int(j4)
    print('Number of Computer Security Student1 Are',j4)

    j5 = Student1.objects.filter(Journal_db='TCI กลุ่ม 1').count()
    j5 = int(j5)
    print('Number of Computer Security Student1 Are',j5)

    j6 = Student1.objects.filter(Journal_db='Scopus').count()
    j6 = int(j6)
    print('Number of Computer Security Student1 Are',j6)

    j7 = Student1.objects.filter(Journal_db='WoS').count()
    j7 = int(j7)
    print('Number of Computer Security Student1 Are',j7)

    j8 = Student1.objects.filter(Journal_db='TCI กลุ่ม 2').count()
    j8 = int(j8)
    print('Number of Computer Security Student1 Are',j8)

    j9 = Student1.objects.filter(Journal_db='SSRN').count()
    j9 = int(j9)
    print('Number of Computer Security Student1 Are',j9)

    j10 = Student1.objects.filter(Journal_db='EBSCO').count()
    j10 = int(j10)
    print('Number of Computer Security Student1 Are',j10)

    j11 = Student1.objects.filter(Journal_db='ไม่อยู่ในฐานข้อมูล').count()
    j11 = int(j11)
    print('Number of Computer Security Student1 Are',j11)

    y2555 = Student1.objects.filter(Cal_year=2555).count()
    y2555 = int(y2555)
    print('จำนวนปี 2555 มีจำนวน ',y2555)

    y2556 = Student1.objects.filter(Cal_year=2556).count()
    y2556 = int(y2556)
    print('จำนวนปี 2555 มีจำนวน ',y2556)

    y2557 = Student1.objects.filter(Cal_year=2557).count()
    y2557 = int(y2557)
    print('จำนวนปี 2555 มีจำนวน ',y2557)

    y2558 = Student1.objects.filter(Cal_year=2558).count()
    y2558 = int(y2558)
    print('จำนวนปี 2555 มีจำนวน ',y2558)

    y2559 = Student1.objects.filter(Cal_year=2559).count()
    y2559 = int(y2559)
    print('จำนวนปี 2555 มีจำนวน ',y2559)

    y2560 = Student1.objects.filter(Cal_year=2560).count()
    y2560 = int(y2560)
    print('จำนวนปี 2555 มีจำนวน ',y2560)

    y2561 = Student1.objects.filter(Cal_year=2561).count()
    y2561 = int(y2561)
    print('จำนวนปี 2555 มีจำนวน ',y2561)

    y2562 = Student1.objects.filter(Cal_year=2562).count()
    y2562 = int(y2562)
    print('จำนวนปี 2555 มีจำนวน ',y2562)

    y2563 = Student1.objects.filter(Cal_year=2563).count()
    y2563 = int(y2563)
    print('จำนวนปี 2555 มีจำนวน ',y2563)

    y2564 = Student1.objects.filter(Cal_year=2564).count()
    y2564 = int(y2564)
    print('จำนวนปี 2555 มีจำนวน ',y2564)

    Cal_year_list = [2555,2556,2557,2558,2559,2560,2561,2562,2563,2564]
    Cal_year_number = [y2555,y2556,y2557,y2558,y2559,y2560,y2561,y2562,y2563,y2564]
    jlist = [1,2,3,4,5,6,7,8,9,10]
    course_list = ['การประชุมวิชาการระดับชาติ', 'การประชุมวิชาการระดับนานาชาติ', 'ตีพิมพ์ลักษณะใดลักษณะหนึ่ง', 'ฐานข้อมูลระดับนานาชาติอื่น',
                   'TCI กลุ่ม 1','Scopus','WoS','TCI กลุ่ม 2','SSRN','EBSCO','ไม่อยู่ในฐานข้อมูล']
    number_list = [j1, j2, j3,j4,j5,j6,j7,j8,j9,j10,j11]
    context = {'course_list':course_list, 'number_list':number_list
               , 'Cal_year_list':Cal_year_list, 'Cal_year_number':Cal_year_number,'jlist':jlist}
    return render(request,'chartdo2.html',context)

def chartpo1(request):
    j1 = Student1.objects.filter(Publish_type='การประชุมวิชาการระดับชาติ').count()
    j1 = int(j1)
    print('จำนวนของประเภทการประชุมวิชาการระดับชาติเท่ากับ ',j1)

    j2 = Student1.objects.filter(Publish_type='การประชุมวิชาการระดับนานาชาติ').count()
    j2 = int(j2)
    print('Number of Computer Engineering Student1 Are',j2)

    j3 = Student1.objects.filter(Publish_type='ตีพิมพ์ลักษณะใดลักษณะหนึ่ง').count()
    j3 = int(j3)
    print('Number of Software Engineering Student1 Are',j3)

    j4 = Student1.objects.filter(Journal_db='ฐานข้อมูลระดับนานาชาติอื่น').count()
    j4 = int(j4)
    print('Number of Computer Security Student1 Are',j4)

    j5 = Student1.objects.filter(Journal_db='TCI กลุ่ม 1').count()
    j5 = int(j5)
    print('Number of Computer Security Student1 Are',j5)

    j6 = Student1.objects.filter(Journal_db='Scopus').count()
    j6 = int(j6)
    print('Number of Computer Security Student1 Are',j6)

    j7 = Student1.objects.filter(Journal_db='WoS').count()
    j7 = int(j7)
    print('Number of Computer Security Student1 Are',j7)

    j8 = Student1.objects.filter(Journal_db='TCI กลุ่ม 2').count()
    j8 = int(j8)
    print('Number of Computer Security Student1 Are',j8)

    j9 = Student1.objects.filter(Journal_db='SSRN').count()
    j9 = int(j9)
    print('Number of Computer Security Student1 Are',j9)

    j10 = Student1.objects.filter(Journal_db='EBSCO').count()
    j10 = int(j10)
    print('Number of Computer Security Student1 Are',j10)

    j11 = Student1.objects.filter(Journal_db='ไม่อยู่ในฐานข้อมูล').count()
    j11 = int(j11)
    print('Number of Computer Security Student1 Are',j11)

    y2555 = Student1.objects.filter(Cal_year=2555).count()
    y2555 = int(y2555)
    print('จำนวนปี 2555 มีจำนวน ',y2555)

    y2556 = Student1.objects.filter(Cal_year=2556).count()
    y2556 = int(y2556)
    print('จำนวนปี 2555 มีจำนวน ',y2556)

    y2557 = Student1.objects.filter(Cal_year=2557).count()
    y2557 = int(y2557)
    print('จำนวนปี 2555 มีจำนวน ',y2557)

    y2558 = Student1.objects.filter(Cal_year=2558).count()
    y2558 = int(y2558)
    print('จำนวนปี 2555 มีจำนวน ',y2558)

    y2559 = Student1.objects.filter(Cal_year=2559).count()
    y2559 = int(y2559)
    print('จำนวนปี 2555 มีจำนวน ',y2559)

    y2560 = Student1.objects.filter(Cal_year=2560).count()
    y2560 = int(y2560)
    print('จำนวนปี 2555 มีจำนวน ',y2560)

    y2561 = Student1.objects.filter(Cal_year=2561).count()
    y2561 = int(y2561)
    print('จำนวนปี 2555 มีจำนวน ',y2561)

    y2562 = Student1.objects.filter(Cal_year=2562).count()
    y2562 = int(y2562)
    print('จำนวนปี 2555 มีจำนวน ',y2562)

    y2563 = Student1.objects.filter(Cal_year=2563).count()
    y2563 = int(y2563)
    print('จำนวนปี 2555 มีจำนวน ',y2563)

    y2564 = Student1.objects.filter(Cal_year=2564).count()
    y2564 = int(y2564)
    print('จำนวนปี 2555 มีจำนวน ',y2564)

    Cal_year_list = [2555,2556,2557,2558,2559,2560,2561,2562,2563,2564]
    Cal_year_number = [y2555,y2556,y2557,y2558,y2559,y2560,y2561,y2562,y2563,y2564]
    jlist = [1,2,3,4,5,6,7,8,9,10]
    course_list = ['การประชุมวิชาการระดับชาติ', 'การประชุมวิชาการระดับนานาชาติ', 'ตีพิมพ์ลักษณะใดลักษณะหนึ่ง', 'ฐานข้อมูลระดับนานาชาติอื่น',
                   'TCI กลุ่ม 1','Scopus','WoS','TCI กลุ่ม 2','SSRN','EBSCO','ไม่อยู่ในฐานข้อมูล']
    number_list = [j1, j2, j3,j4,j5,j6,j7,j8,j9,j10,j11]
    context = {'course_list':course_list, 'number_list':number_list
               , 'Cal_year_list':Cal_year_list, 'Cal_year_number':Cal_year_number,'jlist':jlist}
    return render(request,'chartpo1.html',context)

def chartpo2(request):
    j1 = Student1.objects.filter(Publish_type='การประชุมวิชาการระดับชาติ').count()
    j1 = int(j1)
    print('จำนวนของประเภทการประชุมวิชาการระดับชาติเท่ากับ ',j1)

    j2 = Student1.objects.filter(Publish_type='การประชุมวิชาการระดับนานาชาติ').count()
    j2 = int(j2)
    print('Number of Computer Engineering Student1 Are',j2)

    j3 = Student1.objects.filter(Publish_type='ตีพิมพ์ลักษณะใดลักษณะหนึ่ง').count()
    j3 = int(j3)
    print('Number of Software Engineering Student1 Are',j3)

    j4 = Student1.objects.filter(Journal_db='ฐานข้อมูลระดับนานาชาติอื่น').count()
    j4 = int(j4)
    print('Number of Computer Security Student1 Are',j4)

    j5 = Student1.objects.filter(Journal_db='TCI กลุ่ม 1').count()
    j5 = int(j5)
    print('Number of Computer Security Student1 Are',j5)

    j6 = Student1.objects.filter(Journal_db='Scopus').count()
    j6 = int(j6)
    print('Number of Computer Security Student1 Are',j6)

    j7 = Student1.objects.filter(Journal_db='WoS').count()
    j7 = int(j7)
    print('Number of Computer Security Student1 Are',j7)

    j8 = Student1.objects.filter(Journal_db='TCI กลุ่ม 2').count()
    j8 = int(j8)
    print('Number of Computer Security Student1 Are',j8)

    j9 = Student1.objects.filter(Journal_db='SSRN').count()
    j9 = int(j9)
    print('Number of Computer Security Student1 Are',j9)

    j10 = Student1.objects.filter(Journal_db='EBSCO').count()
    j10 = int(j10)
    print('Number of Computer Security Student1 Are',j10)

    j11 = Student1.objects.filter(Journal_db='ไม่อยู่ในฐานข้อมูล').count()
    j11 = int(j11)
    print('Number of Computer Security Student1 Are',j11)

    y2555 = Student1.objects.filter(Cal_year=2555).count()
    y2555 = int(y2555)
    print('จำนวนปี 2555 มีจำนวน ',y2555)

    y2556 = Student1.objects.filter(Cal_year=2556).count()
    y2556 = int(y2556)
    print('จำนวนปี 2555 มีจำนวน ',y2556)

    y2557 = Student1.objects.filter(Cal_year=2557).count()
    y2557 = int(y2557)
    print('จำนวนปี 2555 มีจำนวน ',y2557)

    y2558 = Student1.objects.filter(Cal_year=2558).count()
    y2558 = int(y2558)
    print('จำนวนปี 2555 มีจำนวน ',y2558)

    y2559 = Student1.objects.filter(Cal_year=2559).count()
    y2559 = int(y2559)
    print('จำนวนปี 2555 มีจำนวน ',y2559)

    y2560 = Student1.objects.filter(Cal_year=2560).count()
    y2560 = int(y2560)
    print('จำนวนปี 2555 มีจำนวน ',y2560)

    y2561 = Student1.objects.filter(Cal_year=2561).count()
    y2561 = int(y2561)
    print('จำนวนปี 2555 มีจำนวน ',y2561)

    y2562 = Student1.objects.filter(Cal_year=2562).count()
    y2562 = int(y2562)
    print('จำนวนปี 2555 มีจำนวน ',y2562)

    y2563 = Student1.objects.filter(Cal_year=2563).count()
    y2563 = int(y2563)
    print('จำนวนปี 2555 มีจำนวน ',y2563)

    y2564 = Student1.objects.filter(Cal_year=2564).count()
    y2564 = int(y2564)
    print('จำนวนปี 2555 มีจำนวน ',y2564)

    Cal_year_list = [2555,2556,2557,2558,2559,2560,2561,2562,2563,2564]
    Cal_year_number = [y2555,y2556,y2557,y2558,y2559,y2560,y2561,y2562,y2563,y2564]
    jlist = [1,2,3,4,5,6,7,8,9,10]
    course_list = ['การประชุมวิชาการระดับชาติ', 'การประชุมวิชาการระดับนานาชาติ', 'ตีพิมพ์ลักษณะใดลักษณะหนึ่ง', 'ฐานข้อมูลระดับนานาชาติอื่น',
                   'TCI กลุ่ม 1','Scopus','WoS','TCI กลุ่ม 2','SSRN','EBSCO','ไม่อยู่ในฐานข้อมูล']
    number_list = [j1, j2, j3,j4,j5,j6,j7,j8,j9,j10,j11]
    context = {'course_list':course_list, 'number_list':number_list
               , 'Cal_year_list':Cal_year_list, 'Cal_year_number':Cal_year_number,'jlist':jlist}
    return render(request,'chartpo2.html',context)

def chartra1(request):
    j1 = Student1.objects.filter(Publish_type='การประชุมวิชาการระดับชาติ').count()
    j1 = int(j1)
    print('จำนวนของประเภทการประชุมวิชาการระดับชาติเท่ากับ ',j1)

    j2 = Student1.objects.filter(Publish_type='การประชุมวิชาการระดับนานาชาติ').count()
    j2 = int(j2)
    print('Number of Computer Engineering Student1 Are',j2)

    j3 = Student1.objects.filter(Publish_type='ตีพิมพ์ลักษณะใดลักษณะหนึ่ง').count()
    j3 = int(j3)
    print('Number of Software Engineering Student1 Are',j3)

    j4 = Student1.objects.filter(Journal_db='ฐานข้อมูลระดับนานาชาติอื่น').count()
    j4 = int(j4)
    print('Number of Computer Security Student1 Are',j4)

    j5 = Student1.objects.filter(Journal_db='TCI กลุ่ม 1').count()
    j5 = int(j5)
    print('Number of Computer Security Student1 Are',j5)

    j6 = Student1.objects.filter(Journal_db='Scopus').count()
    j6 = int(j6)
    print('Number of Computer Security Student1 Are',j6)

    j7 = Student1.objects.filter(Journal_db='WoS').count()
    j7 = int(j7)
    print('Number of Computer Security Student1 Are',j7)

    j8 = Student1.objects.filter(Journal_db='TCI กลุ่ม 2').count()
    j8 = int(j8)
    print('Number of Computer Security Student1 Are',j8)

    j9 = Student1.objects.filter(Journal_db='SSRN').count()
    j9 = int(j9)
    print('Number of Computer Security Student1 Are',j9)

    j10 = Student1.objects.filter(Journal_db='EBSCO').count()
    j10 = int(j10)
    print('Number of Computer Security Student1 Are',j10)

    j11 = Student1.objects.filter(Journal_db='ไม่อยู่ในฐานข้อมูล').count()
    j11 = int(j11)
    print('Number of Computer Security Student1 Are',j11)

    y2555 = Student1.objects.filter(Cal_year=2555).count()
    y2555 = int(y2555)
    print('จำนวนปี 2555 มีจำนวน ',y2555)

    y2556 = Student1.objects.filter(Cal_year=2556).count()
    y2556 = int(y2556)
    print('จำนวนปี 2555 มีจำนวน ',y2556)

    y2557 = Student1.objects.filter(Cal_year=2557).count()
    y2557 = int(y2557)
    print('จำนวนปี 2555 มีจำนวน ',y2557)

    y2558 = Student1.objects.filter(Cal_year=2558).count()
    y2558 = int(y2558)
    print('จำนวนปี 2555 มีจำนวน ',y2558)

    y2559 = Student1.objects.filter(Cal_year=2559).count()
    y2559 = int(y2559)
    print('จำนวนปี 2555 มีจำนวน ',y2559)

    y2560 = Student1.objects.filter(Cal_year=2560).count()
    y2560 = int(y2560)
    print('จำนวนปี 2555 มีจำนวน ',y2560)

    y2561 = Student1.objects.filter(Cal_year=2561).count()
    y2561 = int(y2561)
    print('จำนวนปี 2555 มีจำนวน ',y2561)

    y2562 = Student1.objects.filter(Cal_year=2562).count()
    y2562 = int(y2562)
    print('จำนวนปี 2555 มีจำนวน ',y2562)

    y2563 = Student1.objects.filter(Cal_year=2563).count()
    y2563 = int(y2563)
    print('จำนวนปี 2555 มีจำนวน ',y2563)

    y2564 = Student1.objects.filter(Cal_year=2564).count()
    y2564 = int(y2564)
    print('จำนวนปี 2555 มีจำนวน ',y2564)

    Cal_year_list = [2555,2556,2557,2558,2559,2560,2561,2562,2563,2564]
    Cal_year_number = [y2555,y2556,y2557,y2558,y2559,y2560,y2561,y2562,y2563,y2564]
    jlist = [1,2,3,4,5,6,7,8,9,10]
    course_list = ['การประชุมวิชาการระดับชาติ', 'การประชุมวิชาการระดับนานาชาติ', 'ตีพิมพ์ลักษณะใดลักษณะหนึ่ง', 'ฐานข้อมูลระดับนานาชาติอื่น',
                   'TCI กลุ่ม 1','Scopus','WoS','TCI กลุ่ม 2','SSRN','EBSCO','ไม่อยู่ในฐานข้อมูล']
    number_list = [j1, j2, j3,j4,j5,j6,j7,j8,j9,j10,j11]
    context = {'course_list':course_list, 'number_list':number_list
               , 'Cal_year_list':Cal_year_list, 'Cal_year_number':Cal_year_number,'jlist':jlist}
    return render(request,'chartra1.html',context)

def chartra2(request):
    j1 = Student1.objects.filter(Publish_type='การประชุมวิชาการระดับชาติ').count()
    j1 = int(j1)
    print('จำนวนของประเภทการประชุมวิชาการระดับชาติเท่ากับ ',j1)

    j2 = Student1.objects.filter(Publish_type='การประชุมวิชาการระดับนานาชาติ').count()
    j2 = int(j2)
    print('Number of Computer Engineering Student1 Are',j2)

    j3 = Student1.objects.filter(Publish_type='ตีพิมพ์ลักษณะใดลักษณะหนึ่ง').count()
    j3 = int(j3)
    print('Number of Software Engineering Student1 Are',j3)

    j4 = Student1.objects.filter(Journal_db='ฐานข้อมูลระดับนานาชาติอื่น').count()
    j4 = int(j4)
    print('Number of Computer Security Student1 Are',j4)

    j5 = Student1.objects.filter(Journal_db='TCI กลุ่ม 1').count()
    j5 = int(j5)
    print('Number of Computer Security Student1 Are',j5)

    j6 = Student1.objects.filter(Journal_db='Scopus').count()
    j6 = int(j6)
    print('Number of Computer Security Student1 Are',j6)

    j7 = Student1.objects.filter(Journal_db='WoS').count()
    j7 = int(j7)
    print('Number of Computer Security Student1 Are',j7)

    j8 = Student1.objects.filter(Journal_db='TCI กลุ่ม 2').count()
    j8 = int(j8)
    print('Number of Computer Security Student1 Are',j8)

    j9 = Student1.objects.filter(Journal_db='SSRN').count()
    j9 = int(j9)
    print('Number of Computer Security Student1 Are',j9)

    j10 = Student1.objects.filter(Journal_db='EBSCO').count()
    j10 = int(j10)
    print('Number of Computer Security Student1 Are',j10)

    j11 = Student1.objects.filter(Journal_db='ไม่อยู่ในฐานข้อมูล').count()
    j11 = int(j11)
    print('Number of Computer Security Student1 Are',j11)

    y2555 = Student1.objects.filter(Cal_year=2555).count()
    y2555 = int(y2555)
    print('จำนวนปี 2555 มีจำนวน ',y2555)

    y2556 = Student1.objects.filter(Cal_year=2556).count()
    y2556 = int(y2556)
    print('จำนวนปี 2555 มีจำนวน ',y2556)

    y2557 = Student1.objects.filter(Cal_year=2557).count()
    y2557 = int(y2557)
    print('จำนวนปี 2555 มีจำนวน ',y2557)

    y2558 = Student1.objects.filter(Cal_year=2558).count()
    y2558 = int(y2558)
    print('จำนวนปี 2555 มีจำนวน ',y2558)

    y2559 = Student1.objects.filter(Cal_year=2559).count()
    y2559 = int(y2559)
    print('จำนวนปี 2555 มีจำนวน ',y2559)

    y2560 = Student1.objects.filter(Cal_year=2560).count()
    y2560 = int(y2560)
    print('จำนวนปี 2555 มีจำนวน ',y2560)

    y2561 = Student1.objects.filter(Cal_year=2561).count()
    y2561 = int(y2561)
    print('จำนวนปี 2555 มีจำนวน ',y2561)

    y2562 = Student1.objects.filter(Cal_year=2562).count()
    y2562 = int(y2562)
    print('จำนวนปี 2555 มีจำนวน ',y2562)

    y2563 = Student1.objects.filter(Cal_year=2563).count()
    y2563 = int(y2563)
    print('จำนวนปี 2555 มีจำนวน ',y2563)

    y2564 = Student1.objects.filter(Cal_year=2564).count()
    y2564 = int(y2564)
    print('จำนวนปี 2555 มีจำนวน ',y2564)

    Cal_year_list = [2555,2556,2557,2558,2559,2560,2561,2562,2563,2564]
    Cal_year_number = [y2555,y2556,y2557,y2558,y2559,y2560,y2561,y2562,y2563,y2564]
    jlist = [1,2,3,4,5,6,7,8,9,10]
    course_list = ['การประชุมวิชาการระดับชาติ', 'การประชุมวิชาการระดับนานาชาติ', 'ตีพิมพ์ลักษณะใดลักษณะหนึ่ง', 'ฐานข้อมูลระดับนานาชาติอื่น',
                   'TCI กลุ่ม 1','Scopus','WoS','TCI กลุ่ม 2','SSRN','EBSCO','ไม่อยู่ในฐานข้อมูล']
    number_list = [j1, j2, j3,j4,j5,j6,j7,j8,j9,j10,j11]
    context = {'course_list':course_list, 'number_list':number_list
               , 'Cal_year_list':Cal_year_list, 'Cal_year_number':Cal_year_number,'jlist':jlist}
    return render(request,'chartra2.html',context)


