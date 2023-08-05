class HashTable{
    constructor(size){
        this.data=new Array(size);
    }

    set=(key,value)=>{
       const address=this._hash(key);
       if(!this.data[address]){
        this.data[address]=[key,value]; 
       }
    }
    get=(key)=>{
     
        const address=this._hash(key);
        if(this.data[address]){
            return this.data[address];
        }
        return "Not found for this key";
    }

    _hash=(key)=>{
        let hash=0;
        for(let i=0;i<key.length;i++){
            hash=(hash+key.charCodeAt(i)*i)%this.data.length;
        }
    
        return hash;
    }
    print=()=>{
        for(let i of this.data){
            console.log(i);
        }
    }

}

hashTable=new HashTable(50);
hashTable.set('grapes',100000)
output=hashTable.get('grapes')
console.log(output)
hashTable.print();



