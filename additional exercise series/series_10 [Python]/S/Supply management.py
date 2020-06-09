class Article:
    def __init__(self, code: str, name: str, purchaseprice: int, stock: int,
                 minimum_number_in_stock: int, maximum_number_in_stock=None):
        self.code = code
        self.name = name
        self.purchaseprice = purchaseprice
        self.stock = stock
        self.minimumstock = minimum_number_in_stock
        self.maximumstock = maximum_number_in_stock or minimum_number_in_stock
        assert self.minimumstock <= self.maximumstock, "minimum stock may not be larger than maximum stock"

    def __repr__(self):
        return self.__class__.__name__ \
               + f"{self.code, self.name, self.purchaseprice, self.stock, self.minimumstock, self.maximumstock}"

    def __str__(self):
        return "\n".join([
            f"article: {self.name}",
            f"code: {self.code}",
            f"purchaseprice: {self.purchaseprice}",
            f"stock: {self.stock}",
            f"minimumstock: {self.minimumstock}",
            f"maximumstock: {self.maximumstock}"
        ])

    def value(self):
        return self.stock * self.purchaseprice

    def shortage(self):
        return self.stock - self.minimumstock if self.stock < self.minimumstock else 0

    def reorder(self):
        return self.maximumstock - self.stock if self.shortage() else 0


class Stock:
    def __init__(self, articles=None):
        self.articles = articles or dict()

    def addArticle(self, article: Article):
        self.articles[article.code] = article

    def value(self):
        return sum(map(Article.value, self.articles.values()))

    def purchase(self, code: str, count: int):
        assert count >= 0, "number must be positive"
        assert code in self.articles, "article does not exist"
        self.articles[code].stock += count

    def sales(self, code: str, count: int):
        assert count >= 0, "number must be positive"
        assert code in self.articles, "article does not exist"
        delta = self.articles[code].stock - count
        assert delta >= 0, f"not enough supply of article {code} ({-delta} pieces short)"
        self.articles[code].stock -= count

    def replenish(self):
        to_replenish = sorted([(article, article.reorder()) for article in self.articles.values()
                               if article.shortage()], key=lambda l: l[0].code)
        print(f"\n{'=' * 30}\n".join([f"{article}\n--> {reorder} reorders" for article, reorder in to_replenish]))
        for article, reorder in to_replenish:
            self.purchase(article.code, reorder)
