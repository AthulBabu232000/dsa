class HashTable:
    def __init__(self,list) -> None:
        self.data=list
    def set(self,key,value)->None:
        address=self._hash(key)
        if (not self.data[address]):
            self.data[address]=[key,value]
    def _hash(self,key):
        s=''
        for i in key:
            s+=(str(ord(i)))
        return int(s)
    def get(self,itemkey)->list:
        address=self._hash(itemkey)
        if (self.data[address]):
            return self.data[address]
        return "Not present in the data table"
    def printHashTable(self):
        return self.data
l=list()
hashTable=HashTable(l)
hashTable.set('grapes',100000)
output=hashTable.get('grapes')
print(output)