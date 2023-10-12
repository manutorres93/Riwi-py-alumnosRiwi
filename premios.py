def create ():
    students_list_a=[]
    students_list_b=[]
    students_list_c=[]
    
    age_list_a=[]
    age_list_b=[]
    age_list_c=[]
    
    month_list_a=[]
    month_list_b=[]
    month_list_c=[]

    monitor_list_a=[]
    monitor_list_b=[]
    monitor_list_c=[]

    asist_list_a=[]
    asist_list_b=[]
    asist_list_c=[]

    aula_list_a=[]
    aula_list_b=[]
    aula_list_c=[]

    colaborator_list_a=[]
    colaborator_list_b=[]
    colaborator_list_c=[]

    note_list_a=[]
    note_list_b=[]
    note_list_c=[]

    participate_list_a=[]
    participate_list_b=[]
    participate_list_c=[]

    review_list_a=[]
    review_list_b=[]
    review_list_c=[]



    
    cant= int (input("Ingrese la cantidad de estudiantes: "))
    
    


    for x in range (cant):
        group= input ("Ingrese el grupo al que pertenece (A, B o C): ")

        if group == "A":

            students_list_a.append(input("Digite el nombre del estudiante: "))
            age_list_a.append(int(input("Digite la edad del estudiante: ")))
            month_list_a.append(input("Digite el mes en que ingresó el estudiante: "))
            monitor_list_a.append(int(input("Veces desempeñado como monitor: ")))
            asist_list_a.append(int(input("Inasistencias del estudiante ")))
            aula_list_a.append(int(input("Numero dentrega de talleres en en aula ")))
            colaborator_list_a.append(int(input("Digite en % que tan colaborador es el coder ")))
            note_list_a.append(float(input("Digite la nota del test de nivelación ")))
            participate_list_a.append(int(input("Digite en % que tan participativo es el coder ")))
            review_list_a.append(int(input("Digite en % que que tanto desarrolla en el SkillReview ")))
            

                    
        
        elif group== "B":
            students_list_b.append(input("Digite el nombre del estudiante: "))
            age_list_b.append(int(input("Digite la edad del estudiante: ")))
            month_list_b.append(input("Digite el mes en que ingresó el estudiante: "))  
            monitor_list_b.append(int(input("Veces desempeñado como monitor: ")))
            asist_list_b.append(int(input("Inasistencias del estudiante ")))
            aula_list_b.append(int(input("Numero dentrega de talleres en en aula ")))
            colaborator_list_b.append(int(input("Digite en % que tan colaborador es el coder ")))
            note_list_b.append(float(input("Digite la nota del test de nivelación ")))
            participate_list_b.append(int(input("Digite en % que tan participativo es el coder ")))
            review_list_b.append(int(input("Digite en % que que tanto desarrolla en el SkillReview ")))
        
        elif group== "C":
            students_list_c.append(input("Digite el nombre del estudiante: "))
            age_list_c.append(int(input("Digite la edad del estudiante: ")))
            month_list_c.append(input("Digite el mes en que ingresó el estudiante: "))
            monitor_list_c.append(int(input("Veces desempeñado como monitor: ")))
            asist_list_c.append(int(input("Inasistencias del estudiante ")))
            aula_list_c.append(int(input("Numero de entrega de talleres en en aula ")))
            colaborator_list_c.append(int(input("Digite en % que tan colaborador es el coder ")))
            note_list_c.append(float(input("Digite la nota del test de nivelación ")))
            participate_list_c.append(int(input("Digite en % que tan participativo es el coder ")))
            review_list_c.append(int(input("Digite en % que que tanto desarrolla en el SkillReview ")))
        
        else:

            print ("Error")
            break

    
    return (students_list_a,age_list_a ,month_list_a, 
            monitor_list_a,asist_list_a,aula_list_a,colaborator_list_a,note_list_a,participate_list_a,review_list_a,
            students_list_b, age_list_b, month_list_b,
            monitor_list_b,asist_list_b,aula_list_b,colaborator_list_b,note_list_b,participate_list_b,review_list_b,
            students_list_c, age_list_c, month_list_c,
            monitor_list_c,asist_list_c,aula_list_c,colaborator_list_c,note_list_c,participate_list_c,review_list_c,)

