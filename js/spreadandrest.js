const fruits=[ 2,4,5,6,7,8]
function iterator(tax, ...fruit){
    return fruit.map((f)=>tax*f);
}
console.log(iterator(...fruits));
