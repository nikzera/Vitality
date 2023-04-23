#include <iostream>

int main(){
    int size,i,j,k;
    char a = 65;
    std::cout<<"please input the branch size: ";
    std::cin>>size;
    for(i = 0; i <= size; i++){
        for(j = 1; j <= size - i; j++){
            std::cout<<" ";
        }
        for(k = 1; k <= i * 2 - 1; k++){
            std::cout<<a;
            if(a <= 89){
                a++;
            }
            else{
                a = 65;
            }

        }
        std::cout<<std::endl;
    }
    for(i = 1; i <= size / 2; i++){
        for(j = 0; j <= size - 3; j++){
            std::cout<<" ";
        }
        std::cout<< a <<" "<< a <<std::endl;
        if (a <= 89){
            a++;
        }
        else{
            a = 65;
        }

    }

    return 0;
}
