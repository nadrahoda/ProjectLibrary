class Issue:
    list_one = []

    def __init__(self):
        self.name = 0
        self.id = 0
        self.stream = 0
        self.date = 0
        self.book = 0
        self.status = "Issued"

    def bookIssue(self):
        Issue.list_one.append(self)

    def returnBook(self):
        for e in Issue.list_one:
            if self.book == e.book:
                self.name= e.name
                self.stream= e.stream
                self.id = e.id
                self.date= "within \nthe time\n period"
                self.book=e.book
                self.status = "Returned"
                Issue.list_one.append(self)
                return 1