def trainer (trainer_a,trainer_b, trainer_c):
    
    trainer_a="No se asignó"
    trainer_b="No se asignó"
    trainer_c="No se asignó"

    for x in range (3):    
        name= input("Escriba el nombre del Trainer: ")
        group_trainer= input ("Escriba el grupo al que se le asignará (A, B o C):")
        

        if group_trainer == "A":
            trainer_a=name
        elif group_trainer =="B":
            trainer_b=name
        elif group_trainer=="C":
            trainer_c= name
        else:
            print ("Error")
        
    

    print("El Trainer del grupo A es ", trainer_a, "El Trainer del grupo B es ",trainer_b, "El Trainer del grupo C es ", trainer_c) 

def show_students():
    
    group_show= input("Digite el listado del grupo que quiere mostrar: ")
    print("NOMBRE               EDAD          MES DE INGRESO")
    
    if group_show == "A":
        for x in range (len(st_ls_a)):
            print(f"ID {x+1}:",st_ls_a[x],"         ", age_ls_a[x],"        ", month_ls_a[x])
    elif group_show == "B":
        for x in range (len(st_ls_b)):
            print(f"ID {x+1}:",st_ls_b[x] ,"        ", age_ls_b[x],"        ", month_ls_b[x])
    elif group_show == "C":
        for x in range (len(st_ls_c)):
            print(f"ID {x+1}:",st_ls_c[x], "        ", age_ls_c[x],"        ", month_ls_c[x])

def duplicate_coder ():

    group_student= input("Digite el grupo que quiere consultar: ")
    name_student= input("Digite el nombre que quiere consultar: ")

    if group_student=="A":
        
        n= st_ls_a.count(f"{name_student}")

        print("El nombre ",name_student, "está ", n, "veces")
    
    elif group_student=="B":
        
        n= st_ls_b.count(f"{name_student}")

        print("El nombre ",name_student, "está ", n, "veces")

    elif group_student=="C":
        
        n= st_ls_c.count(f"{name_student}")
        print("El nombre ",name_student, "está ", n, "veces")

    
    if n>1:
        print("Debe eliminar los registros duplicados de ", name_student)

def eliminate ():
    
    group_show= input("Digite el listado del grupo que quiere mostrar: ")

    if group_show == "A":
        for x in range (len(st_ls_a)):
            
            print(f"ID {x+1}:",st_ls_a[x])
    
    elif group_show == "B":
        for x in range (len(st_ls_b)):
            
            print(f"ID {x+1}:",st_ls_b[x])

    elif group_show == "C":
        for x in range (len(st_ls_c)):
            
            print(f"ID {x+1}:",st_ls_c[x])

            

    id_student= int(input("Digite el ID del estudiante que quiere eliminar: "))
    position=id_student-1
    
    if group_show=="A":

        del st_ls_a[position]
        del age_ls_a[position]
        del month_ls_a[position]
        del monitor_ls_a[position]
        del asist_ls_a[position]
        del aula_ls_a[position]
        del colaborator_ls_a[position]
        del note_ls_a[position]
        del participate_ls_a[position]
        del review_ls_a[position]           
    
    elif group_show=="B":

        del st_ls_b[position]
        del age_ls_b[position]
        del month_ls_b[position]
        del monitor_ls_b[position]
        del asist_ls_b[position]
        del aula_ls_b[position]
        del colaborator_ls_b[position]
        del note_ls_b[position]
        del participate_ls_b[position]
        del review_ls_b[position] 
    
    elif group_show=="C":

        del st_ls_c[position]
        del age_ls_c[position]
        del month_ls_c[position]
        del monitor_ls_c[position]
        del asist_ls_c[position]
        del aula_ls_c[position]
        del colaborator_ls_c[position]
        del note_ls_c[position]
        del participate_ls_c[position]
        del review_ls_c[position] 
    
