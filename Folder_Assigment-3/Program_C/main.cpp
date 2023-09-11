#include <iostream>
//#include <typeinfo>
#include<vector>


using namespace std;


class Student{
    int rollNumber;
    string name;
    int age; 
    int grade;
    

    public:
    static int nr;

    Student(string name,int age,int grade);

    void Print_Info_Student();
    int Get_rollnumber();
    void Set_name(string name);
    void Set_age(int age);
    void Set_grade(int grade);
    //void func();

    ~Student(){ cout << "Destructor Call" << endl; }
};

int Student::nr=1;

bool isNumber(string nr);
int String_to_Number(string s);

void Main_Menu_Choose();
void Create_Student(vector<Student *> &v);
void Display_All_Students(vector<Student *> v);
void Update_Student(vector<Student *> v);
void Delete_Student(vector<Student *> &v);


int main(){
    vector<Student *> vec_st;
    int nr=-1;
    do{
        string option;
        Main_Menu_Choose();
        getline(cin >> std::ws,option); //std::ws for eliminate new line from buffer if exist
        if(option.size()==0){ option=-1; continue; }
        //cin.ignore();
        if(isNumber(option)){
            nr=String_to_Number(option);
            switch(nr){
                case 0: cout << "\nProgram Finished\n";  break;
                case 1: Create_Student(vec_st);  break; //cout << "\nCreate Student\n";  break;
                case 2: Display_All_Students(vec_st); break; //cout << "\nDisplay Students\n";  break;
                case 3: Update_Student(vec_st); break;  //cout << "\nUpdate a Student\n";  break;
                case 4: Delete_Student(vec_st); break; //cout << "\nDelete a Student\n";  break;
                default: 
                    cout << "\n\n--------- This option doesn't exist ---------\n\n";   
                    break;
            }

        }else{
            cout << "\n\n-------- Insert a Properly Number --------\n\n";
        }

    }while(nr!=0);  

    
    //Student **s=
    /* while(true){

        Student *s1=new Student("S1",15,8);
        s1->Print_Info_Student();
        int nr;
        cout << "Insert 0 to exit or continue: ";
        cin >> nr;
        if(nr==0){
            break;
        }

    } */

    //Student s1("S1",15,8);
    //s1.Print_Info_Student();
    
    /* vector<Student *> vec_st;
    for(int i=0;i<2;i++){
        string name;
        int age,grade;
        cout <<"Name:"; //getline(cin >> std::ws,name);
        //cin.ignore();
        cout << "Age:"; cin >> age;
        cout << "Grade:"; cin >> grade;
        Student *s1=new Student(name,age,grade);
        vec_st.push_back(s1);
        cin.ignore();

    }

    for(auto it=vec_st.begin();it!=vec_st.end();it++){
        (*it)->Print_Info_Student(); 
    } */

    return 1;
}



void Main_Menu_Choose(){
    cout << "\n Choose an Option: \n"; 
    cout << " _______________________________ \n";
    cout << "                                 \n";
    cout << "|     1.Create one Student      |\n";
    cout << "|     2.Display All Students    |\n";
    cout << "|     3.Update a Student        |\n";
    cout << "|     4.Delete a Student        |\n";
    cout << "|     0.Exit Program            |\n";
    cout << " _______________________________ \n";
    cout << " Option: ";
}

bool isNumber(string nr){
    if(nr.size()==0){
        return false;
    }
    for(int i=0;i<nr.size();i++){
        if( !(int(nr[i])>=48 && int(nr[i])<=57) ){
            return false;
        }
    }


    return true;
}

int String_to_Number(string s){
    int nr=0;
    int k=0;
    for(int i=0;i<s.size();i++){
        nr=nr*10+(int(s[i])-48);
    }
    return nr;

}



void Create_Student(vector<Student *> &v){
    string name,age,grade;
    //int age,grade;
    cout << "Name-Student: "; getline(cin >> std::ws,name); //
    cout << "Age-Student: ";  getline(cin >> std::ws,age);
    cout << "Grade-Student(1-10 integer):"; getline(cin >> std::ws,grade);

    if(isNumber(age) && isNumber(grade)){
        Student *s=new Student(name,String_to_Number(age),String_to_Number(grade));    
        v.push_back(s);
        cout << "\nStudent Created with Roll-Number:"<<s->Get_rollnumber() <<endl;
        
    }
    else{
        cout << "\n\nInsert an int positive number to Age/Grade , Student wasn't created!!!\n\n ";
    }

    /* string str;
    cout << "\nInsert something continue: ";
    cin >> str; */
    //cout << "Age-Student: "; cin >> age;
    //cout << "Grade-Student(1-10 integer):"; cin >> grade;
    //cout << "\nInsert something continue: ";
    cout << "\nPress a enter to continue...";
    cin.ignore();

}




