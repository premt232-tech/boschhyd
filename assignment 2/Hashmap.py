class Hashmap:
    def __init__(self,size =10):
        self.size =size
        self.buckets = [[] for _ in range(size)]
    
    def hashm(self,key):
        return hash(key)%self.size


    def put(self,key ,value):
        i = self.hashm(key)
        bucket = self.buckets[i]

        for pair in bucket:
            if pair[0]== key:
                pair[1] = value
                return
        bucket.append([key,value])
    def get(self,key):
        i = self.hashm(key)
        bucket = self.buckets[i]
        for pair in bucket :
            if pair[0]== key:
                return pair[1]
        return None
    def remove(self,key):
        i = self.hashm(key)
        bucket = self.buckets[i]
        for i, pair in enumerate(bucket):
            if pair[0] == key:
                bucket.pop(i)
                return True
        return False
    def display(self):
        for i ,bucket in enumerate(self.buckets):
            print(f"{i} : {bucket}")


def test():
    h1 = Hashmap()
    h1.put("a",10)
    h1.put("b",30)
    h1.put("c",70)
    h1.put("d",100)
    h1.display()


    print("get value :", h1.get("a"))
    h1.remove("b")
    h1.display()
    print("get the value :", h1.get("b"))
test()