def move ():
    group_show= input("Digite el listado del grupo del que sacará al estudiante: ")
    

    if group_show == "A":
        for x in range (len(st_ls_a)):
            print(f"ID {x+1}:",st_ls_a[x],"         ", age_ls_a[x],"        ", month_ls_a[x])
    elif group_show == "B":
        for x in range (len(st_ls_b)):
            print(f"ID {x+1}:",st_ls_b[x] ,"        ", age_ls_b[x],"        ", month_ls_b[x])
    elif group_show == "C":
        for x in range (len(st_ls_c)):
            print(f"ID {x+1}:",st_ls_c[x], "        ", age_ls_c[x],"        ", month_ls_c[x])

    
    id_student= int(input("Digite el ID del estudiante a trasladar: "))
    position=id_student-1
    
    if group_show=="A":

        student_move= st_ls_a.pop(position)
        age_move=age_ls_a.pop(position)
        month_move=month_ls_a.pop(position)
        monitor_move= monitor_ls_a.pop(position)
        asist_move= asist_ls_a.pop(position)
        aula_move=aula_ls_a.pop(position)
        colaborator_move=colaborator_ls_a.pop(position)
        note_move=note_ls_a.pop(position)
        participate_move= participate_ls_a.pop(position)
        review_move=review_ls_a.pop(position)

        
    
    
    elif group_show=="B":

        student_move=st_ls_b.pop(position)
        age_move=age_ls_b.pop(position)
        month_move=month_ls_b.pop(position)
        monitor_move= monitor_ls_b.pop(position)
        asist_move= asist_ls_b.pop(position)
        aula_move=aula_ls_b.pop(position)
        colaborator_move=colaborator_ls_b.pop(position)
        note_move=note_ls_b.pop(position)
        participate_move= participate_ls_b.pop(position)
        review_move=review_ls_b.pop(position)
    
    elif group_show=="C":

        student_move=st_ls_c.pop(position)
        age_move=age_ls_c.pop(position)
        month_move=month_ls_c.pop(position)
        monitor_move= monitor_ls_c.pop(position)
        asist_move= asist_ls_c.pop(position)
        aula_move=aula_ls_c.pop(position)
        colaborator_move=colaborator_ls_c.pop(position)
        note_move=note_ls_c.pop(position)
        participate_move= participate_ls_c.pop(position)
        review_move=review_ls_c.pop(position)
    
    group= input("Ingrese el grupo a mover al estudiante ")
    
    if group == "A":
        
        st_ls_a.append(student_move)
        age_ls_a.append(age_move)
        month_ls_a.append(month_move)
        monitor_ls_a.append(monitor_move)
        asist_ls_a.append(asist_move)
        aula_ls_a.append(aula_move)
        colaborator_ls_a.append(colaborator_move)
        note_ls_a.append(note_move)
        participate_ls_a.append(participate_move)
        review_ls_a.append(review_move)
    
    elif group== "B":
        
        st_ls_b.append(student_move)
        age_ls_b.append(age_move)
        month_ls_b.append(month_move)
        monitor_ls_b.append(monitor_move)
        asist_ls_b.append(asist_move)
        aula_ls_b.append(aula_move)
        colaborator_ls_b.append(colaborator_move)
        note_ls_b.append(note_move)
        participate_ls_b.append(participate_move)
        review_ls_b.append(review_move)

    elif group== "C":
        st_ls_c.append(student_move)
        age_ls_c.append(age_move)
        month_ls_c.append(month_move)
        monitor_ls_c.append(monitor_move)
        asist_ls_c.append(asist_move)
        aula_ls_c.append(aula_move)
        colaborator_ls_c.append(colaborator_move)
        note_ls_c.append(note_move)
        participate_ls_c.append(participate_move)
        review_ls_c.append(review_move)

