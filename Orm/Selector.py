class Selector:
    selectFields = []
    selectWhere = []
    new_where = None
    or_new_where = None
    and_new_where = None
    n_len = None
    line = None
    adder = None
    help_list = None
    selector_list = []
    field_list = []
    select_name = None
    field_name = None
    searcher_where = None
    stringer = None
    searcher_field = None
    searcher_selector = None

    def searcher(self):
        self.searcher_field = ", ".join(self.field_list)
        self.searcher_selector = ", ".join(self.selector_list)
        self.searcher_where = " ".join(self.selectFields[0])
        if self.searcher_selector == "":
            self.searcher_selector = " *"
        self.stringer = 'SELECT' + self.searcher_selector + ' FROM ' + self.searcher_field + ' WHERE ' + self.searcher_where + ' ;'
        return str(self.stringer)

    # Fields code
    def selectfield(self, field_name):
        self.field_name = field_name
        self.field_list.append(self.field_name)

    # Select code
    def selecter(self, select_name):
        self.select_name = select_name
        self.selector_list.append(self.select_name)

    # Where code
    def where(self, new_where):
        self.new_where: list = new_where
        if len(self.selectFields) == 0:
            self.selectFields.append(new_where)
        else:
            self.adder = ", " + self.new_where[0]
            self.selectFields[0].append(self.adder)

    def orwhere(self, or_new_where):
        self.or_new_where: list = or_new_where
        self.or_new_where.insert(0, 'or')
        self.or_new_where = " ".join(self.or_new_where)
        self.line = len(self.selectFields)
        self.selectFields[self.line - 1].append(self.or_new_where)

    def andwhere(self, and_new_where):
        self.and_new_where: list = and_new_where
        self.and_new_where.insert(0, 'and')
        self.and_new_where = " ".join(self.and_new_where)
        self.line = len(self.selectFields)
        self.selectFields[self.line - 1].append(self.and_new_where)
