from numbers import Integral


class Field:
    def __init__(self, cls):
        pass


class FloatField(Field):
    def __init__(self, col=None, cost=None, bid_price=None):
        self._value = None
        self.col = col
        self.cost = cost
        self.bid_price = bid_price
        if cost is not None:
            if not isinstance(cost, float):
                raise ValueError("cost is needed an float price")
            elif cost < 0:
                raise ValueError("cost is needed a positive price")
        if bid_price is not None:
            if not isinstance(bid_price, float):
                raise ValueError("bid_price is needed an float price")
            elif cost < 0:
                raise ValueError("bid_price is needed a positive price")
        if cost > bid_price:
            raise ValueError("losing proposition")

    def __get__(self, instance, owner):
        return self._value

    def __set__(self, instance, value):
        if not isinstance(value, float):
            raise ValueError("need an float value ")
        elif value < self.cost or value > self.bid_price:
            raise ValueError("Unreasonable price")
        self._value = value


class CharField(Field):
    def __init__(self, col, max_length=None):
        self.col = col
        self.max_length = max_length
        self._value = None
        if max_length is not None:
            if not isinstance(max_length, Integral):
                raise ValueError("max_length is an int")
            elif max_length < 0:
                raise ValueError("max_length is a positive int")

    def __get__(self, instance, owner):
        return self._value

    def __set__(self, instance, value):
        if not isinstance(value, str):
            raise ValueError("need an string value ")
        elif len(value) > self.max_length:
            raise ValueError("Unreasonable name")
        self._value = value


class ModelMetaClass(type):
    def __new__(cls, name, bases, attrs, **kwargs):
        if name == "BaseModel":
            return super().__new__(cls, name, bases, attrs, **kwargs)
        fields = {}
        for k, v in attrs.items():
            if isinstance(v, Field):
                fields[k] = v
        attrs_metal = attrs.get("Metal", None)
        _metal = {}
        db_table = name.lower()
        if attrs_metal is not None:
            table = getattr(attrs_metal, "table", None)
            if table is not None:
                db_table = table
        _metal["db_table"] = db_table
        attrs["_metal"] = _metal
        attrs["fields"] = fields
        del attrs["Metal"]
        return super().__new__(cls, name, bases, attrs, **kwargs)


class BaseModel(metaclass=ModelMetaClass):
    def __init__(self, *args, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)
        return super().__init__()

    def save(self):
        fields = []
        values = []
        for key, value in self.fields.items():
            db_col = value.col
            if db_col is None:
                db_col = key.lower()
            fields.append(db_col)
            value = getattr(self, key)
            values.append(str(value))
        sql = "INSERT {db_table}({fields}) value({values})".format(db_table=self._metal["db_table"], fields=",".join(fields),
                                                                   values=",".join(values))
        print(sql)


class Commodity(BaseModel):
    def __init__(self, name, price):
        self.name = name
        self.price = price

    name = CharField(col='name', max_length=10)
    price = FloatField(col='price', cost=5.0, bid_price=10.0)

    class Metal:
        table = 'user'


if __name__ == '__main__':
    cookies = Commodity("cookies", 6.5)
    cookies.name = 'inedible'
    cookies.price = 8.8
    cookies.save()

