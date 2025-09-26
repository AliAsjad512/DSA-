public class navieLongesSub {
    
}


int res=0;

for(int i=0;i<n;i++){
    int c0 =0; int c1=0;
    for(int j=i;j<n;j++){
        if(arr[j] ==0){
            c0++;
        }
        else{
            c1++;
        }
        if(c0==c1){
            res = max(res,c0+c1)
        }
    }
}
return res;