def agregate():

    trainer= int(input(f"Digite [1] para Trainer grupo A, [2] para Trainer grupo B, [3] para trainer grupo C "))
    name= input("Ingrese el nombre nuevo estudiante ")
    age=  int(input("Ingrese la edad del nuevo estudiante "))
    month= input("Ingrese el mes en que ingreso el nuevo estudiante ")
    monitor=int(input("Veces desempeñado como monitor: "))
    asist= int(input("Inasistencias del estudiante "))
    aula= int(input("Numero dentrega de talleres en en aula "))
    colaborator= int(input("Digite en % que tan colaborador es el coder "))
    note=float(input("Digite la nota del test de nivelación "))
    participate=int(input("Digite en % que tan participativo es el coder "))
    review=int(input("Digite en % que que tanto desarrolla en el SkillReview "))
    



    if trainer ==1:
        
        st_ls_a.append(name)
        age_ls_a.append(age)
        month_ls_a.append(month)
        monitor_ls_a.append(monitor)
        asist_ls_a.append(asist)
        aula_ls_a.append(aula)
        colaborator_ls_a.append(colaborator)
        note_ls_a.append(note)
        participate_ls_a.append(participate)
        review_ls_a.append(review)
    
    elif trainer== 2:
        
        st_ls_b.append(name)
        age_ls_b.append(age)
        month_ls_b.append(month)
        monitor_ls_b.append(monitor)
        asist_ls_b.append(asist)
        aula_ls_b.append(aula)
        colaborator_ls_b.append(colaborator)
        note_ls_b.append(note)
        participate_ls_b.append(participate)
        review_ls_b.append(review)

    elif trainer== 3:
        st_ls_c.append(name)
        age_ls_c.append(age)
        month_ls_c.append(month)
        monitor_ls_c.append(monitor)
        asist_ls_c.append(asist)
        aula_ls_c.append(aula)
        colaborator_ls_c.append(colaborator)
        note_ls_c.append(note)
        participate_ls_c.append(participate)
        review_ls_c.append(review)

def max():
    
    group= input("Digite el listado del grupo del que quiere consultar la mayoría de edad: ")
    max_init=0
    if group =="A":
        
        
        for x in range(len(age_ls_a)):
            
            if age_ls_a[x]>max_init:               
                max_position=x
                max_init=age_ls_a[x]
                eldest=st_ls_a[max_position]
        
        return print ("El coder de más edad es",eldest,"con", max_init, "años" )
    elif group =="B":
        
        for x in range(len(age_ls_b)):
            
            if age_ls_b[x]>max_init:               
                max_position=x
                max_init=age_ls_b[x]
                eldest=st_ls_b[max_position]
        
        return print ("El coder de más edad es",eldest,"con", max_init, "años" )
    
    elif group =="C":
        
        for x in range(len(age_ls_c)):
            
            if age_ls_c[x]>max_init:               
                max_position=x
                max_init=age_ls_c[x]
                eldest=st_ls_c[max_position]
        
        return print ("El coder de más edad es",eldest,"con", max_init, "años" )
    
def min ():
    
    group= input("Digite el listado del grupo del que quiere consultar el menor: ")
    min_init=99
    if group =="A":
        
        
        for x in range(len(age_ls_a)):
            
            if age_ls_a[x]<min_init:               
                min_position=x
                min_init=age_ls_a[x]
                youngest=st_ls_a[min_position]
        
        return print ("El coder de menor edad es",youngest,"con", min_init, "años" )
    
    elif group =="B":
        
        
        for x in range(len(age_ls_b)):
            
            if age_ls_b[x]<min_init:               
                min_position=x
                min_init=age_ls_b[x]
                youngest=st_ls_b[min_position]
        
        return print ("El coder de menor edad es",youngest,"con", min_init, "años" )
    
    elif group =="C":
        
        
        for x in range(len(age_ls_c)):
            
            if age_ls_c[x]<min_init:               
                min_position=x
                min_init=age_ls_c[x]
                youngest=st_ls_c[min_position]
        
        return print ("El coder de menor edad es",youngest,"con", min_init, "años" )
    
