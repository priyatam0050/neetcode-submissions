class LRUCache:

    def __init__(self, capacity: int):
        self.cache={}
        self.limit=capacity
        self.temp=[]
        self.cache_list=[]
        self.temp2=0
        self.used=0
        

    def get(self, key: int) -> int:
        
     
        if key not in self.cache:
            return -1
        if key in self.cache_list:
            self.cache_list.remove(key)
           
        if self.cache[key]!=-1:
            self.cache_list.append(key)
        
        
        
        return self.cache[key]

        

    def put(self, key: int, value: int) -> None:

        

        if key in self.cache_list:
            self.cache_list.remove(key)
        

        elif len(self.cache)==self.limit :
            #k1_temp=list(self.cache_list)
            
            k1=self.cache_list[0]
            

            if k1 in self.cache:
                self.cache.pop(k1)
                self.cache_list.remove(k1)
           
               
        self.cache_list.append(key)
        self.cache[key]=value
       
        