void Display_All_Students(vector<Student *> v){
    cout << "\n\n";
    if(v.size()==0){
        cout << "No students...\n";
        cout << "\nPress a enter to continue...";
        cin.ignore();
        return;
    }
    for(auto it=v.begin();it!=v.end();it++){
        (*it)->Print_Info_Student();
    }

    //string val;
    cout << "\nPress a enter to continue...";
    cin.ignore();
    /* string str;
    cout << "\nInsert something continue: ";
    cin >> str; */
}


void Update_Student(vector<Student *> v){
    string nr_check;
    cout << "\nInsert the rollNUmber of the student which you want to update: "; getline(cin >> std::ws,nr_check);
    int nr_student=0;
    if(isNumber(nr_check)){
        nr_student=String_to_Number(nr_check);
    }
    else{
        cout << "\nInsert a properly number! \n";
        cout << "\nPress enter to continue...";
        cin.ignore();
        return;
    }

    cout << endl;

    bool check_rollnr=false;
    Student *add_student=nullptr;
    for(vector<Student *>::iterator it=v.begin();it!=v.end();it++){
        if((*it)->Get_rollnumber()==nr_student){
            check_rollnr=true;
            add_student=*it;
            break;
        }
    }

    if(!check_rollnr){
        cout << "\nThe student with " << nr_student <<" rollNumber wasn't found  \n";
    }else{
        string opt;
        cout << "\nWhat do you wish to update:\n";
        cout << "1-Name\n2-Age\n3-Grade\nOption:";
        getline(cin >> std::ws,opt);
        if( !(opt=="1" || opt=="2" || opt=="3")  ){
            cout << "\nInvalid Option\n";
        }else{
            int var_check=1;
            if(opt=="1"){ 
                string name;
                cout << "rollNumber-"<<  add_student->Get_rollnumber()<< " Update Name:";
                getline(cin >> std::ws,name);
                add_student->Set_name(name);                

            }
            else if(opt=="2"){
                //int age_var;
                string age_var;
                cout << "rollNumber-"<<  add_student->Get_rollnumber()<< " Update Age:";
                getline(cin >> std::ws,age_var);
                if(isNumber(age_var)){
                    add_student->Set_age(String_to_Number(age_var));
                }
                else{
                    cout << "\n\n Student wasn't updated , insert a properly number to Age \n\n";
                    var_check=0;
                }
                
            }
            else if(opt=="3"){
                string grade_var;
                cout << "rollNumber-"<<  add_student->Get_rollnumber()<< " Update Grade:";
                //cin >> grade_var;
                getline(cin >> std::ws,grade_var);
                if(isNumber(grade_var)){
                    add_student->Set_grade(String_to_Number(grade_var));
                }
                else{
                    cout << "\n\n Student wasn't updated , insert a properly number to Grade \n\n";
                    var_check=0;

                }
                
            }

            if(var_check==1){ cout << "\nStudent Updated!!!\n"; }
        }    
    }

    //string str;
    cout << "\nPress enter to continue...";
    //cin >> str;
    cin.ignore();

}


void Delete_Student(vector<Student *> &v){
    string nr_check;
    cout << "\nInsert the rollNUmber of the student which you want to delete: "; getline(cin >> std::ws,nr_check);
    int nr_student=0;
    if(isNumber(nr_check)){
        nr_student=String_to_Number(nr_check);
    }
    else{
        cout << "\nInsert a properly number! \n";
        cout << "\nPress enter to continue...";
        cin.ignore();
        return;
    }



    bool check_rollnr=false;
    vector<Student *>::iterator it_student_del;
    for(vector<Student *>::iterator it=v.begin();it!=v.end();it++){
        if((*it)->Get_rollnumber()==nr_student){
            check_rollnr=true;
            //add_student=*it;
            it_student_del=it;
            break;
        }
    }

    if(!check_rollnr){
        cout << "\nThe student with " << nr_student <<" rollNumber wasn't found  \n";
    }
    else{
        int rollnr_del=(*it_student_del)->Get_rollnumber();
        delete *(it_student_del);
        v.erase(it_student_del);

        cout << "\nStudent with rollNumber:"<< rollnr_del <<" Deleted!!!\n";
    }

    cout << "\nPress enter to continue...";
    cin.ignore();

}

Student::Student(string name,int age,int grade){
    this->rollNumber=(Student::nr)++;
    this->name=name;
    this->age=age;
    this->grade=grade;
}

void Student::Print_Info_Student(){
    //cout << endl;
    cout << "Roll-Number:"<<this->rollNumber << " Name:"<< this->name << " Age:"<< this->age << " Grade:" << this->grade << endl;
}


int Student::Get_rollnumber(){
    return this->rollNumber;
}


void Student::Set_name(string name){
    this->name=name;
}


void Student::Set_age(int age){
    this->age=age;
}


void Student::Set_grade(int grade){
    this->grade=grade;
}