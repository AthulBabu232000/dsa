arr=new Array(10);

arr[0]=["orange",10000];
console.log(arr);
for(let i in arr){
    console.log(arr[i])
}

console.log("printing using let of operator");
for(let j of arr){
    console.log(arr['j'])
}