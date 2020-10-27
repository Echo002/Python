// #include <stdio.h>
// #include <stdlib.h>
// int main(){
//     int arr1[] = {0,1,2,3,4,5,6,7,8};
//     int arr2[] = {2,3,4,5,9};
//     int len1 = 9, len2 = 5;
//     for (int now1 = 0, now2 = 0; (now1 < len1) && (now2 < len2);){
//         if (arr1[now1] == arr2[now2]){
//             printf("%d ",arr1[now1]);
//             now1++;
//             now2++;
//         }
//         else if (arr1[now1] < arr2[now2])
//             now1++;
//         else
//             now2++;
//     }
//     printf("\n");
//     system("pause");
//     return 0;
// }

#include <stdio.h>
// typedef struct node{
//     int data;
//     struct node* next;
// }Node;

// int main(void){
//     int a[2][2] = {{1},{2,3}};
//     printf("%d", a[0][1]);
// }

int main(void){
    int a[2][2] = {{1, 2}, {3, 4}};
    int* p = a;
    // int i,j;
    // for(i = 0; i < 2; i++){
    //     for(j = 0; j < 2; j++){
    //         printf("%d\t", a[i][j]);
    //     }
    // }
    printf("%d",p[3]);
}