def monitor():   
    group= input("Digite el listado del grupo del que quiere consultar los monitores: ")
    max_init=0
    if group =="A":

        for x in range(len(monitor_ls_a)):
            
            if monitor_ls_a[x]>max_init:               
                max_position=x
                max_init=monitor_ls_a[x]
                mt_monitor=st_ls_a[max_position]
        
        return print ("El coder que más hizo monitorias fue ",mt_monitor,"con", max_init, "monitorias" )
    
    elif group =="B":
        
        for x in range(len(monitor_ls_b)):
            
            if monitor_ls_b[x]>max_init:               
                max_position=x
                max_init=monitor_ls_b[x]
                mt_monitor=st_ls_b[max_position]
        
        return print ("El coder que más hizo monitorias fue",mt_monitor,"con", max_init, "monitorias" )
    
    elif group =="C":
        
        for x in range(len(monitor_ls_c)):
            
            if monitor_ls_c[x]>max_init:               
                max_position=x
                max_init=monitor_ls_c[x]
                mt_monitor=st_ls_c[max_position]
        
        return print ("El coder que más hizo monitorias fue",mt_monitor,"con", max_init, "monitorias" )

def inasistencia():
    group= input("Digite el listado del grupo del que quiere consultar: ")
    min_init=99
    if group =="A":

        for x in range(len(asist_ls_a)):
            
            if asist_ls_a[x]<min_init:               
                min_position=x
                min_init=asist_ls_a[x]
                youngest=st_ls_a[min_position]
        
        return print ("El coder con menores inasistencias es",youngest,"con", min_init, "inasistencias" )
    
    elif group =="B":
        
        
        for x in range(len(asist_ls_b)):
            
            if asist_ls_b[x]<min_init:               
                min_position=x
                min_init=asist_ls_b[x]
                youngest=st_ls_b[min_position]
        
        return print ("El coder con menores inasistencias es",youngest,"con", min_init, "inasistencias" )
    
    elif group =="C":
        
        
        for x in range(len(asist_ls_c)):
            
            if asist_ls_c[x]<min_init:               
                min_position=x
                min_init=asist_ls_c[x]
                youngest=st_ls_c[min_position]
        
        return print ("El coder con menores inasistencias es",youngest,"con", min_init, "inasistencias" )

def aula_talleres():
    group= input("Digite el listado del grupo del que quiere consultar: ")
    max_init=0
    if group =="A":

        for x in range(len(aula_ls_a)):
            
            if aula_ls_a[x]>max_init:               
                max_position=x
                max_init=aula_ls_a[x]
                max=st_ls_a[max_position]
        
        return print ("El coder que más entregas hizo ",max,"con", max_init, "entregas" )
    
    elif group =="B":
        
        for x in range(len(aula_ls_b)):
            
            if aula_ls_b[x]>max_init:               
                max_position=x
                max_init=aula_ls_b[x]
                max=st_ls_b[max_position]
        
        return print ("El coder que más entregas hizo ",max,"con", max_init, "entregas" )
    
    elif group =="C":
        
        for x in range(len(aula_ls_c)):
            
            if aula_ls_c[x]>max_init:               
                max_position=x
                max_init=aula_ls_c[x]
                max=st_ls_c[max_position]
        
        return print ("El coder que más entregas hizo ",max,"con", max_init, "entregas" )
    
