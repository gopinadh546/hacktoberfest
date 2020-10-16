
#include<stdio.h>
#include<string.h>
int main(){
int a[26];
for(int i=0;i<26;i++)
    scanf("%d",&a[i]);
  char c[10];
  scanf("%s",c);
  int k[10];
  int l=strlen(c);
    for(int j=0;j<l;j++){
      if(c[j]=='a')
      k[j]=a[0];
      if(c[j]=='b')
      k[j]=a[1];
      if(c[j]=='c')
      k[j]=a[2];
      if(c[j]=='d')
      k[j]=a[3];
      if(c[j]=='e')
      k[j]=a[4];
      if(c[j]=='f')
      k[j]=a[5];
      if(c[j]=='g')
      k[j]=a[6];
      if(c[j]=='h')
      k[j]=a[7];
      if(c[j]=='i')
      k[j]=a[8];
      if(c[j]=='j')
      k[j]=a[9];
      if(c[j]=='k')
      k[j]=a[10];
      if(c[j]=='l')
      k[j]=a[11];
      if(c[j]=='m')
      k[j]=a[12];
      if(c[j]=='n')
      k[j]=a[13];
      if(c[j]=='o')
      k[j]=a[14];
      if(c[j]=='p')
      k[j]=a[15];
      if(c[j]=='q')
      k[j]=a[16];
      if(c[j]=='r')
      k[j]=a[17];
      if(c[j]=='s')
      k[j]=a[18];
      if(c[j]=='t')
      k[j]=a[19];
      if(c[j]=='u')
      k[j]=a[20];
      if(c[j]=='v')
      k[j]=a[21];
      if(c[j]=='w')
      k[j]=a[22];
      if(c[j]=='x')
      k[j]=a[23];
      if(c[j]=='y')
      k[j]=a[24];
      if(c[j]=='z')
      k[j]=a[25];
    }
    int large=k[0];
    for(int i=0;i<l;i++)
    if(k[i]>large){
      large=k[i];
    }    
    int final=large*l;
    printf("%d",final);
  return 0;
}
