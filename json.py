class json:
    def createjsonstr(self, i, k=None):
        if isinstance(i, int) or isinstance(i, float):
            return  f'"{k}": {i}' if k else f'{i}'
        elif isinstance(i, str):
            return f'"{k}": "{i}"' if k else f'"{i}"'
        elif isinstance(i, bool):
            return f'"{k}": {self._truefalse(i)}' if k else self._truefalse(i)
        elif i is None:
            return f'"{k}": null' if k else f'null'
        elif isinstance(i, list) or isinstance(i, tuple):
            return f'"{k}": {self._array(i)}' if k else self._array(i)
        elif isinstance(i, dict):
            return f'"{k}": {self._object(i)}' if k else self._object(i)
        return ''

    def dumps(self, obj):
        return self.createjsonstr(obj)

    def _truefalse(self, obj):
        return 'true' if obj==True else 'false'

    def _array(self, obj):
        s=[]
        for i in obj:
            s.append(self.createjsonstr(i))
        return '[' + ', '.join(s) +']'

    def _object(self, obj):
        s =[]
        for k, v in obj.items():
            s.append(self.createjsonstr(v, k))
        return '{' + ', '.join(s) + '}'

if __name__ == "__main__":
    j = json()
    print(j.dumps({1:2,3:[4,5],7:'test',10:4.8}))