def colaborador():
    group= input("Digite el listado del grupo del que quiere consultar: ")
    max_init=0
    if group =="A":

        for x in range(len(colaborator_ls_a)):
            
            if colaborator_ls_a[x]>max_init:               
                max_position=x
                max_init=colaborator_ls_a[x]
                max=st_ls_a[max_position]
        
        return print ("El coder que es más colaborador es ",max,"con", max_init, "%" )
    
    elif group =="B":
        
        for x in range(len(colaborator_ls_b)):
            
            if colaborator_ls_b[x]>max_init:               
                max_position=x
                max_init=colaborator_ls_b[x]
                max=st_ls_b[max_position]
        
        return print ("El coder que es más colaborador es ",max,"con", max_init, "%" )
    
    elif group =="C":
        
        for x in range(len(colaborator_ls_c)):
            
            if colaborator_ls_c[x]>max_init:               
                max_position=x
                max_init=colaborator_ls_c[x]
                max=st_ls_c[max_position]
        
        return print ("El coder que es más colaborador es ",max,"con", max_init, "%" )

def nota():
    group= input("Digite el listado del grupo del que quiere consultar: ")
    max_init=0
    if group =="A":

        for x in range(len(note_ls_a)):
            
            if note_ls_a[x]>max_init:               
                max_position=x
                max_init=note_ls_a[x]
                max=st_ls_a[max_position]
        
        return print ("El coder con mayor nota es ",max,"con", max_init )
    
    elif group =="B":
        
        for x in range(len(note_ls_b)):
            
            if note_ls_b[x]>max_init:               
                max_position=x
                max_init=note_ls_b[x]
                max=st_ls_b[max_position]
        
        return print ("El coder con mayor nota es ",max,"con", max_init  )
    
    elif group =="C":
        
        for x in range(len(note_ls_c)):
            
            if note_ls_c[x]>max_init:               
                max_position=x
                max_init=note_ls_c[x]
                max=st_ls_c[max_position]
        
        return print ("El coder con mayor nota es ",max,"con", max_init  )

def participativo():
    group= input("Digite el listado del grupo del que quiere consultar: ")
    max_init=0
    if group =="A":

        for x in range(len(participate_ls_a)):
            
            if participate_ls_a[x]>max_init:               
                max_position=x
                max_init=participate_ls_a[x]
                max=st_ls_a[max_position]
        
        return print ("El coder que es más participativo es ",max,"con", max_init, "%" )
    
    elif group =="B":
        
        for x in range(len(participate_ls_b)):
            
            if participate_ls_b[x]>max_init:               
                max_position=x
                max_init=participate_ls_b[x]
                max=st_ls_b[max_position]
        
        return print ("El coder que es más participativo es ",max,"con", max_init, "%" )
    
    elif group =="C":
        
        for x in range(len(participate_ls_c)):
            
            if participate_ls_c[x]>max_init:               
                max_position=x
                max_init=participate_ls_c[x]
                max=st_ls_c[max_position]
        
        return print ("El coder que es más participativo es ",max,"con", max_init, "%" )

def skill_review():
    group= input("Digite el listado del grupo del que quiere consultar: ")

    if group =="A":
        aprobados_a_100=[]
        aprobados_a_75=[]
        reprobados_a=[]

        for x in range(len(review_ls_a)):
            
            if review_ls_a[x]==100:               
                aprobados_a_100.append(st_ls_a[x])

            elif review_ls_a[x]<100 and review_ls_a[x]>= 75:
                aprobados_a_75.append(st_ls_a[x])
            
            elif review_ls_a[x]<75:
                reprobados_a.append(st_ls_a[x])
        
            
        option=int(input("Digite [1]Aprobados 100  [2]Aprobados 75-100 [3]Reprobados"))

        if option==1:
            print(aprobados_a_100)
        elif option==2:
            print(aprobados_a_75)
        elif option==3:
            print(reprobados_a)
    
    elif group =="B":
        aprobados_b_100=[]
        aprobados_b_75=[]
        reprobados_b=[]

        for x in range(len(review_ls_b)):
            
            if review_ls_b[x]==100:               
                aprobados_b_100.append(st_ls_b[x])

            elif review_ls_b[x]<100 and review_ls_b[x]>= 75:
                aprobados_b_75.append(st_ls_b[x])
            
            elif review_ls_b[x]<75:
                reprobados_b.append(st_ls_b[x])
        
            
        option=int(input("Digite [1]Aprobados 100  [2]Aprobados 75-100 [3]Reprobados"))

        if option==1:
            print(aprobados_b_100)
        elif option==2:
            print(aprobados_b_75)
        elif option==3:
            print(reprobados_b)

    elif group =="C":
        aprobados_c_100=[]
        aprobados_c_75=[]
        reprobados_c=[]

        for x in range(len(review_ls_c)):
            
            if review_ls_c[x]==100:               
                aprobados_c_100.append(st_ls_b[x])

            elif review_ls_c[x]<100 and review_ls_c[x]>= 75:
                aprobados_c_75.append(st_ls_b[x])
            
            elif review_ls_c[x]<75:
                reprobados_c.append(st_ls_b[x])
        
            
        option=int(input("Digite [1]Aprobados 100  [2]Aprobados 75-100 [3]Reprobados"))

        if option==1:
            print(aprobados_c_100)
        elif option==2:
            print(aprobados_c_75)
        elif option==3:
            print(reprobados_c)

init=-1

while init!=0:
    
    print("--------MENU------")
    print("1. Crear la lista de estudiantes")
    print("2. Asignar Trainers a los grupos")
    print("3. Listar coders del grupo")
    print("4. Buscar coders duplicados")    
    print("5. Eliminar un coder por inasistencia") 
    print("6. Traslado del coder ") 
    print("7. Agregar coder ") 
    print("8. Buscar mayor ")
    print("9. Buscar menor ")
    print("10. Monitor de la clase ")
    print("11. Coder con menos inasistencias ")
    print("12. Coder con más talleres entregados en aula ")
    print("13. Coder colaborador ")
    print("14. Coder con mayor nota")
    print("15. Coder participativo")
    print("16. Clasificación Skill Review")
    

    option= int(input("digite la opción deseada: "))

    if option==1:
        list_st= create()
        
        #listado estudiantes 
        st_ls_a= list_st[0] 
        st_ls_b= list_st[10]
        st_ls_c= list_st[20]
        
        #listado de edades por grupo
        age_ls_a=list_st[1]
        age_ls_b=list_st[11]
        age_ls_c=list_st[21]


        #listado de mes de ingreso
        month_ls_a=list_st[2]
        month_ls_b=list_st[12]
        month_ls_c=list_st[22]

        #listado veces monitor
        monitor_ls_a=list_st[3]
        monitor_ls_b=list_st[13]
        monitor_ls_c=list_st[23]

        #Inasistencias
        asist_ls_a=list_st[4]
        asist_ls_b=list_st[14]
        asist_ls_c=list_st[24]

        #Entrega tarbajos en aula
        aula_ls_a=list_st[5]
        aula_ls_b=list_st[15]
        aula_ls_c=list_st[25]

        #Colaborador
        colaborator_ls_a=list_st[6]
        colaborator_ls_b=list_st[16]
        colaborator_ls_c=list_st[26]

        #Nota
        note_ls_a=list_st[7]
        note_ls_b=list_st[17]
        note_ls_c=list_st[27]

        #Participacion
        participate_ls_a=list_st[8]
        participate_ls_b=list_st[18]
        participate_ls_c=list_st[28]
        
        #Participacion
        review_ls_a=list_st[9]
        review_ls_b=list_st[19]
        review_ls_c=list_st[29]
        
    elif option ==2:
        trainer("","","")
    
    elif option ==3:
        show_students()
    
    elif option ==4:
        duplicate_coder()
    
    elif option ==5:
        eliminate()

    elif option ==6:
        move()

    elif option==7:
        agregate()

    elif option==8:
        max()

    elif option==9:
        min()

    elif option==10:
        monitor()

    elif option==11:
        inasistencia()

    elif option==12:
        aula_talleres()

    elif option==13:
        colaborador()

    elif option==14:
        nota()

    elif option==15:
        participativo()
        
    elif option==16:
        skill_review()
        
        